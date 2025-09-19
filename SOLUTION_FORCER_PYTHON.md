# 🚨 SOLUTION - Forcer Python 3.11 dans Render

## ❌ Problème persistant
Render ignore complètement notre fichier `runtime.txt` et utilise toujours Python 3.13.4. Il faut utiliser une approche différente.

## ✅ Solution : Modifier la commande de build

### 1. Changer la commande de build
**Dans Render Dashboard :**
1. Allez dans **"Settings"** → **"Build & Deploy"**
2. **Commande de build** : Changez de :
   ```
   pip install -r requirements.txt
   ```
   Vers :
   ```
   python3.11 -m pip install -r requirements.txt
   ```

### 2. Alternative : Utiliser pyenv
**Commande de build :**
```
pyenv install 3.11.9 && pyenv local 3.11.9 && pip install -r requirements.txt
```

### 3. Alternative : Spécifier Python dans requirements.txt
**Ajoutez cette ligne au début de `requirements.txt` :**
```
--python-version 3.11
```

### 4. Alternative : Utiliser un Dockerfile
**Créer un fichier `Dockerfile` :**
```dockerfile
FROM python:3.11.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 10000

CMD ["gunicorn", "cabinet_avocat.wsgi"]
```

## 🎯 Résultat attendu
Avec Python 3.11 :
- ✅ Django lira les variables d'environnement
- ✅ `ALLOWED_HOSTS = ['cabinet-avocat-7wrs.onrender.com']`
- ✅ Site accessible sur `https://cabinet-avocat-7wrs.onrender.com/`

## 📋 Variables d'environnement à vérifier
```
DEBUG=False
SECRET_KEY=django-insecure-votre-cle-secrete-longue-et-complexe
ALLOWED_HOSTS=cabinet-avocat-7wrs.onrender.com
DATABASE_URL=postgresql://cabinet_avocat_db_user:K0rObikDroqb8pvEp6yMcFGrfBrAF8bm@dpg-d36s2sbipnbc738i77ug-a.frankfurt-postgres.render.com/cabinet_avocat_db
DJANGO_SETTINGS_MODULE=cabinet_avocat.settings_render
```

## 🚀 Prochaines étapes
Une fois le site accessible :
1. Migrer la base de données PostgreSQL
2. Créer le superutilisateur
3. Tester le site complet

**Render ignore notre fichier runtime.txt !** 🎯
