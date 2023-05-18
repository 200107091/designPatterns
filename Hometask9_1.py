class Product:
    def __init__(self, name, price, weight, width, height, depth):
        self.name = name
        self.price = price
        self.weight = weight
        self.width = width
        self.height = height
        self.depth = depth

    def accept(self, visitor):
        visitor.visit(self)


class Book(Product):
    def __init__(self, name, price, weight, width, height, depth, author, publisher):
        super().__init__(name, price, weight, width, height, depth)
        self.author = author
        self.publisher = publisher


class Clothing(Product):
    def __init__(self, name, price, weight, width, height, depth, size, color):
        super().__init__(name, price, weight, width, height, depth)
        self.size = size
        self.color = color


class Electronics(Product):
    def __init__(self, name, price, weight, width, height, depth, brand, model):
        super().__init__(name, price, weight, width, height, depth)
        self.brand = brand
        self.model = model


class ShippingCostCalculator:
    def __init__(self):
        self.total_weight = 0
        self.total_volume = 0

    def visit(self, product):
        self.total_weight += product.weight
        self.total_volume += product.width * product.height * product.depth

    def calculate_cost(self):
        return self.total_weight * 2 + self.total_volume * 0.01


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def accept(self, visitor):
        for product in self.products:
            product.accept(visitor)


if __name__ == '__main__':
    order = Order()
    order.add_product(Book('The Lord of the Rings', 19.99, 1.5, 0.2, 0.3, 0.05, 'J.R.R. Tolkien', 'Houghton Mifflin Harcourt'))
    order.add_product(Clothing('T-Shirt', 9.99, 0.2, 0.3, 0.2, 0.05, 'M', 'Blue'))
    order.add_product(Electronics('iPhone 13', 999.99, 0.2, 0.1, 0.2, 0.01, 'Apple', 'iPhone 13'))

    shipping_cost_calculator = ShippingCostCalculator()
    order.accept(shipping_cost_calculator)
    shipping_cost = shipping_cost_calculator.calculate_cost()
    print('Shipping Cost:', shipping_cost)