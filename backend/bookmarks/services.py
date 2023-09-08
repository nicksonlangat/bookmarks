from django.db import transaction

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from common.services import model_update
from .models import Bookmark

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
        title=title['content'] if title else "No meta title given", 
        url=url_link['content'] if url_link else url, 
        description=description['content'] if description else "Click the button below to view this link", 
        thumbnail=image['content'] if image else "No meta image given",
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
