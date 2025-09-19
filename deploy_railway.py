#!/usr/bin/env python3
"""
Script de déploiement automatique sur Railway
"""

import os
import subprocess
import sys
import webbrowser

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

def check_git_status():
    """Vérifie le statut Git"""
    print("🔍 Vérification du statut Git...")
    
    # Vérifier si on est dans un repository Git
    if not os.path.exists('.git'):
        print("❌ Pas de repository Git. Initialisation...")
        if not run_command("git init", "Initialisation de Git"):
            return False
    
    # Vérifier le statut
    if not run_command("git status", "Vérification du statut Git"):
        return False
    
    return True

def prepare_railway_deployment():
    """Prépare le projet pour Railway"""
    print("\n📦 Préparation pour Railway...")
    
    # Créer un fichier railway.json
    railway_config = {
        "build": {
            "builder": "NIXPACKS"
        },
        "deploy": {
            "startCommand": "gunicorn cabinet_avocat.wsgi --log-file -",
            "healthcheckPath": "/",
            "healthcheckTimeout": 100,
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 10
        }
    }
    
    import json
    with open('railway.json', 'w') as f:
        json.dump(railway_config, f, indent=2)
    
    print("✅ Fichier railway.json créé")
    
    # Collecter les fichiers statiques
    if not run_command("python manage.py collectstatic --noinput", "Collecte des fichiers statiques"):
        return False
    
    # Ajouter tous les fichiers
    if not run_command("git add .", "Ajout des fichiers à Git"):
        return False
    
    # Créer un commit
    if not run_command('git commit -m "Deploy: Préparation pour Railway"', "Commit des changements"):
        return False
    
    return True

def check_github_repo():
    """Vérifie si le repository GitHub existe"""
    print("\n🔍 Vérification du repository GitHub...")
    
    # Vérifier si on a un remote origin
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    
    if "origin" not in result.stdout:
        print("❌ Pas de remote GitHub configuré.")
        print("\n📝 Pour configurer GitHub :")
        print("1. Créer un repository sur https://github.com")
        print("2. Exécuter : git remote add origin https://github.com/votre-username/cabinet-avocat.git")
        print("3. Exécuter : git push -u origin main")
        return False
    
    print("✅ Remote GitHub configuré")
    return True

def open_railway():
    """Ouvre Railway dans le navigateur"""
    print("\n🌐 Ouverture de Railway...")
    webbrowser.open("https://railway.app")
    print("✅ Railway ouvert dans votre navigateur")

def show_railway_instructions():
    """Affiche les instructions pour Railway"""
    print("\n" + "="*60)
    print("🚀 INSTRUCTIONS POUR RAILWAY")
    print("="*60)
    
    print("\n📋 ÉTAPES À SUIVRE :")
    print("\n1️⃣  Dans Railway :")
    print("   • Cliquer sur 'Start a New Project'")
    print("   • Sélectionner 'Deploy from GitHub repo'")
    print("   • Autoriser l'accès à votre repository")
    print("   • Sélectionner 'cabinet-avocat'")
    
    print("\n2️⃣  Configuration des variables :")
    print("   • Aller dans 'Variables'")
    print("   • Ajouter ces variables :")
    print("     DEBUG=False")
    print("     SECRET_KEY=django-insecure-votre-cle-secrete-longue")
    print("     ALLOWED_HOSTS=votre-domaine.railway.app")
    
    print("\n3️⃣  Base de données :")
    print("   • Cliquer sur 'New'")
    print("   • Sélectionner 'Database'")
    print("   • Choisir 'PostgreSQL'")
    
    print("\n4️⃣  Migrations :")
    print("   • Aller dans 'Deployments'")
    print("   • Cliquer sur 'View Logs'")
    print("   • Exécuter : railway run python manage.py migrate")
    print("   • Exécuter : railway run python manage.py createsuperuser")
    
    print("\n🎉 Votre site sera disponible à : https://votre-domaine.railway.app")
    
    print("\n" + "="*60)

def main():
    """Fonction principale"""
    print("🚀 Déploiement Railway - Cabinet d'Avocat")
    print("="*50)
    
    # Vérifier Git
    if not check_git_status():
        print("❌ Problème avec Git")
        sys.exit(1)
    
    # Vérifier GitHub
    if not check_github_repo():
        print("\n⚠️  Configurez d'abord votre repository GitHub")
        print("Puis relancez ce script")
        sys.exit(1)
    
    # Préparer le déploiement
    if not prepare_railway_deployment():
        print("❌ Échec de la préparation")
        sys.exit(1)
    
    # Pousser sur GitHub
    print("\n📤 Poussée vers GitHub...")
    if not run_command("git push origin main", "Poussée vers GitHub"):
        print("❌ Échec de la poussée vers GitHub")
        sys.exit(1)
    
    # Ouvrir Railway
    open_railway()
    
    # Afficher les instructions
    show_railway_instructions()
    
    print("\n🎉 Préparation terminée !")
    print("Suivez les instructions ci-dessus pour finaliser le déploiement sur Railway.")

if __name__ == "__main__":
    main()
