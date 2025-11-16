# Guida per Collaboratori

Questa guida spiega come contribuire al progetto del Parco Letterario Verismo. È scritta in modo semplice, passo dopo passo.

## Prima di Iniziare

### Cosa ti Serve

1. **Git** - Per scaricare e aggiornare il codice
2. **Python 3.8 o superiore** - Il linguaggio di programmazione usato
3. **Un editor di testo** - Come VS Code, PyCharm, o anche Notepad++
4. **Un account GitHub/GitLab** (se il progetto è su un repository)

### Chiedere Aiuto

Se qualcosa non è chiaro, chiedi! È meglio chiedere prima di fare errori.

## Passo 1: Scaricare il Progetto

### Se è la Prima Volta

1. Apri il terminale (o Prompt dei comandi su Windows)
2. Vai nella cartella dove vuoi salvare il progetto
3. Esegui questo comando:

```bash
git clone <URL_DEL_REPOSITORY>
cd sito_parco_verismo
```

**Cosa significa?**
- `git clone` scarica tutto il progetto sul tuo computer
- `cd` entra nella cartella del progetto

### Se il Progetto Esiste Già

Se hai già il progetto, aggiornalo prima di iniziare:

```bash
cd sito_parco_verismo
git pull
```

**Cosa significa?**
- `git pull` scarica le ultime modifiche fatte da altri

## Passo 2: Preparare l'Ambiente

### Creare l'Ambiente Virtuale

L'ambiente virtuale è come una scatola separata dove mettiamo tutte le cose necessarie per questo progetto.

```bash
python3 -m venv .venv
```

**Su Windows:**
```bash
python -m venv .venv
```

### Attivare l'Ambiente Virtuale

**Su Linux/Mac:**
```bash
source .venv/bin/activate
```

**Su Windows:**
```bash
.venv\Scripts\activate
```

**Come capire se funziona?**
Vedrai `(.venv)` all'inizio della riga nel terminale. Tipo così:
```
(.venv) user@computer:~/sito_parco_verismo$
```

### Installare le Dipendenze

Le dipendenze sono i programmi che servono al progetto per funzionare.

```bash
pip install -r requirements.txt
```

**Cosa fa?**
Installa tutti i programmi necessari elencati nel file `requirements.txt`.

## Passo 3: Configurare il Database

Il database è dove vengono salvati tutti i dati (opere, eventi, notizie, ecc.).

### Creare il Database

```bash
python manage.py migrate
```

**Cosa fa?**
Crea tutte le tabelle necessarie nel database.

### Creare un Account Admin

```bash
python manage.py createsuperuser
```

Ti chiederà:
- Username (scegli un nome)
- Email (la tua email)
- Password (scegli una password sicura)

**A cosa serve?**
Per accedere all'area admin del sito (`/admin/`) e aggiungere/modificare contenuti.

### Compilare le Traduzioni

```bash
python manage.py compilemessages
```

**Cosa fa?**
Prepara le traduzioni in inglese e italiano per il sito.

## Passo 4: Avviare il Server

Ora puoi vedere il sito sul tuo computer!

```bash
python manage.py runserver
```

Apri il browser e vai su: **http://127.0.0.1:8000/**

**Per fermare il server:**
Premi `Ctrl + C` nel terminale.

## Come Fare Modifiche

### 1. Creare un Branch (Ramo)

Un branch è come una copia del progetto dove puoi lavorare senza rovinare la versione principale.

```bash
git checkout -b nome-della-tua-modifica
```

**Esempio:**
```bash
git checkout -b aggiungo-nuova-pagina
```

**Cosa significa il nome?**
Usa un nome che descrive cosa stai facendo:
- `aggiungo-nuova-pagina`
- `sistemo-bug-navbar`
- `traduco-testi-inglese`

### 2. Fare le Modifiche

Ora puoi modificare i file del progetto con il tuo editor.

**File Importanti:**
- `parco_verismo/models.py` - I modelli (cosa c'è nel database)
- `parco_verismo/views.py` - Le viste (cosa fa ogni pagina)
- `parco_verismo/templates/` - I template HTML (come appaiono le pagine)
- `parco_verismo/static/css/` - Gli stili CSS (i colori e il design)

### 3. Testare le Modifiche

Dopo ogni modifica:

1. **Riavvia il server** (se necessario):
   ```bash
   python manage.py runserver
   ```

2. **Vai sul sito** e controlla che tutto funzioni

3. **Prova tutte le funzionalità** che hai modificato

4. **Controlla che non ci siano errori** nel terminale

### 4. Verificare che Non Ci Siano Errori

```bash
python manage.py check
```

**Cosa fa?**
Controlla se ci sono errori nella configurazione.

## Come Salvare le Modifiche

### 1. Vedere Cosa Hai Modificato

```bash
git status
```

**Cosa mostra?**
Tutti i file che hai modificato, aggiunto o cancellato.

### 2. Aggiungere i File Modificati

```bash
git add .
```

**Cosa fa?**
Prepara tutti i file modificati per essere salvati.

**Se vuoi aggiungere solo un file:**
```bash
git add nome-file.py
```

### 3. Salvare le Modifiche (Commit)

```bash
git commit -m "Descrizione di cosa hai fatto"
```

**Esempi di messaggi buoni:**
```bash
git commit -m "Aggiunto link alla pagina archivio nella navbar"
git commit -m "Corretto bug nel carosello delle foto"
git commit -m "Tradotto pagina documenti in inglese"
```

**Cosa significa?**
- `commit` salva le modifiche con un messaggio che spiega cosa hai fatto
- Il messaggio deve essere chiaro, così altri capiscono cosa hai cambiato

### 4. Inviare le Modifiche (Push)

```bash
git push origin nome-della-tua-modifica
```

**Cosa fa?**
Invia le tue modifiche al repository online (GitHub/GitLab).

## Regole da Seguire

### 1. Prima di Iniziare a Lavorare

Sempre aggiornare il progetto:
```bash
git pull
```

### 2. Fare Modifiche Piccole

È meglio fare tante modifiche piccole che una grande:
- Più facile da capire
- Più facile da testare
- Più facile da correggere se c'è un errore

### 3. Testare Sempre

Prima di salvare, prova sempre che tutto funzioni!

### 4. Scrivere Messaggi Chiari

Quando fai un commit, scrivi sempre un messaggio che spiega:
- **Cosa** hai fatto
- **Perché** l'hai fatto (se non è ovvio)

**Esempi:**
- ✅ Buono: "Aggiunto filtro per tipo documento nella pagina documenti"
- ❌ Cattivo: "modifiche"
- ❌ Cattivo: "fix"

### 5. Non Modificare File che Non Conosci

Se non sei sicuro di cosa fa un file, chiedi prima di modificarlo.

### 6. Fare Backup

Prima di fare modifiche importanti, fai un backup:
```bash
git branch backup-prima-delle-modifiche
```

## Cosa Fare se Qualcosa Va Storto

### Il Server Non Parte

1. Controlla che l'ambiente virtuale sia attivo (vedi `(.venv)` nel terminale)
2. Controlla che tutte le dipendenze siano installate: `pip install -r requirements.txt`
3. Controlla che il database sia creato: `python manage.py migrate`

### Ci Sono Errori nel Codice

1. Leggi il messaggio di errore nel terminale
2. Cerca su Google l'errore (spesso trovi la soluzione)
3. Chiedi aiuto se non riesci a risolvere

### Ho Rotto Qualcosa

Non preoccuparti! Puoi sempre tornare indietro:

```bash
git checkout -- nome-file.py
```

**Cosa fa?**
Ripristina il file alla versione precedente.

### Voglio Annullare Tutte le Modifiche

```bash
git reset --hard
```

**ATTENZIONE:** Questo cancella TUTTE le modifiche non salvate!

## Esempio Completo: Aggiungere una Nuova Pagina

Ecco un esempio passo-passo per aggiungere una nuova pagina "Chi Siamo":

### 1. Creare il Branch

```bash
git checkout -b aggiungo-pagina-chi-siamo
```

### 2. Creare la View

Apri `parco_verismo/views.py` e aggiungi:

```python
def chi_siamo_view(request):
    return render(request, 'parco_verismo/chi_siamo.html')
```

### 3. Creare il Template

Crea il file `parco_verismo/templates/parco_verismo/chi_siamo.html`:

```html
{% extends "parco_verismo/base.html" %}
{% load static i18n %}

{% block title %}{% trans 'Chi Siamo - Parco Letterario Verismo' %}{% endblock %}

{% block content %}
<section class="container my-5">
  <h1>{% trans 'Chi Siamo' %}</h1>
  <p>{% trans 'Contenuto della pagina...' %}</p>
</section>
{% endblock %}
```

### 4. Aggiungere l'URL

Apri `parco_verismo/urls.py` e aggiungi:

```python
path('chi-siamo/', views.chi_siamo_view, name='chi_siamo'),
```

### 5. Testare

1. Avvia il server: `python manage.py runserver`
2. Vai su: http://127.0.0.1:8000/chi-siamo/
3. Controlla che la pagina funzioni

### 6. Salvare

```bash
git add .
git commit -m "Aggiunta pagina Chi Siamo"
git push origin aggiungo-pagina-chi-siamo
```

## Domande Frequenti

### Devo Installare Tutto Ogni Volta?

No! Una volta installato, basta:
1. Attivare l'ambiente virtuale: `source .venv/bin/activate`
2. Aggiornare: `git pull`
3. Avviare: `python manage.py runserver`

### Come Vedo le Modifiche che Ho Fatto?

1. Avvia il server: `python manage.py runserver`
2. Apri il browser: http://127.0.0.1:8000/
3. Vai alla pagina che hai modificato

### Posso Modificare Più Cose Insieme?

Sì, ma è meglio fare un commit per ogni modifica logica. Per esempio:
- Un commit per aggiungere una pagina
- Un commit separato per sistemare un bug
- Un commit separato per tradurre

### Cosa Faccio se Vedo un Errore che Non Ho Fatto Io?

1. Assicurati di aver fatto `git pull` per avere l'ultima versione
2. Se l'errore c'è ancora, segnalalo
3. Non modificare codice che non capisci

### Come Aggiungo una Traduzione?

1. Nel template, usa: `{% trans 'Testo italiano' %}`
2. Genera il file traduzione: `python manage.py makemessages -l en`
3. Apri `locale/en/LC_MESSAGES/django.po`
4. Trova la stringa e aggiungi la traduzione inglese
5. Compila: `python manage.py compilemessages`

## Chiedere Aiuto

Se sei bloccato:

1. **Rileggi questa guida** - Spesso la risposta è qui
2. **Cerca su Google** - L'errore che vedi probabilmente è già stato risolto da altri
3. **Chiedi al team** - Non avere paura di chiedere!

Quando chiedi aiuto, includi sempre:
- Cosa stavi cercando di fare
- L'errore esatto che vedi (copia e incolla)
- Cosa hai già provato

## Ricapitoliamo: Workflow Completo

Ecco il flusso completo per contribuire:

```bash
# 1. Aggiorna il progetto
git pull

# 2. Crea un nuovo branch
git checkout -b nome-modifica

# 3. Fai le modifiche (con il tuo editor)

# 4. Testa che funzioni
python manage.py runserver
# Vai sul sito e prova

# 5. Controlla errori
python manage.py check

# 6. Salva le modifiche
git add .
git commit -m "Descrizione chiara"

# 7. Invia
git push origin nome-modifica
```

## Consigli Finali

- **Fai piccoli passi** - Non cercare di fare tutto in una volta
- **Testa sempre** - Prima di salvare, prova che funzioni
- **Chiedi se non sei sicuro** - È meglio chiedere che rompere qualcosa
- **Leggi il codice esistente** - È il modo migliore per capire come funziona
- **Divertiti!** - Contribuire a un progetto è un modo fantastico per imparare

Buon lavoro! 🚀

