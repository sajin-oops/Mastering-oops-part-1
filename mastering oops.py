class Player:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def display_info(self):
        print(f"Player - {self.name}, Health = {self.health}, Attack Power = {self.attack_power}")

player_one = Player("Sky White",100,74)
player_two = Player("Turn Red",99,100)
player_one.display_info()
player_two.display_info()

'''
O/P

Player - Sky White, Health = 100, Attack Power = 74
Player - Turn Red, Health = 99, Attack Power = 100
'''