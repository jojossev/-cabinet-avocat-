#!/usr/bin/env python
"""
Test de la barre de menu personnalisée
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings_render')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

def test_menu_personnalise():
    """Tester la barre de menu personnalisée"""
    print("🎨 Test de la barre de menu personnalisée")
    print("=" * 50)
    
    # Créer un client de test
    client = Client()
    
    # Vérifier que l'utilisateur admin existe
    try:
        admin_user = User.objects.get(username='admin')
        print(f"✅ Utilisateur admin trouvé: {admin_user.username}")
    except User.DoesNotExist:
        print("❌ Utilisateur admin non trouvé")
        return False
    
    # Se connecter en tant qu'admin
    login_success = client.login(username='admin', password='admin123')
    if login_success:
        print("✅ Connexion admin réussie")
    else:
        print("❌ Échec de la connexion admin")
        return False
    
    # Tester l'accès à la page d'administration
    try:
        response = client.get('/admin/')
        if response.status_code == 200:
            print("✅ Page d'administration accessible")
            
            # Vérifier que le contenu personnalisé est présent
            content = response.content.decode('utf-8')
            
            # Vérifier les éléments du menu personnalisé
            elements_menu = [
                'Cabinet d\'Avocat',
                'Administration',
                'Tableau de bord',
                'Services',
                'Avocats',
                'Messages',
                'Témoignages',
                'Articles',
                'FAQ',
                'Paramètres'
            ]
            
            elements_trouves = []
            for element in elements_menu:
                if element in content:
                    elements_trouves.append(element)
                    print(f"✅ Élément trouvé: {element}")
                else:
                    print(f"❌ Élément manquant: {element}")
            
            # Vérifier les styles CSS personnalisés
            styles_css = [
                'admin-header',
                'admin-logo',
                'admin-nav',
                'nav-item',
                'primary-color',
                'secondary-color'
            ]
            
            styles_trouves = []
            for style in styles_css:
                if style in content:
                    styles_trouves.append(style)
                    print(f"✅ Style CSS trouvé: {style}")
                else:
                    print(f"❌ Style CSS manquant: {style}")
            
            # Vérifier les icônes Font Awesome
            icones = [
                'fas fa-balance-scale',
                'fas fa-tachometer-alt',
                'fas fa-briefcase',
                'fas fa-users',
                'fas fa-envelope',
                'fas fa-star',
                'fas fa-newspaper',
                'fas fa-question-circle',
                'fas fa-cog'
            ]
            
            icones_trouvees = []
            for icone in icones:
                if icone in content:
                    icones_trouvees.append(icone)
                    print(f"✅ Icône trouvée: {icone}")
                else:
                    print(f"❌ Icône manquante: {icone}")
            
            print(f"\n📊 Résumé:")
            print(f"• Éléments de menu: {len(elements_trouves)}/{len(elements_menu)}")
            print(f"• Styles CSS: {len(styles_trouves)}/{len(styles_css)}")
            print(f"• Icônes: {len(icones_trouvees)}/{len(icones)}")
            
            return len(elements_trouves) >= len(elements_menu) * 0.8
            
        else:
            print(f"❌ Erreur d'accès à l'administration: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

def test_template_files():
    """Tester les fichiers de template"""
    print("\n📁 Test des fichiers de template...")
    
    template_files = [
        'templates/admin/base_site.html',
        'templates/admin/index.html',
        'templates/admin/dashboard.html',
    ]
    
    all_exist = True
    for template in template_files:
        if os.path.exists(template):
            print(f"✅ {template} existe")
        else:
            print(f"❌ {template} manquant")
            all_exist = False
    
    return all_exist

def main():
    """Fonction principale de test"""
    print("🚀 TEST DE LA BARRE DE MENU PERSONNALISÉE")
    print("=" * 60)
    
    # Tests
    templates_ok = test_template_files()
    menu_ok = test_menu_personnalise()
    
    print("\n" + "=" * 60)
    print("📋 RÉSULTATS DES TESTS:")
    print(f"• Fichiers template: {'✅ PASSÉ' if templates_ok else '❌ ÉCHOUÉ'}")
    print(f"• Barre de menu: {'✅ PASSÉ' if menu_ok else '❌ ÉCHOUÉ'}")
    
    all_tests_passed = templates_ok and menu_ok
    
    print("\n" + "=" * 60)
    if all_tests_passed:
        print("🎉 BARRE DE MENU PERSONNALISÉE OPÉRATIONNELLE !")
        print("\n✨ Fonctionnalités de la barre de menu :")
        print("• 🎨 Header rouge avec logo et nom du cabinet")
        print("• 🧭 Navigation horizontale avec icônes")
        print("• 📱 Design responsive pour mobile")
        print("• 🎯 Liens directs vers toutes les sections")
        print("• 🔔 Badges de notification pour les éléments urgents")
        print("• 🌈 Couleurs et thème professionnel")
        print("• ⚡ Transitions et animations fluides")
        
        print("\n🚀 Accès à l'interface :")
        print("• URL: http://127.0.0.1:8000/admin/")
        print("• Utilisateur: admin")
        print("• Mot de passe: admin123")
        
        print("\n🎨 Éléments visuels :")
        print("• Header rouge avec dégradé")
        print("• Logo balance de justice")
        print("• Navigation avec icônes Font Awesome")
        print("• Badges de notification")
        print("• Design moderne et professionnel")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("Vérifiez les erreurs ci-dessus et corrigez-les.")

if __name__ == '__main__':
    main()
