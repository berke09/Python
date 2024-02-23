# design a game which has several characters whose fight amoung each other
# they will have life bar as a number 
# the users1 will pick a charecter first , and then users 2
# will be a movement list (yumruk tokat tekme vs)
# users will chose the movement 

import time

print("*************** WELCOME THE GAME ****************")

user_1 = 0
user_2 = 0

Character_list_name = ["batman","ironman","hulk","spiderman"]
Character_list_life = {"batman":100,"ironman":120,"hulk":200,"spiderman":80}
Character_list_hit_power = {"batman":25,"ironman":20,"hulk":50,"spiderman":30}

while(True):
    enter = int(input("Press 0 to start the game :"))
    if enter != 0 :
        break
    else :
        print("Loading......")
        time.sleep(1)

        print(Character_list_name)

        print("\ncharacters life power")
        for a,b in Character_list_life.items():
            print(a,b)
        
        print("\ncharacters hit power ")
        for a,b in Character_list_hit_power.items():
            print(a,b)
        
        user_1_character = input("\nUser1 please chose a character with name :")
        user_2_character = input("user2 please chose a character with name :")

        print("\nuser1 choose "+ user_1_character + " :) good luck")
        print("user2 choose "+ user_2_character + " :) good luck")

        print("\nArea is loading......")
        time.sleep(1.5)
        
        print("\nGuys ready to fight I can see so much blood on the floor hahahahahahhh\n")

        user_1_character_life = Character_list_life[user_1_character]
        user_1_character_hit  = Character_list_hit_power[user_1_character]
            
        user_2_character_life = Character_list_life[user_2_character]
        user_2_character_hit  = Character_list_hit_power[user_2_character]




        for i in range(100):
            
            did_user1_hit = int(input("User 1 press the 1 to hit user 2 :"))
            
            if did_user1_hit == 1:
                user_2_character_life = user_2_character_life - user_1_character_hit
                print("user2 life bar = " + str(user_2_character_life))
                if user_2_character_life <= 0 :
                    print("GAME OVER\n USER 1 WON")
                    break
                else : 
                    pass
            
            did_user2_hit = int(input("User 2 press the 2 to hit user 1 :"))

            if did_user2_hit == 2:
                user_1_character_life = user_1_character_life - user_2_character_hit
                print("user1 life bar = " + str(user_1_character_life))
                if user_1_character_life <= 0 :
                    print("GAME OVER\n\nUSER 2 WON :)")
                    break
                else : 
                    pass
        
    break