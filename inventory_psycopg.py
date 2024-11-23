import psycopg2


class InventoryConnection:
    connection_inventory = None
    @classmethod
    def get_connection(cls):
        if cls.connection_inventory:
            return connection_inventory
        else:
            connection = psycopg2.connect(database="inventory_psycopg", user='postgres', password='1234', host='127.0.0.1', port= '5432')

            cursor = connection.cursor()
            cls.connection_inventory = cursor
            return cls.connection_inventory


