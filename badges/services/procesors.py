from urlparse import urlparse
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def check_if_url_is_valid(url):
    """ validates oEmbed url parameter"""

    val = URLValidator(verify_exists=False)
    try:
        val(url)
    except ValidationError:
        return False

    domain = urlparse(url).netloc
    if domain.split('.')[0] == 'www':
        domain = '.'.join(domain.split('.')[1:])

    if settings.DEBUG:
        return True
    elif domain != Site.objects.get_current():
        return False
    return True