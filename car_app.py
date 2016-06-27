##############################
## - Kevin Winston, 10339721##
##############################
from car import  * # Import the classes 

class Dealership(object):
    
    def __init__(self):
       self.electric_cars = []
       self.petrol_cars = []
       self.rotary_cars = []
       self.hybrid_cars = []
       self.diesel_cars = []

    	
    def current_stock(self): # populates the inventory
        for i in range(10):
			self.electric_cars.append(ElectricCar())
        for i in range(60):
			self.petrol_cars.append(PetrolCar())
        for i in range(20):
            self.diesel_cars.append(DieselCar())
        for i in range(10):
            self.hybrid_cars.append(HybridCar())
        for i in range(5):
            self.rotary_cars.append(RotaryCar())
    
    def stock_count(self):   # displays the current inventory
        print 'Petrol Cars in stock: ' + str(len(self.petrol_cars))
        print 'Electric Cars in stock: ' + str(len(self.electric_cars))
        print 'Diesel Cars in stock: ' + str(len(self.diesel_cars))
        print 'hybrid Cars in stock: ' + str(len(self.hybrid_cars))
        print 'Rotary Cars in stock: ' + str(len(self.rotary_cars))

    def rent(self, car_list, amount): # Tracks the number of cars currently available
        if len(car_list) < amount:
            print 'Not enough stock'
            return
        total = 0
        while total < amount:   
            car_list.pop()
            total = total + 1
    
    
    def process_rental(self): #Gives the customer a choice of vehicles
                
        answer = raw_input('What type of Car would you like to rent?:\n p-Petrol\n e-Electric\n d-Diesel\n h-hybrid\n r-Rotary: ') 
        amount = int(raw_input('How many would you like to rent?: '))
        if answer == 'p':
            self.rent(self.petrol_cars, amount)
        elif answer == 'e':
            self.rent(self.electric_cars, amount)
        elif answer =='d':
            self.rent(self.diesel_cars, amount)
        elif answer =='h':
            self.rent(self.hybrid_cars, amount)
        elif answer =='r':
            self.rent(self.rotary_cars, amount)

        dealership.stock_count()    
        
    def returns(self, car_list, amount): #Allows vehicles to be returned to the inventory
        total = 0
        if amount < 0:
            print 'Value Error '
        elif amount == 0:
            print 'Do you wish to extend your lease.'
        else:
            while total < amount:
                car_list.append(1)
                total = total + 1
            print 'Vehicle(s) returned successfully.'
    
    def CarReturn(self): # Determines which list returning vehicles should be added to 
        type = raw_input("Which type of car are you returning?\nElectric - e\nPetrol - p\nHybrid - h\nDiesel - d\n Rotary - r\n: ")
        amount = int(raw_input('How many vehicles are you returning?\n: '))
        if type == 'e' and len(self.electric_cars) + amount <= 10:
            self.returns(self.electric_cars, amount)
        elif type == 'p' and len(self.petrol_cars) + amount <= 60:
            self.returns(self.petrol_cars, amount)
        elif type == 'h' and len(self.hybrid_cars) + amount <= 10:
            self.returns(self.hybrid_cars, amount)
        elif type == 'd'and len(self.diesel_cars) + amount <= 20:
            self.returns(self.diesel_cars, amount)
        elif type =='r' and len(self.rotary_cars) + amount <= 5:
                self.returns(self.rotary_cars, amount)    
        
    def frontend(self): # Takes the users input, allowing either the rental or return of a vehicle
        print 'Welcome to DBS Car Rental. This is our current stock:\n'
        self.stock_count()
        user = raw_input("Do you wish to rent 'r' or return 't' a car?\n: ")
        if user == 'r':
            self.process_rental()
        else:
            self.CarReturn()
            

if __name__ == '__main__':
    rent = Dealership()
    rent.current_stock()
    cont = 'y'
    
    while cont == 'y':
        try:
            rent.frontend()
        except:
            print 'Thank you.'
        cont = raw_input('Do you wish to continue? y/n: ')
    print ' Safe Travels'
        
    
