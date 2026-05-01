import os
from pathlib import Path

# 1. Chemins de base
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Sécurité (NE JAMAIS PARTAGER CETTE CLÉ EN PRODUCTION)
SECRET_KEY = "django-insecure-votre-cle-secrete-ici-mettez-ce-que-vous-voulez"

# 3. Mode Débogage (True pour le développement, False pour la mise en ligne)
DEBUG = True

# 4. Hôtes autorisés (Vide pour le local)
ALLOWED_HOSTS = []

# 5. Applications installées (Les modules de Django + les tiens)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
]

# 6. Middlewares (Gestion des requêtes/réponses)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 7. Configuration des URLs principales
ROOT_URLCONF = "my_site.urls"

# 8. Configuration des Templates (HTML)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# 9. Serveur WSGI
WSGI_APPLICATION = "my_site.wsgi.application"

# 10. Base de données (Ce qui causait ton erreur précédente)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 11. Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 12. Internationalisation (Langue et Heure)
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 13. Fichiers statiques (CSS, JavaScript, Images)
STATIC_URL = "static/"

# 14. Type de champ par défaut pour les IDs
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
