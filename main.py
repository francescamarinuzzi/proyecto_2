from Cruise import Cruise
from Room import Room
from Floor import Floor
from Tour import Tour
from ComboMenu import ProductMenu
from ComboMenu import ComboMenu
from Product import Product
from Combo import Combo
from Reservation import TourReservation
from Reservation import RoomReservation

#funcion para  elegir el tour a reservar
def choose_tour():
    #se le pide el DNI al cliente y se le muestran los tours que provee el crucero
    while True:
        try: 
            dni = int(input('DNI: '))
            for i, tour in enumerate(Tour.create(), 1):
                print(f'''\n {i}. {tour.name}
                - Precio por persona: {tour.price_per_person}
                - Hasta {tour.group_capacity} personas
                - Descuento del {tour.discount} % para la tercera y cuarta persona
                - Empieza a las {tour.time}
                - Capacidad total: {tour.total_capacity}
                ''')
               
            choice = int(input('Cuál tour desea reservar?: '))
            
            if choice == 1:
                quantity_of_people = int(input('Cuántas personas son?: '))
                #gc = group capacity
                gc = Tour.create()[0].group_capacity
                #si su grupo de personas es mayor a la capacidad por grupos del tour, no podrá reservar
                if quantity_of_people > gc:
                    print(f'No se pueden grupos mayores a {gc} personas')
                else:
                    print(reserve_tour(quantity_of_people, dni, choice))
            #lo mismo que en el 1
            elif choice == 2:
                quantity_of_people = int(input('Cuántas personas son?: '))
                gc = Tour.create()[1].group_capacity
                if quantity_of_people > gc:
                    print(f'No se pueden grupos mayores a {gc} personas')
                else:
                    print(reserve_tour(quantity_of_people, dni, choice))

            elif choice == 3:
                #aquí no se pide cantidad del grupo de personas porque este tour no tiene límite
                quantity_of_people = int(input('Cuántas personas son?: '))
                print(reserve_tour(quantity_of_people, dni, choice))

            #lo mismo que en el 1
            elif choice == 4:
                quantity_of_people = int(input('Cuántas personas son?: '))
                gc = Tour.create()[0].group_capacity
                if quantity_of_people > gc:
                    print(f'No se pueden grupos mayores a {gc} personas')
                else:
                   print(reserve_tour(quantity_of_people, dni, choice))

            else:
                raise Exception

            break
        
        except:
            print('Ingrese una opción válida')
    
#función para reservar tour
def reserve_tour(quantity_of_people, dni, choice):
    #si aplican descuentos
    #4 porque los tours que tienen descuento es en la 3ra y 4ta persona
    if quantity_of_people == 4:
        #variable que va a indicar cual tour
        i = choice - 1
        final_price = Tour.apply_discount(Tour.create()[i].price_per_person, Tour.create()[i].discount, quantity_of_people)
        tour_reservation = TourReservation(dni, Tour.create()[i].name, Tour.create()[i].time, final_price)

    #si no hay ningun descuento
    else:
         #variable que va a indicar cual tour
        i = choice - 1
        final_price = Tour.create()[i].price_per_person * quantity_of_people
        tour_reservation = TourReservation(dni, Tour.create()[i].name, Tour.create()[i].time, final_price)

    #con Tour.vacancy() chequeo si todavia queda espacio para el tour elegido
    if Tour.vacancy(i, quantity_of_people):
        #si queda espacio, se hace la reserva
        tour_reservation.tour_reservation_file('tour_reservations.txt')
        tour_reservation.show(quantity_of_people)
    else:
        # si no, se le avisa al cliente que no es posible
        print(f'No quedan suficientes cupos disponibles para el tour {tour_reservation.name}, disculpe.')

    #retorno esto para que no salga 'none' lol
    return ''

    
#función para vender las habitaciones
def choose_room():
    while True:
        #se le pide la información requerida al cliente
        try:
            q = int(input('¿Está comprando un boleto en base al barco(1) o al destino(2)? : '))
            if q == 1:
                #mostrar los nombres de los cruceros
                Cruise.show_name(Cruise)
                #le resto 1 al input para que matchee con los índices de la lista de los cruceros
                cruise = int(input('Escoja su crucero: ')) - 1
                room_type = int(input('¿Qué tipo de habitación desea?: Sencilla(1), Premium(2), VIP(3): '))
                people = int(input('Cantidad de personas que viajan con usted: '))
                #si la cantidad de personas es mayor a la capacidad de la habitación que eligió, se le indica que debe elegir varias
                if Room.room_capacity(cruise, room_type) < people:
                    print(f'Disculpe, estas habitaciones tienen capacidad, deberá elegir varias habitaciones.')
                else:
                    print('Espere un momento por favor.')
                    #para mostrar las habitaciones
                    Room.show(cruise, room_type)
                    r = input('Ingrese el número y letra de la habitación que desea reservar: ')
                    #estás funciones son para chequear si la habitación está disponible y poder hacer la reserva
                    Room.reserve_room(cruise, room_type, r)
                    if Room.vacancy(cruise, room_type, r) == 1:
                        print('La habitación se encuentra disponible')
                        print(reserve_room(r, cruise, room_type))
                    else:
                        print('La habitación que desea ya se encuentra ocupada')

                    
            elif q == 2:
                #mostrar las rutas de los cruceros
                Cruise.show_route(Cruise)
                #le resto 1 al input para que matchee con los índices de la lista de los cruceros
                cruise = int(input('Escoja su crucero: ')) - 1
                room_type = int(input('¿Qué tipo de habitación desea?: Sencilla(1), Premium(2), VIP(3): '))
                people = int(input('Cantidad de personas que viajan con usted: '))
                #si la cantidad de personas es mayor a la capacidad de la habitación que eligió, se le indica que debe elegir varias
                if Room.room_capacity(cruise, room_type) < people:
                    print(f'Disculpe, estas habitaciones tienen capacidad menor capacidad, deberá elegir varias habitaciones.')
                else:
                    print('Espere un momento por favor.')
                    #para mostrar las habitaciones
                    Room.show(cruise, room_type)
                    r = input('Ingrese el número y letra de la habitación que desea reservar: ')
                    #estás funciones son para chequear si la habitación está disponible y poder hacer la reserva
                    Room.reserve_room(cruise, room_type, r)
                    if Room.vacancy(cruise, room_type, r) == 1:
                        print('La habitación se encuentra disponible')
                        print(reserve_room(r, cruise, room_type))
                    else:
                        print('La habitación que desea ya se encuentra ocupada')
            else:
                raise Exception
            
            break

        except:
            print('Ingrese una opción válida')
    
    
#función para hacer la factura de la reserva
def reserve_room(r, cruise, room_type):
    while True:
        #se le pregunta al cliente por estos datos
        try:
            name = input('Nombre: ')
            iden = int(input('Identificación: '))
            age = int(input('Edad: '))
            disability = int(input('¿Posee alguna discapacidad? si(1), no(2): '))
            if disability == 1:
                disability = 'si'
            elif disability == 2:
                disability = 'no'
            else:
                raise Exception

            break
        
        except:
            print('Ingrese una opción válida')
    
    
    price = Room.price(cruise, room_type)

    room_reservation = RoomReservation(name, iden, age, disability, r, price)
    room_reservation.room_reservation_file('room_reservation_file.txt')
    print('Reservación exitosa')

    return room_reservation.show()


   


#función para agregar producto al menú de productos
def add_product():
    while True:
        #se pide la información del producto
        try: 
            name = input('Producto que desea agregar: ')
            classification = int(input('Indique si el producto es un alimento(1) o bebida(2): '))
            if classification == 1:
                classification = 'alimento'
                type_of_food = int(input('Indique si el alimento es de empaque(1) o de preparación(2): '))
                if type_of_food == 1:
                    type_of_food = 'empaque'
                elif type_of_food == 2:
                    type_of_food = 'preparación'
                else:
                    raise Exception
                beverage_size = 'No aplica'
            elif classification == 2:
                classification = 'bebida'
                beverage_size = int(input('Indique tamaño de la bebida: pequeño(1), mediano(2), grande(3): '))
                if beverage_size == 1:
                    beverage_size = 'pequeño'
                elif beverage_size == 2:
                    beverage_size = 'mediano'
                elif beverage_size == 3:
                    beverage_size = 'grande'
                else:
                    raise Exception
                type_of_food = 'No aplica'
            else:
                raise Exception

            raw_price = float(input('Precio: '))
            
            price = Product.product_price(raw_price)

            break
        
        except:
            print('Error: ingrese una opción válida')
    
    #guardo el producto en una variable y se lo paso a la función que lo va a agregar al menú
    product = Product(name, classification, beverage_size, type_of_food, price)

    m = ProductMenu(product)
    #función de la clase para agregar el producto al menú
    m.add_product('product_menu.txt')

    print(f'Producto {product.name} agregado exitosamente')
    return m.show_menu()

#función para agregar combo al menú
def add_combo():
    while True:
        #se pide la información del combo
        try: 
            name = input('Combo que desea agregar: ')
            number_of_products = int(input('¿Cuántos productos tiene el combo?: '))
            #si el combo no tiene 2  o más productos no se puede agregar
            if number_of_products >= 2:
                products = products_list(number_of_products)
            else:
                print('El combo debe de tener más de 2 productos')
                raise Exception

            #raw_price es el precio sin iva
            raw_price = float(input('Precio: '))
            
            #aqui se le agrega el IVA al precio
            price = Combo.combo_price(raw_price)

            break
        
        except:
            print('Ingrese datos válidos')
    
    #guardo el combo en una variable
    combo = Combo(name, products, price)

    m = ComboMenu(combo)
    #función de la clase para agregar el combo al menú
    m.add_combo('combo_menu.txt')

    print(f'Combo {combo.name} agregado exitosamente')
    return m.show_combo_menu()

#esta función es para guardar los todos los productos del combo en una lista
def products_list(number_of_products):
    products = []
    i = 0
    while i < number_of_products:
        p = input('Ingrese producto: ')
        products.append(p)
        i += 1
    return products


def main():
    while True:
        #le pregunto a la persona que quiere hacer
        try:
            menu = int(input('''\n Bienvenido a Saman Caribbean
            1. Cruceros
            2. Habitaciones
            3. Tours
            4. Restaurante
            5. Estadísticas
            6. Salir
            > '''))
            if menu == 1:
                Cruise.show(Cruise)
            elif menu == 2:
                choose_room()
            elif menu == 3:
                choose_tour()
                
            elif menu == 4:
                while True:
                    try:
                        option = int(input('''\n ¿Qué desea hacer?: 
                        1. Agregar un producto al menú.
                        2. Eliminar un producto del menú.
                        3. Modificar un producto del menú.
                        4. Agregar un combo al menú de combos.
                        5. Eliminar un combo del menú de combos.
                        6. Buscar productos por nombre o rango de precio.
                        7. Buscar combos por nombre o rango de precio.
                        8. Salir
                        > '''))
                        if option == 1:
                            print(add_product())

                        elif option == 2:
                            while True:
                                try:
                                    p = input('¿Cuál producto desea eliminar?: ')
                                    #se busca el producto en el menú de la corrida actual y en el archivo de texto
                                    if ProductMenu.search_for_product(ProductMenu, p) == 0 and ProductMenu.search_for_product_in_file('product_menu.txt', p) == 0:
                                        raise Exception
                                    else:
                                        ProductMenu.remove_product(ProductMenu, p)
                                            
                                    break

                                except:
                                    print('Ese producto no se encuentra en el menú')

                                    break


                        elif option == 3:
                            while True:
                                try:
                                    p = input('¿Cuál producto desea modificar?: ')
                                    
                                    #se busca el producto en el menú de la corrida del momento
                                    if ProductMenu.search_for_product(ProductMenu, p) == 0:
                                        print('Ese producto no se encuentra en el menú')
                                    
                                    a = int(input('''\n ¿Qué le desea modificar?:  
                                    1. Nombre.
                                    2. Clasificación.
                                    3. Precio.
                                    4. Salir
                                    > '''))

                                    break

                                except:
                                    print('Ingrese datos válidos')
                                    break
                            
                            ProductMenu.modify_product(ProductMenu, p, a)
                            ProductMenu.show_menu(ProductMenu)

                        elif option == 4:
                            print(add_combo())
                        
                        elif option == 5:
                            while True:
                                try:
                                    p = input('¿Cuál combo desea eliminar?: ')
                                    #se busca el combo en el menú de la corrida actual y en el archivo de texto
                                    if ComboMenu.search_for_combo(ComboMenu, p) == 0 and ComboMenu.search_for_combo_in_file('combo_menu.txt', p) == 0:
                                        raise Exception
                                    else:
                                        ComboMenu.remove_combo(ComboMenu, p)
                                            
                                    break

                                except:
                                    print('Ese producto no se encuentra en el menú')
                                    break

                        
                        elif option == 6:
                            while True:
                                try:
                                    n = int(input('¿Desea buscar producto por nombre(1) o rango de precio(2)?: '))
                                    if n == 1:
                                        p = input('Ingrese el nombre del producto: ')
                                        #se busca el producto en el menú de la corrida actual y en el archivo de texto
                                        if ProductMenu.search_for_product(ProductMenu, p) == 0 and ProductMenu.search_for_product_in_file('product_menu.txt', p) == 0:
                                            print('Ese producto no se encuentra en el menú')
                                            
                                    
                                    elif n == 2:
                                        l = int(input('De: '))
                                        r = int(input('A: '))
                                        #solo se puede buscar por rango de precio en la corrida, no en los archivos
                                        if ProductMenu.search_for_product_per_price(ProductMenu, l, r) == 0:
                                            print('No hay productos en ese rango de precios')
                                    
                                    else:
                                        print('Ingrese una opción válida')
                                            
                                    break

                                except:
                                    print('Ingrese datos válidos')
                                    break 
                            
                        elif option == 7:
                            while True:
                                try:
                                    n = int(input('¿Desea buscar combo por nombre(1) o rango de precio(2)?: '))
                                    if n == 1:
                                        p = input('Ingrese el nombre del combo: ')
                                        #se busca el producto en el menú de la corrida actual y en el archivo de texto
                                        if ComboMenu.search_for_combo(ComboMenu, p) == 0 and ComboMenu.search_for_combo_in_file('combo_menu.txt', p) == 0:
                                            print('Ese producto no se encuentra en el menú')
                                    
                                    elif n == 2:
                                        l = int(input('De: '))
                                        r = int(input('A: '))

                                        #solo se puede buscar por rango de precio en la corrida, no en los archivos
                                        if ComboMenu.search_for_combo_per_price(ComboMenu, l, r) == 0:
                                            print('No hay combos en ese rango de precios')

                                    else:
                                        print('Ingrese una opción válida')
                                    
                                    break

                                except:
                                    print('Ingrese datos válidos')
                                    break 

                        else:
                            break
                    
                    except:
                        print('Ingrese una opción válida')

                
            elif menu == 5:
                print('Módulo en desarrollo!')
                #sorryprofe
                break
            else:
                print('Bai')
                break
        except:
            print('Ingrese una opción válida')
main()