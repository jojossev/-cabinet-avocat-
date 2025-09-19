#!/usr/bin/env python3
"""
Script de déploiement automatique pour le cabinet d'avocat
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Succès")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erreur")
        print(f"Erreur: {e.stderr}")
        return False

def check_requirements():
    """Vérifie que tous les outils nécessaires sont installés"""
    print("🔍 Vérification des prérequis...")
    
    # Vérifier Git
    if not run_command("git --version", "Vérification de Git"):
        print("❌ Git n'est pas installé. Veuillez l'installer d'abord.")
        return False
    
    # Vérifier Heroku CLI (optionnel)
    heroku_installed = run_command("heroku --version", "Vérification de Heroku CLI")
    if not heroku_installed:
        print("⚠️  Heroku CLI n'est pas installé. Vous devrez l'installer pour déployer sur Heroku.")
    
    return True

def prepare_deployment():
    """Prépare le projet pour le déploiement"""
    print("\n📦 Préparation du déploiement...")
    
    # Collecter les fichiers statiques
    if not run_command("python manage.py collectstatic --noinput", "Collecte des fichiers statiques"):
        return False
    
    # Créer un commit Git
    if not run_command("git add .", "Ajout des fichiers à Git"):
        return False
    
    if not run_command('git commit -m "Deploy: Préparation pour l\'hébergement"', "Commit des changements"):
        return False
    
    return True

def deploy_heroku():
    """Déploie sur Heroku"""
    print("\n🚀 Déploiement sur Heroku...")
    
    # Vérifier si on est connecté à Heroku
    if not run_command("heroku auth:whoami", "Vérification de la connexion Heroku"):
        print("❌ Vous n'êtes pas connecté à Heroku. Exécutez 'heroku login' d'abord.")
        return False
    
    # Créer l'application Heroku (si elle n'existe pas)
    app_name = input("📝 Nom de votre application Heroku (ou appuyez sur Entrée pour 'cabinet-avocat'): ").strip()
    if not app_name:
        app_name = "cabinet-avocat"
    
    # Essayer de créer l'application
    run_command(f"heroku create {app_name}", f"Création de l'application {app_name}")
    
    # Configurer les variables d'environnement
    print("\n🔧 Configuration des variables d'environnement...")
    
    secret_key = input("🔑 Clé secrète Django (ou appuyez sur Entrée pour générer automatiquement): ").strip()
    if not secret_key:
        secret_key = "django-insecure-" + os.urandom(32).hex()
    
    run_command(f"heroku config:set SECRET_KEY='{secret_key}'", "Configuration de SECRET_KEY")
    run_command(f"heroku config:set DEBUG=False", "Configuration de DEBUG")
    run_command(f"heroku config:set ALLOWED_HOSTS={app_name}.herokuapp.com", "Configuration de ALLOWED_HOSTS")
    
    # Ajouter la base de données PostgreSQL
    run_command("heroku addons:create heroku-postgresql:hobby-dev", "Ajout de la base de données PostgreSQL")
    
    # Déployer
    if not run_command(f"git push heroku main", "Déploiement sur Heroku"):
        return False
    
    # Migrer la base de données
    if not run_command("heroku run python manage.py migrate", "Migration de la base de données"):
        return False
    
    # Créer un superutilisateur
    print("\n👤 Création du superutilisateur...")
    print("Vous devrez entrer les informations du superutilisateur :")
    run_command("heroku run python manage.py createsuperuser", "Création du superutilisateur")
    
    print(f"\n🎉 Déploiement terminé !")
    print(f"🌐 Votre site est disponible à : https://{app_name}.herokuapp.com")
    print(f"🔧 Administration : https://{app_name}.herokuapp.com/admin/")
    
    return True

def deploy_railway():
    """Instructions pour déployer sur Railway"""
    print("\n🚀 Instructions pour Railway :")
    print("1. Allez sur https://railway.app")
    print("2. Connectez-vous avec votre compte GitHub")
    print("3. Cliquez sur 'New Project'")
    print("4. Sélectionnez 'Deploy from GitHub repo'")
    print("5. Choisissez votre repository 'cabinet-avocat'")
    print("6. Railway déploiera automatiquement votre application")
    print("7. Configurez les variables d'environnement dans Railway :")
    print("   - DEBUG=False")
    print("   - SECRET_KEY=votre-cle-secrete")
    print("   - ALLOWED_HOSTS=votre-domaine.railway.app")
    print("8. Ajoutez une base de données PostgreSQL")
    print("9. Exécutez les migrations : railway run python manage.py migrate")

def main():
    """Fonction principale"""
    print("🏛️  Déploiement du Cabinet d'Avocat")
    print("=" * 50)
    
    # Vérifier les prérequis
    if not check_requirements():
        sys.exit(1)
    
    # Préparer le déploiement
    if not prepare_deployment():
        print("❌ Échec de la préparation du déploiement")
        sys.exit(1)
    
    # Choisir la plateforme
    print("\n🌐 Choisissez votre plateforme d'hébergement :")
    print("1. Heroku (recommandé pour débuter)")
    print("2. Railway (moderne et simple)")
    print("3. Instructions pour Railway")
    
    choice = input("\nVotre choix (1-3) : ").strip()
    
    if choice == "1":
        if not deploy_heroku():
            print("❌ Échec du déploiement sur Heroku")
            sys.exit(1)
    elif choice == "2":
        deploy_railway()
    elif choice == "3":
        deploy_railway()
    else:
        print("❌ Choix invalide")
        sys.exit(1)
    
    print("\n🎉 Déploiement terminé avec succès !")

if __name__ == "__main__":
    main()
