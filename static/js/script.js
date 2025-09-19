// Navigation mobile
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Fermer le menu mobile quand on clique sur un lien
    document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }));
}

// Navigation sticky avec effet de transparence
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.15)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        }
    }
});

// Animation d'apparition des éléments au scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('loaded');
        }
    });
}, observerOptions);

// Observer les éléments à animer
document.addEventListener('DOMContentLoaded', () => {
    const elementsToAnimate = document.querySelectorAll('.service-card, .team-member, .contact-item');
    elementsToAnimate.forEach(el => {
        el.classList.add('loading');
        observer.observe(el);
    });
});

// Gestion des messages Django
document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Afficher l'alerte
        setTimeout(() => {
            alert.classList.add('show');
        }, 100);
        
        // Fermer automatiquement après 5 secondes
        setTimeout(() => {
            closeAlert(alert);
        }, 5000);
    });
    
    // Fermeture manuelle des alertes
    const closeButtons = document.querySelectorAll('.alert-close');
    closeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const alert = btn.closest('.alert');
            closeAlert(alert);
        });
    });
});

function closeAlert(alert) {
    if (alert) {
        alert.classList.remove('show');
        setTimeout(() => {
            if (alert.parentNode) {
                alert.parentNode.removeChild(alert);
            }
        }, 300);
    }
}

// Validation du formulaire de contact
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        // Validation côté client
        const nom = contactForm.querySelector('input[name="nom"]');
        const email = contactForm.querySelector('input[name="email"]');
        const service = contactForm.querySelector('select[name="service"]');
        const message = contactForm.querySelector('textarea[name="message"]');
        const rgpd = contactForm.querySelector('input[name="rgpd"]');
        
        let isValid = true;
        
        // Réinitialiser les erreurs
        clearFormErrors();
        
        if (!nom.value.trim()) {
            showFieldError(nom, 'Le nom est obligatoire');
            isValid = false;
        }
        
        if (!email.value.trim()) {
            showFieldError(email, 'L\'email est obligatoire');
            isValid = false;
        } else if (!isValidEmail(email.value)) {
            showFieldError(email, 'Veuillez entrer une adresse email valide');
            isValid = false;
        }
        
        if (!service.value) {
            showFieldError(service, 'Veuillez sélectionner un service');
            isValid = false;
        }
        
        if (!message.value.trim()) {
            showFieldError(message, 'Le message est obligatoire');
            isValid = false;
        }
        
        if (!rgpd.checked) {
            showFieldError(rgpd, 'Vous devez accepter l\'utilisation de vos données');
            isValid = false;
        }
        
        if (!isValid) {
            e.preventDefault();
        }
    });
}

function showFieldError(field, message) {
    // Supprimer l'erreur existante
    const existingError = field.parentNode.querySelector('.field-error');
    if (existingError) {
        existingError.remove();
    }
    
    // Ajouter la nouvelle erreur
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    errorDiv.style.color = '#e74c3c';
    errorDiv.style.fontSize = '0.9rem';
    errorDiv.style.marginTop = '0.25rem';
    
    field.parentNode.appendChild(errorDiv);
    field.style.borderColor = '#e74c3c';
}

function clearFormErrors() {
    const errors = document.querySelectorAll('.field-error');
    errors.forEach(error => error.remove());
    
    const fields = document.querySelectorAll('.contact-form input, .contact-form select, .contact-form textarea');
    fields.forEach(field => {
        field.style.borderColor = '#e9ecef';
    });
}

// Validation email
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Smooth scrolling pour les liens d'ancrage
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 70; // Compenser la hauteur de la navbar
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Effet de parallaxe léger sur le hero
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// Gestion des erreurs JavaScript
window.addEventListener('error', (e) => {
    console.error('Erreur JavaScript:', e.error);
});

// Performance: Lazy loading des images (si ajoutées plus tard)
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    // Ajouter une classe pour les animations CSS
    document.body.classList.add('loaded');
    
    // Précharger les polices critiques
    if ('fonts' in document) {
        document.fonts.ready.then(() => {
            document.body.classList.add('fonts-loaded');
        });
    }
    
    // Gestion des formulaires avec pré-remplissage
    const urlParams = new URLSearchParams(window.location.search);
    const serviceId = urlParams.get('service');
    if (serviceId) {
        const serviceSelect = document.querySelector('select[name="service"]');
        if (serviceSelect) {
            serviceSelect.value = serviceId;
        }
    }
});

// Gestion du thème sombre (optionnel pour plus tard)
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
}

// Charger le thème sauvegardé
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-theme');
}

// Fonction pour afficher une notification toast
function showNotification(message, type = 'info') {
    // Supprimer les notifications existantes
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    // Créer la nouvelle notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle'}"></i>
            <span>${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;
    
    // Styles pour la notification
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#27ae60' : type === 'error' ? '#e74c3c' : '#3498db'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        transform: translateX(400px);
        transition: transform 0.3s ease;
        max-width: 400px;
    `;
    
    // Styles pour le contenu de la notification
    const content = notification.querySelector('.notification-content');
    content.style.cssText = `
        display: flex;
        align-items: center;
        gap: 10px;
    `;
    
    // Styles pour le bouton de fermeture
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        margin-left: auto;
    `;
    
    document.body.appendChild(notification);
    
    // Animation d'entrée
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Fermeture automatique après 5 secondes
    setTimeout(() => {
        closeNotification(notification);
    }, 5000);
    
    // Fermeture manuelle
    closeBtn.addEventListener('click', () => {
        closeNotification(notification);
    });
}

function closeNotification(notification) {
    notification.style.transform = 'translateX(400px)';
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 300);
}
