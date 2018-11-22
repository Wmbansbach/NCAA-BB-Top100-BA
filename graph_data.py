import matplotlib.pyplot as plt
import numpy as np



class GraphData:
    def __init__(self, pDict):
        self.p_dict = pDict
        
    def getTeamChart(self):
        plt.rcdefaults()
        fig, ax = plt.subplots()        
        
        teams, frequency = self.getTeamData()
        y_pos = np.arange(len(teams))

        
        ax.barh(y_pos, frequency, align='center',
        color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(teams)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Players in Top 100 BA')
        ax.set_title('Team w/ Most Top Players')
        fig.canvas.set_window_title("Team Frequency")

        plt.show()
    
    def getTeamData(self):
        teamDict = {}
        checked_list = []
        # Compare team names of each player
        for val in self.p_dict.values():
            if val.team in checked_list:
                teamDict[val.team] += 1     # increment duplicate teams within dict
            else:
                checked_list.append(val.team)   # append non-duplicate to list
                teamDict[val.team] = 1          # create new dict entry

        # Filter teams with more than 1 player in Top 100
        buffer_dict = {}
        for team, amt in teamDict.items():
            if amt > 1:
                buffer_dict[team] = amt
        
        # Breakdown dict into seperate lists
        teams = []
        frequency = []
        for key, val in buffer_dict.items():
            teams.append(key)
            frequency.append(val)

        return tuple(teams), tuple(frequency)
                
    def getGradeChart(self):
        
        labels = 'Freshman', 'Sophmore', 'Junior', 'Senior'
        sizes = self.getGradeData()
        fig1, ax1 = plt.subplots()
        fig1.canvas.set_window_title("Grade Distribution")
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()

    def getGradeData(self):
        total_count, 
        freshman,
        sophmore,
        junior,
        senior = 0
        # Parse dict for player grades, tally each respectively
        for val in self.p_dict.values():
            if 'Fr.' in val.grade:
                freshman += 1
            elif 'So.' in val.grade:
                sophmore += 1
            elif 'Jr.' in val.grade:
                junior += 1
            else:
                senior += 1
            total_count += 1

        return [ (freshman / total_count) * 100,
                (sophmore / total_count) * 100,
                (junior / total_count) * 100,
                (senior / total_count) * 100 ]


        