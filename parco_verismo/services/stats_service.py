"""
Servizi per statistiche e report.
"""
from django.db.models import Count, Avg
from django.utils import timezone
from datetime import timedelta


def get_stats_prenotazioni():
    """
    Restituisce statistiche sulle prenotazioni.
    
    Returns:
        Dict con le statistiche
    """
    from ..models import Prenotazione
    
    oggi = timezone.now().date()
    settimana_fa = oggi - timedelta(days=7)
    mese_fa = oggi - timedelta(days=30)
    
    stats = {
        'totali': Prenotazione.objects.count(),
        'nuove': Prenotazione.objects.filter(stato='nuova').count(),
        'in_lavorazione': Prenotazione.objects.filter(stato='in_lavorazione').count(),
        'confermate': Prenotazione.objects.filter(stato='confermata').count(),
        'completate': Prenotazione.objects.filter(stato='completata').count(),
        'questa_settimana': Prenotazione.objects.filter(
            data_richiesta__gte=settimana_fa
        ).count(),
        'questo_mese': Prenotazione.objects.filter(
            data_richiesta__gte=mese_fa
        ).count(),
        'per_luogo': Prenotazione.objects.values('luogo').annotate(
            count=Count('id')
        ).order_by('-count'),
        'per_itinerario': Prenotazione.objects.values('itinerario').annotate(
            count=Count('id')
        ).order_by('-count'),
    }
    
    return stats


def get_stats_contenuti():
    """
    Restituisce statistiche sui contenuti pubblicati.
    
    Returns:
        Dict con le statistiche
    """
    from ..models import Opera, Evento, Notizia, Documento, Itinerario
    
    stats = {
        'opere': Opera.objects.count(),
        'eventi': Evento.objects.filter(is_active=True).count(),
        'notizie': Notizia.objects.filter(is_active=True).count(),
        'documenti': Documento.objects.filter(is_active=True).count(),
        'itinerari': Itinerario.objects.filter(is_active=True).count(),
    }
    
    return stats
