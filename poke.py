# create a Pokemon
class Pokemon:
    def __init__(self,name,primary_type,max_hp):
        self.name=name
        self.primary_type=primary_type
        self.hp=0
        self.max_hp=max_hp

    def __str__(self):
        return f"{self.name} ({self.primary_type})"

    # feed them to increase health
    def feed(self):
        if self.hp<self.max_hp:
            self.hp +=1
            print(f"{self.name} has now {self.hp} HP")
        else:
            print(f"{self.name} is full.")

    # make them battle and decide for a winner 
    def battle(self, other_pokemon):
        print(f'Battle:' , self.name, other_pokemon.name)
        result=self.typewheel(self.primary_type, other_pokemon.primary_type)
        print(f"{self.name} fough {other_pokemon.name} and the result is a {result}")


    @staticmethod
    def typewheel(type1,type2):
        result={0:'lose', 1:'win', -1:'tie'}
        # mapping between types and results condition
        game_map={"water":0, "fire":1, "grass":2} 
        #the logic is: water win over fire, fire win over and grass win over water
        # implement win-lose matrix
        wl_matrix = [

            [-1,1,0],  # water (gap_map['water'] => index 0 in wl_matrix)
            [0,-1,1],  # fire (gap_map['fire'])
            [1,0,-1],  # grass (gap_map['grass'])
        ]
        # declare the winner
        wl_result=wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]

# take a look at it
if __name__=='__main__':
    print(Pokemon(name='bulbasaur',primary_type='grass',max_hp=100))
    print(Pokemon(name='charmander', primary_type='fire',max_hp=100))