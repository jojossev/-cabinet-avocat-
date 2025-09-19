#!/usr/bin/env python
"""
Test final pour vérifier que toutes les fonctionnalités de l'interface d'administration fonctionnent
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

from website.models import *
from django.contrib import admin

def test_all_models():
    """Tester tous les modèles"""
    print("🧪 Test de tous les modèles...")
    
    models_to_test = [
        (Service, "Services"),
        (Avocat, "Avocats"),
        (ContactMessage, "Messages de contact"),
        (CabinetInfo, "Informations du cabinet"),
        (Article, "Articles"),
        (Témoignage, "Témoignages"),
        (FAQ, "FAQs"),
        (Newsletter, "Newsletter"),
        (Statistique, "Statistiques"),
    ]
    
    all_ok = True
    
    for model, name in models_to_test:
        try:
            count = model.objects.count()
            print(f"✅ {name}: {count} enregistrements")
        except Exception as e:
            print(f"❌ {name}: Erreur - {e}")
            all_ok = False
    
    return all_ok

def test_admin_registration():
    """Tester l'enregistrement des admins"""
    print("\n🔧 Test de l'enregistrement des admins...")
    
    models_to_check = [
        (Service, "ServiceAdmin"),
        (Avocat, "AvocatAdmin"),
        (ContactMessage, "ContactMessageAdmin"),
        (CabinetInfo, "CabinetInfoAdmin"),
        (Article, "ArticleAdmin"),
        (Témoignage, "TémoignageAdmin"),
        (FAQ, "FAQAdmin"),
        (Newsletter, "NewsletterAdmin"),
        (Statistique, "StatistiqueAdmin"),
    ]
    
    all_ok = True
    
    for model, admin_name in models_to_check:
        try:
            if model in admin.site._registry:
                print(f"✅ {admin_name} enregistré")
            else:
                print(f"❌ {admin_name} non enregistré")
                all_ok = False
        except Exception as e:
            print(f"❌ {admin_name}: Erreur - {e}")
            all_ok = False
    
    return all_ok

def test_data_integrity():
    """Tester l'intégrité des données"""
    print("\n📊 Test de l'intégrité des données...")
    
    try:
        # Test des services actifs
        services_actifs = Service.objects.filter(actif=True).count()
        print(f"✅ Services actifs: {services_actifs}")
        
        # Test des avocats actifs
        avocats_actifs = Avocat.objects.filter(actif=True).count()
        print(f"✅ Avocats actifs: {avocats_actifs}")
        
        # Test des messages non traités
        messages_non_traites = ContactMessage.objects.filter(traite=False).count()
        print(f"✅ Messages non traités: {messages_non_traites}")
        
        # Test des témoignages approuvés
        temoignages_approuves = Témoignage.objects.filter(approuve=True).count()
        print(f"✅ Témoignages approuvés: {temoignages_approuves}")
        
        # Test des articles actifs
        articles_actifs = Article.objects.filter(actif=True).count()
        print(f"✅ Articles actifs: {articles_actifs}")
        
        # Test des FAQs actives
        faqs_actives = FAQ.objects.filter(actif=True).count()
        print(f"✅ FAQs actives: {faqs_actives}")
        
        # Test des abonnés newsletter actifs
        newsletter_actifs = Newsletter.objects.filter(actif=True).count()
        print(f"✅ Abonnés newsletter actifs: {newsletter_actifs}")
        
        # Test des statistiques actives
        stats_actives = Statistique.objects.filter(actif=True).count()
        print(f"✅ Statistiques actives: {stats_actives}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur d'intégrité: {e}")
        return False

def test_admin_functionality():
    """Tester les fonctionnalités admin"""
    print("\n⚙️ Test des fonctionnalités admin...")
    
    try:
        # Test des list_display
        service_admin = admin.site._registry[Service]
        if 'nom' in service_admin.list_display:
            print("✅ ServiceAdmin list_display configuré")
        else:
            print("❌ ServiceAdmin list_display manquant")
            return False
        
        # Test des list_filter
        if 'actif' in service_admin.list_filter:
            print("✅ ServiceAdmin list_filter configuré")
        else:
            print("❌ ServiceAdmin list_filter manquant")
            return False
        
        # Test des search_fields
        if 'nom' in service_admin.search_fields:
            print("✅ ServiceAdmin search_fields configuré")
        else:
            print("❌ ServiceAdmin search_fields manquant")
            return False
        
        # Test des actions
        contact_admin = admin.site._registry[ContactMessage]
        if 'mark_as_treated' in contact_admin.actions:
            print("✅ ContactMessageAdmin actions configurées")
        else:
            print("❌ ContactMessageAdmin actions manquantes")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur fonctionnalités admin: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 TEST FINAL - Interface d'administration du cabinet d'avocat")
    print("=" * 70)
    
    # Tests
    models_ok = test_all_models()
    admin_ok = test_admin_registration()
    data_ok = test_data_integrity()
    functionality_ok = test_admin_functionality()
    
    print("\n" + "=" * 70)
    print("📋 RÉSULTATS DES TESTS:")
    print(f"• Modèles: {'✅ PASSÉ' if models_ok else '❌ ÉCHOUÉ'}")
    print(f"• Enregistrement Admin: {'✅ PASSÉ' if admin_ok else '❌ ÉCHOUÉ'}")
    print(f"• Intégrité des données: {'✅ PASSÉ' if data_ok else '❌ ÉCHOUÉ'}")
    print(f"• Fonctionnalités Admin: {'✅ PASSÉ' if functionality_ok else '❌ ÉCHOUÉ'}")
    
    all_tests_passed = models_ok and admin_ok and data_ok and functionality_ok
    
    print("\n" + "=" * 70)
    if all_tests_passed:
        print("🎉 TOUS LES TESTS SONT PASSÉS !")
        print("\n✅ L'interface d'administration est parfaitement fonctionnelle !")
        print("\n🚀 Vous pouvez maintenant utiliser votre site :")
        print("• Site web: http://127.0.0.1:8000/")
        print("• Administration: http://127.0.0.1:8000/admin/")
        print("• Utilisateur: admin")
        print("• Mot de passe: admin123")
        print("\n📊 Fonctionnalités disponibles :")
        print("• Gestion des services juridiques")
        print("• Gestion des avocats et profils")
        print("• Suivi des messages de contact")
        print("• Modération des témoignages")
        print("• Publication d'articles de blog")
        print("• Gestion des FAQs")
        print("• Gestion de la newsletter")
        print("• Configuration des statistiques")
        print("• Paramètres du cabinet")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("Vérifiez les erreurs ci-dessus et corrigez-les.")

if __name__ == '__main__':
    main()
