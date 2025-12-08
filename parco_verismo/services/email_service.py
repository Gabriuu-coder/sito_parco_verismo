"""
Servizi per la gestione delle email.
"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def invia_email_prenotazione_confermata(prenotazione):
    """
    Invia email di conferma al cliente dopo aver ricevuto la prenotazione.
    
    Args:
        prenotazione: Oggetto Prenotazione
    
    Returns:
        True se l'email è stata inviata con successo, False altrimenti
    """
    try:
        subject = f'Prenotazione ricevuta - {prenotazione.get_luogo_display()}'
        
        # Crea il messaggio email
        context = {
            'prenotazione': prenotazione,
        }
        
        # TODO: Creare template email quando necessario
        # message = render_to_string('emails/prenotazione_confermata.html', context)
        
        message = f"""
        Gentile {prenotazione.nome} {prenotazione.cognome},

        Abbiamo ricevuto la tua richiesta di prenotazione per:
        - Luogo: {prenotazione.get_luogo_display()}
        - Itinerario: {prenotazione.get_itinerario_display()}
        - Numero partecipanti: {prenotazione.numero_partecipanti}
        {f'- Data preferita: {prenotazione.data_preferita.strftime("%d/%m/%Y")}' if prenotazione.data_preferita else ''}

        Ti contatteremo presto per confermare i dettagli.

        Cordiali saluti,
        Il Team del Parco Letterario del Verismo
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@parcolettverismo.it',
            [prenotazione.email],
            fail_silently=False,
        )
        
        return True
    except Exception as e:
        # Log l'errore
        print(f"Errore nell'invio email: {e}")
        return False


def invia_notifica_admin_nuova_prenotazione(prenotazione):
    """
    Invia una notifica agli amministratori quando arriva una nuova prenotazione.
    
    Args:
        prenotazione: Oggetto Prenotazione
    
    Returns:
        True se l'email è stata inviata con successo, False altrimenti
    """
    try:
        subject = f'Nuova prenotazione: {prenotazione.nome} {prenotazione.cognome}'
        
        message = f"""
        Nuova prenotazione ricevuta:

        Cliente: {prenotazione.nome} {prenotazione.cognome}
        Email: {prenotazione.email}
        Telefono: {prenotazione.telefono or 'Non fornito'}
        
        Dettagli:
        - Luogo: {prenotazione.get_luogo_display()}
        - Itinerario: {prenotazione.get_itinerario_display()}
        - Numero partecipanti: {prenotazione.numero_partecipanti}
        {f'- Data preferita: {prenotazione.data_preferita.strftime("%d/%m/%Y")}' if prenotazione.data_preferita else ''}
        
        {f'Messaggio: {prenotazione.messaggio}' if prenotazione.messaggio else ''}
        
        Gestisci la prenotazione dall'admin.
        """
        
        # TODO: Configurare ADMIN_EMAIL in settings
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'admin@parcolettverismo.it')
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@parcolettverismo.it',
            [admin_email],
            fail_silently=False,
        )
        
        return True
    except Exception as e:
        # Log l'errore
        print(f"Errore nell'invio notifica admin: {e}")
        return False
