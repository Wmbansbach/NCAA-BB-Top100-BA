import urllib.request as urllib
import bs4 as bs
import data_cleaner

class PageScraper:

    def __init__(self):
        
        self.is_init = True
        self.player_dict = dict()
        self.init_url = "http://www.ncaa.com/stats/baseball/d1/current/individual/200"
        self.page2_url = "http://www.ncaa.com/stats/baseball/d1/current/individual/200/p2"
        self.request = ''
        
    def setHeaders(self, target):
        browserAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
        requestHeader = {"User-Agent": browserAgent}

        self.request = urllib.Request(target, headers=requestHeader)

    def ScrapePage(self):
        # Check if initial request
        if self.is_init:
            self.is_init = False
            self.setHeaders(self.init_url)
        else:
             # Run second request if not
            self.setHeaders(self.page2_url)

        dataList = []
        with urllib.urlopen(self.request) as response:
            html = response.read()
            _html = bs.BeautifulSoup(html, "lxml")

            for tag in _html.find_all("tr"):
                valueList = []
                formattedString = tag.text.format()
                valueList = formattedString.split('\n')
                dataList.append(valueList)
            
            cleaner = data_cleaner.DataCleaner()

            if self.is_init:
                self.player_dict = cleaner.cleanUp(dataList)
            else:
                self.player_dict.update(cleaner.cleanUp(dataList))
            
