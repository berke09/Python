

import time
introduction = "********** WELCOME TO BERKE'S GYM ************ "



while(True):
    chosing_1 = int(input("Losing Weight = 1 Gaining weight = 2\t press a number:"))
    if chosing_1 == 1 :
        print("\nWe are here to help you losing weight and being fit :)\n")
        losing_weight_sport = {"chest day ->": "Bench Press , rope , walking , Butterfly", "Back day ->":"Pull up , Lat pull down , cycle , dumbel row ","Shoulder day ->":"Shoulder Press , lateral raise , shruq , swimming"}
        losing_weight_food  = {"Day1":"Oatmeal-coffee","Day2":"Meat-Vegetables","Day3":"Soup-Yogurt"}
        
        print("That is your sport Program \n")
        for a,b in losing_weight_sport.items():
            print(a,b)
        print("\n")
        print("That is your food Program \n")

        for a,b in losing_weight_food.items():
            print(a,b)
        print("\n")
        
        print("\nThank you to chose our gym ")
        print("\n")

        control = int(input("press zero to end the program if not press any :"))
        if control == 0 :
            print("good bye")
            time.sleep(0.5)
            break

    elif chosing_1 == 2 : 
        print("\nWe are here to help to gaining weight and being fit :)\n")
        gaining_weight_sport = {"chest day ->": "Bench Press , Dips , Push up , Butterfly", "Back day ->":"Pull up , Lat pull down , Seated pull down , dumbel row ","Shoulder day ->":"Shoulder Press , lateral raise , shruq , back shoulder"}
        gaining_weight_food  = {"Day1":"Chicken-Rice","Day2":"Meat-pasta","Day3":"Tuna-Bread"}
        
        print("That is your sport Program \n")
        for a,b in gaining_weight_sport.items():
            print(a,b)
        print("\n")
        print("That is your food Program \n")
        for a,b in gaining_weight_food.items():
            print(a,b)
        print("\n")

        print("\nThank you to chose our gym ")
        print("\n")

        control = int(input("press zero to end the program if not press any :"))
        if control == 0 :
            print("good bye")
            time.sleep(0.5)
            break

    else :
        print("you press a wrong number ! Please start again.")
        chosing_2 = int(input("Press 0 to start again :"))

        if chosing_2 == 0 :
            print("You will direct to start point .")
            time.sleep(1)

        else :
            break

    
