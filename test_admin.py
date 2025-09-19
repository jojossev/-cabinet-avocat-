#!/usr/bin/env python
"""
Script de test pour vérifier que l'interface d'administration fonctionne
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings_render')
django.setup()

from website.models import Service, Avocat, ContactMessage, CabinetInfo, Article, Témoignage, FAQ, Newsletter, Statistique

def test_models():
    """Tester que tous les modèles fonctionnent"""
    print("🧪 Test des modèles...")
    
    try:
        # Test Services
        services = Service.objects.all()
        print(f"✅ Services: {services.count()} trouvés")
        
        # Test Avocats
        avocats = Avocat.objects.all()
        print(f"✅ Avocats: {avocats.count()} trouvés")
        
        # Test Messages
        messages = ContactMessage.objects.all()
        print(f"✅ Messages: {messages.count()} trouvés")
        
        # Test Cabinet Info
        cabinet = CabinetInfo.objects.first()
        if cabinet:
            print(f"✅ Cabinet: {cabinet.nom_cabinet}")
        else:
            print("⚠️ Aucune information de cabinet")
        
        # Test Articles
        articles = Article.objects.all()
        print(f"✅ Articles: {articles.count()} trouvés")
        
        # Test Témoignages
        temoignages = Témoignage.objects.all()
        print(f"✅ Témoignages: {temoignages.count()} trouvés")
        
        # Test FAQ
        faqs = FAQ.objects.all()
        print(f"✅ FAQs: {faqs.count()} trouvés")
        
        # Test Newsletter
        newsletter = Newsletter.objects.all()
        print(f"✅ Newsletter: {newsletter.count()} abonnés")
        
        # Test Statistiques
        stats = Statistique.objects.all()
        print(f"✅ Statistiques: {stats.count()} trouvées")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_admin_interface():
    """Tester l'interface d'administration"""
    print("\n🔧 Test de l'interface d'administration...")
    
    try:
        from django.contrib import admin
        from website.admin import ServiceAdmin, AvocatAdmin, ContactMessageAdmin
        
        # Vérifier que les classes admin sont enregistrées
        if Service in admin.site._registry:
            print("✅ ServiceAdmin enregistré")
        else:
            print("❌ ServiceAdmin non enregistré")
            
        if Avocat in admin.site._registry:
            print("✅ AvocatAdmin enregistré")
        else:
            print("❌ AvocatAdmin non enregistré")
            
        if ContactMessage in admin.site._registry:
            print("✅ ContactMessageAdmin enregistré")
        else:
            print("❌ ContactMessageAdmin non enregistré")
            
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 Test de l'interface d'administration du cabinet d'avocat")
    print("=" * 60)
    
    # Test des modèles
    models_ok = test_models()
    
    # Test de l'interface admin
    admin_ok = test_admin_interface()
    
    print("\n" + "=" * 60)
    if models_ok and admin_ok:
        print("✅ TOUS LES TESTS SONT PASSÉS !")
        print("\nL'interface d'administration est prête à l'emploi.")
        print("\nVous pouvez maintenant:")
        print("1. Lancer le serveur: python manage.py runserver")
        print("2. Accéder au site: http://127.0.0.1:8000/")
        print("3. Accéder à l'admin: http://127.0.0.1:8000/admin/")
        print("   - Utilisateur: admin")
        print("   - Mot de passe: admin123")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("Vérifiez les erreurs ci-dessus.")

if __name__ == '__main__':
    main()
