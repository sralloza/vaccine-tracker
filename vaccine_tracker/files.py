from collections import namedtuple
from typing import Generator

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString

from vaccine_tracker.config import settings

File = namedtuple("File", "title url")
URL = "https://www.saludcastillayleon.es/es/covid-19-poblacion/vacunacion-covid-19/lugares-vacunacion/burgos"


def get_files() -> Generator[File, None, None]:
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find("ul", id="cmContentResourcesList")
    if not container or isinstance(container, NavigableString):
        raise SystemExit("Invalid container")

    resource_list = container("li")
    for resource in resource_list:
        title = [text for text in resource.stripped_strings][0]
        if settings.filter_keyword is not None:
            if settings.filter_keyword not in title.lower():
                continue

        url = "https://www.saludcastillayleon.es" + resource.a["href"]
        yield File(title, url)
