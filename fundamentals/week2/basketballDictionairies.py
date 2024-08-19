kevin = {
"name": "Kevin Durant", 
"age":34, 
"position": "small forward", 
"team": "Brooklyn Nets"
}
jason = {
"name": "Jason Tatum", 
"age":24, 
"position": "small forward", 
"team": "Boston Celtics"
}
kyrie = {
"name": "Kyrie Irving", 
"age":32, "position": "Point Guard", 
"team": "Brooklyn Nets"
}

players = [
    {
"name": "Kevin Durant", 
"age":34, 
"position": "small forward", 
"team": "Brooklyn Nets"
    },
    {
"name": "Jason Tatum", 
"age":24, 
"position": "small forward", 
"team": "Boston Celtics"
    },
    {
"name": "Kyrie Irving", 
"age":32, "position": "Point Guard", 
"team": "Brooklyn Nets"
    },
    {
"name": "Damian Lillard", 
"age":33, "position": "Point Guard", 
"team": "Portland Trailblazers"
    }
]

team_list=[]
class Player :
    def __init__(self,info):
      self.name =info.get("name")
      self.age=info.get("age")
      self.position=info.get("position")
      self.team=info.get("team")
      
    @classmethod
    def get_team(cls, team_list):
        new_list = []
        for player in team_list:
            new_player = cls(player)
            new_list.append(new_player)
        return new_list
      
new_list=Player.get_team(players)
for player in new_list:
  print(player.name,player.age,player.position,player.team)

player1=Player(info=kevin)
player2=Player(info=jason)
player3=Player(info=kyrie)

new_team=[]

for player in players :
  PLAYER=player.get("name")
  PLAYER=Player(player)
  new_team.append(PLAYER)



for player in new_team:
  print(player.name)


# conclusio  to get information from a dictionarie you just have top call the name of the key with the get("") so you get the value of that  key 
  
  # the difference between
  
  # new_list.append(new_player)
  
  # AND 
  
  # player1=Player(info=kevin)
  