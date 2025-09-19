# 🗄️ Guide Base de Données Render - Cabinet d'Avocat

## 🎯 **Configuration de la base de données PostgreSQL dans Render**

### 📋 **Étape 1 : Créer la base de données PostgreSQL**

#### **1️⃣ Dans votre dashboard Render :**
1. Cliquer sur **"New +"**
2. Sélectionner **"PostgreSQL"**
3. **Name :** `cabinet-avocat-db`
4. **Plan :** `Free` (gratuit)
5. **Region :** Choisir la région la plus proche
6. Cliquer sur **"Create Database"**

#### **2️⃣ Render va créer votre base de données :**
- ✅ **Host :** `dpg-xxxxx-a.oregon-postgres.render.com`
- ✅ **Port :** `5432`
- ✅ **Database :** `cabinet_avocat_db`
- ✅ **User :** `cabinet_avocat_user`
- ✅ **Password :** `xxxxxxxxxxxxxxxx`

---

### 📋 **Étape 2 : Configurer les variables d'environnement**

#### **1️⃣ Dans votre service web :**
1. Aller dans **"Environment"**
2. Cliquer sur **"Environment Variables"**
3. Ajouter ces variables :

```
DEBUG=False
SECRET_KEY=django-insecure-votre-cle-secrete-longue-et-complexe
ALLOWED_HOSTS=votre-domaine.onrender.com
DATABASE_URL=postgresql://cabinet_avocat_user:password@dpg-xxxxx-a.oregon-postgres.render.com:5432/cabinet_avocat_db
```

#### **2️⃣ Variables détaillées (optionnel) :**
Si vous préférez les variables séparées :
```
DB_NAME=cabinet_avocat_db
DB_USER=cabinet_avocat_user
DB_PASSWORD=votre-mot-de-passe
DB_HOST=dpg-xxxxx-a.oregon-postgres.render.com
DB_PORT=5432
```

---

### 📋 **Étape 3 : Modifier les settings Django**

#### **1️⃣ Créer un fichier settings pour Render :**
```python
# cabinet_avocat/settings_render.py
import os
from decouple import config
from .settings import *

# Configuration de production
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Base de données PostgreSQL pour Render
import dj_database_url

# Si DATABASE_URL est définie, l'utiliser
if config('DATABASE_URL', default=None):
    DATABASES = {
        'default': dj_database_url.parse(config('DATABASE_URL'))
    }
else:
    # Sinon, utiliser les variables séparées
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
    }

# Fichiers statiques avec WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Configuration de sécurité
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Configuration SSL
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

#### **2️⃣ Modifier le Procfile :**
```
web: gunicorn cabinet_avocat.wsgi --settings=cabinet_avocat.settings_render
```

---

### 📋 **Étape 4 : Migrations et superutilisateur**

#### **1️⃣ Dans Render, aller dans votre service web :**
1. Cliquer sur **"Shell"**
2. Exécuter les commandes :

```bash
# Migrer la base de données
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser
```

#### **2️⃣ Commandes de migration :**
```bash
# Si vous avez des données à importer
python manage.py loaddata initial_data.json

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
```

---

### 📋 **Étape 5 : Vérification**

#### **1️⃣ Vérifier la connexion :**
1. Aller sur votre site : `https://votre-domaine.onrender.com`
2. Tester l'administration : `https://votre-domaine.onrender.com/admin/`
3. Se connecter avec le superutilisateur créé

#### **2️⃣ Vérifier les logs :**
1. Dans Render → **"Logs"**
2. Vérifier qu'il n'y a pas d'erreurs de base de données

---

## 🔧 **Configuration automatique avec render.yaml**

### 📝 **Fichier render.yaml complet :**
```yaml
services:
  - type: web
    name: cabinet-avocat
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn cabinet_avocat.wsgi --settings=cabinet_avocat.settings_render
    envVars:
      - key: DEBUG
        value: False
      - key: SECRET_KEY
        value: django-insecure-votre-cle-secrete-longue-et-complexe
      - key: ALLOWED_HOSTS
        value: votre-domaine.onrender.com
      - key: DATABASE_URL
        fromDatabase:
          name: cabinet-avocat-db
          property: connectionString
    healthCheckPath: /
    
  - type: pserv
    name: cabinet-avocat-db
    env: postgresql
    plan: free
```

---

## 🆘 **En cas de problème**

### 🔍 **Erreurs courantes :**

#### **1️⃣ Erreur de connexion à la base de données :**
- Vérifier que `DATABASE_URL` est correcte
- Vérifier que la base de données est démarrée
- Vérifier les variables d'environnement

#### **2️⃣ Erreur de migration :**
```bash
# Réinitialiser les migrations
python manage.py migrate --fake-initial
```

#### **3️⃣ Erreur de fichiers statiques :**
```bash
# Recollecter les fichiers statiques
python manage.py collectstatic --noinput --clear
```

### 📞 **Support :**
- **Render Docs :** https://render.com/docs/databases
- **Django + PostgreSQL :** https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes

---

## 🎉 **Résultat final**

Votre cabinet d'avocat aura :
- ✅ **Base de données PostgreSQL** fonctionnelle
- ✅ **Données persistantes** (ne se perdent pas)
- ✅ **Administration** complète
- ✅ **Sauvegarde automatique** (Render gère les backups)
- ✅ **Performance optimale**

**Votre site sera maintenant complètement fonctionnel avec une vraie base de données !** 🚀✨
