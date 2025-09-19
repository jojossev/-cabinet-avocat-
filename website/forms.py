from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Service


class ContactForm(forms.ModelForm):
    """Formulaire de contact"""
    
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'telephone', 'service', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre email',
                'required': True
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre téléphone'
            }),
            'service': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Décrivez votre situation',
                'rows': 5,
                'required': True
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrer les services actifs
        self.fields['service'].queryset = Service.objects.filter(actif=True)
        self.fields['service'].empty_label = "Sélectionnez un service"
    
    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if len(nom.strip()) < 2:
            raise forms.ValidationError("Le nom doit contenir au moins 2 caractères.")
        return nom.strip()
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message.strip()) < 10:
            raise forms.ValidationError("Le message doit contenir au moins 10 caractères.")
        return message.strip()
    
    def save(self, commit=True):
        message = super().save(commit=False)
        
        if commit:
            message.save()
            
            # Envoyer un email de notification (optionnel)
            try:
                send_mail(
                    subject=f'Nouveau message de contact de {message.nom}',
                    message=f'''
Nouveau message reçu sur le site du cabinet :

Nom: {message.nom}
Email: {message.email}
Téléphone: {message.telephone or 'Non renseigné'}
Service: {message.service or 'Non spécifié'}

Message:
{message.message}

Date: {message.date_creation.strftime('%d/%m/%Y à %H:%M')}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                # En cas d'erreur d'envoi d'email, on continue
                pass
        
        return message
