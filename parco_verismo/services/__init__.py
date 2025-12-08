"""
Servizi business logic del Parco Letterario del Verismo.
"""

from .email_service import (
    invia_email_prenotazione_confermata,
    invia_notifica_admin_nuova_prenotazione,
)

from .search_service import (
    ricerca_opere,
    ricerca_documenti,
    get_eventi_futuri,
    get_notizie_recenti,
)

from .stats_service import (
    get_stats_prenotazioni,
    get_stats_contenuti,
)

__all__ = [
    # Email
    'invia_email_prenotazione_confermata',
    'invia_notifica_admin_nuova_prenotazione',
    # Ricerca
    'ricerca_opere',
    'ricerca_documenti',
    'get_eventi_futuri',
    'get_notizie_recenti',
    # Statistiche
    'get_stats_prenotazioni',
    'get_stats_contenuti',
]
