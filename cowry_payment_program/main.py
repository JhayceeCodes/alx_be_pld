#calculate_price    1km - $5 --done
#deduct_price --done
#refund_price --done
#greetings -- done 

#Passenger (name, balance) --- Bus (max_bus
import cowry

max_bus_distances = {
    "bus1": 100, #90km (100-90)
    "bus2": 40,
    "bus3": 500
}



user_balances = {
    "Samuel": 500,
    "Jethro": 500
}

price_per_km_in_dollars =  5

#Jethro - $500 ---bus2 --30km

def calculate(name, bus, user_distance):
    user_balance = user_balances[name] 
    bus_distance = max_bus_distances[bus]

    print(f"Original balance: ${user_balance}")

    #deduction
    new_balance = cowry.deduct_price(user_balance, bus_distance, price_per_km_in_dollars)
    print(f"New balance: ${new_balance}")

    #welcome user
    greeting = cowry.greetings(name, "welcome")
    print(greeting)

    #refund
    refund_price = cowry.refund_price(user_distance, bus_distance, price_per_km_in_dollars)
    print(f"Balance after refund: ${refund_price + new_balance}")

    #goodbye
    greeting = cowry.greetings(name, "goodbye")
    print(greeting)

calculate("Jethro", "bus2", 30)