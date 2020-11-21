from bs4 import BeautifulSoup
import urllib.request
import re
import lxml

class colors:
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"


html_page = urllib.request.urlopen("http://www.sae.edu/")
soup = BeautifulSoup(html_page, features='lxml')
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    printlink = link.get('href')
    print(f'{colors.GREEN}URL: {colors.RESET} {colors.BLUE}' + printlink)