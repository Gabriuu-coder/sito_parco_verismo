"""
Modelli per il sistema di Prenotazioni.
"""
# Django imports
from django.db import models


class Prenotazione(models.Model):
    """Modello per salvare le prenotazioni dal form della homepage"""
    LUOGO_CHOICES = [
        ('vizzini', 'Vizzini'),
        ('mineo', 'Mineo'),
        ('licodia', 'Licodia Eubea'),
    ]
    
    ITINERARIO_CHOICES = [
        ('verghiani', 'Itinerari verghiani'),
        ('capuaniani', 'Itinerari capuaniani'),
        ('tematici', 'Itinerari tematici'),
    ]
    
    PRIORITA_CHOICES = [
        ('bassa', 'Bassa'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    
    STATO_CHOICES = [
        ('nuova', 'Nuova richiesta'),
        ('in_lavorazione', 'In lavorazione'),
        ('confermata', 'Confermata'),
        ('completata', 'Completata'),
        ('cancellata', 'Cancellata'),
    ]
    
    # Dati contatto
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cognome = models.CharField(max_length=100, verbose_name="Cognome")
    email = models.EmailField(verbose_name="Email")
    telefono = models.CharField(max_length=20, blank=True, verbose_name="Telefono", help_text="Opzionale ma consigliato per contatto rapido")
    
    # Dettagli richiesta
    luogo = models.CharField(max_length=20, choices=LUOGO_CHOICES, verbose_name="Luogo")
    itinerario = models.CharField(max_length=20, choices=ITINERARIO_CHOICES, blank=True, verbose_name="Tipologia itinerario", help_text="Opzionale - sarà suggerito in base al luogo scelto")
    data_preferita = models.DateField(null=True, blank=True, verbose_name="Data preferita visita", help_text="Opzionale")
    numero_partecipanti = models.PositiveIntegerField(default=1, verbose_name="Numero partecipanti", help_text="Numero persone che parteciperanno")
    messaggio = models.TextField(blank=True, verbose_name="Messaggio/Richieste particolari", help_text="Eventuali richieste o informazioni aggiuntive")
    
    # Gestione amministrativa
    data_richiesta = models.DateTimeField(auto_now_add=True, verbose_name="Data richiesta")
    stato = models.CharField(max_length=20, choices=STATO_CHOICES, default='nuova', verbose_name="Stato", db_index=True)
    priorita = models.CharField(max_length=10, choices=PRIORITA_CHOICES, default='media', verbose_name="Priorità", db_index=True)
    
    # Gestione date
    data_completamento = models.DateTimeField(null=True, blank=True, verbose_name="Data completamento", help_text="Quando il servizio è stato erogato")
    
    # Team e note
    responsabile = models.CharField(max_length=100, blank=True, verbose_name="Responsabile", help_text="Chi ha gestito la richiesta")
    guida_assegnata = models.CharField(max_length=100, blank=True, verbose_name="Guida assegnata", help_text="Nome della guida turistica assegnata")
    note_admin = models.TextField(blank=True, verbose_name="Note amministratore", help_text="Note interne per il follow-up")
    
    # Metadati
    ultima_modifica = models.DateTimeField(auto_now=True, verbose_name="Ultima modifica")
    
    class Meta:
        ordering = ['-data_richiesta']
        verbose_name = "Prenotazione"
        verbose_name_plural = "Prenotazioni"
    
    def __str__(self):
        stato_emoji = {
            'nuova': '🆕',
            'in_lavorazione': '⏳',
            'confermata': '✅',
            'completata': '✔️',
            'cancellata': '❌',
        }
        emoji = stato_emoji.get(self.stato, '📋')
        return f"{emoji} {self.nome} {self.cognome} - {self.get_luogo_display()} ({self.numero_partecipanti}p)"
    
    def save(self, *args, **kwargs):
        from django.utils import timezone
        
        # Auto-update data completamento quando stato diventa completata
        if self.stato == 'completata' and not self.data_completamento:
            self.data_completamento = timezone.now()
        
        super().save(*args, **kwargs)
    
    @property
    def giorni_attesa(self):
        """Calcola i giorni di attesa dalla richiesta"""
        from django.utils import timezone
        if self.stato in ['completata', 'cancellata']:
            data_fine = self.data_completamento or timezone.now()
        else:
            data_fine = timezone.now()
        return (data_fine.date() - self.data_richiesta.date()).days
    
    @property
    def in_ritardo(self):
        """Verifica se la prenotazione è in ritardo"""
        if self.stato in ['completata', 'cancellata']:
            return False
        if self.data_preferita:
            from django.utils import timezone
            return self.data_preferita < timezone.now().date() and self.stato != 'confermata'
        return False
