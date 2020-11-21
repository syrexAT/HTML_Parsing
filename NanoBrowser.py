from html.parser import HTMLParser
import urllib.request
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._path = []
        self._anchor_text = ''
        self._anchor_link = ''

    def handle_starttag(self, tag, attrs):
        self._path.append(tag)
        if tag == 'a':
            self._anchor_text = ''
            self._anchor_link = dict(attrs).get('href')
        #print(' > '.join(self._path))
        
    def handle_endtag(self, tag):
        if self._path[-1] == 'a': #a is link tag
            print('\033[31m LINK: \033[32m', self._anchor_text, '\033[33mURL:', self._anchor_link, '\033[0m')
        self._path.pop()

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        if self._path and self._path[-1] == 'a':
            self._anchor_text += data
        else:
            print(end=data)

ReadURL = urllib.request.urlopen('http://www.sae.edu/').read().decode('UTF-8')
print(ReadURL)

parser = MyHTMLParser()
parser.feed(ReadURL)