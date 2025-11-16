# Parco Letterario Verismo

Sito web del Parco Letterario del Verismo - piattaforma per la promozione della letteratura verista siciliana.

## Stack Tecnologico

- **Django 5.2.8** - Framework web Python
- **Python 3.8+** - Linguaggio di programmazione
- **Bootstrap 5.3.3** - Framework CSS
- **django-parler** - Traduzioni multilingua
- **SQLite** - Database (PostgreSQL ready per produzione)

## Requisiti

- Python 3.8 o superiore
- Node.js e npm (per asset management)
- pip (Python package manager)

## Setup

### Setup Automatico

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```powershell
.\setup.ps1
```

### Setup Manuale

```bash
# Crea ambiente virtuale
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Installa dipendenze Python
pip install -r requirements.txt

# Installa dipendenze Node.js
npm install
npm run setup

# Database
python manage.py migrate
python manage.py createsuperuser

# Compila traduzioni
python manage.py compilemessages

# Avvia server di sviluppo
python manage.py runserver
```

**URL**: http://127.0.0.1:8000/  
**Admin**: http://127.0.0.1:8000/admin/

## Struttura del Progetto

### Modelli

- **Autore**: Autori delle opere veriste (Verga, Capuana, ecc.)
- **Opera**: Opere letterarie con traduzioni multilingua, link a Wikisource
- **Evento**: Eventi e manifestazioni culturali con date, luoghi, descrizioni
- **Notizia**: News e aggiornamenti del parco
- **Documento**: Documenti e studi pubblicati (solo admin, upload PDF)
- **FotoArchivio**: Archivio fotografico con carosello (solo admin)

### Funzionalità

- **Biblioteca Digitale**: Opere di Verga e Capuana con ricerca e link a Wikisource
- **Calendario Eventi**: Visualizzazione calendario con export e condivisione
- **Sistema Notizie**: News con immagini e contenuti multilingua
- **Documenti e Studi**: Upload PDF, anteprime, categorie (Documento/Studio/Ricerca/Saggio)
- **Archivio Fotografico**: Carosello automatico con modal fullscreen, thumbnails
- **Traduzioni Multilingua**: Supporto IT/EN con django-parler
- **Ricerca e Filtri**: Ricerca testuale e filtri per tipo/categoria

### Pagine Principali

- `/` - Homepage con hero video
- `/biblioteca/` - Biblioteca digitale con ricerca
- `/opere/<autore-slug>/` - Opere per autore
- `/opera/<slug>/` - Dettaglio opera
- `/eventi/` - Lista eventi
- `/calendario/` - Calendario eventi
- `/evento/<slug>/` - Dettaglio evento
- `/notizie/` - Lista notizie
- `/notizia/<slug>/` - Dettaglio notizia
- `/documenti/` - Documenti e studi
- `/documento/<slug>/` - Dettaglio documento
- `/archivio/` - Archivio fotografico

## Struttura Directory

```
parco_verismo/
├── models.py          # Modelli del database
├── views.py           # Viste e logica applicazione
├── urls.py            # Routing URL
├── admin.py           # Configurazione admin Django
├── templates/         # Template HTML
│   └── parco_verismo/
│       ├── components/    # Componenti riutilizzabili
│       ├── *.html         # Template pagine
├── static/            # File statici
│   ├── css/           # Fogli di stile
│   ├── js/            # JavaScript
│   ├── assets/        # Immagini, video
│   └── fonts/         # Font personalizzati
└── migrations/        # Migrazioni database

mysite/
├── settings.py        # Configurazione Django
└── urls.py            # URL root

locale/                # File traduzione
├── it/LC_MESSAGES/   # Traduzioni italiano
└── en/LC_MESSAGES/   # Traduzioni inglese

media/                 # File caricati dagli utenti/admin
```

## Sviluppo

### Creare un nuovo modello

```python
# parco_verismo/models.py
from parler.models import TranslatableModel, TranslatedFields
from django.db import models

class MioModello(TranslatableModel):
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    
    translations = TranslatedFields(
        titolo=models.CharField(max_length=200),
        descrizione=models.TextField(),
    )
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Mio Modello"
        verbose_name_plural = "I Miei Modelli"
```

```bash
python manage.py makemigrations
python manage.py migrate
```

### Aggiungere una view

```python
# parco_verismo/views.py
from django.shortcuts import render
from .models import MioModello

def mia_view(request):
    oggetti = MioModello.objects.filter(is_active=True)
    context = {'oggetti': oggetti}
    return render(request, 'parco_verismo/pagina.html', context)
```

### Aggiungere URL

```python
# parco_verismo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pagina/', views.mia_view, name='pagina'),
]
```

### Aggiungere Admin

```python
# parco_verismo/admin.py
from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import MioModello

@admin.register(MioModello)
class MioModelloAdmin(TranslatableAdmin):
    list_display = ('__str__', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('translations__titolo',)
```

### Stili CSS

- `parco_verismo/static/css/styles.css` - Stili principali e tema
- `parco_verismo/static/css/navbar.css` - Stili navbar
- `parco_verismo/static/css/index.css` - Stili homepage
- `parco_verismo/static/css/archivio.css` - Stili archivio fotografico
- `parco_verismo/static/css/calendario.css` - Stili calendario

## Traduzioni

Il progetto supporta traduzioni multilingua (IT/EN) tramite django-parler per i modelli e Django i18n per i template.

### Aggiungere nuove stringhe da tradurre

1. Usa `{% trans 'Testo' %}` nei template
2. Genera file traduzione: `python manage.py makemessages -l en`
3. Traduci nel file `locale/en/LC_MESSAGES/django.po`
4. Compila: `python manage.py compilemessages`

### Traduzioni modelli

I modelli che ereditano da `TranslatableModel` supportano automaticamente traduzioni multilingua tramite django-parler.

## Comandi Utili

```bash
# Verifica configurazione
python manage.py check

# Shell Django interattiva
python manage.py shell

# Esegui test
python manage.py test

# Raccogli file statici (produzione)
python manage.py collectstatic

# Traduzioni
python manage.py makemessages -l en    # Genera file traduzione
python manage.py compilemessages        # Compila traduzioni

# Database
python manage.py makemigrations         # Crea migrazioni
python manage.py migrate                # Applica migrazioni
python manage.py showmigrations         # Mostra stato migrazioni

# Creare superuser
python manage.py createsuperuser
```

## Admin

L'interfaccia admin Django (`/admin/`) permette di gestire:

- **Autori**: Nome, slug
- **Opere**: Titolo, trama, analisi, copertina, link Wikisource
- **Eventi**: Titolo, descrizione, date, luogo, immagine
- **Notizie**: Titolo, contenuto, immagine, data pubblicazione
- **Documenti**: Titolo, descrizione, PDF, anteprima, tipo, autori
- **Archivio Fotografico**: Immagini, titolo, descrizione, categoria, ordine

Solo gli admin possono creare e modificare i contenuti. I visitatori possono solo visualizzare.

## Media Files

I file caricati vengono salvati in `media/`:

- `media/copertine_opere/` - Copertine opere
- `media/eventi/` - Immagini eventi
- `media/notizie/` - Immagini notizie
- `media/documenti/` - PDF documenti
- `media/documenti/anteprime/` - Anteprime documenti
- `media/archivio_fotografico/` - Foto archivio

In produzione, configurare `MEDIA_ROOT` e `MEDIA_URL` in `settings.py`.

## Produzione

### Configurazione

1. Impostare `DEBUG = False` in `settings.py`
2. Configurare `ALLOWED_HOSTS`
3. Configurare database PostgreSQL (opzionale)
4. Configurare server web (Nginx/Apache)
5. Configurare WSGI server (Gunicorn/uWSGI)

### Variabili Ambiente

Usa un file `.env` con:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Static Files

```bash
python manage.py collectstatic
```

Configurare `STATIC_ROOT` e servire file statici tramite web server o CDN.

## Licenza

MIT License
