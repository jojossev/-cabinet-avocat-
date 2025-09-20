# 🔧 Solution GRATUITE - Migrer la base de données

## ❌ Problème
La commande de prédéploiement n'est disponible qu'en mode payant sur Render.

## ✅ Solution GRATUITE

### Option 1 : Modifier la commande de démarrage
**Dans Render Dashboard :**
1. Allez dans **"Settings"** → **"Build & Deploy"**
2. **Commande de démarrage** : Changez de :
   ```
   gunicorn cabinet_avocat.wsgi
   ```
   **Vers :**
   ```
   python manage.py migrate && gunicorn cabinet_avocat.wsgi
   ```

### Option 2 : Modifier la commande de build
**Commande de build** : Changez de :
   ```
   pip install -r requirements.txt
   ```
   **Vers :**
   ```
   pip install -r requirements.txt && python manage.py migrate
   ```

## 🎯 Résultat attendu
Après le redéploiement :
- ✅ Tables créées dans PostgreSQL
- ✅ Site accessible sans erreur 500
- ✅ Page d'accueil s'affiche correctement
- ✅ Admin accessible sur `/admin/`

## 🚀 Recommandation
**Utilisez l'Option 1** (commande de démarrage) car elle est plus fiable :
```
python manage.py migrate && gunicorn cabinet_avocat.wsgi
```

## 📋 Prochaines étapes
1. ✅ **Migrer la base de données** (en cours)
2. ✅ **Créer le superutilisateur** 
3. ✅ **Tester le site complet**

**Solution 100% gratuite !** 🎯
