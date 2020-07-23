from Cruise import Cruise
from Floor import Floor
import string

class Room:
    def __init__(self, cost, classification, capacity, hall_letter, number, reference, extra_info):  
        self.cost = cost
        self.classification = classification
        self.capacity = capacity
        self.hall_letter = hall_letter
        self.number = number
        self.reference = reference
        self.extra_info = extra_info
    
    def create(self, cruise, room_type):
        #el día que esta función se ejecutó sin errores fue el día más feliz de mi trimestre no joke
        room_list = []
        rooms_per_floor = Floor.create(Floor, cruise)[room_type - 1].quantity_of_rooms_per_hall * Floor.create(Floor, cruise)[room_type - 1].quantity_of_halls
        for n in range(rooms_per_floor):
            for rt, price in Cruise.api_saman_caribbean()[cruise].cost.items():
                if room_type == 1:
                    self.cost = Cruise.api_saman_caribbean()[cruise].cost['simple']
                    self.classification = 'simple'
                    self.extra_info = 'Room service'

                elif room_type == 2:
                    self.cost = Cruise.api_saman_caribbean()[cruise].cost['premium']
                    self.classification = 'premium'
                    self.extra_info = 'Vista al mar'
                
                elif room_type == 3:
                    self.cost = Cruise.api_saman_caribbean()[cruise].cost['vip']
                    self.classification = 'vip'
                    self.extra_info = 'Se pueden realizar fiestas'
                

            self.capacity = self.room_capacity(cruise, room_type)
            self.reference = '-'
            self.hall_letter = self.assing_hall_letter(Floor.create(Floor, cruise)[room_type - 1].quantity_of_halls, Floor.create(Floor, cruise)[room_type - 1].quantity_of_rooms_per_hall)[n]
            self.number = n + 1

            room = Room(self.cost, self.classification, self.capacity, self.hall_letter, self.number, self.reference, self.extra_info)
            room_list.append(room)
        
        return room_list

    #obtengo la capacidad de cada tipo de habitación
    def room_capacity(cruise, room_type):
        capacity = Cruise.api_saman_caribbean()[cruise].capacity.items()
        for rt, cap in capacity:
            if room_type == 1:
                capacity2 = Cruise.api_saman_caribbean()[cruise].capacity['simple']
                    
            elif room_type == 2:
                capacity2 = Cruise.api_saman_caribbean()[cruise].capacity['premium']
                
            elif room_type == 3:
                capacity2 = Cruise.api_saman_caribbean()[cruise].capacity['vip']
            
        return capacity2
    

    #asignar la letras de los pasillos a las habitaciones
    #creo una lista a la cual se le van a appendear la cantidad de letras según 
    #la cantidad de pasillos y habitaciones
    def assing_hall_letter(quantity_of_halls, quantity_of_rooms_per_hall):
        alphabet_string = string.ascii_uppercase
        alphabet_list = list(alphabet_string)
        letters = []
        x = 0
        i = 0
        z = 0
        while z < quantity_of_halls:
            while x < quantity_of_rooms_per_hall:
                letters.append(alphabet_list[i])
                x += 1
        
            i += 1
            z += 1
            x = 0

        return letters

    #mostrar en una matriz las habitaciones disponibles
    def show(cruise, room_type):
        #guardo en una variable la lista que devuelve la función create
        rl = Room.create(Room, cruise, room_type)
        l1 = []
        for n in range(len(rl)):
            #en una lista vacía appendeo la información de las habitaciones que necesito
            l1.append(f'{rl[n].number}{rl[n].hall_letter}')
        
        #le paso la lista a la función que va a mostrar la matriz
        Floor.show(Floor.create(Floor, cruise), room_type, l1)
    
    def price(cruise, room_type):
        price = Room.create(Room, cruise, room_type)[0].cost
        taxes = price * 0.16
        total = price + taxes
        return total


    
    #la habitación que pida el cliente se apendea al archivo de texto correspondiente al crucero y tipo de habitación
    def reserve_room(cruise, room_type, room):
        with open(f'{cruise}_{room_type}.txt', 'a') as f:
            f.write(f'{room} \n')
    
    #función para indicar la disponibilidad de las habitaciones
    def vacancy(cruise, room_type, room):
        #chequea el archivo de texto para ver si la habitación que están pidiendo ya está reservada.
        with open(f'{cruise}_{room_type}.txt', 'r') as f:
            c = 0
            for line in f:
                if room in line:
                    #si la encuentra, le suma 1 a la variable c que actua como pote
                    c += 1
        
            #si c es > 1, significa que la habitación está dos veces en el archivo
            #por lo que se borra y se le indica al cliente que esa habitación ya está tomada
            if c > 1:
                with open(f'{cruise}_{room_type}.txt', 'r') as f:
                    lines = f.readlines()
                #borro la última línea del archivo
                with open(f'{cruise}_{room_type}.txt', 'w') as f:
                    for line in lines[:-1]:
                        f.write(f'{line} \n')
                
        return c







    
