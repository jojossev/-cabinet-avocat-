#!/usr/bin/env python
"""
Script pour peupler la base de données avec des données d'exemple
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

from website.models import Service, Avocat, CabinetInfo

def create_services():
    """Créer les services juridiques"""
    services_data = [
        {
            'nom': 'Droit des Affaires',
            'description': 'Conseil en création d\'entreprise, contrats commerciaux, fusion-acquisition et restructuration. Nous accompagnons les entreprises dans leur développement et leur protection juridique.',
            'icone': 'fas fa-briefcase',
            'ordre_affichage': 1
        },
        {
            'nom': 'Droit Immobilier',
            'description': 'Transactions immobilières, baux commerciaux, copropriété et urbanisme. Expertise complète pour tous vos projets immobiliers.',
            'icone': 'fas fa-home',
            'ordre_affichage': 2
        },
        {
            'nom': 'Droit de la Famille',
            'description': 'Divorce, garde d\'enfants, succession, adoption et protection des majeurs. Accompagnement bienveillant dans les moments difficiles.',
            'icone': 'fas fa-users',
            'ordre_affichage': 3
        },
        {
            'nom': 'Droit Pénal',
            'description': 'Défense pénale, conseil aux victimes, droit routier et procédures d\'urgence. Protection de vos droits et de votre réputation.',
            'icone': 'fas fa-shield-alt',
            'ordre_affichage': 4
        },
        {
            'nom': 'Droit du Travail',
            'description': 'Conseil RH, licenciement, harcèlement, négociation collective et prud\'hommes. Défense des droits des salariés et employeurs.',
            'icone': 'fas fa-handshake',
            'ordre_affichage': 5
        },
        {
            'nom': 'Droit Fiscal',
            'description': 'Optimisation fiscale, contentieux fiscal, conseil en investissement et transmission. Expertise pour optimiser votre situation fiscale.',
            'icone': 'fas fa-chart-line',
            'ordre_affichage': 6
        }
    ]
    
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            nom=service_data['nom'],
            defaults=service_data
        )
        if created:
            print(f"✓ Service créé: {service.nom}")
        else:
            print(f"- Service existant: {service.nom}")

def create_avocats():
    """Créer les avocats"""
    avocats_data = [
        {
            'nom': 'Maître Jean Dupont',
            'titre': 'Avocat Associé',
            'specialites': 'Droit des Affaires & Fiscal',
            'email': 'j.dupont@cabinet-juridique.fr',
            'telephone': '+33 1 23 45 67 89',
            'linkedin': 'https://linkedin.com/in/jean-dupont',
            'ordre_affichage': 1
        },
        {
            'nom': 'Maître Marie Martin',
            'titre': 'Avocat Associé',
            'specialites': 'Droit de la Famille & Immobilier',
            'email': 'm.martin@cabinet-juridique.fr',
            'telephone': '+33 1 23 45 67 90',
            'linkedin': 'https://linkedin.com/in/marie-martin',
            'ordre_affichage': 2
        },
        {
            'nom': 'Maître Pierre Durand',
            'titre': 'Avocat',
            'specialites': 'Droit Pénal & Travail',
            'email': 'p.durand@cabinet-juridique.fr',
            'telephone': '+33 1 23 45 67 91',
            'linkedin': 'https://linkedin.com/in/pierre-durand',
            'ordre_affichage': 3
        }
    ]
    
    for avocat_data in avocats_data:
        avocat, created = Avocat.objects.get_or_create(
            nom=avocat_data['nom'],
            defaults=avocat_data
        )
        if created:
            print(f"✓ Avocat créé: {avocat.nom}")
        else:
            print(f"- Avocat existant: {avocat.nom}")

def create_cabinet_info():
    """Créer les informations du cabinet"""
    cabinet_data = {
        'nom_cabinet': 'Cabinet Juridique Dupont & Associés',
        'adresse': '123 Avenue de la Justice\n75001 Paris, France',
        'telephone': '+33 1 23 45 67 89',
        'email': 'contact@cabinet-juridique.fr',
        'horaires': 'Lun - Ven: 9h00 - 18h00\nSam: 9h00 - 12h00',
        'description': 'Votre partenaire juridique de confiance depuis plus de 20 ans. Expertise, intégrité et dévouement au service de vos droits.'
    }
    
    cabinet, created = CabinetInfo.objects.get_or_create(
        id=1,
        defaults=cabinet_data
    )
    if created:
        print(f"✓ Informations du cabinet créées")
    else:
        # Mettre à jour les informations existantes
        for key, value in cabinet_data.items():
            setattr(cabinet, key, value)
        cabinet.save()
        print(f"✓ Informations du cabinet mises à jour")

def main():
    """Fonction principale"""
    print("🚀 Peuplement de la base de données...")
    print("=" * 50)
    
    create_services()
    print()
    create_avocats()
    print()
    create_cabinet_info()
    print()
    
    print("=" * 50)
    print("✅ Peuplement terminé avec succès!")
    print("\nVous pouvez maintenant:")
    print("1. Lancer le serveur: python manage.py runserver")
    print("2. Accéder au site: http://127.0.0.1:8000/")
    print("3. Accéder à l'admin: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    main()
