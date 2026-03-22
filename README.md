# Email Complaint Classifier — IT Helpdesk
n8n + Django + Groq (Llama 3)

## First Time Setup

### 1. Create & activate virtual environment
```
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Add your Groq API key
- Go to https://console.groq.com
- Sign up and create a free API key
- Open django_project/tickets/ml_model.py
- Replace YOUR_GROQ_API_KEY_HERE with your key

### 4. Run Django
```
cd django_project
python manage.py migrate
python manage.py runserver
```

### 5. Start n8n (separate terminal)
```
n8n start
```

API endpoint: http://127.0.0.1:8000/api/predict/

## Every Day
```
venv\Scripts\activate
cd django_project
python manage.py runserver
```
And n8n start in a second terminal.

## Categories
- network  → WiFi, internet, VPN connectivity, network drops
- hardware → laptop, printer, monitor, battery, physical devices
- software → apps, ERP, crash, Teams, Zoom, Excel, browser
- access   → password, account locked, permissions, MFA
- unclassified → Groq could not determine category (rare)

## File Structure
email-classifier/
├── dataset/
│   └── tickets.csv
├── django_project/
│   ├── django_project/     ← Django settings, urls
│   ├── tickets/
│   │   ├── ml_model.py     ← Groq classifier (only file changed)
│   │   ├── views.py        ← unchanged
│   │   └── ...
│   └── manage.py
├── n8n workflow.json       ← import into n8n
└── requirements.txt
