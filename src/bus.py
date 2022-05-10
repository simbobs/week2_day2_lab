class Bus:
    def __init__(self,route_number,destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    
    def drive(self):
        return "The VengaBus is coming!"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)
        
    def drop_off(self,passenger):
        self.passengers.remove(passenger)
    
    def empty(self):
        self.passengers = []
        
    def pick_up_from_stop(self, bus_stop):
        queue_passengers = bus_stop.queue
        if queue_passengers != None:
            self.passengers.append(self.pick_up(queue_passengers))
            return bus_stop.clear()
            
        
        
        
    