class Point():
    def __init__(self, input1, input2):
       self.x = input1
       self.y = input2
p= Point(2,8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self,name):
        if not self.opens_seats():
            return False
        self.passengers.append(name)
        return True

    def opens_seats(self):
        return self.capacity- len(self.passengers)
    
flight = Flight(3)

people = ["Harry", "Leo", "Murat", "Rachel"]
for person in people:
    if flight.add_passenger(person):
           print(f"Added{person} to flight successfully.")
    else:
         print(f"no available open seat for {person}")

