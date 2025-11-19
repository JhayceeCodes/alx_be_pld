def deduct_price(user_balance, bus_distance, price_per_km):
    price = calculate_price(bus_distance, price_per_km)
    new_user_balance = user_balance - price
    return new_user_balance

def refund_price(user_distance, bus_distance, price_per_km):
    if user_distance < bus_distance:
        original_price = calculate_price(bus_distance, price_per_km)
        new_price = calculate_price(user_distance, price_per_km)
        return original_price - new_price
    elif user_distance == bus_distance:
        return 0
    else:
        return None

def calculate_price(distance, price_per_km):
    price = distance * price_per_km
    return price

def greetings(name, mode):
    if mode == "welcome":
        return f"Welcome, {name}"
    elif mode == "goodbye":
        return f"Goodbye, {name}"
    else:
        return "Please enter either welcome or goodbye for mode!"