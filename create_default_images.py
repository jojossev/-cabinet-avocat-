#!/usr/bin/env python
"""
Script pour créer des images par défaut pour les avocats
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_default_avatar(name, filename):
    """Créer une image par défaut pour un avocat"""
    
    # Créer une image 300x300
    size = 300
    img = Image.new('RGB', (size, size), (44, 62, 80))  # Couleur primaire
    draw = ImageDraw.Draw(img)
    
    # Dessiner un cercle de fond
    margin = 20
    draw.ellipse([margin, margin, size-margin, size-margin], fill=(52, 73, 94))
    
    # Dessiner les initiales
    try:
        # Essayer d'utiliser une police système
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 80)
        except:
            # Police par défaut
            font = ImageFont.load_default()
    
    # Obtenir les initiales
    initials = ''.join([word[0].upper() for word in name.split()[:2]])
    
    # Centrer le texte
    bbox = draw.textbbox((0, 0), initials, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - 10
    
    # Dessiner le texte
    draw.text((x, y), initials, fill=(255, 255, 255), font=font)
    
    # Sauvegarder
    os.makedirs('media/avocats', exist_ok=True)
    img.save(f'media/avocats/{filename}', 'JPEG', quality=90)
    
    print(f"✅ Image créée: {filename}")

def create_default_images():
    """Créer des images par défaut pour tous les avocats"""
    
    print("🎨 CRÉATION D'IMAGES PAR DÉFAUT...")
    
    # Créer des images pour les avocats existants
    avocats = [
        ("Marie Martin", "marie_martin.jpg"),
        ("Pierre Durand", "pierre_durand.jpg"),
        ("Marie Dubois", "marie_dubois.jpg"),
        ("Jean Martin", "jean_martin.jpg")
    ]
    
    for name, filename in avocats:
        create_default_avatar(name, filename)
    
    print("✅ Toutes les images par défaut ont été créées!")

if __name__ == "__main__":
    create_default_images()
