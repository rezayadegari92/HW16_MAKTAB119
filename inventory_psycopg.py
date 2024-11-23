import psycopg2
from typing import List, Tuple

class InventoryConnection:
    connection_inventory = None

    @classmethod
    def get_connection(cls):
        if cls.connection_inventory:
            return cls.connection_inventory
        else:
            cls.connection_inventory = psycopg2.connect(database="inventory_psycopg", user='postgres', password='1234',
                                                        host='127.0.0.1', port='5432')
            cls.connection_inventory.autocommit = True
            return cls.connection_inventory

    @classmethod
    def get_cursor(cls):
        cursor = cls.get_connection().cursor()
        return cursor

    @classmethod
    def create_table(cls):
        query = """CREATE TABLE inventory(id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	QUANTITY INT,
	PRICE DECIMAL(10,2))"""
        db_cursor = cls.get_cursor()
        db_cursor.execute(query)
        print("TABLE CREATE WAS SUCCESSFUL")
    @classmethod
    def get_all(cls, table_name: str) -> List[Tuple]:
        """the function return all TABLE INFO list
        """
        query = """SELECT * FROM {}""".format(table_name)

        db_cursor = cls.get_cursor()
        db_cursor.execute(query)
        item_list = db_cursor.fetchall()
        return item_list




if __name__ == '__main__':
 #   inventory_instance = InventoryConnection.create_table()
    list_ = InventoryConnection.get_all('inventory')
    print(list_)