"""Agregar Prodcutos"""
"""
Creat
Read
Update
Delete
CRUD
"""

class ProdcutDao:
    def __init__(self):
        self.products = []
    
    def add(self, prodcut):
        self.products.append(prodcut)
    
    def show(self):
        for product in self.products:
            print(product)