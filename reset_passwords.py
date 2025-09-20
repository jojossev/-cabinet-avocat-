#!/usr/bin/env python
"""
Script pour réinitialiser les mots de passe des superutilisateurs
"""
import os
import django
from django.contrib.auth import get_user_model

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

User = get_user_model()

def reset_passwords():
    """Réinitialiser les mots de passe des superutilisateurs"""
    
    # Nouveau mot de passe simple
    new_password = "admin123"
    
    # Trouver tous les superutilisateurs
    superusers = User.objects.filter(is_superuser=True)
    
    if not superusers.exists():
        print("❌ Aucun superutilisateur trouvé !")
        return
    
    print("🔧 Réinitialisation des mots de passe...")
    print(f"📝 Nouveau mot de passe: {new_password}")
    print()
    
    for user in superusers:
        try:
            user.set_password(new_password)
            user.save()
            print(f"✅ {user.username} - Mot de passe réinitialisé")
            print(f"   Email: {user.email}")
            print(f"   Mot de passe: {new_password}")
            print()
        except Exception as e:
            print(f"❌ Erreur pour {user.username}: {e}")
    
    print("🌐 Accès à l'admin:")
    print("   https://cabinet-avocat-7wrs.onrender.com/admin/")
    print()
    print("📋 Identifiants mis à jour:")
    for user in superusers:
        print(f"   - {user.username} / {new_password}")

if __name__ == "__main__":
    reset_passwords()
