#!/usr/bin/env python
"""
Script pour diagnostiquer et corriger les problèmes d'images et d'icônes
"""
import os
import django
from django.contrib.auth import get_user_model

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

from website.models import Service, Avocat, CabinetInfo

def diagnose_images_icons():
    """Diagnostiquer les problèmes d'images et d'icônes"""
    
    print("🔍 DIAGNOSTIC DES IMAGES ET ICÔNES...")
    
    # Vérifier les services
    print("\n📋 SERVICES:")
    services = Service.objects.all()
    for service in services:
        print(f"   - {service.nom}")
        print(f"     Icône: {service.icone}")
        print(f"     Actif: {service.actif}")
    
    # Vérifier les avocats
    print("\n👥 AVOCATS:")
    avocats = Avocat.objects.all()
    for avocat in avocats:
        print(f"   - {avocat.nom}")
        if avocat.photo:
            print(f"     Photo: {avocat.photo}")
        else:
            print(f"     Photo: ❌ Aucune photo")
    
    # Vérifier les fichiers statiques
    print("\n📁 FICHIERS STATIQUES:")
    static_dir = "static"
    if os.path.exists(static_dir):
        print(f"   ✅ Dossier static existe")
        for root, dirs, files in os.walk(static_dir):
            for file in files:
                print(f"     - {os.path.join(root, file)}")
    else:
        print(f"   ❌ Dossier static n'existe pas")
    
    # Vérifier les fichiers media
    print("\n📁 FICHIERS MEDIA:")
    media_dir = "media"
    if os.path.exists(media_dir):
        print(f"   ✅ Dossier media existe")
        for root, dirs, files in os.walk(media_dir):
            for file in files:
                print(f"     - {os.path.join(root, file)}")
    else:
        print(f"   ❌ Dossier media n'existe pas")

def create_sample_data():
    """Créer des données d'exemple avec des icônes"""
    
    print("\n🔧 CRÉATION DE DONNÉES D'EXEMPLE...")
    
    # Créer des services avec des icônes Font Awesome
    services_data = [
        {
            'nom': 'Droit des Affaires',
            'description': 'Conseil et accompagnement en droit des affaires',
            'icone': 'fas fa-briefcase',
            'actif': True
        },
        {
            'nom': 'Droit de la Famille',
            'description': 'Divorce, garde d\'enfants, pension alimentaire',
            'icone': 'fas fa-heart',
            'actif': True
        },
        {
            'nom': 'Droit Pénal',
            'description': 'Défense pénale et conseil juridique',
            'icone': 'fas fa-gavel',
            'actif': True
        },
        {
            'nom': 'Droit Immobilier',
            'description': 'Achat, vente, location de biens immobiliers',
            'icone': 'fas fa-home',
            'actif': True
        }
    ]
    
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            nom=service_data['nom'],
            defaults=service_data
        )
        if created:
            print(f"   ✅ Service créé: {service.nom}")
        else:
            print(f"   ℹ️ Service existe déjà: {service.nom}")
    
    # Créer des avocats
    avocats_data = [
        {
            'nom': 'Marie Dubois',
            'titre': 'Avocate Associée',
            'specialites': 'Droit des Affaires, Droit Commercial',
            'biographie': 'Spécialisée en droit des affaires avec plus de 10 ans d\'expérience.',
            'actif': True
        },
        {
            'nom': 'Jean Martin',
            'titre': 'Avocat Senior',
            'specialites': 'Droit Pénal, Droit de la Famille',
            'biographie': 'Expert en droit pénal et droit de la famille.',
            'actif': True
        }
    ]
    
    for avocat_data in avocats_data:
        avocat, created = Avocat.objects.get_or_create(
            nom=avocat_data['nom'],
            defaults=avocat_data
        )
        if created:
            print(f"   ✅ Avocat créé: {avocat.nom}")
        else:
            print(f"   ℹ️ Avocat existe déjà: {avocat.nom}")
    
    # Créer les informations du cabinet
    cabinet_info, created = CabinetInfo.objects.get_or_create(
        nom_cabinet='Cabinet Juridique Excellence',
        defaults={
            'description': 'Votre partenaire juridique de confiance pour tous vos besoins légaux.',
            'adresse': '123 Avenue de la Justice\n75001 Paris, France',
            'telephone': '+33 1 23 45 67 89',
            'email': 'contact@cabinet-juridique.fr',
            'horaires': 'Lun-Ven: 9h-18h\nSam: 9h-12h'
        }
    )
    
    if created:
        print(f"   ✅ Informations du cabinet créées")
    else:
        print(f"   ℹ️ Informations du cabinet existent déjà")

if __name__ == "__main__":
    diagnose_images_icons()
    create_sample_data()
    print("\n🎉 DIAGNOSTIC TERMINÉ!")
    print("Les données d'exemple ont été créées avec des icônes Font Awesome.")
    print("Vérifiez maintenant votre site web.")
