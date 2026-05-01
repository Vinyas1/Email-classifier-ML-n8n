# 🚀 ML-Based Email Ticket Classification System

## 📌 Overview

This system automatically reads emails, classifies them using ML, and routes them to appropriate teams using n8n workflows.

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Workflow Automation:** n8n
* **Machine Learning:** Scikit-learn (TF-IDF + Logistic Regression)
* **Database:** MySQL
* **Integration:** Gmail API (Google Cloud)
* **Language:** Python

---
<details>
<summary><b>Click to expand full setup & configuration</b></summary>


## 📦 Setup Instructions

Git clone my repo
cd "repo-name"

### 1️⃣ Create Virtual Environment in project folder

```bash
python -m venv venv
```
```bash
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

---

### 2️⃣ Pre Requirements 

Create a folder in the project folder called:        

```bash
trained_model
```

Requirements.txt
```bash
pip install
django
djangorestframework
scikit-learn
pandas
numpy
joblib
python-dotenv
pymysql
```

---

### 3️⃣ Setup ML Model

Prepare dataset:

```bash
cd ml_training

python prepare_dataset.py     #cleans the dataset
python train_model.py         #training the model

```
---

### 4️⃣ Run Django Backend (ML API)

```bash
cd ..             #exit from ml_training folder
cd django_project
python manage.py runserver
```

---

## ⚙️ n8n Setup

### 5️⃣ Start n8n

```bash
n8n
```

👉 Opens at: http://localhost:5678

---

### 6️⃣ Import Workflow

* Open n8n UI
* Click **Import**
* Upload `n8n workflow.json`

---

### 7️⃣ Configure Gmail Trigger

## 🔧 Post-Setup: Gmail Trigger Configuration (After Importing workflow.json)

After importing the provided `workflow.json` into n8n, follow these steps to enable Gmail integration.

---

# 🧠 Step 1 — Create Google Cloud Project

1. Go to: https://console.cloud.google.com
2. Click **Project Selector (top left)**
3. Click **New Project**
4. Name it:

```
n8n-helpdesk-system
```

5. Click **Create**

---

# ⚙️ Step 2 — Enable Gmail API

1. Navigate to:

```
APIs & Services → Library
```

2. Search for:

```
Gmail API
```

3. Click → **Enable**

---

# 🔐 Step 3 — Configure OAuth Consent Screen

1. Go to:

```
APIs & Services → OAuth consent screen
```

2. Select:

```
External
```

3. Fill required details:

| Field              | Value       |
| ------------------ | ----------- |
| App Name           | Helpdesk AI |
| User Support Email | your Gmail  |
| Developer Email    | your Gmail  |

4. Click **Save & Continue**

---

## ➕ Add Scopes

Click **Add Scopes** and include:

```
https://www.googleapis.com/auth/gmail.readonly
https://www.googleapis.com/auth/gmail.send
https://www.googleapis.com/auth/gmail.modify
```

Click **Save & Continue**

---

## 👤 Add Test User

Add your Gmail address:

```
yourgmail@gmail.com
```

Click **Save**

---

# 🔑 Step 4 — Create OAuth Credentials

1. Go to:

```
APIs & Services → Credentials
```

2. Click:

```
Create Credentials → OAuth Client ID
```

3. Select:

```
Application Type: Web Application
```

---

## Fill details:

**Name:**

```
n8n Gmail OAuth
```

---

## 🔴 IMPORTANT — Redirect URI

Add EXACTLY:

```
http://localhost:5678/rest/oauth2-credential/callback
```

(If using ngrok, replace with your HTTPS URL)

---

Click **Create**

---

## 📋 Copy Credentials

You will get:

```
Client ID
Client Secret
```

Keep these for n8n.

---

# 🔌 Step 5 — Configure Gmail Credential in n8n

1. Open n8n
2. Go to:

```
Credentials → New
```

3. Select:

```
Gmail OAuth2 API
```

---

## Fill:

| Field         | Value               |
| ------------- | ------------------- |
| Client ID     | (paste from Google) |
| Client Secret | (paste from Google) |

---

Click:

```
Connect Account
```
---

# 📥 Step 6 — Activate Gmail Trigger

1. Open the imported workflow
2. Locate **Gmail Trigger node**
3. Ensure settings:

| Option      | Value        |
| ----------- | ------------ |
| Label       | INBOX        |
| Read Status | UNREAD       |
| Poll Time   | Every Minute |

---



# 🧪 Step 7 — Add your gmails (4 diffrent gmail accounts)


Provide 4 diffrent g-mail accounts in the respective gmail nodes

---

## ✅ Expected Result

* Workflow triggers automatically
* Email is classified
* Ticket is created
* Auto-reply is sent
---

# 🗄️ MySQL Setup (Database Configuration)

Before running the workflow, you need to set up the MySQL database and required table.

---

## 🔧 Step 1 — Install MySQL

Download & install MySQL if not already installed:

👉 https://dev.mysql.com/downloads/

---

## 🔑 Step 2 — Create Database

Login to MySQL: (runs at 3306 port )

```bash
mysql -u root -p
```

Create database:

```sql
CREATE DATABASE helpdesk_db;
```

---

## 🧱 Step 3 — Create Table

Run the following SQL:

```sql
USE helpdesk_db;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT,
    category VARCHAR(100),
    timestamp DATETIME,
    email VARCHAR(255),
    status VARCHAR(50),
    assigned_to VARCHAR(100)
);
```

---

## 📦 Step 5 — Install MySQL Driver

```bash
pip install pymysql
```

## 📥 Step 8 — Configure MySQL in n8n

1. Open n8n
2. Go to **Credentials → New Credential**
3. Select **MySQL**

---

### Fill:

| Field    | Value         |
| -------- | ------------- |
| Host     | localhost     |
| Database | helpdesk_db   |
| User     | root          |
| Password | your_password |

---

Click **Save**

---

## ✅ Final Check

When workflow runs:

* Tickets should be inserted into `tickets` table
* Fields stored:

```text
text
category
timestamp
email
status
assigned_to
```

---


## ▶️ Running the System

1. Start Django backend
2. Start n8n
3. Activate workflow in n8n

👉 Now:

* Emails → captured via Gmail
* Sent to ML API
* Classified into categories
* Routed to respective teams

---

</details>
