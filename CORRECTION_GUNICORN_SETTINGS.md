# 🔧 Correction commande Gunicorn - Variable d'environnement

## 🚨 Problème identifié
Gunicorn ne reconnaît pas l'argument `--settings`. Il faut utiliser la variable d'environnement `DJANGO_SETTINGS_MODULE`.

## ✅ Solution correcte

### 1. Commande de démarrage correcte
**Changez la commande de démarrage vers :**
```
gunicorn cabinet_avocat.wsgi
```

### 2. Ajoutez la variable d'environnement
**Dans les variables d'environnement de Render, ajoutez :**
```
DJANGO_SETTINGS_MODULE=cabinet_avocat.settings_render
```

## 📋 Variables d'environnement complètes

Assurez-vous que ces variables sont définies dans Render :

```
DEBUG=False
SECRET_KEY=django-insecure-votre-cle-secrete-longue-et-complexe
ALLOWED_HOSTS=cabinet-avocat-7wrs.onrender.com
DATABASE_URL=postgresql://cabinet_avocat_db_user:K0rObikDroqb8pvEp6yMcFGrfBrAF8bm@dpg-d36s2sbipnbc738i77ug-a.frankfurt-postgres.render.com/cabinet_avocat_db
DJANGO_SETTINGS_MODULE=cabinet_avocat.settings_render
```

## 🎯 Configuration finale

### Commande de démarrage :
```
gunicorn cabinet_avocat.wsgi
```

### Variables d'environnement :
- `DJANGO_SETTINGS_MODULE` = `cabinet_avocat.settings_render`
- `DEBUG` = `False`
- `SECRET_KEY` = `django-insecure-votre-cle-secrete-longue-et-complexe`
- `ALLOWED_HOSTS` = `cabinet-avocat-7wrs.onrender.com`
- `DATABASE_URL` = `postgresql://cabinet_avocat_db_user:K0rObikDroqb8pvEp6yMcFGrfBrAF8bm@dpg-d36s2sbipnbc738i77ug-a.frankfurt-postgres.render.com/cabinet_avocat_db`

## 🚀 Résultat attendu
Après cette correction :
- ✅ Gunicorn démarre sans erreur
- ✅ Django utilise `cabinet_avocat.settings_render`
- ✅ PostgreSQL au lieu de SQLite
- ✅ Variables d'environnement lues correctement
- ✅ Site accessible sur `https://cabinet-avocat-7wrs.onrender.com/`
