class User:

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
    
    def check_balance(self):
        return self._balance
    
    def deduct_fare(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
            return True
        else:
            return False
        
    def refund(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False


class Cowry:
    def __init__(self, vehicle_id, max_distances={}):
        self.vehicle_id = vehicle_id
        self.max_distances = max_distances
        self._price_per_km = 5


    def calculate_price(self, distance):
        price = distance * self._price_per_km
        return price
    
    def deduct_price(self, user:User):
        #deduct money for total distance
        total_price = self.calculate_price(self.max_distances[self.vehicle_id])
        user.deduct_fare(total_price)
        print("====Deduction successful!====")
        print(f"New balance: {user.check_balance()}")

        
    
    def refund_price(self, distance, user:User):
        vehicle_max_distance = self.max_distances[self.vehicle_id]

        if not distance <= 0:
            if distance < vehicle_max_distance:
                original_price = self.calculate_price(vehicle_max_distance)
                new_price = self.calculate_price(distance)
                user.refund(original_price-new_price)
                print("====Refund successful!====")
                print(f"New balance: {user.check_balance()}")

            elif distance == vehicle_max_distance:
                print("Sorry, no refund")
            else:
                print("Oh, your distance is more than the max distance")
        else:
            print("Distance must be greater than zero.")
        
        
        
        
       
#sample data
"""bus_max_distances = {
    "1": 500,
    "2": 300,
    "3": 400
}

john = User("John", 2000)
bus1 = Cowry("2", bus_max_distances)

#deduct
bus1.deduct_price(john)
#refund
bus1.refund_price(200,john)
"""






















    


