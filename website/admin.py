from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from .models import (
    Service, Avocat, ContactMessage, CabinetInfo, 
    Article, Témoignage, FAQ, Newsletter, Statistique
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'icone_preview', 'ordre_affichage', 'actif', 'nb_avocats']
    list_filter = ['actif', 'date_creation']
    search_fields = ['nom', 'description']
    ordering = ['ordre_affichage', 'nom']
    list_editable = ['ordre_affichage', 'actif']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('nom', 'description', 'icone')
        }),
        ('Affichage', {
            'fields': ('ordre_affichage', 'actif')
        }),
    )
    
    def icone_preview(self, obj):
        if obj.icone:
            return format_html('<i class="{}"></i> {}', obj.icone, obj.icone)
        return '-'
    icone_preview.short_description = 'Icône'
    
    def nb_avocats(self, obj):
        count = Avocat.objects.filter(
            actif=True,
            specialites__icontains=obj.nom.split()[0]
        ).count()
        if count > 0:
            url = reverse('admin:website_avocat_changelist') + f'?specialites__icontains={obj.nom.split()[0]}'
            return format_html('<a href="{}">{} avocat(s)</a>', url, count)
        return '0 avocat'
    nb_avocats.short_description = 'Avocats spécialisés'


@admin.register(Avocat)
class AvocatAdmin(admin.ModelAdmin):
    list_display = ['nom', 'titre', 'specialites', 'photo_preview', 'email', 'telephone', 'ordre_affichage', 'actif']
    list_filter = ['actif', 'titre', 'date_creation']
    search_fields = ['nom', 'specialites', 'email']
    ordering = ['ordre_affichage', 'nom']
    list_editable = ['ordre_affichage', 'actif']
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('nom', 'titre', 'specialites', 'photo')
        }),
        ('Contact', {
            'fields': ('email', 'telephone', 'linkedin')
        }),
        ('Affichage', {
            'fields': ('ordre_affichage', 'actif')
        }),
    )
    
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />', obj.photo.url)
        return format_html('<div style="width: 50px; height: 50px; background: #f0f0f0; border-radius: 50%; display: flex; align-items: center; justify-content: center;"><i class="fas fa-user-tie"></i></div>')
    photo_preview.short_description = 'Photo'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'service', 'date_creation', 'traite', 'contact_actions']
    list_filter = ['traite', 'service', 'date_creation']
    search_fields = ['nom', 'email', 'message']
    readonly_fields = ['date_creation', 'message_preview']
    ordering = ['-date_creation']
    list_per_page = 25
    
    fieldsets = (
        ('Informations du contact', {
            'fields': ('nom', 'email', 'telephone', 'service')
        }),
        ('Message', {
            'fields': ('message', 'message_preview')
        }),
        ('Suivi', {
            'fields': ('traite', 'date_creation')
        }),
    )
    
    def message_preview(self, obj):
        if obj.message:
            preview = obj.message[:200] + '...' if len(obj.message) > 200 else obj.message
            return format_html('<div style="background: #f8f9fa; padding: 10px; border-radius: 5px; white-space: pre-wrap;">{}</div>', preview)
        return '-'
    message_preview.short_description = 'Aperçu du message'
    
    def contact_actions(self, obj):
        if not obj.traite:
            return format_html(
                '<a class="button" href="mailto:{}?subject=Re: Votre demande du {}">Répondre</a>',
                obj.email,
                obj.date_creation.strftime('%d/%m/%Y')
            )
        return 'Traité'
    contact_actions.short_description = 'Actions'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('service')
    
    def mark_as_treated(self, request, queryset):
        queryset.update(traite=True)
        self.message_user(request, f"{queryset.count()} message(s) marqué(s) comme traité(s).")
    mark_as_treated.short_description = "Marquer comme traité"
    
    actions = ['mark_as_treated']


@admin.register(CabinetInfo)
class CabinetInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informations générales', {
            'fields': ('nom_cabinet', 'description')
        }),
        ('Contact', {
            'fields': ('adresse', 'telephone', 'email', 'horaires')
        }),
        ('Réseaux sociaux', {
            'fields': ('facebook', 'twitter', 'linkedin', 'instagram'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        return not CabinetInfo.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def changelist_view(self, request, extra_context=None):
        if not CabinetInfo.objects.exists():
            # Créer une instance par défaut si elle n'existe pas
            CabinetInfo.objects.create(
                nom_cabinet="Cabinet Juridique",
                adresse="123 Avenue de la Justice\n75001 Paris, France",
                telephone="+33 1 23 45 67 89",
                email="contact@cabinet-juridique.fr",
                horaires="Lun - Ven: 9h00 - 18h00\nSam: 9h00 - 12h00",
                description="Votre partenaire juridique de confiance."
            )
        return super().changelist_view(request, extra_context)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'date_publication', 'actif']
    list_filter = ['actif', 'date_publication', 'auteur']
    search_fields = ['titre', 'contenu', 'resume']
    prepopulated_fields = {'slug': ('titre',)}
    ordering = ['-date_publication']
    
    fieldsets = (
        ('Contenu', {
            'fields': ('titre', 'slug', 'resume', 'contenu', 'image')
        }),
        ('Publication', {
            'fields': ('auteur', 'date_publication', 'actif')
        }),
    )


@admin.register(Témoignage)
class TémoignageAdmin(admin.ModelAdmin):
    list_display = ['nom_client', 'entreprise', 'service', 'avocat', 'note', 'approuve', 'ordre_affichage']
    list_filter = ['approuve', 'service', 'avocat', 'note']
    search_fields = ['nom_client', 'entreprise', 'témoignage']
    list_editable = ['approuve', 'ordre_affichage']
    ordering = ['ordre_affichage', '-date_creation']
    
    fieldsets = (
        ('Informations client', {
            'fields': ('nom_client', 'entreprise', 'photo')
        }),
        ('Témoignage', {
            'fields': ('témoignage', 'note', 'service', 'avocat')
        }),
        ('Publication', {
            'fields': ('approuve', 'ordre_affichage')
        }),
    )
    
    def approve_témoignages(self, request, queryset):
        queryset.update(approuve=True)
        self.message_user(request, f"{queryset.count()} témoignage(s) approuvé(s).")
    approve_témoignages.short_description = "Approuver les témoignages sélectionnés"
    
    actions = ['approve_témoignages']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'service', 'ordre_affichage', 'actif']
    list_filter = ['actif', 'service']
    search_fields = ['question', 'reponse']
    list_editable = ['ordre_affichage', 'actif']
    ordering = ['ordre_affichage', 'question']
    
    fieldsets = (
        ('Question', {
            'fields': ('question', 'reponse')
        }),
        ('Catégorie', {
            'fields': ('service',)
        }),
        ('Affichage', {
            'fields': ('ordre_affichage', 'actif')
        }),
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'nom', 'actif', 'date_inscription']
    list_filter = ['actif', 'date_inscription']
    search_fields = ['email', 'nom']
    list_editable = ['actif']
    ordering = ['-date_inscription']
    
    def export_emails(self, request, queryset):
        emails = queryset.filter(actif=True).values_list('email', flat=True)
        response = HttpResponse('\n'.join(emails), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="newsletter_emails.txt"'
        return response
    export_emails.short_description = "Exporter les emails"
    
    actions = ['export_emails']


@admin.register(Statistique)
class StatistiqueAdmin(admin.ModelAdmin):
    list_display = ['nom', 'valeur', 'unite', 'icone_preview', 'ordre_affichage', 'actif']
    list_filter = ['actif']
    search_fields = ['nom']
    list_editable = ['valeur', 'ordre_affichage', 'actif']
    ordering = ['ordre_affichage']
    
    fieldsets = (
        ('Statistique', {
            'fields': ('nom', 'valeur', 'unite', 'icone')
        }),
        ('Affichage', {
            'fields': ('ordre_affichage', 'actif')
        }),
    )
    
    def icone_preview(self, obj):
        if obj.icone:
            return format_html('<i class="{}"></i> {}', obj.icone, obj.icone)
        return '-'
    icone_preview.short_description = 'Icône'


# Personnalisation de l'interface d'administration
admin.site.site_header = "Administration - Cabinet d'Avocat"
admin.site.site_title = "Cabinet d'Avocat"
admin.site.index_title = "Tableau de bord"

# Interface d'administration personnalisée
from django.urls import path, reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta

def admin_dashboard(request):
    """Tableau de bord personnalisé"""
    if not request.user.is_staff:
        return redirect('admin:login')
    
    # Statistiques générales
    stats = {
        'total_services': Service.objects.filter(actif=True).count(),
        'total_avocats': Avocat.objects.filter(actif=True).count(),
        'total_messages': ContactMessage.objects.count(),
        'messages_non_traites': ContactMessage.objects.filter(traite=False).count(),
        'total_articles': Article.objects.filter(actif=True).count(),
        'total_temoignages': Témoignage.objects.filter(approuve=True).count(),
        'total_faqs': FAQ.objects.filter(actif=True).count(),
        'total_newsletter': Newsletter.objects.filter(actif=True).count(),
        'total_stats': Statistique.objects.filter(actif=True).count(),
    }
    
    # Messages récents
    messages_recents = ContactMessage.objects.select_related('service').order_by('-date_creation')[:5]
    
    # Témoignages en attente
    temoignages_en_attente = Témoignage.objects.filter(approuve=False).order_by('-date_creation')[:5]
    
    # Articles récents
    articles_recents = Article.objects.filter(actif=True).order_by('-date_publication')[:3]
    
    context = {
        'title': 'Tableau de bord',
        'stats': stats,
        'messages_recents': messages_recents,
        'temoignages_en_attente': temoignages_en_attente,
        'articles_recents': articles_recents,
    }
    
    return render(request, 'admin/dashboard.html', context)

# Rediriger l'index vers le tableau de bord personnalisé
original_index = admin.site.index

def custom_index(request, extra_context=None):
    """Index personnalisé avec redirection vers le tableau de bord"""
    if not request.user.is_staff:
        return redirect('admin:login')
    
    # Statistiques pour l'index
    stats = {
        'total_services': Service.objects.filter(actif=True).count(),
        'total_avocats': Avocat.objects.filter(actif=True).count(),
        'total_messages': ContactMessage.objects.count(),
        'messages_non_traites': ContactMessage.objects.filter(traite=False).count(),
        'total_articles': Article.objects.filter(actif=True).count(),
        'total_temoignages': Témoignage.objects.filter(approuve=True).count(),
        'total_faqs': FAQ.objects.filter(actif=True).count(),
        'total_newsletter': Newsletter.objects.filter(actif=True).count(),
        'total_stats': Statistique.objects.filter(actif=True).count(),
    }
    
    context = {
        'title': 'Administration',
        'stats': stats,
    }
    
    return render(request, 'admin/index.html', context)

admin.site.index = custom_index

# Intégrer le tableau de bord personnalisé
original_get_urls = admin.site.get_urls

def custom_get_urls():
    custom_urls = [
        path('dashboard/', admin_dashboard, name='admin_dashboard'),
    ]
    return custom_urls + original_get_urls()

admin.site.get_urls = custom_get_urls
