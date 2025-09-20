# 🔧 Solution GRATUITE - Créer le superutilisateur depuis votre machine

## ❌ Problème
Le shell Render n'est disponible qu'en version payante.

## ✅ Solution GRATUITE

### Créer le superutilisateur depuis votre machine locale

**Dans votre terminal local :**

1. **Installer psycopg2** (si pas déjà fait) :
   ```bash
   pip install psycopg2-binary
   ```

2. **Créer le superutilisateur** :
   ```bash
   python manage.py createsuperuser
   ```

3. **Suivre les instructions** :
   - Nom d'utilisateur : `admin` (ou votre choix)
   - Email : `admin@cabinet-avocat.com` (ou votre email)
   - Mot de passe : `admin123` (ou un mot de passe sécurisé)

### Alternative : Script automatique

**Créer un fichier `create_admin.py` :**
```python
import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings_render')
django.setup()

User = get_user_model()

# Créer le superutilisateur
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@cabinet-avocat.com',
        password='admin123'
    )
    print("Superutilisateur créé avec succès !")
else:
    print("Superutilisateur existe déjà !")
```

**Exécuter :**
```bash
python create_admin.py
```

## 🎯 Accès à l'admin
Une fois créé, accédez à l'admin sur :
**https://cabinet-avocat-7wrs.onrender.com/admin/**

## 📋 Identifiants par défaut
- **Nom d'utilisateur :** `admin`
- **Mot de passe :** `admin123`

## 🚀 Prochaines étapes
1. ✅ **Se connecter à l'admin**
2. ✅ **Ajouter du contenu** (articles, services, etc.)
3. ✅ **Personnaliser le site**

**Solution 100% gratuite depuis votre machine !** 🎯
