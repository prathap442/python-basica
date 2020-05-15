import pdb

class Checkout():
    dashboard = {

    }
    def add_items_to_board(self,item_name, item_qty, item_price=None):
        item_keys = self.dashboard.keys()
        if (type(item_qty) != int):
            raise Exception('qty should be integer')
        if item_name in item_keys:
           self.dashboard[item_name]['price'] = item_price
           self.add_quantity(item_name, item_qty)
        else:
            if(item_qty < 0):
                item_qty = 0
            self.dashboard[item_name] = {
                "quantity": item_qty,
                "price": item_price
            }
        return self.dashboard

    def add_quantity(self,item_name, quantity):
        if type(quantity) == int:
            self.dashboard[item_name]['quantity'] += quantity
            if(int(self.dashboard_item_quantity(item_name)) < 0):
                self.dashboard[item_name]['quantity'] = 0


    def dashboard_item_quantity(self,item_name):
        item_info = self.get_dashboard()[item_name]
        if item_name:
            return item_info['quantity']
        raise Exception("No such item exists")

    def get_dashboard(self):
        return self.dashboard

    