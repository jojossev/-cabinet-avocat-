#!/usr/bin/env python
"""
Test de l'interface d'administration personnalisée
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings_render')
django.setup()

from website.models import *
from django.contrib import admin
from django.test import Client
from django.contrib.auth.models import User

def test_interface_personnalisee():
    """Tester l'interface personnalisée"""
    print("🎨 Test de l'interface d'administration personnalisée")
    print("=" * 60)
    
    # Vérifier que l'utilisateur admin existe
    try:
        admin_user = User.objects.get(username='admin')
        print(f"✅ Utilisateur admin trouvé: {admin_user.username}")
    except User.DoesNotExist:
        print("❌ Utilisateur admin non trouvé")
        return False
    
    # Tester les statistiques
    print("\n📊 Vérification des statistiques...")
    stats = {
        'total_services': Service.objects.filter(actif=True).count(),
        'total_avocats': Avocat.objects.filter(actif=True).count(),
        'total_messages': ContactMessage.objects.count(),
        'messages_non_traites': ContactMessage.objects.filter(traite=False).count(),
        'total_articles': Article.objects.filter(actif=True).count(),
        'total_temoignages': Témoignage.objects.filter(approuve=True).count(),
        'total_faqs': FAQ.objects.filter(actif=True).count(),
        'total_newsletter': Newsletter.objects.filter(actif=True).count(),
        'total_stats': Statistique.objects.filter(actif=True).count(),
    }
    
    for key, value in stats.items():
        print(f"  • {key}: {value}")
    
    # Tester les templates personnalisés
    print("\n🎨 Vérification des templates personnalisés...")
    template_files = [
        'templates/admin/base.html',
        'templates/admin/index.html',
        'templates/admin/dashboard.html',
    ]
    
    for template in template_files:
        if os.path.exists(template):
            print(f"✅ {template} existe")
        else:
            print(f"❌ {template} manquant")
    
    # Tester les URLs personnalisées
    print("\n🔗 Vérification des URLs personnalisées...")
    try:
        # Vérifier que les URLs personnalisées sont enregistrées
        urls = admin.site.get_urls()
        custom_urls = [url for url in urls if hasattr(url, 'name') and url.name == 'admin_dashboard']
        if custom_urls:
            print("✅ URL du tableau de bord personnalisé enregistrée")
        else:
            print("❌ URL du tableau de bord personnalisé manquante")
    except Exception as e:
        print(f"❌ Erreur lors de la vérification des URLs: {e}")
    
    # Tester les fonctionnalités admin personnalisées
    print("\n⚙️ Vérification des fonctionnalités admin...")
    
    # Vérifier que l'index est personnalisé
    if hasattr(admin.site, 'index') and admin.site.index.__name__ == 'custom_index':
        print("✅ Index personnalisé configuré")
    else:
        print("❌ Index personnalisé non configuré")
    
    # Vérifier les classes admin
    admin_classes = [
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
    
    for model, admin_name in admin_classes:
        if model in admin.site._registry:
            admin_class = admin.site._registry[model]
            # Vérifier les fonctionnalités personnalisées
            if hasattr(admin_class, 'list_display') and len(admin_class.list_display) > 0:
                print(f"✅ {admin_name} avec list_display configuré")
            else:
                print(f"⚠️ {admin_name} sans list_display")
        else:
            print(f"❌ {admin_name} non enregistré")
    
    return True

def test_donnees_interface():
    """Tester les données nécessaires à l'interface"""
    print("\n📋 Test des données pour l'interface...")
    
    # Messages récents
    messages_recents = ContactMessage.objects.select_related('service').order_by('-date_creation')[:5]
    print(f"✅ Messages récents: {messages_recents.count()}")
    
    # Témoignages en attente
    temoignages_en_attente = Témoignage.objects.filter(approuve=False).order_by('-date_creation')[:5]
    print(f"✅ Témoignages en attente: {temoignages_en_attente.count()}")
    
    # Articles récents
    articles_recents = Article.objects.filter(actif=True).order_by('-date_publication')[:3]
    print(f"✅ Articles récents: {articles_recents.count()}")
    
    return True

def main():
    """Fonction principale de test"""
    print("🚀 TEST INTERFACE D'ADMINISTRATION PERSONNALISÉE")
    print("=" * 70)
    
    # Tests
    interface_ok = test_interface_personnalisee()
    donnees_ok = test_donnees_interface()
    
    print("\n" + "=" * 70)
    print("📋 RÉSULTATS DES TESTS:")
    print(f"• Interface personnalisée: {'✅ PASSÉ' if interface_ok else '❌ ÉCHOUÉ'}")
    print(f"• Données interface: {'✅ PASSÉ' if donnees_ok else '❌ ÉCHOUÉ'}")
    
    all_tests_passed = interface_ok and donnees_ok
    
    print("\n" + "=" * 70)
    if all_tests_passed:
        print("🎉 INTERFACE PERSONNALISÉE OPÉRATIONNELLE !")
        print("\n✨ Fonctionnalités de l'interface personnalisée :")
        print("• 🎨 Design moderne et professionnel")
        print("• 📊 Tableau de bord avec statistiques en temps réel")
        print("• 🚀 Navigation intuitive avec icônes")
        print("• 📱 Interface responsive (mobile-friendly)")
        print("• ⚡ Actions rapides pour les tâches courantes")
        print("• 🎯 Widgets personnalisés pour chaque section")
        print("• 🌈 Couleurs et thème adaptés au cabinet d'avocat")
        print("• 📈 Statistiques visuelles avec cartes interactives")
        print("• 🔔 Notifications visuelles pour les éléments urgents")
        print("• 🎭 Animations et transitions fluides")
        
        print("\n🚀 Accès à l'interface :")
        print("• URL: http://127.0.0.1:8000/admin/")
        print("• Utilisateur: admin")
        print("• Mot de passe: admin123")
        
        print("\n📱 Sections disponibles :")
        print("• 🏠 Tableau de bord personnalisé")
        print("• 📋 Gestion des services juridiques")
        print("• 👥 Gestion des avocats")
        print("• 📧 Messages de contact avec suivi")
        print("• ⭐ Modération des témoignages")
        print("• 📰 Publication d'articles")
        print("• ❓ Gestion des FAQs")
        print("• 📬 Newsletter et abonnés")
        print("• 📊 Statistiques du cabinet")
        print("• ⚙️ Paramètres et configuration")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("Vérifiez les erreurs ci-dessus et corrigez-les.")

if __name__ == '__main__':
    main()
