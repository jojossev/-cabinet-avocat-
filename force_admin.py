#!/usr/bin/env python
"""
Script pour forcer la création d'un superutilisateur admin
"""
import os
import django
from django.contrib.auth import get_user_model

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

User = get_user_model()

def force_create_admin():
    """Forcer la création d'un superutilisateur admin"""
    
    print("🔧 FORCE CRÉATION D'UN NOUVEL ADMIN...")
    
    # Supprimer tous les anciens admins
    print("🗑️ Suppression des anciens utilisateurs admin...")
    User.objects.filter(is_superuser=True).delete()
    print("✅ Anciens admins supprimés")
    
    # Créer un nouvel admin simple
    print("🆕 Création d'un nouvel admin...")
    
    try:
        # Créer l'utilisateur
        admin_user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )
        
        # Le rendre superutilisateur
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.is_active = True
        admin_user.save()
        
        print("✅ NOUVEL ADMIN CRÉÉ AVEC SUCCÈS!")
        print(f"   - Nom d'utilisateur: admin")
        print(f"   - Email: admin@test.com")
        print(f"   - Mot de passe: admin123")
        print(f"   - Superuser: {admin_user.is_superuser}")
        print(f"   - Staff: {admin_user.is_staff}")
        print(f"   - Actif: {admin_user.is_active}")
        
        # Vérifier la connexion
        print("\n🔍 Test de connexion...")
        from django.contrib.auth import authenticate
        user = authenticate(username='admin', password='admin123')
        
        if user:
            print("✅ CONNEXION TESTÉE ET FONCTIONNE!")
        else:
            print("❌ Problème de connexion détecté")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        
        # Essayer avec un nom différent
        try:
            admin_user = User.objects.create_user(
                username='superuser',
                email='super@test.com',
                password='admin123'
            )
            
            admin_user.is_superuser = True
            admin_user.is_staff = True
            admin_user.is_active = True
            admin_user.save()
            
            print("✅ ADMIN ALTERNATIF CRÉÉ!")
            print(f"   - Nom d'utilisateur: superuser")
            print(f"   - Mot de passe: admin123")
            
        except Exception as e2:
            print(f"❌ Erreur alternative: {e2}")
    
    print(f"\n🌐 ACCÈS À L'ADMIN:")
    print(f"   URL: https://cabinet-avocat-7wrs.onrender.com/admin/")
    print(f"   Nom d'utilisateur: admin")
    print(f"   Mot de passe: admin123")
    
    print(f"\n📋 SI ÇA NE MARCHE PAS, ESSAYEZ:")
    print(f"   Nom d'utilisateur: superuser")
    print(f"   Mot de passe: admin123")

if __name__ == "__main__":
    force_create_admin()
