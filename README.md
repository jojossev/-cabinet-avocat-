# Site Web Cabinet d'Avocat - Django

Un site web professionnel pour cabinet d'avocat développé avec Django.

## 🚀 Fonctionnalités

- **Page d'accueil** avec présentation du cabinet
- **Services juridiques** avec gestion dynamique
- **Présentation de l'équipe** avec profils détaillés
- **Formulaire de contact** avec validation
- **Interface d'administration** Django
- **Design responsive** et moderne
- **Système de messages** et notifications

## 📋 Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)

## 🛠️ Installation

1. **Cloner le projet**
   ```bash
   git clone <url-du-repo>
   cd cabinet-avocat
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurer la base de données**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

7. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

8. **Accéder au site**
   - Site web: http://127.0.0.1:8000/
   - Administration: http://127.0.0.1:8000/admin/

## 📁 Structure du projet

```
cabinet-avocat/
├── cabinet_avocat/          # Configuration Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── website/                 # Application principale
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/               # Templates HTML
│   ├── base.html
│   └── website/
│       ├── home.html
│       ├── services.html
│       ├── service_detail.html
│       ├── equipe.html
│       ├── avocat_detail.html
│       └── contact.html
├── static/                  # Fichiers statiques
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
├── media/                   # Fichiers uploadés
├── manage.py
├── requirements.txt
└── README.md
```

## 🎨 Personnalisation

### Ajouter des services
1. Connectez-vous à l'interface d'administration
2. Allez dans "Services"
3. Cliquez sur "Ajouter un service"
4. Remplissez les informations

### Ajouter des avocats
1. Dans l'administration, allez dans "Avocats"
2. Cliquez sur "Ajouter un avocat"
3. Remplissez le profil complet

### Modifier les informations du cabinet
1. Dans l'administration, allez dans "Informations du cabinet"
2. Modifiez les informations de contact

## 🔧 Configuration

### Variables d'environnement
Créez un fichier `.env` à la racine du projet :

```env
SECRET_KEY=votre-clé-secrète-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Configuration email (optionnel)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe
```

### Base de données
Par défaut, le projet utilise SQLite. Pour utiliser PostgreSQL ou MySQL, modifiez `settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nom_de_la_base',
        'USER': 'utilisateur',
        'PASSWORD': 'mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Déploiement

### Production
1. Modifiez `settings.py` pour la production :
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['votre-domaine.com']
   ```

2. Collectez les fichiers statiques :
   ```bash
   python manage.py collectstatic
   ```

3. Utilisez un serveur WSGI comme Gunicorn :
   ```bash
   pip install gunicorn
   gunicorn cabinet_avocat.wsgi:application
   ```

## 📝 Utilisation

### Interface d'administration
- Accédez à `/admin/`
- Connectez-vous avec votre superutilisateur
- Gérez le contenu du site

### Gestion du contenu
- **Services** : Ajoutez, modifiez ou supprimez les services juridiques
- **Avocats** : Gérez les profils de l'équipe
- **Messages** : Consultez les demandes de contact
- **Informations** : Modifiez les coordonnées du cabinet

## 🎯 Fonctionnalités avancées

- **Recherche** : Fonction de recherche dans les services et l'équipe
- **Responsive** : Design adaptatif pour tous les écrans
- **SEO** : Structure optimisée pour les moteurs de recherche
- **Sécurité** : Protection CSRF et validation des données
- **Performance** : Optimisations pour un chargement rapide

## 🤝 Contribution

1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Support

Pour toute question ou problème, n'hésitez pas à ouvrir une issue sur GitHub.

---

**Développé avec ❤️ pour les cabinets d'avocat**
