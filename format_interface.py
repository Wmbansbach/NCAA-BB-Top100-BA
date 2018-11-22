import pandas

class FormatInterface():

    def __init__(self, dataDict):
        self.data_dict = dataDict
        self.frame = pandas.DataFrame()
        self.makeFrame()
     

    def makeFrame(self):
        for rank, val in self.data_dict.items():
            self.buffer_dict = {"Rank": pandas.Series([val.rank], index=[rank]),
                               "Name": pandas.Series([val.name], index=[rank]),
                               "Bat.Av.": pandas.Series([val.ba], index=[rank]),
                               "Team": pandas.Series([val.team], index=[rank]),
                               "Grade": pandas.Series([val.grade], index=[rank]),
                               "Position": pandas.Series([val.pos], index=[rank]),
                               "Games": pandas.Series([val.games], index=[rank]),
                               "At Bats": pandas.Series([val.ab], index=[rank]),
                               "Hits": pandas.Series([val.h], index=[rank])}

            self.frame = self.frame.append(pandas.DataFrame(self.buffer_dict)) 
    
    def toCSV(self):
        filename = input("Create a filename: ")
        self.frame.to_csv(filename + ".csv")
            
             