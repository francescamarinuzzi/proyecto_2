import requests

class Cruise:
    def __init__(self, name, route, departure, cost, rooms, capacity, sells):
        self.name = name
        self.route = route
        self.departure = departure
        self.cost = cost
        self.rooms = rooms
        self.capacity = capacity
        self.sells = sells

    #pegándolealapi
    def api_saman_caribbean():

        url = "https://saman-caribbean.vercel.app/api/cruise-ships"

        response = requests.request('GET', url)

        resp = response.json()

        #armo una lista de cruceros
        cruises = []
        for i in resp:
            name = i['name']
            route = i['route']
            departure = i['departure']
            cost = i['cost']
            rooms = i['rooms']
            capacity = i['capacity']
            sells = i['sells']
            cruise = Cruise(name, route, departure, cost, rooms, capacity, sells)
            cruises.append(cruise)
        
        return cruises
    
    def show_name(self):
        i = 0
        for cruise in self.api_saman_caribbean():
            i += 1
            print(f'{i}. {cruise.name}\n')
    
    def show_route(self):
        i = 0
        for cruise in self.api_saman_caribbean():
            i += 1
            print(f'{i}. {cruise.route}\n')
    
    #mostrar cruceros
    def show(self):
        for cruise in self.api_saman_caribbean():
            print(f' Nombre: {cruise.name}, Ruta: {cruise.route}, Partida: {cruise.departure}, Costo habitaciones: {cruise.cost}')
            print(f' Habitaciones: {cruise.rooms}, Capacidad de las habitaciones: {cruise.capacity}, Comida: {cruise.sells} \n')
    
   

            
                



