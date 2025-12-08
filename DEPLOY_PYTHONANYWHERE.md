# Guida Deploy su PythonAnywhere

## 1. Crea account su PythonAnywhere
- Vai su https://www.pythonanywhere.com
- Crea un account gratuito o a pagamento

## 2. Carica il codice

### Opzione A: Da Git (consigliata)
```bash
# Nel terminale Bash di PythonAnywhere
git clone https://github.com/Triba14/sito_parco_verismo.git
cd sito_parco_verismo
```

### Opzione B: Upload manuale
- Usa "Files" per caricare i file via web interface

## 3. Crea Virtual Environment
```bash
# Nel terminale Bash
cd ~/sito_parco_verismo
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Configura l'ambiente
```bash
# Copia il file .env.pythonanywhere in .env
cp .env.pythonanywhere .env

# Modifica .env con i tuoi dati
nano .env
```

**Importante:** Modifica questi valori nel .env:
- `SECRET_KEY`: genera una chiave random (puoi usare https://djecrety.ir/)
- `ALLOWED_HOSTS`: metti il tuo username, es: `tuousername.pythonanywhere.com`
- `STATIC_ROOT`: `/home/tuousername/sito_parco_verismo/staticfiles/`
- `MEDIA_ROOT`: `/home/tuousername/sito_parco_verismo/media/`

## 5. Prepara il database e i file statici
```bash
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
# Opzionale: popola database demo
python populate_db_complete.py
```

## 6. Configura Web App su PythonAnywhere

### Nel tab "Web":
1. Clicca "Add a new web app"
2. Scegli "Manual configuration" (non "Django")
3. Scegli Python 3.10

### Configura WSGI file:
Clicca sul link del WSGI file e sostituisci tutto con:

```python
import os
import sys

# Aggiungi la directory del progetto al path
path = '/home/tuousername/sito_parco_verismo'
if path not in sys.path:
    sys.path.append(path)

# Carica variabili d'ambiente dal file .env
from pathlib import Path
env_path = Path('/home/tuousername/sito_parco_verismo/.env')
if env_path.exists():
    from decouple import Config, RepositoryEnv
    config = Config(RepositoryEnv(env_path))

# Imposta il modulo settings di Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Importa l'applicazione WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Configura Virtual Environment:
- Nella sezione "Virtualenv"
- Path: `/home/tuousername/sito_parco_verismo/venv`

### Configura Static files:
Nella sezione "Static files" aggiungi:

| URL           | Directory                                        |
|---------------|--------------------------------------------------|
| /static/      | /home/tuousername/sito_parco_verismo/staticfiles |
| /media/       | /home/tuousername/sito_parco_verismo/media       |

## 7. Ricarica l'app
- Clicca sul grande pulsante verde "Reload tuousername.pythonanywhere.com"

## 8. Verifica il sito
- Vai su https://tuousername.pythonanywhere.com
- Verifica che tutto funzioni
- Accedi all'admin: https://tuousername.pythonanywhere.com/admin

## Troubleshooting

### Se vedi errori:
1. Controlla i log in "Web" → "Log files"
2. Controlla error.log e server.log

### Se i CSS non si caricano:
```bash
source venv/bin/activate
python manage.py collectstatic --clear --noinput
```
Poi ricarica la web app

### Se il database non funziona:
```bash
source venv/bin/activate
python manage.py migrate --run-syncdb
```

## Aggiornamenti futuri

Quando fai modifiche al codice:
```bash
cd ~/sito_parco_verismo
git pull  # se usi git
source venv/bin/activate
pip install -r requirements.txt  # se hai nuove dipendenze
python manage.py migrate  # se hai nuove migrazioni
python manage.py collectstatic --noinput  # se hai modificato CSS/JS
```

Poi clicca "Reload" nella web app.

## Note importanti

1. **Account gratuito** ha limitazioni:
   - 1 web app
   - 512MB spazio disco
   - Traffico limitato
   - Il sito va in sleep dopo inattività (si riattiva al primo accesso)

2. **Per produzione seria**, considera:
   - Account a pagamento PythonAnywhere
   - MySQL invece di SQLite
   - Backup regolari del database

3. **Domini custom**:
   - Account gratuito: solo `tuousername.pythonanywhere.com`
   - Account a pagamento: puoi collegare il tuo dominio

## Supporto
- Documentazione: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
- Forum: https://www.pythonanywhere.com/forums/
