import sqlite3
import os
"""
Database utilities
"""


class ToDatabase:

    def __init__(self, playerDictionary, tName):
        self.player_dict = playerDictionary
        self.t_name = tName
        self.new_db = True
        self.connection = ""
        self.cursor = ""

        self.dbConnect()
        self.dbCreate()
        self.dbPop()
        self.dbCommit()
        self.dbClose()
    
    # Connect to SQLite db if it exists
    def dbConnect(self):
        if os.path.isfile("C:\\Users\\dev\\Desktop\\" + self.t_name + ".sqlite"):
            self.new_db = False
            print("Database File Found...")

        self.connection = sqlite3.connect("C:\\Users\\dev\\Desktop\\" + self.t_name + ".sqlite")

        self.cursor = self.connection.cursor()

    # Create new table if none exists
    def dbCreate(self):
        if self.new_db:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
                                 {} (Rank INT,
                                 Name TEXT,
                                 Batting_Average REAL,
                                 Team TEXT,
                                 Grade TEXT,
                                 Position TEXT,
                                 Games INT,
                                 At_Bats INT,
                                 Hits INT)""".format(self.t_name))
        
    # Populate the table
    def dbPop(self):
        for val in self.player_dict.values():
            self.cursor.execute("""INSERT INTO {} 
                                (Rank, Name, Batting_Average,
                                Team, Grade, Position, 
                                Games, At_Bats, Hits) 
                                VALUES (?, ?, ?, ?, ?, ?, ?,
                                ?, ?)""".format(self.t_name),
                                (val.rank, val.name, val.ba,
                                val.team, val.grade, val.pos, 
                                val.games, val.ab, val.h))


    def dbCommit(self):
        self.connection.commit()
        print('\nDatabase has been committed..')

    def dbClose(self):
        self.connection.close()
    

        

        

        