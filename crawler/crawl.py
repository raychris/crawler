''' drive the web crawling '''

from crawler.logging.app_logging import enableLogging
from crawler.argparsing.argparsing import getArguments
from crawler.crawling.utilities import get_links_from_uri

import time


# turn on logging
log = enableLogging()

def crawl():
    '''drive the web crawling workflow'''

    commandline_args = vars(getArguments(argList=None))

    log.info(f'Starting crawl for domain: {commandline_args['starting_domain']}')

    # keep track of uri's visited and uri's to visit
    where_weve_been = []

    where_were_going = ['https://' + commandline_args['starting_domain']]

    # take a look at links on each uri
    while len(where_were_going) > 0:
        uri = where_were_going.pop(0)
        if uri not in where_weve_been:
            where_weve_been.append(uri)
            log.info(f'Getting links for {uri}')
            links = get_links_from_uri(uri=uri,
                                        domain=commandline_args['starting_domain'],
                                        log=log)
            where_were_going += links
            log.info(f'Links on this page: {links}')
            log.info(f'Crawl delay of {commandline_args['crawl_delay']}')
            time.sleep(commandline_args['crawl_delay'])

    log.info(f'A list of each URI visited at {commandline_args['starting_domain']}: {where_weve_been}')

    


if __name__ == '__main__':
    crawl()