import time


class OliveIncomes:
    def __init__(self, olive_price_per_kg=0, olive_kg=0, oil_price_per_kg=0, oil_kg=0):
        self.olive_price = olive_price_per_kg
        self.olive_kg = olive_kg
        self.oil_price = oil_price_per_kg
        self.oil_kg = oil_kg

    def income_from_olive(self):
        return self.olive_price * self.olive_kg

    def income_from_oil(self):
        return self.oil_price * self.oil_kg


class OliveExpenses:
    def __init__(self, fuel_liters=0, fuel_price=0,
                 medicine_price=0, medicine_kg=0,
                 fertilizer_price=0, fertilizer_kg=0,
                 worker1_price=0, worker2_price=0):
        self.fuel_liters = fuel_liters
        self.fuel_price = fuel_price
        self.medicine_price = medicine_price
        self.medicine_kg = medicine_kg
        self.fertilizer_price = fertilizer_price
        self.fertilizer_kg = fertilizer_kg
        self.worker1_price = worker1_price
        self.worker2_price = worker2_price

    def expense_for_fuel(self):
        return self.fuel_liters * self.fuel_price

    def expense_for_medicine(self):
        return self.medicine_kg * self.medicine_price

    def expense_for_fertilizer(self):
        return self.fertilizer_kg * self.fertilizer_price

    def expense_for_workers(self, worker_type_price, days, num_workers):
        return worker_type_price * days * num_workers


def main():
    print("**************** WELCOME TO THE OLIVE FARM CALCULATOR ****************\n")

    while True:
        try:
            print("\nChoose an option:\n1 - Calculate Incomes\n2 - Calculate Expenses\n0 - Exit")
            choice = int(input("Enter a number: "))

            if choice == 0:
                print("Exiting the program... Goodbye!")
                break

            elif choice == 1:
                print("\n*** INCOME CALCULATION ***")
                olive_kg = int(input("Enter the amount of olives harvested (kg): "))
                olive_price = int(input("Enter the price per kg of olives: "))
                oil_kg = int(input("Enter the amount of olive oil produced (kg): "))
                oil_price = int(input("Enter the price per kg of olive oil: "))

                income = OliveIncomes(olive_price, olive_kg, oil_price, oil_kg)
                total_income = income.income_from_olive() + income.income_from_oil()

                print(f"\nTotal Income: {total_income} TL")

            elif choice == 2:
                print("\n*** EXPENSE CALCULATION ***")
                fuel_liters = int(input("Enter the amount of fuel used (liters): "))
                fuel_price = int(input("Enter the price per liter of fuel: "))
                medicine_kg = int(input("Enter the amount of medicine used (kg): "))
                medicine_price = int(input("Enter the price per kg of medicine: "))
                fertilizer_kg = int(input("Enter the amount of fertilizer used (kg): "))
                fertilizer_price = int(input("Enter the price per kg of fertilizer: "))

                worker1_price = int(input("Enter the daily wage of harvest workers: "))
                harvest_days = int(input("Enter the number of days harvest workers worked: "))
                harvest_workers = int(input("Enter the number of harvest workers: "))

                worker2_price = int(input("Enter the daily wage of pruning workers: "))
                pruning_days = int(input("Enter the number of days pruning workers worked: "))
                pruning_workers = int(input("Enter the number of pruning workers: "))

                expenses = OliveExpenses(fuel_liters, fuel_price,
                                         medicine_price, medicine_kg,
                                         fertilizer_price, fertilizer_kg,
                                         worker1_price, worker2_price)

                total_expense = (expenses.expense_for_fuel() +
                                 expenses.expense_for_medicine() +
                                 expenses.expense_for_fertilizer() +
                                 expenses.expense_for_workers(worker1_price, harvest_days, harvest_workers) +
                                 expenses.expense_for_workers(worker2_price, pruning_days, pruning_workers))

                print(f"\nTotal Expenses: {total_expense} TL")

            else:
                print("Invalid input. Please enter 1, 2, or 0.")

            # Calculate net profit/loss
            if choice == 1 and 'total_income' in locals():
                print(f"Your total income for the year is {total_income} TL")
            elif choice == 2 and 'total_expense' in locals():
                print(f"Your total expenses for the year are {total_expense} TL")

            if 'total_income' in locals() and 'total_expense' in locals():
                net_profit_loss = total_income - total_expense
                if net_profit_loss > 0:
                    print(f"\nYou made a profit of {net_profit_loss} TL!")
                elif net_profit_loss == 0:
                    print("\nYou broke even, no profit or loss!")
                else:
                    print(f"\nYou incurred a loss of {abs(net_profit_loss)} TL!")

        except ValueError:
            print("Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting safely...")
            break


if __name__ == "__main__":
    main()
