"""
Middleware pour améliorer la sécurité et les performances
"""
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import time

class SecurityHeadersMiddleware(MiddlewareMixin):
    """
    Middleware pour ajouter des headers de sécurité et de performance
    """
    
    def process_response(self, request, response):
        # Headers de sécurité
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
        
        # Content Security Policy
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data: https:; "
            "connect-src 'self'; "
            "frame-ancestors 'none';"
        )
        response['Content-Security-Policy'] = csp
        
        # Headers de performance pour les fichiers statiques
        if request.path.startswith('/static/'):
            response['Cache-Control'] = 'public, max-age=31536000, immutable'
            response['Expires'] = ''
        else:
            response['Cache-Control'] = 'public, max-age=3600'
        
        # Headers pour les cookies
        if hasattr(response, 'cookies'):
            for cookie in response.cookies.values():
                cookie['httponly'] = True
                cookie['samesite'] = 'Lax'
                if not settings.DEBUG:
                    cookie['secure'] = True
        
        return response
