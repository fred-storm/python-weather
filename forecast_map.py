"""
Author: Adam Frederick
Date: 2026-02-23
Project: Weather forecast map via web scrapper
"""
import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def map_scrapper():

    url = "https://www.wpc.ncep.noaa.gov/national_forecast/natfcst.php"

    grab = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})

    grab_content = grab.content

    soup = BeautifulSoup(grab_content, 'html.parser')

    img_tags = soup.find_all('img')

    image_urls = []
    for img in img_tags:
        src = img.get('src')
        if src:
            absolute_url = urllib.parse.urljoin(url, src)
            image_urls.append(absolute_url)

    if not os.path.exists('images'):
        os.makedirs('images')

    for img_url in image_urls:
        if "noaad" in img_url:
            try:
                img_name = os.path.basename(urllib.parse.urlparse(img_url).path)
                if not img_name:
                    continue
                urllib.request.urlretrieve(img_url, os.path.join('images', img_name))
                print(f'Downloaded: {img_name}')

            except Exception as e:
                print(f'Error downloading {img_name}: {e}')
    return