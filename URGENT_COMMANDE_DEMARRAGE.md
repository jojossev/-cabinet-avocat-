# 🚨 URGENT - Modifier la commande de démarrage

## ❌ Problème
Le script de création d'admin n'a pas été exécuté lors du déploiement.

## ✅ Solution IMMÉDIATE

### Dans Render Dashboard :
1. **Allez dans "Settings"** → **"Build & Deploy"**
2. **Commande de démarrage** : Changez de :
   ```
   python manage.py migrate && python manage.py collectstatic --noinput && gunicorn cabinet_avocat.wsgi
   ```
   **Vers :**
   ```
   python manage.py migrate && python manage.py collectstatic --noinput && python create_production_admin.py && gunicorn cabinet_avocat.wsgi
   ```

## 🎯 Résultat attendu
Après le redéploiement :
- ✅ Admin créé automatiquement
- ✅ Connexion garantie
- ✅ Accès à l'interface admin

## 🔑 Identifiants après modification :
- **URL :** https://cabinet-avocat-7wrs.onrender.com/admin/
- **Nom d'utilisateur :** `admin`
- **Mot de passe :** `admin123`

## ⚡ Action requise
**Modifiez la commande de démarrage MAINTENANT** pour que l'admin soit créé automatiquement au prochain déploiement !
