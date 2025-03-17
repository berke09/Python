import time

benzin = 40.00
diesel_fuel = 42.00
gas = 21.00

choosing = {"benzin": "40 TL", "diesel": "42 TL", "gas": "21 TL"}


def benzin_(liter_benzin, money_benzin):
    if liter_benzin > 0:
        return liter_benzin * 40.00, liter_benzin
    elif money_benzin > 0:
        liter = money_benzin / 40
        print(f"{liter:.2f} liter benzin filled")
        return money_benzin, liter
    else:
        print("You must enter either liter or money!")
        return 0, 0


def diesel_fuel_(liter_diesel, money_diesel):
    if liter_diesel > 0:
        return liter_diesel * 42.00, liter_diesel
    elif money_diesel > 0:
        liter = money_diesel / 42
        print(f"{liter:.2f} liter diesel filled")
        return money_diesel, liter
    else:
        print("You must enter either liter or money!")
        return 0, 0


def gas_(m3_gas, money_gas):
    if m3_gas > 0:
        return m3_gas * 21.00, m3_gas
    elif money_gas > 0:
        m3 = money_gas / 21
        print(f"{m3:.2f} m3 gas filled")
        return money_gas, m3
    else:
        print("You must enter either m3 or money!")
        return 0, 0


def Did_pay(okey):
    if okey == 1:
        print("\nWe got the price. Thank you :)")
        print(f"{eid_number} is leaving ... ")
        print("Come again!")
        time.sleep(0.5)
    else:
        while True:
            print("\nWe could not get the price. Please try again ...")
            okey = int(input("New try Success yes:1, no:0:"))
            if okey == 1:
                print("\nWe got the price. Thank you!")
                print(f"{eid_number} is leaving ... ")
                print("Come again!")
                time.sleep(0.5)
                break
            else:
                print("\nWe could not get the price. Please try again ...")


# MAIN PROGRAM
print("WELCOME TO OUR GAS STATION")

while True:
    try:
        eid_number = input("Please enter your car ID number: ")

        if eid_number.lower() == 'exit':
            print("Exiting the program. Have a nice day!")
            break

        print("Loading...\n")
        time.sleep(1)

        a = 1
        for i, j in choosing.items():
            print(f"{a}- {i}: {j}")
            a += 1

        fuel_type = int(
            input("\nWhich type of fuel do you want? (1 - Benzin, 2 - Diesel, 3 - Gas), or type 'exit' to quit: "))

        if fuel_type == 'exit':
            print("Exiting the program. Have a nice day!")
            break

        if fuel_type == 1:
            print("\nBenzin... What is the quantity you want as liter or money?")
            liter_benzin = input("Liter: ")
            money_benzin = input("Money: ")

            if not liter_benzin and not money_benzin:
                print("You must enter either liter or money!")
                continue

            liter_benzin = int(liter_benzin) if liter_benzin else 0
            money_benzin = int(money_benzin) if money_benzin else 0

            price, fuel_quantity = benzin_(liter_benzin, money_benzin)
            if price > 0:
                time.sleep(0.5)
                print(f"\nPlease pay your fuel price {price} TL for {fuel_quantity} liters.")
                okey = int(input("\nIs the payment successful? Yes=1, No=0: "))
                Did_pay(okey)

        elif fuel_type == 2:
            print("\nDiesel... What is the quantity you want as liter or money?")
            liter_diesel = input("Liter: ")
            money_diesel = input("Money: ")

            if not liter_diesel and not money_diesel:
                print("You must enter either liter or money!")
                continue

            liter_diesel = int(liter_diesel) if liter_diesel else 0
            money_diesel = int(money_diesel) if money_diesel else 0

            price, fuel_quantity = diesel_fuel_(liter_diesel, money_diesel)
            if price > 0:
                time.sleep(0.5)
                print(f"\nPlease pay your fuel price {price} TL for {fuel_quantity} liters.")
                okey = int(input("\nIs the payment successful? Yes=1, No=0: "))
                Did_pay(okey)

        elif fuel_type == 3:
            print("\nGas... What is the quantity you want as m3 or money?")
            m3_gas = input("m3: ")
            money_gas = input("Money: ")

            if not m3_gas and not money_gas:
                print("You must enter either m3 or money!")
                continue

            m3_gas = int(m3_gas) if m3_gas else 0
            money_gas = int(money_gas) if money_gas else 0

            price, fuel_quantity = gas_(m3_gas, money_gas)
            if price > 0:
                time.sleep(0.5)
                print(f"\nPlease pay your fuel price {price} TL for {fuel_quantity} m3.")
                okey = int(input("\nIs the payment successful? Yes=1, No=0: "))
                Did_pay(okey)

        # Exit the program after a transaction
        break

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting the program safely.")
        break
