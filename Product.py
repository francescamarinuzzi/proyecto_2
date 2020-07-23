class Product:
    def __init__(self, name, classification, beverage_size, type_of_food, price):
        self.name = name
        self.classification = classification
        self.beverage_size = beverage_size
        self.type_of_food = type_of_food
        self.price = price

    def product_price(price):
        #calculo el precio con IVA
        iva = price * 0.16
        final_price = price + iva
        return final_price

    def show_product(self):
        print(f'[ Nombre: {self.name}, Clasificación: {self.classification}, Tamaño de bebida: {self.beverage_size}, Tipo de alimento: {self.type_of_food}, Precio con IVA: {self.price} Bs ]')
        return ''

    def modify_name(self, new_name):
        self.name = new_name

    def modify_classification(self, new_classification, new_type_of_food, new_beverage_size):
        self.classification = new_classification
        self.type_of_food = new_type_of_food
        self.beverage_size = new_beverage_size
    
    def modify_price(self, new_price):
        self.price = new_price
    
    



