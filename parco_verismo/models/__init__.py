"""
Modelli del Parco Letterario del Verismo.
Organizzati per funzionalità e dominio.
"""

# Import tutti i modelli per renderli disponibili
from .autori_opere import Autore, Opera
from .eventi import Evento, Notizia
from .documenti import Documento, FotoArchivio
from .itinerari import Itinerario, TappaItinerario
from .prenotazioni import Prenotazione

# Esporta tutti i modelli
__all__ = [
    # Biblioteca
    'Autore',
    'Opera',
    # Eventi e Notizie
    'Evento',
    'Notizia',
    # Documenti e Archivio
    'Documento',
    'FotoArchivio',
    # Itinerari
    'Itinerario',
    'TappaItinerario',
    # Prenotazioni
    'Prenotazione',
]
