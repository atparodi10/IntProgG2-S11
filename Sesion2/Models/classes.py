class Prodcut:
    def __init__(self, producto, precio, stock):
        self.producto = producto
        self.precio = precio
        self.stock = stock
        
    def __str__(self):
        return f"Nombre: {self.producto}. Precio: {self.precio}. Stock: {self.stock}"
    