''' utilities for the package'''

from bs4 import BeautifulSoup
import requests
import logging

def get_links_from_uri(uri: str,domain: str,log: logging.logger) -> list:
    '''Find links at uri from a specified domain
    
    Parameters
    ----------
    uri: str
        a uri to crawl
    domain: str
        the domain name for filtering links at the uri
    log: logging.logger
        logger object

    Return
    ------
    links: list
        a list of domain specific links
    
    '''
    try:
        log.info(f'Making http request to {uri}')
        r = requests.get(uri,timeout=2)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, 'html.parser')
        all_uris = set([ link['href'] for link in soup.find_all('a',href=True) ])
        # assuming relative links here
        links = [ 'https://' + domain + link for link in all_uris 
                            if 'https://' not in link and 
                            'http://' not in link and
                            'mailto' not in link and 
                            domain + link != domain +'/' ]
        # assuming fully qualified links here
        # if len(links) < 1:
        links = links + [ link for link in all_uris 
                         if link.startswith('https://' + domain) and
                         'mailto' not in link ]
        return links
    except requests.exceptions.RequestException as e:
        log.warning(f'Error getting {uri}')
        log.warning(f'{e}')
        return []