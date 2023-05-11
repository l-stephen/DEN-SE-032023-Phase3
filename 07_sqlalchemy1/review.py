import sqlite3
# Setting up connection
connection = sqlite3.connect("pokemon.db")
# Setting up object to run commands
cursor = connection.cursor()
# Setting up classes like normal
class Pokemon:
    all = []
    def __init__(self,name,type,size,owned, id =-1):
        self.id = id
        self.name = name
        self.type = type
        self.size = size
        self.owned = owned
        Pokemon.all.append(self)

    #Create
    def pushtobackend(self):
        # Write out a command
        value = f'''
        INSERT INTO pokemon (name,type,size,owned)
        VALUES ("{self.name}","{self.type}",{self.size},{self.owned});
        '''
        # Run command
        cursor.execute(value)
        # Commit when changing database
        connection.commit()
        # Logic to get all data and input id
        input = self.fetchall()
        self.id = input[-1][0]
    # Delete
    def delete(self):
        value = f'''
        DELETE FROM pokemon
        WHERE id = {self.id}
        '''
        cursor.execute(value)
        connection.commit()
    # Read
    @classmethod
    def fetchone(cls,id):
        value = f'''
        SELECT * FROM pokemon
        WHERE id = {id}
        '''
        x = cursor.execute(value).fetchone()
        return x
    @classmethod
    def fetchall(cls):
        value = f'''
        SELECT * FROM pokemon
        '''
        x = cursor.execute(value).fetchall()
        return x

picachu = Pokemon("Picachu","Electric",1.5,1)
#picachu.pushtobackend()
picachu.edit(picachu,"Pica", "Lighthng", 2, 0, 1)
#picachu.delete()
