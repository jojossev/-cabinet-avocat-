#!/usr/bin/env python
"""
Script pour synchroniser l'admin local avec la production
"""
import os
import django
from django.contrib.auth import get_user_model
from django.core.management import call_command

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

User = get_user_model()

def sync_admin_to_production():
    """Synchroniser l'admin avec la production"""
    
    print("🔄 SYNCHRONISATION AVEC LA PRODUCTION...")
    
    # Créer un fichier de données pour la production
    print("📝 Création du fichier de données...")
    
    # Exporter les utilisateurs
    call_command('dumpdata', 'auth.User', '--indent=2', '--output=admin_data.json')
    
    print("✅ Fichier admin_data.json créé")
    
    # Instructions pour la production
    print("\n🚀 INSTRUCTIONS POUR LA PRODUCTION:")
    print("1. Allez sur Render Dashboard")
    print("2. Ouvrez le shell (si disponible) ou utilisez la console")
    print("3. Exécutez ces commandes:")
    print("   python manage.py shell")
    print("   from django.contrib.auth import get_user_model")
    print("   User = get_user_model()")
    print("   User.objects.filter(is_superuser=True).delete()")
    print("   admin = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')")
    print("   print('Admin créé:', admin.username)")
    
    print("\n🔑 IDENTIFIANTS GARANTIS:")
    print("   - Nom d'utilisateur: admin")
    print("   - Mot de passe: admin123")
    print("   - Email: admin@test.com")
    
    print("\n🌐 URL ADMIN:")
    print("   https://cabinet-avocat-7wrs.onrender.com/admin/")

if __name__ == "__main__":
    sync_admin_to_production()
