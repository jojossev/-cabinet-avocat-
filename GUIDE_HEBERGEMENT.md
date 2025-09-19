# 🚀 Guide d'Hébergement - Cabinet d'Avocat

## 🌐 Options d'hébergement recommandées

### 🥇 **Option 1 : Heroku (Recommandé pour débuter)**

#### ✅ **Avantages :**
- **Gratuit** pour commencer
- **Simple** à déployer
- **Automatique** : Git push = déploiement
- **Base de données** incluse
- **SSL** automatique

#### 📋 **Étapes de déploiement :**

1. **Créer un compte Heroku**
   ```bash
   # Installer Heroku CLI
   # Aller sur https://heroku.com
   ```

2. **Préparer le projet**
   ```bash
   # Créer requirements.txt (déjà fait)
   # Créer Procfile
   # Configurer les variables d'environnement
   ```

3. **Déployer**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku create cabinet-avocat
   git push heroku main
   ```

### 🥈 **Option 2 : Railway (Moderne et simple)**

#### ✅ **Avantages :**
- **Interface moderne**
- **Déploiement automatique**
- **Base de données PostgreSQL**
- **Prix abordable**

#### 📋 **Étapes :**
1. Aller sur https://railway.app
2. Connecter votre GitHub
3. Sélectionner le repository
4. Railway déploie automatiquement

### 🥉 **Option 3 : DigitalOcean App Platform**

#### ✅ **Avantages :**
- **Performance excellente**
- **Prix compétitif**
- **Interface intuitive**
- **Base de données gérée**

## 🔧 Configuration pour l'hébergement

### 📝 **1. Créer le fichier Procfile**
```bash
web: gunicorn cabinet_avocat.wsgi --log-file -
```

### 📝 **2. Mettre à jour requirements.txt**
```txt
Django==4.2.10
gunicorn==21.2.0
psycopg2-binary==2.9.7
whitenoise==6.6.0
python-decouple==3.8
```

### 📝 **3. Configurer les variables d'environnement**
```python
# Dans settings.py
import os
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Base de données
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

# Fichiers statiques
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 📝 **4. Créer .env pour le développement**
```env
DEBUG=True
SECRET_KEY=votre-cle-secrete-developpement
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=cabinet_avocat
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

## 🚀 Déploiement étape par étape

### 📋 **Préparation du projet**

1. **Installer les dépendances**
   ```bash
   pip install gunicorn psycopg2-binary whitenoise python-decouple
   ```

2. **Créer Procfile**
   ```bash
   echo "web: gunicorn cabinet_avocat.wsgi --log-file -" > Procfile
   ```

3. **Mettre à jour requirements.txt**
   ```bash
   pip freeze > requirements.txt
   ```

4. **Configurer les fichiers statiques**
   ```python
   # Dans settings.py
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

### 🌐 **Déploiement sur Heroku**

1. **Créer un compte Heroku**
   - Aller sur https://heroku.com
   - Créer un compte gratuit

2. **Installer Heroku CLI**
   - Télécharger depuis https://devcenter.heroku.com/articles/heroku-cli

3. **Se connecter**
   ```bash
   heroku login
   ```

4. **Créer l'application**
   ```bash
   heroku create cabinet-avocat-votre-nom
   ```

5. **Configurer les variables**
   ```bash
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=votre-cle-secrete-production
   heroku config:set ALLOWED_HOSTS=cabinet-avocat-votre-nom.herokuapp.com
   ```

6. **Ajouter la base de données**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

7. **Déployer**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

8. **Migrer la base de données**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### 🌐 **Déploiement sur Railway**

1. **Aller sur Railway**
   - https://railway.app
   - Se connecter avec GitHub

2. **Créer un nouveau projet**
   - "New Project"
   - "Deploy from GitHub repo"

3. **Sélectionner le repository**
   - Choisir votre repository cabinet-avocat

4. **Configurer les variables**
   - DEBUG=False
   - SECRET_KEY=votre-cle-secrete
   - ALLOWED_HOSTS=votre-domaine.railway.app

5. **Railway déploie automatiquement**

## 🔐 Configuration de sécurité

### 🛡️ **Variables d'environnement importantes**

```env
# Production
DEBUG=False
SECRET_KEY=votre-cle-secrete-tres-longue-et-complexe
ALLOWED_HOSTS=votre-domaine.com,www.votre-domaine.com
DB_NAME=cabinet_avocat_prod
DB_USER=utilisateur_db
DB_PASSWORD=mot-de-passe-securise
DB_HOST=localhost
DB_PORT=5432
```

### 🔒 **Sécurité Django**

```python
# Dans settings.py
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

## 📊 Monitoring et maintenance

### 📈 **Outils recommandés**

1. **Sentry** - Monitoring des erreurs
2. **Google Analytics** - Statistiques de visite
3. **Uptime Robot** - Surveillance de disponibilité

### 🔄 **Sauvegarde**

```bash
# Sauvegarde de la base de données
heroku pg:backups:capture
heroku pg:backups:download
```

## 💰 Coûts estimés

### 🆓 **Gratuit (début)**
- **Heroku** : 0€/mois (limité)
- **Railway** : 0€/mois (limité)

### 💵 **Payant (production)**
- **Heroku** : 7€/mois
- **Railway** : 5€/mois
- **DigitalOcean** : 12€/mois

## 🎯 Recommandation finale

### 🥇 **Pour commencer : Railway**
- Interface moderne
- Déploiement simple
- Prix abordable
- Bonne performance

### 🥈 **Pour la production : DigitalOcean**
- Performance excellente
- Support professionnel
- Évolutivité
- Fiabilité

## 🚀 Prochaines étapes

1. **Choisir une plateforme**
2. **Préparer le projet** (Procfile, requirements.txt)
3. **Configurer les variables d'environnement**
4. **Déployer**
5. **Tester en production**
6. **Configurer un nom de domaine**

**Votre cabinet d'avocat sera bientôt en ligne !** 🌐✨
