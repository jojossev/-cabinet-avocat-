#!/usr/bin/env python
"""
Script pour créer automatiquement un superutilisateur
"""
import os
import django
from django.contrib.auth import get_user_model

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

User = get_user_model()

def create_superuser():
    """Créer un superutilisateur automatiquement"""
    
    # Vérifier si un superutilisateur existe déjà
    if User.objects.filter(is_superuser=True).exists():
        print("✅ Un superutilisateur existe déjà !")
        superusers = User.objects.filter(is_superuser=True)
        for user in superusers:
            print(f"   - {user.username} ({user.email})")
        return
    
    # Créer le superutilisateur
    try:
        user = User.objects.create_superuser(
            username='admin',
            email='admin@cabinet-avocat.com',
            password='admin123'
        )
        print("🎉 Superutilisateur créé avec succès !")
        print(f"   - Nom d'utilisateur: {user.username}")
        print(f"   - Email: {user.email}")
        print(f"   - Mot de passe: admin123")
        print("\n🌐 Accès à l'admin:")
        print("   https://cabinet-avocat-7wrs.onrender.com/admin/")
        
    except Exception as e:
        print(f"❌ Erreur lors de la création: {e}")
        
        # Essayer avec un nom différent
        try:
            user = User.objects.create_superuser(
                username='superuser',
                email='superuser@cabinet-avocat.com',
                password='admin123'
            )
            print("🎉 Superutilisateur créé avec succès (nom: superuser) !")
            print(f"   - Nom d'utilisateur: {user.username}")
            print(f"   - Email: {user.email}")
            print(f"   - Mot de passe: admin123")
            print("\n🌐 Accès à l'admin:")
            print("   https://cabinet-avocat-7wrs.onrender.com/admin/")
            
        except Exception as e2:
            print(f"❌ Erreur avec le nom alternatif: {e2}")

if __name__ == "__main__":
    print("🔧 Création du superutilisateur...")
    create_superuser()
