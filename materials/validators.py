from rest_framework.serializers import ValidationError
import re
from urllib.parse import urlparse

def validate_only_youtube_links(value):
    if not value:
        return

    # Все URL в тексте
    url_pattern = r'(?:https?://|www\.)[^\s<>"\'()]+'
    urls = re.findall(url_pattern, value, flags=re.IGNORECASE)

    for url in urls:
        # Если ссылка начинается с www., корректно выделяем домен
        parsed_url = urlparse(url if url.startswith(('http://', 'https://')) else f'http://{url}')
        domain = parsed_url.netloc.lower()

        # Убираем порт
        domain = domain.split(':')[0]

        # Проверяем, что домен — это youtube.com или его поддомен
        if domain != 'youtube.com' and not domain.endswith('.youtube.com'):
            raise ValidationError(
                f'Обнаружена недопустимая ссылка ({url}). Разрешены ссылки только на youtube.com.'
            )
