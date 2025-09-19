from django.shortcuts import render
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import Service, Avocat, ContactMessage, Article, Témoignage, FAQ, Newsletter, Statistique

def admin_dashboard(request):
    """Tableau de bord personnalisé pour l'administration"""
    
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
    }
    
    # Messages récents
    messages_recents = ContactMessage.objects.select_related('service').order_by('-date_creation')[:5]
    
    # Témoignages en attente d'approbation
    temoignages_en_attente = Témoignage.objects.filter(approuve=False).order_by('-date_creation')[:5]
    
    # Articles récents
    articles_recents = Article.objects.filter(actif=True).order_by('-date_publication')[:3]
    
    # Statistiques par service
    services_stats = Service.objects.annotate(
        nb_messages=Count('contactmessage', filter=Q(contactmessage__date_creation__gte=timezone.now() - timedelta(days=30)))
    ).order_by('-nb_messages')[:5]
    
    # Messages par mois (derniers 6 mois)
    messages_par_mois = []
    for i in range(6):
        date = timezone.now() - timedelta(days=30*i)
        mois = date.strftime('%B %Y')
        count = ContactMessage.objects.filter(
            date_creation__year=date.year,
            date_creation__month=date.month
        ).count()
        messages_par_mois.append({'mois': mois, 'count': count})
    
    context = {
        'title': 'Tableau de bord',
        'stats': stats,
        'messages_recents': messages_recents,
        'temoignages_en_attente': temoignages_en_attente,
        'articles_recents': articles_recents,
        'services_stats': services_stats,
        'messages_par_mois': messages_par_mois,
    }
    
    return render(request, 'admin/dashboard.html', context)

# Cette fonction est maintenant dans admin.py
