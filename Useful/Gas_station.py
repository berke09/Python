import time


benzin = 40.00
diesel_fuel = 42.00
gas = 21.00

choosing = {"benzin":"40 TL","diesel":"42 TL","gas":"21 TL"}



Quantity_as_liter = 0
Quantity_as_money = 0 

def benzin_(liter_benzin ,money_benzin):
    if liter_benzin  > 0 :
        return liter_benzin  * 40.00
    elif money_benzin > 0 :
        liter = money_benzin / 40
        print(f"{liter:.2f} liter benzin filled")
        return money_benzin
    

def diesel_fuel_(liter_diesel,money_diesel):
    if liter_diesel > 0 :
        return liter_diesel * 42.00
    elif money_diesel > 0 :
        liter = money_diesel / 42
        print(f"{liter:.2f} liter diesel filled")
        return money_diesel
    

def gas_(m3_gas,money_gas):
    if m3_gas > 0 :
        return m3_gas * 21.00
    elif money_gas > 0 :
        m3 = money_gas / 21
        print(f"{m3:.2f} m3 gas filled")
        return money_gas ,

def Did_pay(okey):
        if okey == 1 :
            print("\nWe got the price . Thank you :)")
            print(f"{eid_number} is leaving ... ")
            print("come againnn")
            time.sleep(0.5)

        else :
            while True :
                print("\nWe could not get the price please try again ...")
                okey = int(input("New try Success yes:1,no:0:"))
                if okey == 1 :
                    print("\nWe got the price . Thank you")
                    print(f"{eid_number} is leaving ... ")
                    print("come againnn")
                    time.sleep(0.5)
                    break
                else :
                    print("\nWe could not get the price please try again ...")
            
# MAIN PROGRAM 

okey = 0

print("WELCOME OUR GAS STATION")
while True:

    eid_number = 0
    eid_number = input("please enter your car ied number : ")
    print("loading...\n")
    time.sleep(1)
    a = 1
    for i,j in choosing.items():
        
        print(f"{a}-"+ i,j)
        a = a + 1 
        
    fuel_type = int(input("\nWhich type of fuel do you want?:"))

    # prees 1 for benzin
    # press 2 for diesel
    # press 3 for gas 

    if fuel_type == 1 :

        print("\nBenzin... What is quantity you want as liter or money ?")
        liter_benzin = int(input("Liter :"))
        money_benzin = int(input("Money :"))
        price = benzin_(liter_benzin,money_benzin)
        time.sleep(0.5)
        print(f"\nPlease pay your fuel price {price} TL")
        okey = int(input("\nIs the paying is succesfull ? Yes=1,No=0:"))
        Did_pay(okey)
    
    elif fuel_type == 2 :

        print("\nDiesel... What is quantity you want as liter or money ?")
        liter_diesel = int(input("Liter :"))
        money_diesel = int(input("Money :"))
        price = diesel_fuel_(liter_diesel,money_diesel)
        time.sleep(0.5)
        print(f"\nPlease pay your fuel price {price} TL")
        okey = int(input("\nIs the paying is succesfull ? Yes=1,No=0:"))
        Did_pay(okey)
    
    elif fuel_type == 3 :

        print("\nGas... What is quantity you want as liter or money ?")
        m3_gas = int(input("m3 :"))
        money_gas= int(input("Money :"))
        price = gas_(m3_gas,money_gas)
        time.sleep(0.5)
        print(f"\nPlease pay your fuel price {price} TL")
        okey = int(input("\nIs the paying is succesfull ? Yes=1,No=0:"))
        Did_pay(okey)
    
    break

        