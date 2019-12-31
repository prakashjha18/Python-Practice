#DSA-Assgn-4
class Game:
    def __init__(self,players_list):
        self.players_list=players_list
    def sort_players_based_on_experience(self):
        self.players_list.sort(key=lambda x: x.get_experience(), reverse=True)
    def shift_player_to_new_position( self,old_index_position, new_index_position):
        temp = self.players_list.pop(old_index_position)
        self.players_list.insert(new_index_position,temp)
    def display_player_details(self):
        for i in self.players_list:
            print(i.get_name()+" " + str(i.get_experience()))
class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
game1 = Game(players_list)
game1.sort_players_based_on_experience()
game1.display_player_details()
game1.shift_player_to_new_position(0,3)
game1.display_player_details()
