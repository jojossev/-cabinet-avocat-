#!/usr/bin/env python
"""
Script pour mettre à jour les avocats avec des images par défaut
"""
import os
import django
from django.contrib.auth import get_user_model

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabinet_avocat.settings')
django.setup()

from website.models import Avocat

def update_avocats_images():
    """Mettre à jour les avocats avec des images par défaut"""
    
    print("🔄 MISE À JOUR DES IMAGES D'AVOCATS...")
    
    # Mapping des noms vers les fichiers d'images
    image_mapping = {
        "Marie Martin": "marie_martin.jpg",
        "Pierre Durand": "pierre_durand.jpg", 
        "Marie Dubois": "marie_dubois.jpg",
        "Jean Martin": "jean_martin.jpg"
    }
    
    # Mettre à jour chaque avocat
    for avocat in Avocat.objects.all():
        if not avocat.photo:  # Seulement si pas de photo
            if avocat.nom in image_mapping:
                avocat.photo = f"avocats/{image_mapping[avocat.nom]}"
                avocat.save()
                print(f"✅ {avocat.nom} - Image mise à jour: {avocat.photo}")
            else:
                print(f"⚠️ {avocat.nom} - Pas d'image par défaut disponible")
        else:
            print(f"ℹ️ {avocat.nom} - A déjà une photo: {avocat.photo}")
    
    print("✅ Mise à jour terminée!")

if __name__ == "__main__":
    update_avocats_images()
