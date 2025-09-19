#!/usr/bin/env python
"""
Script pour peupler la base de données avec des données d'exemple étendues
"""
import os
import sys
import django
from django.utils import timezone

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings_render')
django.setup()

from website.models import Service, Avocat, CabinetInfo, Article, Témoignage, FAQ, Newsletter, Statistique

def create_statistiques():
    """Créer les statistiques du cabinet"""
    statistiques_data = [
        {
            'nom': 'Années d\'expérience',
            'valeur': 25,
            'unite': 'ans',
            'icone': 'fas fa-calendar-alt',
            'ordre_affichage': 1
        },
        {
            'nom': 'Clients satisfaits',
            'valeur': 500,
            'unite': 'clients',
            'icone': 'fas fa-users',
            'ordre_affichage': 2
        },
        {
            'nom': 'Dossiers traités',
            'valeur': 1200,
            'unite': 'dossiers',
            'icone': 'fas fa-folder-open',
            'ordre_affichage': 3
        },
        {
            'nom': 'Taux de réussite',
            'valeur': 95,
            'unite': '%',
            'icone': 'fas fa-trophy',
            'ordre_affichage': 4
        }
    ]
    
    for stat_data in statistiques_data:
        stat, created = Statistique.objects.get_or_create(
            nom=stat_data['nom'],
            defaults=stat_data
        )
        if created:
            print(f"✓ Statistique créée: {stat.nom}")
        else:
            print(f"- Statistique existante: {stat.nom}")

def create_faqs():
    """Créer les questions fréquemment posées"""
    faqs_data = [
        {
            'question': 'Comment prendre rendez-vous ?',
            'reponse': 'Vous pouvez nous contacter par téléphone, email ou en remplissant le formulaire de contact sur notre site. Nous vous recontacterons dans les plus brefs délais pour convenir d\'un rendez-vous.',
            'ordre_affichage': 1
        },
        {
            'question': 'La première consultation est-elle gratuite ?',
            'reponse': 'Oui, nous proposons une consultation gratuite pour évaluer votre situation et vous orienter vers la meilleure solution juridique.',
            'ordre_affichage': 2
        },
        {
            'question': 'Quels sont vos honoraires ?',
            'reponse': 'Nos honoraires sont transparents et adaptés à chaque situation. Nous vous fournirons un devis détaillé avant tout engagement.',
            'ordre_affichage': 3
        },
        {
            'question': 'Êtes-vous disponibles en urgence ?',
            'reponse': 'Nous nous efforçons de répondre rapidement à toutes les demandes. Pour les urgences, n\'hésitez pas à nous appeler directement.',
            'ordre_affichage': 4
        },
        {
            'question': 'Travaillez-vous avec des entreprises ?',
            'reponse': 'Oui, nous accompagnons aussi bien les particuliers que les entreprises dans tous leurs besoins juridiques.',
            'service': Service.objects.filter(nom__icontains='Affaires').first(),
            'ordre_affichage': 5
        }
    ]
    
    for faq_data in faqs_data:
        faq, created = FAQ.objects.get_or_create(
            question=faq_data['question'],
            defaults=faq_data
        )
        if created:
            print(f"✓ FAQ créée: {faq.question}")
        else:
            print(f"- FAQ existante: {faq.question}")

def create_temoignages():
    """Créer les témoignages clients"""
    avocats = list(Avocat.objects.all())
    services = list(Service.objects.all())
    
    temoignages_data = [
        {
            'nom_client': 'Marie Dubois',
            'entreprise': 'Entreprise Dubois SARL',
            'témoignage': 'Excellent service ! Maître Dupont nous a accompagnés dans la création de notre entreprise avec professionnalisme et disponibilité. Je recommande vivement ce cabinet.',
            'note': 5,
            'service': services[0] if services else None,
            'avocat': avocats[0] if avocats else None,
            'approuve': True,
            'ordre_affichage': 1
        },
        {
            'nom_client': 'Jean Martin',
            'témoignage': 'Grâce à Maître Martin, j\'ai pu régler mon divorce dans de bonnes conditions. Elle a su être à l\'écoute et m\'a guidé tout au long de la procédure.',
            'note': 5,
            'service': services[2] if len(services) > 2 else None,
            'avocat': avocats[1] if len(avocats) > 1 else None,
            'approuve': True,
            'ordre_affichage': 2
        },
        {
            'nom_client': 'Sophie Leroy',
            'entreprise': 'Leroy Immobilier',
            'témoignage': 'Service impeccable pour nos transactions immobilières. L\'équipe est réactive et très compétente. Nous faisons appel à eux régulièrement.',
            'note': 5,
            'service': services[1] if len(services) > 1 else None,
            'avocat': avocats[1] if len(avocats) > 1 else None,
            'approuve': True,
            'ordre_affichage': 3
        }
    ]
    
    for temoignage_data in temoignages_data:
        temoignage, created = Témoignage.objects.get_or_create(
            nom_client=temoignage_data['nom_client'],
            defaults=temoignage_data
        )
        if created:
            print(f"✓ Témoignage créé: {temoignage.nom_client}")
        else:
            print(f"- Témoignage existant: {temoignage.nom_client}")

def create_articles():
    """Créer des articles de blog"""
    avocats = list(Avocat.objects.all())
    
    articles_data = [
        {
            'titre': 'Nouvelle réforme du droit des entreprises',
            'slug': 'nouvelle-reforme-droit-entreprises',
            'resume': 'Découvrez les principales modifications apportées par la nouvelle réforme du droit des entreprises et leurs impacts sur votre activité.',
            'contenu': '''<h2>Introduction</h2>
            <p>La nouvelle réforme du droit des entreprises, entrée en vigueur le 1er janvier 2024, apporte des modifications importantes pour les entrepreneurs et dirigeants d'entreprise.</p>
            
            <h2>Principales modifications</h2>
            <ul>
                <li>Simplification des procédures de création d'entreprise</li>
                <li>Nouvelles obligations comptables</li>
                <li>Modifications du droit du travail</li>
            </ul>
            
            <h2>Impacts sur votre entreprise</h2>
            <p>Ces changements peuvent avoir des conséquences importantes sur votre activité. Il est recommandé de faire le point avec votre avocat pour vous assurer de votre conformité.</p>
            
            <h2>Conclusion</h2>
            <p>Notre équipe reste à votre disposition pour vous accompagner dans l'adaptation à ces nouvelles réglementations.</p>''',
            'auteur': avocats[0] if avocats else None,
            'date_publication': timezone.now(),
            'actif': True
        },
        {
            'titre': 'Guide pratique : Divorce par consentement mutuel',
            'slug': 'guide-divorce-consentement-mutuel',
            'resume': 'Tout ce qu\'il faut savoir sur le divorce par consentement mutuel : procédure, délais, coûts et conseils pratiques.',
            'contenu': '''<h2>Qu\'est-ce que le divorce par consentement mutuel ?</h2>
            <p>Le divorce par consentement mutuel est la procédure la plus simple et la moins coûteuse lorsque les deux époux sont d'accord pour divorcer.</p>
            
            <h2>Conditions requises</h2>
            <ul>
                <li>Accord des deux époux</li>
                <li>Convention de divorce signée</li>
                <li>Représentation par un avocat</li>
            </ul>
            
            <h2>Procédure</h2>
            <p>La procédure se déroule en plusieurs étapes : négociation, rédaction de la convention, signature et homologation par le juge.</p>
            
            <h2>Délais et coûts</h2>
            <p>Le divorce par consentement mutuel peut être prononcé en 3 à 6 mois et coûte généralement entre 1500 et 3000 euros par époux.</p>''',
            'auteur': avocats[1] if len(avocats) > 1 else None,
            'date_publication': timezone.now(),
            'actif': True
        }
    ]
    
    for article_data in articles_data:
        article, created = Article.objects.get_or_create(
            slug=article_data['slug'],
            defaults=article_data
        )
        if created:
            print(f"✓ Article créé: {article.titre}")
        else:
            print(f"- Article existant: {article.titre}")

def create_newsletter_subscribers():
    """Créer des abonnés à la newsletter"""
    subscribers_data = [
        {'email': 'client1@example.com', 'nom': 'Client Test 1'},
        {'email': 'client2@example.com', 'nom': 'Client Test 2'},
        {'email': 'entreprise@example.com', 'nom': 'Entreprise Test'},
    ]
    
    for sub_data in subscribers_data:
        subscriber, created = Newsletter.objects.get_or_create(
            email=sub_data['email'],
            defaults=sub_data
        )
        if created:
            print(f"✓ Abonné créé: {subscriber.email}")
        else:
            print(f"- Abonné existant: {subscriber.email}")

def update_cabinet_info():
    """Mettre à jour les informations du cabinet"""
    cabinet = CabinetInfo.objects.first()
    if cabinet:
        cabinet.meta_description = "Cabinet d'avocat spécialisé dans le droit des affaires, immobilier, famille et pénal. Consultation gratuite. Expertise et dévouement au service de vos droits."
        cabinet.meta_keywords = "avocat, droit des affaires, droit immobilier, droit de la famille, droit pénal, consultation juridique, cabinet d'avocat"
        cabinet.save()
        print("✓ Informations du cabinet mises à jour")

def main():
    """Fonction principale"""
    print("🚀 Peuplement étendu de la base de données...")
    print("=" * 60)
    
    create_statistiques()
    print()
    create_faqs()
    print()
    create_temoignages()
    print()
    create_articles()
    print()
    create_newsletter_subscribers()
    print()
    update_cabinet_info()
    print()
    
    print("=" * 60)
    print("✅ Peuplement étendu terminé avec succès!")
    print("\nNouvelles fonctionnalités disponibles:")
    print("• Statistiques du cabinet")
    print("• Questions fréquemment posées")
    print("• Témoignages clients")
    print("• Articles de blog")
    print("• Gestion de la newsletter")
    print("\nVous pouvez maintenant:")
    print("1. Lancer le serveur: python manage.py runserver")
    print("2. Accéder au site: http://127.0.0.1:8000/")
    print("3. Accéder à l'admin: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    main()
