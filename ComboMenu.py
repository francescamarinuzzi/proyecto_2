from Product import Product

class ComboMenu:
    combo_menu = []
    def __init__(self, combo):
        self.combo = combo

    #función para agregar combos tanto al menú de la corrida del momento como al archivo de texto
    def add_combo(self, file_name):
        self.combo_menu.append(self.combo) 
        with open(file_name, 'a') as f:
            f.write(f'Combo: {self.combo.name}, Productos: {self.combo.products}, Precio: {self.combo.price} \n')

    #función para eliminar combos del menú de la corrida del momento y del archivo de texto
    def remove_combo(self, p):
        for item in self.combo_menu:
            if item.name == p:
                self.combo_menu.remove(item)
                ComboMenu.remove_combo_from_file('combo_menu.txt', p)
                print(f'Combo {item.name} fue eliminado')
        
        #esto es por si la persona está buscando un combo que está en el archivo de texto pero no en el menú de la corrida del momento
        if p not in self.combo_menu:
            if ComboMenu.search_for_combo_in_file('combo_menu.txt', p) == 1:
                ComboMenu.remove_combo_from_file('combo_menu.txt', p)
                print(f'Combo fue eliminado')
                
    #función para eliminar combos del archivo
    def remove_combo_from_file(file_name, p):
        #agrego las lineas que no tengan al combo en una lista
        with open(file_name, 'r') as f:
            c = []
            for line in f:
                if p not in line:
                    c.append(line)

        #y las vuelvo a escribir en el mismo archivo
        with open(file_name, 'w') as f:
            for i in c:
                f.write(f'{i} \n')
            
   
    def show_combo_menu(self):
        for item in self.combo_menu:
            item.show_combo()
        return '' #retorno '' para que no salga none lol
    
    #función para buscar combos en el menú de la corrida del momento
    def search_for_combo(self, p):
        count = 0
        for item in self.combo_menu:
            if item.name != p:
                #si no se encuentra el combo, no se le suma nada a c
                count += 0
            elif item.name == p:
                #si se encuentra se le suma 1, y se muestra el producto
                count += 1
                item.show_combo()
        return count
    
    #función para buscar combos en el archivo de texto
    def search_for_combo_in_file(file_name, p):
        with open(file_name, 'r') as f:
            c = 0
            for line in f:
                if p not in line:
                    c += 0
                else:
                    c += 1
                    print(line)
        return c
    
    #función para buscar combos en el menú de la corrida del momento por rango de precio
    def search_for_combo_per_price(self, l, r):
        c = 0
        for i in self.combo_menu:
            if i.price >= l and i.price <= r:
                i.show_combo()
                c += 1
            else:
                c += 0
        return c




class ProductMenu(ComboMenu):
    #esto es literalmente lo mismo que combos pero con productos lol, excepto que estos se pueden modificar
    menu = []
    def __init__(self, combo):
        super().__init__(combo)
        self.product = combo

    def add_product(self, file_name):
        self.menu.append(self.product)
        with open(file_name, 'a') as f:
            f.write(f'Producto: {self.product.name}, Clasificación: {self.product.classification}, Tipo de comida: {self.product.type_of_food}, Tamaño de bebida: {self.product.beverage_size}, Precio: {self.product.price} \n')
        
    def remove_product(self, p):
        for item in self.menu:
            if item.name == p:
                self.menu.remove(item)
                ProductMenu.remove_product_from_file('product_menu.txt', p)
                print(f'Producto {item.name} fue eliminado')
                
        if p not in self.menu:
            if ProductMenu.search_for_product_in_file('product_menu.txt', p) == 1:
                ProductMenu.remove_product_from_file('product_menu.txt', p)
                print(f'Producto fue eliminado')
    
    def remove_product_from_file(file_name, p):
        with open(file_name, 'r') as f:
            a = []
            for line in f:
                if p not in line:
                    a.append(line)
                        
        with open(file_name, 'w') as f:
            for i in a:
                f.write(f'{i} \n')

    #función para modificar productos SOLO en el menú de la corrida del momento
    def modify_product(self, p, a):
        if a == 1:
            #para cambiar el nombre
            new_name = input('Ingrese el nuevo nombre: ')
            for item in self.menu:
                if item.name == p:
                    item.modify_name(new_name)
        #para cambiar la clasificación
        elif a == 2:
            while True:
                try:
                    new_classification = int(input('Ingrese la nueva clasificación: alimento(1), bebida(2): '))
                    if new_classification == 1:
                        new_classification = 'alimento'
                        new_type_of_food = int(input('Indique si el alimento es de empaque(1) o de preparación(2): '))
                        if new_type_of_food == 1:
                            new_type_of_food = 'empaque'
                        elif new_type_of_food == 2:
                            new_type_of_food = 'preparación'
                        else:
                            raise Exception
                        new_beverage_size = 'No aplica'

                    elif new_classification == 2:
                        new_classification = 'bebida'
                        new_beverage_size = int(input('Indique tamaño de la bebida: pequeño(1), mediano(2), grande(3): '))
                        if new_beverage_size == 1:
                            new_beverage_size = 'pequeño'
                        elif new_beverage_size == 2:
                            new_beverage_size = 'mediano'
                        elif new_beverage_size == 3:
                            new_beverage_size = 'grande'
                        else:
                            raise Exception
                        new_type_of_food = 'No aplica'
                    
                    break
                except:
                    print('Ingrese una opción válida')

            for item in self.menu:
                if item.name == p:
                    #función de la clase que cambia los atributos
                    item.modify_classification(new_classification, new_type_of_food, new_beverage_size)
        
        #para cambiar el precio
        elif a == 3:
            while True:
                try:
                    new_raw_price = float(input('Ingrese el nuevo precio: '))
                    new_price = Product.product_price(new_raw_price)

                    break
                
                except:
                    print('Ingrese datos válidos')
            

            for item in self.menu:
                if item.name == p:
                    item.modify_price(new_price)
    
    def show_menu(self):
        for item in self.menu:
            item.show_product()
        return ''
                        

    def search_for_product(self, p):
        count = 0
        for item in self.menu:
            if item.name != p:
                count += 0
            elif item.name == p:
                count += 1
                item.show_product()
        return count
    
    def search_for_product_in_file(file_name, p):
        with open(file_name, 'r') as f:
            c = 0
            for line in f:
                if p not in line:
                    c += 0
                else:
                    c += 1
                    print(line)
        return c

    
    def search_for_product_per_price(self, l, r):
        c = 0
        for i in self.menu:
            if i.price >= l and i.price <= r:
                i.show_product()
                c += 1
            else:
                c += 0
        return c


    
    
    

