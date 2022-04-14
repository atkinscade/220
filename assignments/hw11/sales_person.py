

class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def __str__(self):
        return "{self.employee_id} - {self.name}: {self.sales}"

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self.name

    def enter_sale(self, sale):
        self.sales.append(sale)
        return self.sales

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if quota >= sum(self.sales):
            return False
        else:
            return True

    def compare_to(self, other):
        if self.sales > other.sales:
            return 1
        else:
            return -1



