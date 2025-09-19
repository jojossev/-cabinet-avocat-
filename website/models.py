from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Service(models.Model):
    """Modèle pour les services juridiques"""
    nom = models.CharField(max_length=100, verbose_name="Nom du service")
    description = models.TextField(verbose_name="Description")
    description_courte = models.TextField(
        max_length=200, 
        verbose_name="Description courte",
        help_text="Description affichée sur la page d'accueil",
        blank=True
    )
    icone = models.CharField(
        max_length=50, 
        default="fas fa-briefcase",
        help_text="Classe Font Awesome pour l'icône (ex: fas fa-briefcase)"
    )
    ordre_affichage = models.PositiveIntegerField(
        default=0, 
        verbose_name="Ordre d'affichage"
    )
    actif = models.BooleanField(default=True, verbose_name="Actif")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création", null=True, blank=True)
    date_modification = models.DateTimeField(auto_now=True, verbose_name="Date de modification", null=True, blank=True)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['ordre_affichage', 'nom']
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.description_courte:
            self.description_courte = self.description[:200] + "..." if len(self.description) > 200 else self.description
        super().save(*args, **kwargs)


class Avocat(models.Model):
    """Modèle pour les avocats du cabinet"""
    nom = models.CharField(max_length=100, verbose_name="Nom complet")
    prenom = models.CharField(max_length=100, verbose_name="Prénom", blank=True)
    titre = models.CharField(
        max_length=100, 
        verbose_name="Titre",
        help_text="Ex: Avocat Associé, Avocat"
    )
    specialites = models.CharField(
        max_length=200, 
        verbose_name="Spécialités",
        help_text="Ex: Droit des Affaires & Fiscal"
    )
    biographie = models.TextField(
        blank=True,
        verbose_name="Biographie",
        help_text="Biographie détaillée de l'avocat"
    )
    photo = models.ImageField(
        upload_to='avocats/', 
        blank=True, 
        null=True,
        verbose_name="Photo"
    )
    email = models.EmailField(verbose_name="Email")
    telephone = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Format de téléphone invalide"
        )],
        verbose_name="Téléphone"
    )
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    ordre_affichage = models.PositiveIntegerField(
        default=0, 
        verbose_name="Ordre d'affichage"
    )
    actif = models.BooleanField(default=True, verbose_name="Actif")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création", null=True, blank=True)
    date_modification = models.DateTimeField(auto_now=True, verbose_name="Date de modification", null=True, blank=True)
    
    class Meta:
        verbose_name = "Avocat"
        verbose_name_plural = "Avocats"
        ordering = ['ordre_affichage', 'nom']
    
    def __str__(self):
        return f"{self.nom} - {self.titre}"
    
    @property
    def nom_complet(self):
        if self.prenom:
            return f"{self.prenom} {self.nom}"
        return self.nom


class ContactMessage(models.Model):
    """Modèle pour les messages de contact"""
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Téléphone"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Service concerné"
    )
    message = models.TextField(verbose_name="Message")
    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    traite = models.BooleanField(
        default=False,
        verbose_name="Traité"
    )
    
    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-date_creation']
    
    def __str__(self):
        return f"Message de {self.nom} - {self.date_creation.strftime('%d/%m/%Y %H:%M')}"


class CabinetInfo(models.Model):
    """Modèle pour les informations du cabinet"""
    nom_cabinet = models.CharField(
        max_length=200,
        default="Cabinet Juridique",
        verbose_name="Nom du cabinet"
    )
    adresse = models.TextField(verbose_name="Adresse")
    telephone = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Format de téléphone invalide"
        )],
        verbose_name="Téléphone"
    )
    email = models.EmailField(verbose_name="Email")
    horaires = models.TextField(
        verbose_name="Horaires",
        help_text="Ex: Lun - Ven: 9h00 - 18h00<br>Sam: 9h00 - 12h00"
    )
    description = models.TextField(
        verbose_name="Description du cabinet",
        help_text="Description qui apparaît sur la page d'accueil"
    )
    
    # Réseaux sociaux
    facebook = models.URLField(blank=True, null=True, verbose_name="Facebook")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    
    # SEO
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Meta description",
        help_text="Description pour les moteurs de recherche"
    )
    meta_keywords = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Meta keywords",
        help_text="Mots-clés séparés par des virgules"
    )
    
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création", null=True, blank=True)
    date_modification = models.DateTimeField(auto_now=True, verbose_name="Date de modification", null=True, blank=True)
    
    class Meta:
        verbose_name = "Informations du cabinet"
        verbose_name_plural = "Informations du cabinet"
    
    def __str__(self):
        return self.nom_cabinet
    
    def save(self, *args, **kwargs):
        # S'assurer qu'il n'y a qu'une seule instance
        if not self.pk and CabinetInfo.objects.exists():
            # Si une instance existe déjà, la mettre à jour
            existing = CabinetInfo.objects.first()
            for field in self._meta.fields:
                if field.name != 'id' and field.name != 'date_creation':
                    setattr(existing, field.name, getattr(self, field.name))
            existing.save()
            return existing
        return super().save(*args, **kwargs)


class Article(models.Model):
    """Modèle pour les articles de blog/actualités"""
    titre = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    contenu = models.TextField(verbose_name="Contenu")
    resume = models.TextField(
        max_length=300,
        verbose_name="Résumé",
        help_text="Résumé affiché sur la page d'accueil"
    )
    image = models.ImageField(
        upload_to='articles/',
        blank=True,
        null=True,
        verbose_name="Image"
    )
    auteur = models.ForeignKey(
        Avocat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Auteur"
    )
    date_publication = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date de publication"
    )
    actif = models.BooleanField(default=True, verbose_name="Actif")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création", null=True, blank=True)
    date_modification = models.DateTimeField(auto_now=True, verbose_name="Date de modification", null=True, blank=True)
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-date_publication']
    
    def __str__(self):
        return self.titre


class Témoignage(models.Model):
    """Modèle pour les témoignages clients"""
    nom_client = models.CharField(max_length=100, verbose_name="Nom du client")
    entreprise = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Entreprise"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Service concerné"
    )
    avocat = models.ForeignKey(
        Avocat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Avocat"
    )
    témoignage = models.TextField(verbose_name="Témoignage")
    note = models.PositiveIntegerField(
        default=5,
        verbose_name="Note",
        help_text="Note sur 5"
    )
    photo = models.ImageField(
        upload_to='temoignages/',
        blank=True,
        null=True,
        verbose_name="Photo du client"
    )
    approuve = models.BooleanField(default=False, verbose_name="Approuvé")
    ordre_affichage = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['ordre_affichage', '-date_creation']
    
    def __str__(self):
        return f"Témoignage de {self.nom_client}"


class FAQ(models.Model):
    """Modèle pour les questions fréquemment posées"""
    question = models.CharField(max_length=300, verbose_name="Question")
    reponse = models.TextField(verbose_name="Réponse")
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Service concerné"
    )
    ordre_affichage = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )
    actif = models.BooleanField(default=True, verbose_name="Actif")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['ordre_affichage', 'question']
    
    def __str__(self):
        return self.question


class Newsletter(models.Model):
    """Modèle pour les abonnés à la newsletter"""
    email = models.EmailField(unique=True, verbose_name="Email")
    nom = models.CharField(max_length=100, blank=True, verbose_name="Nom")
    actif = models.BooleanField(default=True, verbose_name="Actif")
    date_inscription = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")
    
    class Meta:
        verbose_name = "Abonné Newsletter"
        verbose_name_plural = "Abonnés Newsletter"
        ordering = ['-date_inscription']
    
    def __str__(self):
        return self.email


class Statistique(models.Model):
    """Modèle pour les statistiques du cabinet"""
    nom = models.CharField(max_length=100, verbose_name="Nom")
    valeur = models.PositiveIntegerField(verbose_name="Valeur")
    unite = models.CharField(
        max_length=20,
        default="ans",
        verbose_name="Unité",
        help_text="Ex: ans, clients, dossiers"
    )
    icone = models.CharField(
        max_length=50,
        default="fas fa-chart-line",
        verbose_name="Icône"
    )
    ordre_affichage = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )
    actif = models.BooleanField(default=True, verbose_name="Actif")
    
    class Meta:
        verbose_name = "Statistique"
        verbose_name_plural = "Statistiques"
        ordering = ['ordre_affichage']
    
    def __str__(self):
        return f"{self.nom}: {self.valeur} {self.unite}"
