# automated pizza order program.

def Pizza_Menu():
    print("Welcome to Bella Pizza 🍕🍕🍕")

    print("Please, place your order: "
        """
1. small_pizza: $15
2. medium_pizza: $20
3. large_pizza: $25
        """
    )

    user_choice = int(input("Select an otpion [1 - 3]: "))
    bill = 0
    pepperoni_for_small_pizza = 1
    pepperoni_for_medium_large_pizza = 2
    extra_cheese_for_any_pizza = 1
    
    if user_choice == 1:
        bill = bill  + 15
        print("pepperoni for small pizza is 1$")
        add_pepperoni = input("Add pepperoni? Yes(Y), No(N): ").upper()
        if add_pepperoni == "Y":
            bill = bill + pepperoni_for_small_pizza
        print("Extra cheese is 1$")
        extra_cheese = input("Add extra cheese? YES(Y), NO(N): ").upper()
        if extra_cheese == "Y":
            bill = bill + extra_cheese_for_any_pizza

    elif user_choice == 2:
        bill = bill  + 20
        print("pepperoni for small pizza is 2$")
        add_pepperoni = input("Add pepperoni? Yes(Y), No(N): ").upper()
        if add_pepperoni == "Y":
            bill = bill + pepperoni_for_medium_large_pizza
        print("Extra cheese is 1$")
        extra_cheese = input("Add extra cheese? YES(Y), NO(N): ").upper()
        if extra_cheese == "Y":
            bill = bill + extra_cheese_for_any_pizza     

    elif user_choice == 3:
        bill = bill  + 25
        print("pepperoni for small pizza is 2$")
        add_pepperoni = input("Add pepperoni? Yes(Y), No(N): ").upper()
        if add_pepperoni == "Y":
            bill = bill + pepperoni_for_medium_large_pizza
        print("Extra cheese is 1$")
        extra_cheese = input("Add extra cheese? YES(Y), NO(N): ").upper()
        if extra_cheese == "Y":
            bill = bill + extra_cheese_for_any_pizza     
    else:
        print("Invalid input")
    
    if bill > 1: #print final bill if and only if the final bill is greater than zero
        print(f"Your final bill is: {bill}$")

Pizza_Menu()    



