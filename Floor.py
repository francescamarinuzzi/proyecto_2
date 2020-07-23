import string
from Cruise import Cruise 

class Floor:
    def __init__(self, quantity_of_halls, quantity_of_rooms_per_hall):
        self.quantity_of_halls = quantity_of_halls
        self.quantity_of_rooms_per_hall = quantity_of_rooms_per_hall

    
    def create(self, cruise):
        #creando pisos del crucero elegido
        floor_list = []
        for rt, info in Cruise.api_saman_caribbean()[cruise].rooms.items():
            self.quantity_of_halls = info[0]
            self.quantity_of_rooms_per_hall = info[1]
            floor = Floor(self.quantity_of_halls, self.quantity_of_rooms_per_hall)
            floor_list.append(floor)
    
        return floor_list
    
    #mostrar habitaciones
    def show(floors, room_type, r):
        i = 0
        for halls in range(floors[room_type - 1].quantity_of_halls):
            for rooms in range(floors[room_type - 1].quantity_of_rooms_per_hall):
                print(r[i], end = '\t')
                i += 1
            print('\n')
        print('\n')


        


    