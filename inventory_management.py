import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',handlers=[logging.FileHandler("inventory_management.log")])
class Item:
    def __init__(self, id_, name, quantity, price):
        self.id_ = id_
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_stock(self,amount):
        logging.info(f"the stock of {self.name} with id {self.id_} updated to {self.quantity}")
        self.quantity += amount
    def get_item_information(self):
        return f"ID: {self.id_}, Name: {self.name}, quantity: {self.quantity}, Price: {self.price}"


class PhysicalItem(Item):
    def __init__(self, id_, name, quantity, price, weight, dimensions):
        super().__init__(id_, name, quantity, price)
        self.weight = weight
        self.dimensions = dimensions


    def get_item_information(self):
        info = super().get_item_information()
        info_physical = f"  weight: {self.weight}, dimensions:{self.dimensions}"
        return info + info_physical

class DigitalItem(Item):
    def __init__(self, id_, name, quantity, price, file_size, link_download):
        super().__init__(id_, name, quantity, price)
        self.file_size = file_size
        self.link_download = link_download

    def get_item_information(self):
        info = super().get_item_information()
        info_digital = f" File size: {self.file_size}  Link download: {self.link_download}"
        return info + info_digital


obj1 = PhysicalItem(1,"apple",10,10,0.3,"solid")
print(obj1.quantity)
obj1.update_stock(30)
print(obj1.quantity)
print(obj1.get_item_information())

obj2 = DigitalItem(1,"music_album",10,29.9,28,"www.reza.com")
print(obj2.get_item_information())