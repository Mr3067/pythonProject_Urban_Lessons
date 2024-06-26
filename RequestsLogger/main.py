import requests as rq
import logging

import logger
sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        logging.root.setLevel(logging.INFO)
        if response.status_code == 200:
            logger.log_info.info(f'%s   code %s',
                                 site,
                                 response.status_code)
        else:
            logging.root.setLevel(logging.WARNING)
            logger.log_warning.warning(f'%s   code %s',
                                 site,
                                 response.status_code)
    except Exception:
        logging.root.setLevel(logging.ERROR)
        logger.log_error.error(f'%s   code %s',
                                   site,
                                   response.status_code)


