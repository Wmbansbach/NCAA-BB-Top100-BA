import player as pl

class DataCleaner:

    def __init__(self):
        self.data_dict = {}
   
    def cleanUp(self, d_list):
        d_list = d_list[1:]     # Remove headers
        
        # Create player object mapping values to new attributes
        for val in d_list:
            player = pl.PlayerData()
            player.rank = val[1]
            player.name = val[2]
            player.team = val[3]
            player.grade = val[4]
            player.pos = val[5]
            player.games = val[6]
            player.ab = val[7]
            player.h = val[8]
            player.ba = val[9]

            self.data_dict[player.rank] = player

        return self.data_dict
            

        
        

    