from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from website.models import CabinetInfo


class Command(BaseCommand):
    help = 'Configure le cabinet d\'avocat avec les données de base'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Nom d\'utilisateur pour le superutilisateur'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@cabinet-juridique.fr',
            help='Email pour le superutilisateur'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Mot de passe pour le superutilisateur'
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🚀 Configuration du cabinet d\'avocat...')
        )
        
        # Créer le superutilisateur
        username = options['username']
        email = options['email']
        password = options['password']
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Superutilisateur créé: {username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'- Superutilisateur existant: {username}')
            )
        
        # Créer les informations du cabinet si elles n'existent pas
        if not CabinetInfo.objects.exists():
            CabinetInfo.objects.create(
                nom_cabinet="Cabinet Juridique Dupont & Associés",
                adresse="123 Avenue de la Justice\n75001 Paris, France",
                telephone="+33 1 23 45 67 89",
                email="contact@cabinet-juridique.fr",
                horaires="Lun - Ven: 9h00 - 18h00\nSam: 9h00 - 12h00",
                description="Votre partenaire juridique de confiance depuis plus de 20 ans. Expertise, intégrité et dévouement au service de vos droits.",
                meta_description="Cabinet d'avocat spécialisé dans le droit des affaires, immobilier, famille et pénal. Consultation gratuite. Expertise et dévouement au service de vos droits.",
                meta_keywords="avocat, droit des affaires, droit immobilier, droit de la famille, droit pénal, consultation juridique, cabinet d'avocat"
            )
            self.stdout.write(
                self.style.SUCCESS('✓ Informations du cabinet créées')
            )
        else:
            self.stdout.write(
                self.style.WARNING('- Informations du cabinet existantes')
            )
        
        self.stdout.write(
            self.style.SUCCESS('\n✅ Configuration terminée avec succès!')
        )
        self.stdout.write('\nVous pouvez maintenant:')
        self.stdout.write('1. Lancer le serveur: python manage.py runserver')
        self.stdout.write('2. Accéder au site: http://127.0.0.1:8000/')
        self.stdout.write('3. Accéder à l\'admin: http://127.0.0.1:8000/admin/')
        self.stdout.write(f'   - Utilisateur: {username}')
        self.stdout.write(f'   - Mot de passe: {password}')
