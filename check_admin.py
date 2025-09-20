#!/usr/bin/env python
"""
Script pour vérifier et créer un superutilisateur admin
"""
import os
import django
from django.contrib.auth import get_user_model

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

User = get_user_model()

def check_and_create_admin():
    """Vérifier et créer un superutilisateur admin"""
    
    print("🔍 Vérification des utilisateurs existants...")
    
    # Lister tous les utilisateurs
    users = User.objects.all()
    print(f"📊 Nombre total d'utilisateurs: {users.count()}")
    
    for user in users:
        print(f"   - {user.username} (Email: {user.email}, Superuser: {user.is_superuser})")
    
    # Vérifier si admin existe
    admin_user = User.objects.filter(username='admin').first()
    
    if admin_user:
        print(f"\n✅ Utilisateur 'admin' trouvé!")
        print(f"   - Email: {admin_user.email}")
        print(f"   - Superuser: {admin_user.is_superuser}")
        print(f"   - Actif: {admin_user.is_active}")
        
        # Réinitialiser le mot de passe
        admin_user.set_password('admin123')
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.is_active = True
        admin_user.save()
        
        print(f"✅ Mot de passe réinitialisé pour 'admin'")
        print(f"   - Nouveau mot de passe: admin123")
        
    else:
        print(f"\n❌ Utilisateur 'admin' non trouvé!")
        print("🔧 Création d'un nouvel utilisateur admin...")
        
        # Créer un nouvel admin
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@cabinet-avocat.com',
            password='admin123'
        )
        
        print(f"✅ Nouvel utilisateur 'admin' créé!")
        print(f"   - Email: {admin_user.email}")
        print(f"   - Mot de passe: admin123")
    
    print(f"\n🌐 Accès à l'admin:")
    print(f"   URL: https://cabinet-avocat-7wrs.onrender.com/admin/")
    print(f"   Nom d'utilisateur: admin")
    print(f"   Mot de passe: admin123")

if __name__ == "__main__":
    check_and_create_admin()
