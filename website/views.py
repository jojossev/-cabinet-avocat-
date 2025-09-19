from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Service, Avocat, ContactMessage, CabinetInfo
from .forms import ContactForm


def home(request):
    """Vue pour la page d'accueil"""
    context = {
        'services': Service.objects.filter(actif=True)[:6],
        'avocats': Avocat.objects.filter(actif=True)[:3],
        'cabinet_info': CabinetInfo.objects.first(),
    }
    return render(request, 'website/home.html', context)


def services(request):
    """Vue pour la page des services"""
    services_list = Service.objects.filter(actif=True)
    
    # Recherche
    search_query = request.GET.get('search')
    if search_query:
        services_list = services_list.filter(
            Q(nom__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    context = {
        'services': services_list,
        'search_query': search_query,
    }
    return render(request, 'website/services.html', context)


def equipe(request):
    """Vue pour la page de l'équipe"""
    avocats = Avocat.objects.filter(actif=True)
    
    # Recherche
    search_query = request.GET.get('search')
    if search_query:
        avocats = avocats.filter(
            Q(nom__icontains=search_query) | 
            Q(specialites__icontains=search_query) |
            Q(titre__icontains=search_query)
        )
    
    context = {
        'avocats': avocats,
        'search_query': search_query,
    }
    return render(request, 'website/equipe.html', context)


def contact(request):
    """Vue pour la page de contact"""
    cabinet_info = CabinetInfo.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 
                'Votre message a été envoyé avec succès ! Nous vous contacterons bientôt.'
            )
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'cabinet_info': cabinet_info,
    }
    return render(request, 'website/contact.html', context)


def service_detail(request, service_id):
    """Vue pour le détail d'un service"""
    try:
        service = Service.objects.get(id=service_id, actif=True)
        # Récupérer les avocats spécialisés dans ce service
        avocats_specialises = Avocat.objects.filter(
            actif=True,
            specialites__icontains=service.nom.split()[0]  # Recherche approximative
        )
        
        context = {
            'service': service,
            'avocats_specialises': avocats_specialises,
        }
        return render(request, 'website/service_detail.html', context)
    except Service.DoesNotExist:
        messages.error(request, 'Service non trouvé.')
        return redirect('services')


def avocat_detail(request, avocat_id):
    """Vue pour le détail d'un avocat"""
    try:
        avocat = Avocat.objects.get(id=avocat_id, actif=True)
        # Récupérer les services liés aux spécialités de l'avocat
        specialites_mots = avocat.specialites.split()
        services_lies = Service.objects.filter(
            actif=True,
            nom__in=specialites_mots
        )
        
        context = {
            'avocat': avocat,
            'services_lies': services_lies,
        }
        return render(request, 'website/avocat_detail.html', context)
    except Avocat.DoesNotExist:
        messages.error(request, 'Avocat non trouvé.')
        return redirect('equipe')
