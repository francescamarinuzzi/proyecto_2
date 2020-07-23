class Reservation:
    def __init__(self, iden, name, final_price):
        self.iden = iden
        self.name = name
        self.final_price = final_price
    
#reservaciones de los tours
class TourReservation(Reservation):
    def __init__(self, iden, name, time, final_price):
        super().__init__(iden, name, final_price)
        self.hour = time

    def show(self, quantity_of_people):
        if quantity_of_people == 4:
            print('Reservación exitosa!')
            print(f'Código de reserva: {self.iden}, Tour: {self.name}, Hora: {self.hour}, Precio final con descuento: {self.final_price}')
        else:
            print('Reservación exitosa!')
            print(f'Código de reserva: {self.iden}, Tour: {self.name}, Hora: {self.hour}, Precio final sin descuento: {self.final_price}')
    
    #appendeo las reservaciones a un archivo
    def tour_reservation_file(self, file_name):
        with open(file_name, 'a') as f:
            f.write(f' \n Código de reserva: {self.iden}, Tour: {self.name}, Hora: {self.hour}, Precio final: {self.final_price}')

#reservaciones de las habitaciones 
class RoomReservation(Reservation):
    taxes = 0.16
    def __init__(self, name, iden, age, disability, room, final_price):
        super().__init__(iden, name, final_price)
        self.persons_age = age
        self.persons_disability = disability
        self.room_information = room
        #self.taxess = taxes
    
    def show(self):
        print(f'Nombre: {self.name}, Identificación: {self.iden}, Edad: {self.persons_age}, Discapacidades: {self.persons_disability}, Habitación: {self.room_information}, Impuestos: {self.taxes}, Precio: {self.final_price}')
        return ''

    #appendeo las reservaciones a un archivo
    def room_reservation_file(self, file_name):
        with open(file_name, 'a') as f:
            f.write(f' \n Nombre: {self.name}, Identificación: {self.iden}, Edad: {self.persons_age}, Discapacidades: {self.persons_disability}, Habitación: {self.room_information}, Impuestos: {self.taxes}, Precio: {self.final_price}')