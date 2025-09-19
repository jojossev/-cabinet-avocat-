#!/usr/bin/env python3
"""
Script de déploiement automatique sur Render
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

def prepare_render_deployment():
    """Prépare le projet pour Render"""
    print("\n📦 Préparation pour Render...")
    
    # Créer un fichier render.yaml
    render_config = """services:
  - type: web
    name: cabinet-avocat
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn cabinet_avocat.wsgi
    envVars:
      - key: DEBUG
        value: False
      - key: SECRET_KEY
        value: django-insecure-votre-cle-secrete-longue-et-complexe
      - key: ALLOWED_HOSTS
        value: votre-domaine.onrender.com
    healthCheckPath: /
    
  - type: pserv
    name: cabinet-avocat-db
    env: postgresql
    plan: free
"""
    
    with open('render.yaml', 'w') as f:
        f.write(render_config)
    
    print("✅ Fichier render.yaml créé")
    
    # Collecter les fichiers statiques
    if not run_command("python manage.py collectstatic --noinput", "Collecte des fichiers statiques"):
        return False
    
    # Ajouter tous les fichiers
    if not run_command("git add .", "Ajout des fichiers à Git"):
        return False
    
    # Créer un commit
    if not run_command('git commit -m "Deploy: Préparation pour Render"', "Commit des changements"):
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

def open_render():
    """Ouvre Render dans le navigateur"""
    print("\n🌐 Ouverture de Render...")
    webbrowser.open("https://render.com")
    print("✅ Render ouvert dans votre navigateur")

def show_render_instructions():
    """Affiche les instructions pour Render"""
    print("\n" + "="*60)
    print("🚀 INSTRUCTIONS POUR RENDER")
    print("="*60)
    
    print("\n📋 ÉTAPES À SUIVRE :")
    print("\n1️⃣  Dans Render :")
    print("   • Se connecter avec GitHub")
    print("   • Cliquer sur 'New +' → 'Web Service'")
    print("   • Sélectionner votre repository '-cabinet-avocat-'")
    print("   • Name: cabinet-avocat")
    print("   • Environment: Python 3")
    print("   • Build Command: pip install -r requirements.txt")
    print("   • Start Command: gunicorn cabinet_avocat.wsgi")
    print("   • Cliquer sur 'Create Web Service'")
    
    print("\n2️⃣  Configuration des variables :")
    print("   • Aller dans 'Environment' → 'Environment Variables'")
    print("   • Ajouter ces variables :")
    print("     DEBUG=False")
    print("     SECRET_KEY=django-insecure-votre-cle-secrete-longue")
    print("     ALLOWED_HOSTS=votre-domaine.onrender.com")
    
    print("\n3️⃣  Base de données :")
    print("   • Cliquer sur 'New +' → 'PostgreSQL'")
    print("   • Name: cabinet-avocat-db")
    print("   • Plan: Free")
    print("   • Cliquer sur 'Create Database'")
    
    print("\n4️⃣  Migrations :")
    print("   • Aller dans votre service web")
    print("   • Cliquer sur 'Shell'")
    print("   • Exécuter : python manage.py migrate")
    print("   • Exécuter : python manage.py createsuperuser")
    
    print("\n🎉 Votre site sera disponible à : https://votre-domaine.onrender.com")
    
    print("\n" + "="*60)

def main():
    """Fonction principale"""
    print("🚀 Déploiement Render - Cabinet d'Avocat")
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
    if not prepare_render_deployment():
        print("❌ Échec de la préparation")
        sys.exit(1)
    
    # Pousser sur GitHub
    print("\n📤 Poussée vers GitHub...")
    if not run_command("git push origin main", "Poussée vers GitHub"):
        print("❌ Échec de la poussée vers GitHub")
        sys.exit(1)
    
    # Ouvrir Render
    open_render()
    
    # Afficher les instructions
    show_render_instructions()
    
    print("\n🎉 Préparation terminée !")
    print("Suivez les instructions ci-dessus pour finaliser le déploiement sur Render.")

if __name__ == "__main__":
    main()
