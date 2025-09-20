#!/usr/bin/env python
"""
Script pour créer automatiquement un admin en production
"""
import os
import django
from django.contrib.auth import get_user_model

# Configuration Django pour la production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings_render')
django.setup()

User = get_user_model()

def create_production_admin():
    """Créer un admin en production"""
    
    print("🚀 CRÉATION ADMIN EN PRODUCTION...")
    
    try:
        # Supprimer les anciens admins
        User.objects.filter(is_superuser=True).delete()
        print("✅ Anciens admins supprimés")
        
        # Créer le nouvel admin
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )
        
        print("✅ ADMIN CRÉÉ EN PRODUCTION!")
        print(f"   - Nom d'utilisateur: {admin.username}")
        print(f"   - Email: {admin.email}")
        print(f"   - Mot de passe: admin123")
        print(f"   - Superuser: {admin.is_superuser}")
        print(f"   - Staff: {admin.is_staff}")
        print(f"   - Actif: {admin.is_active}")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        
        # Essayer avec un nom différent
        try:
            admin = User.objects.create_superuser(
                username='superuser',
                email='super@test.com',
                password='admin123'
            )
            print("✅ ADMIN ALTERNATIF CRÉÉ!")
            print(f"   - Nom d'utilisateur: superuser")
            print(f"   - Mot de passe: admin123")
        except Exception as e2:
            print(f"❌ Erreur alternative: {e2}")

if __name__ == "__main__":
    create_production_admin()
