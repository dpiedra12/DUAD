class Person:

    def __init__(self, name):
        self.name = name
        

class Bus:
    list_of_passengers = []
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
       

    def add_passengers(self, person):
        if len(self.list_of_passengers )  < self.max_passengers:
                self.list_of_passengers.append(person)
                print (self.list_of_passengers[-1].name)

        else:        
            print ("The buss is full")

        
    def remove_passengers(self, person):
             for passenger in self.list_of_passengers:
                  if (passenger.name == person):
                    self.list_of_passengers.remove(passenger)
                    print (f"{passenger.name} got off the bus")
                    break
                    

bus1 = Bus(3)
bus1.add_passengers(Person("Danny"))
bus1.add_passengers(Person("Josue"))
bus1.add_passengers(Person("Jose"))
bus1.remove_passengers("Danny")
bus1.remove_passengers("Josue")


