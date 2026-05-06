# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

# MEDIA
from . import BASE_DIR


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'