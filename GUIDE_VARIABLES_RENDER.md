# 🔧 Guide Variables d'Environnement Render

## 📁 **Fichiers créés pour l'export**

J'ai créé plusieurs formats de fichiers que vous pouvez utiliser :

### 📄 **1. Fichier texte simple :**
- `VARIABLES_ENVIRONNEMENT_RENDER.txt` - Format texte avec instructions

### 📊 **2. Fichier JSON :**
- `VARIABLES_ENVIRONNEMENT_RENDER.json` - Format JSON structuré

### 📈 **3. Fichier CSV :**
- `VARIABLES_ENVIRONNEMENT_RENDER.csv` - Format CSV pour tableur

## 🚀 **Utilisation des fichiers**

### **📋 Méthode 1 : Copier-coller depuis le fichier texte**

1. Ouvrir `VARIABLES_ENVIRONNEMENT_RENDER.txt`
2. Copier les variables
3. Coller dans Render

### **📋 Méthode 2 : Utiliser le fichier CSV**

1. Ouvrir `VARIABLES_ENVIRONNEMENT_RENDER.csv` dans Excel/LibreOffice
2. Voir les variables en format tableau
3. Copier-coller dans Render

### **📋 Méthode 3 : Utiliser le fichier JSON**

1. Ouvrir `VARIABLES_ENVIRONNEMENT_RENDER.json`
2. Voir la structure des variables
3. Copier-coller dans Render

## 🔧 **Variables à configurer dans Render**

### **Variables d'environnement :**

| Clé | Valeur |
|-----|--------|
| `DEBUG` | `False` |
| `SECRET_KEY` | `django-insecure-votre-cle-secrete-longue-et-complexe` |
| `ALLOWED_HOSTS` | `cabinet-avocat-9h1y.onrender.com` |
| `DATABASE_URL` | `postgresql://cabinet_avocat_db_user:K0rObikDroqb8pvEp6yMcFGrfBrAF8bm@dpg-d36s2sbipnbc738i77ug-a.frankfurt-postgres.render.com/cabinet_avocat_db` |

## 📝 **Instructions étape par étape**

### **1️⃣ Aller dans Render :**
1. Ouvrir https://render.com
2. Aller dans votre service web `-cabinet-avocat-`
3. Cliquer sur **"Environment"**
4. Cliquer sur **"Environment Variables"**

### **2️⃣ Nettoyer les variables existantes :**
1. Supprimer toutes les variables existantes
2. Cliquer sur **"Supprimer"** pour chaque variable

### **3️⃣ Ajouter les nouvelles variables :**
1. Cliquer sur **"Ajouter"**
2. Copier-coller chaque variable depuis les fichiers créés
3. Répéter pour les 4 variables

### **4️⃣ Déployer :**
1. Cliquer sur **"Enregistrez, reconstruisez et déployer"**
2. Attendre que le déploiement se termine

### **5️⃣ Migrations :**
1. Aller dans **"Shell"**
2. Exécuter :
```bash
python manage.py migrate
python manage.py createsuperuser
```

## 🎯 **Résultat final**

Votre site sera disponible à :
- **Site principal :** https://cabinet-avocat-9h1y.onrender.com
- **Administration :** https://cabinet-avocat-9h1y.onrender.com/admin/

## 🆘 **En cas de problème**

### **Vérifications :**
1. Vérifier que les 4 variables sont bien configurées
2. Vérifier qu'il n'y a pas de doublons
3. Vérifier que les valeurs sont exactes
4. Vérifier les logs de déploiement

### **Support :**
- **Render Docs :** https://render.com/docs/environment-variables
- **Django + PostgreSQL :** https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes

## 🎉 **Félicitations !**

Votre cabinet d'avocat sera bientôt en ligne avec une base de données PostgreSQL fonctionnelle ! 🚀✨
