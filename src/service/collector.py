from typing import Optional

import requests
from bs4 import BeautifulSoup

from src.utils.err_utils import *
from src.utils.logger import get_logger
from src.utils.conf import headers, cookies


logger = get_logger(__name__)


class KingfishCollector:

    def __init__(self):
        self._home = 'https://kingfisher.kz'

    def get_category_links(self) -> Optional[dict]:
        try:
            r = requests.get(
                url=self._home,
                headers=headers, cookies=cookies,
                timeout=10
            )
            if r.ok:
                _links = {}
                soup = BeautifulSoup(r.content, 'lxml')
                li_tags = soup.find_all('li', class_='dropmenu', )
                logger.info(f'Returning the KingfishCollector\'s result')
                for l in li_tags:
                    category = l.find_all('span')[0].text
                    _links[category] = []
                    for a in l.find_all('a'):
                        _links[category].append(f'{self._home}{a.get("href")}')
                print('\n\n')
                return _links
        except TimeoutError as e:
            logger.error(f'Cannot parse page: {type(e)}')
            raise ApplicationError()

