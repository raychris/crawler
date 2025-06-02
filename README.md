## SIMPLE WEB CRAWLER

`crawler` is a python package that, given a domain name, finds and visits each link found in a web site at the domain name that is also part of that domain.

## INSTALLATION

`crawler` has been packaged according to specifications found in the pyproject.toml.  The `dist` directory contains a .whl file called crawler-0.1-py3-none-any.whl.

`crawler` has been tested on a machine running RHEL 8.

Install `crawler' into your python evironment of choice (dependencies identified in the pyproject.toml):

`pip install path_to_crawler/dist/crawler-0.1-py3-none-any.whl`

Check your installation and see some basic instructions:

`crawl --help`

A sample execution from a terminal:

`crawl --starting-domain ffla-monterey.org --crawl-delay .5`

Logs will output to the console and to a file.  Control the log file output by setting an environment variable called `LOGDIR`.

Alternatively, to run `crawler` without installing the package (making sure the path to the crawler directory is in your PATH or PYTHONPATH):

`python path_to_crawler/crawler/crawler.py --starting-domain ffla-monterey.org --crawl-delay .5`

## FEATURES (TRADE OFFS)

The entry point to `crawler` is crawl.py where the workflow is driven. The package has a logging module, an argparsing module, and a crawling utilities module.  

The web crawling implementation is found in utilities/get_links_from_uri.  I use requests to make http requests and BeautifulSoup to parse the responses for html links.  Some web sites have href's set to relative paths for site internal links.  Others have fully qualified paths.  get_links_from_uri works with those two patterns to construct a list of domain specific links.

`crawl.py` keeps track of what pages have been checked and what pages need to be checked for links.  It also adds in a user defined 'crawl delay' in case of throttling by web servers.  I chose to implement a serial crawler (no parallel requests).  This may avoid some throttling by some organizations.  It also seriously slows down performance for web sites that host things like event calendar items as links (especially when the calendar goes back a ways).

I chose to deliver this product as a package for the benefits that a more formal structure offers (versioning, ease of deployment (pip), automatically adding the executable to a user's bin, and various other metadata options).  This adds overhead but makes managing the codebase easier over the long term.

In .github/workflows/build_deploy.yaml there is a skeleton of a GitHub actions CI/CD pipeline.  On a push to the main branch, the package is built, tested, and deployed.

I wrote this package in VS Code with Ruff default rules for linting.

