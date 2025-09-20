#!/usr/bin/env python
"""
Script pour créer un favicon simple
"""
from PIL import Image, ImageDraw
import os

def create_favicon():
    """Créer un favicon simple avec les initiales du cabinet"""
    
    # Créer une image 32x32
    size = 32
    img = Image.new('RGBA', (size, size), (44, 62, 80, 255))  # Couleur primaire
    draw = ImageDraw.Draw(img)
    
    # Dessiner un "A" simple
    draw.text((8, 4), "A", fill=(255, 255, 255, 255))  # Blanc
    
    # Sauvegarder comme ICO
    img.save('static/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32)])
    
    print("✅ Favicon créé avec succès!")
    print("   - Fichier: static/favicon.ico")
    print("   - Taille: 32x32 pixels")
    print("   - Couleur: Bleu foncé avec 'A' blanc")

if __name__ == "__main__":
    create_favicon()
