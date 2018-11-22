import page_scraper
import database_tools
import format_interface
import graph_data
import sys


class CmdInterface():
    """
    Basic command line interface w/
    simple input validation

    """
    def __init__(self):
        self.scraped = False
        self.pushed = False
        self.scraper = page_scraper.PageScraper()
        self.printer = any
        self.db = any
        self.mainDisplay()

    def graphDisplay(self):
        grapher = graph_data.GraphData(self.scraper.player_dict)
        print('NCAA BA Rank Analyzer')
        print('====================================')
        print('Graphing Options')
        print('1. Pie Chart (Grade Distribution)')
        print('2. Bar Chart (Team Frequency)')
        
        while True:
            sel = input(":")

            if sel == '1':
                grapher.getGradeChart()
            elif sel == '2':
                grapher.getTeamChart()
            elif sel == '-back':
                return
            elif sel == '-quit':
                sys.exit()
            else:
                print()
                print('That is not a recognized command..')
                print()



    def mainDisplay(self):
        print('NCAA BA Rank Analyzer\n\n')
        print('====================================')
        print('Type a command: (--help for help)')

        while True:
            sel = input(":")

            if sel == '--help':
                print()
                print('-parse\tParse the current page')
                print('-push\tPush parsed data to database')
                print('-show\tPrint parsed data')
                print('-graph\tDisplay graphing options')
                print('-csv\tPush parsed data to csv')
                print('-quit\tClose the application')
                print()
                continue

            elif sel == '-parse' and not self.scraped:
                self.scraped = True
                # call scraper twice to scrape both pages (100 players)
                for i in range(2):
                    self.scraper.ScrapePage()

                # Initialize ultility for formatting interface with newly parsed data
                self.printer = format_interface.FormatInterface(self.scraper.player_dict)
                print()
                print('Parse Successful\n')

            
            elif sel == '-push' and not self.pushed:
                self.scraped = True
                playerDictionary = self.scraper.player_dict
                
                database_tools.ToDatabase(playerDictionary, input('Enter a table name: '))
                

            elif sel == '-show':
                print()
                print(self.printer.frame)

            elif sel == '-csv':
                self.printer.toCSV()
                print(".csv was successfully created")

            elif sel == '-graph':
                self.graphDisplay()

            elif sel == '-quit':\
                sys.exit()

            else:
                print()
                print('That is not a recognized command..')
                print()