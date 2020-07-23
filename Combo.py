class Combo:
    def __init__(self, name, products, price):
        self.name = name
        self.products = products
        self.price = price

    def combo_price(price):
        #calculo el precio con IVA
        iva = price * 0.16
        final_price = price + iva
        return final_price
    
    def show_combo(self):
        print(f'[ Nombre: {self.name}, Productos: {self.products}, Precio con IVA: {self.price} Bs ]')
        return ''