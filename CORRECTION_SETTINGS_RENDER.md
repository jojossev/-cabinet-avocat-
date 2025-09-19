# 🚨 CORRECTION URGENTE - Render utilise les mauvais paramètres

## 🔍 Problème identifié
Le site utilise encore `cabinet_avocat.settings` (développement) au lieu de `cabinet_avocat.settings_render` (production).

**Preuve dans les logs :**
- `Using settings module cabinet_avocat.settings` ❌
- `ALLOWED_HOSTS = []` ❌ (vide)
- `DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}` ❌ (SQLite au lieu de PostgreSQL)

## ✅ Solution immédiate

### 1. Vérifier la commande de démarrage dans Render
1. Allez sur https://dashboard.render.com
2. Cliquez sur votre service `cabinet-avocat`
3. Allez dans **"Settings"**
4. Vérifiez la section **"Build & Deploy"**
5. **Commande de démarrage** doit être :
   ```
   gunicorn cabinet_avocat.wsgi --settings=cabinet_avocat.settings_render
   ```

### 2. Si la commande est incorrecte
1. Changez la commande de démarrage vers :
   ```
   gunicorn cabinet_avocat.wsgi --settings=cabinet_avocat.settings_render
   ```
2. Cliquez sur **"Save Changes"**
3. Render va automatiquement redéployer

### 3. Vérifier les variables d'environnement
Assurez-vous que ces variables sont définies :

```
DEBUG=False
SECRET_KEY=django-insecure-votre-cle-secrete-longue-et-complexe
ALLOWED_HOSTS=cabinet-avocat-7wrs.onrender.com
DATABASE_URL=postgresql://cabinet_avocat_db_user:K0rObikDroqb8pvEp6yMcFGrfBrAF8bm@dpg-d36s2sbipnbc738i77ug-a.frankfurt-postgres.render.com/cabinet_avocat_db
```

### 4. Alternative : Utiliser le fichier render.yaml
Si vous utilisez `render.yaml`, vérifiez que la commande est correcte :

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
        value: )p0%y=nsw%bym4d99zuymlj)ashyl2*&v=qn%q(q4g*89q+o-l
      - key: ALLOWED_HOSTS
        value: cabinet-avocat-7wrs.onrender.com
      - key: DATABASE_URL
        value: postgresql://cabinet_avocat_db_user:K0rObikDroqb8pvEp6yMcFGrfBrAF8bm@dpg-d36s2sbipnbc738i77ug-a.frankfurt-postgres.render.com/cabinet_avocat_db
```

## 🎯 Résultat attendu après correction

**Logs corrects :**
- `Using settings module cabinet_avocat.settings_render` ✅
- `ALLOWED_HOSTS = ['cabinet-avocat-7wrs.onrender.com']` ✅
- `DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql'}}` ✅

## 📋 Prochaines étapes après correction

Une fois le site accessible, exécutez dans le **Shell Render** :

```bash
# Migrer la base de données PostgreSQL
python manage.py migrate --settings=cabinet_avocat.settings_render

# Collecter les fichiers statiques
python manage.py collectstatic --noinput --settings=cabinet_avocat.settings_render

# Créer le superutilisateur
python manage.py createsuperuser --settings=cabinet_avocat.settings_render
```

## 🚀 Test final
- **URL** : `https://cabinet-avocat-7wrs.onrender.com/`
- **Admin** : `https://cabinet-avocat-7wrs.onrender.com/admin/`

## ⚠️ Important
Cette correction est **CRITIQUE** car sans elle :
- ❌ Le site utilise SQLite au lieu de PostgreSQL
- ❌ Les variables d'environnement ne sont pas lues
- ❌ Les fichiers statiques ne sont pas servis correctement
- ❌ La sécurité n'est pas configurée
