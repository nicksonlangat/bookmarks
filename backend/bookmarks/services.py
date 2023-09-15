from django.db import transaction

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from common.services import model_update
from .models import Bookmark, Color

@transaction.atomic
def bookmark_create(data, *args, **kwargs) -> Bookmark:
    url = data["url"].replace(" ","")
    try:
        page = requests.get(url)
    except requests.exceptions.MissingSchema:
        url = f"https://{url}"
        page = requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    site = urlparse(url).netloc.split('.')[0]
    if site == "twitter":
        title = soup.find("meta", property="og:site_name")
        url_link = soup.find("meta", property="og:url")
        image = soup.find("meta", property="og:image")
        description = soup.find("meta", property="og:description")
    else:
        title = soup.find("meta", property="og:title")
        url_link = soup.find("meta", property="og:url")
        image = soup.find("meta", property="og:image")
        description = soup.find("meta", property="og:description")

    obj = Bookmark(
        user=data['user'],
        title=title['content'] if title else "", 
        url=url_link['content'] if url_link else url, 
        description=description['content'] if description else "", 
        thumbnail=image['content'] if image else "",
        site_name=site
    )

    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def bookmark_update(*, bookmark: Bookmark, data) -> Bookmark:
    non_side_effect_fields = []

    bookmark, has_updated = model_update(instance=bookmark, fields=non_side_effect_fields, data=data)

    return bookmark


@transaction.atomic
def color_create(data, *args, **kwargs) -> Color:
    code = data['code']
    
    if code.startswith("#"):
        pass
    else:
        code = f"#{code}"
    
    obj = Color(
        code=code
    )

    obj.full_clean()
    obj.save()

    return obj

@transaction.atomic
def color_update(*, color: Color, data) -> Color:
    non_side_effect_fields = []

    color, has_updated = model_update(instance=color, fields=non_side_effect_fields, data=data)

    return color
