import os


class Postgres:
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASS = os.environ.get('POSTGRES_PASSWORD')
    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_HOST = os.environ.get('POSTGRES_HOST')
    ENGINE = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


cookies = {
    'PHPSESSID': '25752b63fb193093122538980ed674cc',
    '_gcl_au': '1.1.1076568257.1633044344',
    '_ga': 'GA1.2.2128147009.1633044345',
    'tmr_reqNum': '125',
    'tmr_lvid': '080c8a7caeeb28a37f42079a9c0a2425',
    'tmr_lvidTS': '1633044345455',
    '_ym_uid': '1633044346695949033',
    '_ym_d': '1633044346',
    'rngst2': '%7B%22utmz%22%3A%7B%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(direct)%22%2C%22utm_content%22%3A%22(not%20set)%22%2C%22utm_term%22%3A%22(none)%22%7D%2C%22sl%22%3A%22fbdc2dcc-c28a-4dda-a4d9-9e9cb9a74d11%22%7D',
    '_csrf': '6e950e934d0e0284f8f3c5844d9921f12a622baf51f9e31c51252fd220c2213aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22j0JZ8l4XdxCNdF8fELya7v_UraHP13PO%22%3B%7D',
    '_fbp': 'fb.1.1633265930490.819488545',
    'tmr_detect': '0%7C1633277213183',
    'plerdy_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fkingfisher.kz%2F',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'DNT': '1',
    'Sec-GPC': '1',
    'Cache-Control': 'max-age=0',
}
