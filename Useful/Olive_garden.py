

# Gelir ->Zeytin Satışı , Zeytin Yağı Satışı
# Gider -> Yakıt , İlaç , Gübre , İşçi 

# zeytin kg = fiyat ve üretilen
# yağ kg = fiyat ve üretilen

# yakıt = fiyat ve litre
# ilaç  = fiyat ve gereksinim miktarı
# gübre = fiyat ve gereksinim miktarı
# işçi toplama = günlük fiyat toplama * adet * gün 
# işçi budama =  günlük fiyat budama * adet * gün 




import time




class Olive_incomes():
    
    def __init__(self,price_per_kg_olive=0,total_olive_to_eat=0,price_per_kg_olive_oil=0,total_olive_oil=0):
        self.price_olive= price_per_kg_olive
        self.total_olive = total_olive_to_eat
        self.price_oil = price_per_kg_olive_oil
        self.total_oil = total_olive_oil

    def income_from_oil(self):
        first_income = self.price_oil * self.total_oil
        return first_income
    def income_from_olive(self):
        second_income = self.price_olive * self.total_olive
        return second_income 
    
class Olive_outgoes():
    
    def __init__(self,fuel_liter,fuel_price,medicine_price,medicine_kg,fertilizer_price,fertilizer_kg,worker1_price,worker2_price):
        # işçilerin olduğı elif bloklarında işçi adeti ve gün sayısını ayrı input olarak al.
        self.fuel_liter = fuel_liter
        self.fuel_price = fuel_price
        self.medicine_price = medicine_price
        self.medicine_kg = medicine_kg
        self.fertilizer_price = fertilizer_price
        self.fertilizer_kg = fertilizer_kg
        self.worker1_price = worker1_price
        self.worker2_price = worker2_price

    def outcomes_for_fuel(self):
        first_outcome = self.fuel_liter * self.fuel_price
        return first_outcome
    def outcomes_for_medicine(self):
        second_outcome = self.medicine_kg * self.medicine_price
        return second_outcome
    def outcomes_for_fertilizer(self):
        third_outcomes = self.fertilizer_kg * self.fertilizer_price    
        return third_outcomes
    def outcomes_for_worker1(self,day,workertimes):
        fourth_outcomes = self.worker1_price * day * workertimes
        return fourth_outcomes
    def outcomes_for_worker2(self,day,workertimes):
        fifth_outcomes = self.worker2_price * day * workertimes
        return fifth_outcomes
    
def Total_income(A1,A2):
    return A1 + A2

def Total_outcome(B1,B2,B3,B4,B5):
    return B1+B2+B3+B4+B5
        
A1 = int()
A2 = int()
B1 = int()
B2 = int()
B3 = int()
B4 = int()
B5 = int()
C1 = int()
C2 = int()


# MAIN PROGRAM #
print("**************************** WELCOME OUR APPLICATION ******************************".center(50))
while True :    
    while True:
        try:
            print("Choose one of the below\nIncomes = 1\nOutcomes = 2")
            choosing_1 = int(input("Please Enter a number :"))
        except:
            print("Please just press a number")
            continue
        else:
            if choosing_1 == 1:
                print("Loading Incomes...")
                time.sleep(0.5)
                print("Incomes List\n1-Olive Selling\n2-Olive Oil Selling")
                while True:
                    try:
                        choosing_2 = int(input("Please Enter a number:"))
                    except:
                        print("Please just press a number")
                        continue
                    else:
                        if choosing_2 == 1 :
                            print("Loading Olive Incomes...")
                            time.sleep(0.5)
                            kg_olive = int(input("How many kg olive did you get this year?:"))
                            price_olive = int(input("What is the current price of olive for per kg?:"))
                            a = Olive_incomes(price_olive,kg_olive,None,None)
                            print(str(a.income_from_olive())+" TL")
                            A1 = a.income_from_olive()
                            print("Now You calculated your oil income.\nYou can update it or keep going ")
                            break
                        else:
                            print("Loading Oil Incomes...")
                            time.sleep(0.5)
                            kg_oil = int(input("How many kg olive oil did you get this year?:"))
                            price_oil = int(input("What is the current price of olive oil  for per kg?:"))
                            a = Olive_incomes(None,None,price_oil,kg_oil)
                            print(str(a.income_from_oil())+" TL")
                            A2 = a.income_from_oil()
                            print("Now You calculated your olive oil income.\nYou can update it or keep going ")
                            break
                if A1 !=0 and A2 != 0 :
                    C1 = Total_income(A1,A2)
                    print(str(C1) + " TL is your total income through whole year:)")

            else :
                print("Loading Outgoes...")
                time.sleep(0.5)
                print("Outgoes List\n1-Fuel\n2-Medicine\n3-Fertilizer\n4-Harvest_worker\n5-Pruning_Worker")
                while True:
                    try:
                        choosing_3 = int(input("Please Enter a number:"))
                    except:
                        print("Please just press a number")
                        continue
                    else:
                        
                        if choosing_3 == 1 :
                            print("Loading Fuel Outgoes...")
                            time.sleep(0.5)
                            fuel_liter = int(input("How many liter fuel did you use in the year ?:"))
                            fuel_price = int(input("What is the current fuel price for per liter ?:"))
                            a = Olive_outgoes(fuel_liter,fuel_price,None,None,None,None,None,None)
                            print(str(a.outcomes_for_fuel())+" TL")
                            B1 = a.outcomes_for_fuel()
                            print("Now You calculated your fuel outgoes.\nYou can update it or keep going ")
                            break 
                        elif choosing_3 == 2:
                            print("Loading Medicine Outgoes...")
                            time.sleep(0.5)
                            medicine_kg = int(input("How many kg medicine did you use in the year ?:"))
                            medicine_price = int(input("What is the current medicine price for per kg ?:"))
                            a = Olive_outgoes(None,None,medicine_price,medicine_kg,None,None,None,None)
                            print(str(a.outcomes_for_medicine())+" TL")
                            B2 = a.outcomes_for_medicine()
                            print("Now You calculated your medicine outgoes.\nYou can update it or keep going ")
                            break 
                        elif choosing_3 == 3:
                            print("Loading Fertilizer Outgoes...")
                            time.sleep(0.5)
                            fertilizer_kg = int(input("How many kg fertilizer did you use in the year ?:"))
                            fertilizer_price = int(input("What is the current fertilizer price for per kg ?:"))
                            a = Olive_outgoes(None,None,None,None,fertilizer_price,fertilizer_kg,None,None)
                            print(str(a.outcomes_for_fertilizer())+" TL")
                            B3 = a.outcomes_for_fertilizer()
                            print("Now You calculated your fertilizer outgoes.\nYou can update it or keep going ")
                            break
                        elif choosing_3 == 4:
                            print("Loading Harvest_worker Outgoes...")
                            time.sleep(0.5)
                            worker1_price = int(input("What is the current price for a hardvest worker ?:"))
                            day = int(input("How many day did hardevst workers work ?:"))
                            workertimes = int(input("How many hardevst workers did work ?:"))
                            a = Olive_outgoes(None,None,None,None,None,None,worker1_price,None)
                            print(str(a.outcomes_for_worker1(day,workertimes))+" TL")
                            B4 = a.outcomes_for_worker1(day,workertimes)
                            print("Now You calculated your Harvest Workers outgoes.\nYou can update it or keep going ")
                            break
                        else:
                            print("Loading Pruning_worker Outgoes...")
                            time.sleep(0.5)
                            worker2_price = int(input("What is the current price for a pruning worker ?:"))
                            day = int(input("How many day did pruning workers work ?:"))
                            workertimes = int(input("How many pruning workers did work ?:"))
                            a = Olive_outgoes(None,None,None,None,None,None,None,worker2_price)
                            print(str(a.outcomes_for_worker2(day,workertimes))+" TL")
                            B5 = a.outcomes_for_worker2(day,workertimes)
                            print("Now You calculated your Pruning Workers outgoes.\nYou can update it or keep going ")
                            break
                if B1 and B2 and B3 and B4 and B5 !=0 :
                    C2 = Total_outcome(B1,B2,B3,B4,B5)
                    print(str(C2)+" TL your total outgoes through whole year ):\n")
                        

                
            break
    if C1 and C2 > 0 :
        print("Calculating earnings and losing situation...")
        time.sleep(1)
        Whole_total = C1 - C2 
        if Whole_total > 0 :
            print(f"You made {Whole_total} TL gain :)")
        elif Whole_total == 0:
            print("You did not make a gain or a lose money...")
        else:
            print(f"You lost {Whole_total} money ):")
        try:
            last_choosing = int(input("Press zero to close the program or another button to calculate again :"))
        except:
            pass
        else:
            if last_choosing == 0 :
                break
            pass
            
    