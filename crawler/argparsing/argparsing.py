'''Command line interface argument handling'''

import argparse
import textwrap    

def getArguments(argList):
    '''Get arguments from the command line interface and return parsed arguments'''
    description = textwrap.dedent('''\
                                       A python package that performs the following tasks
​
                                        1) Given a starting URL, the crawler visits each URL it finds on the same domain
                                        2) print each URL visited and list links found on that page.
                                        3) The crawler should be limited to one subdomain''')

    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    addArguments(parser, argList)
    return parser.parse_args()

def addArguments(parser, argList):
    '''Define how arguments available to the command line interface should be parsed'''
    parser.add_argument('--starting-domain',
                        help='base domain to crawl (no https:// or http:// prefix)',
                        type=str,
                        default='ffla-monterey.org')
    parser.add_argument('--crawl-delay',
                        help='crawl delay in seconds (time between http requests)',
                        type=float,
                        default=.5)