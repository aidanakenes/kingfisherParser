from typing import Optional, List

import requests
from bs4 import BeautifulSoup

from src.models.item import Item
from src.utils.err_utils import *
from src.utils.logger import get_logger
from src.utils.conf import headers, cookies


logger = get_logger(__name__)


class KingfishParser:

    def __init__(self):
        pass

    def _get_item(self, category_link: str) -> List[Item]:
        try:
            r = requests.get(
                url=category_link,
                headers=headers, cookies=cookies,
                timeout=10
            )
            if r.ok:
                _items = []
                soup = BeautifulSoup(r.content, 'lxml')
                div_tags = soup.find_all('div', class_='goodsBlock')
                category, subcategory = category_link.split('/')[-3:-1]
                for l in div_tags:
                    _items.append(Item(
                        item_id='',
                        title=l.find_all('a', class_='title')[0].span.text,
                        category=category,
                        subcategory=subcategory,
                        price=l.find_all('span', class_='price')[0].find_all('span', class_='new')[0].text,
                        city='',
                        url=l.a.get('href')
                    ))
                    logger.info(f'Returning the KingfishParser\'s result for item {l.a.get("href")}')

                return _items
        except TimeoutError as e:
            logger.error(f'Cannot parse page: {type(e)}')
            raise ApplicationError()

    def get_items(self, category_links: dict) -> Optional[dict]:
        try:
            items = dict()
            for key, val in category_links.items():
                items[key] = list()
                for idx in range(len(val)):
                    items[key].append({val[idx]: self._get_item(val[idx])})
            return items
        except TimeoutError as e:
            logger.error(f'Cannot parse page: {type(e)}')
            raise ApplicationError()
