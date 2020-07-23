class Tour:
    def __init__(self, name, price_per_person, group_capacity, discount, time, total_capacity):
        self.name = name
        self.price_per_person = price_per_person
        self.group_capacity = group_capacity
        self.discount = discount
        self.time = time
        self.total_capacity = total_capacity
    

    def create():
        tour_1 = Tour('Tour en el puerto', 30, 4, 10, '7 AM', 10)
        tour_2 = Tour('Degustación de comida local', 100, 2, '-', '12 PM', 100)
        tour_3 = Tour('Trotar por el pueblo/ciudad', 0, '-', '-', '6 AM', '-')
        tour_4 = Tour('Visita a lugares históricos', 40, 4, 10, '10 AM', 15)
        tours = [tour_1, tour_2, tour_3, tour_4]

        return tours
    
    #función para aplicar el descuento correspondiente a las personas comprando tours
    def apply_discount(price, discount, quantity_of_people):
        op = price * (discount / 100)
        price_with_discount = (price * quantity_of_people) - (op * 2)
        return price_with_discount
    
    #chequear disponibilidad de cupos para los tours
    def vacancy(tour, quantity_of_people):
        if tour == 0:
            #creo una lista para meter la cantidad de personas (el grupo) que reservaron
            v = []
            for person in range(quantity_of_people):
                v.append(person + 1)
            
            #appendeo la lista al archivo de texto
            with open('tour1_vacancy_file.txt', 'a') as f:
                for person in v:
                    f.write(f'{person}')
            
            #si la linea donde appendeo la lista, supera la capacidad total del tour, no se pueden hacer más reservaciones
            with open('tour1_vacancy_file.txt', 'r') as f:
                for line in f:
                    if len(line) > 10:
                        return False
                    else:
                        return True

        #LO MISMO PARA LOS DEMÁS TOURS EXCEPTO EL DE TROTAR QUE NO TIENE LÍMITE DE PERSONAS
        elif tour == 1:
            v = []
            for person in range(quantity_of_people):
                v.append(person + 1)
            
            with open('tour2_vacancy_file.txt', 'a') as f:
                for person in v:
                    f.write(f'{person}')
            
            with open('tour2_vacancy_file.txt', 'r') as f:
                for line in f:
                    if len(line) > 100:
                        return False
                    else:
                        return True
        
        elif tour == 3:
            v = []
            for person in range(quantity_of_people):
                v.append(person + 1)
            
            with open('tour4_vacancy_file.txt', 'a') as f:
                for person in v:
                    f.write(f'{person}')
            
            with open('tour4_vacancy_file.txt', 'r') as f:
                for line in f:
                    if len(line) > 15:
                        return False
                    else:
                        return True
        




    
        
        
        
    

    