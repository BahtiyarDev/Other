from functools import reduce

filt = lambda x: 'name' in x and 'price' in x and x['name'].strip() != '' and (isinstance(x['price'], (int, float)) or (isinstance(x['price'], str) and x['price'].lstrip('-').replace('.', '', 1).isdigit())) and (float(x['price']) > 0 if isinstance(x['price'], str) else x['price'] > 0)

raw_products = [
    {"name": "Mouse", "price": 25.5},
    {"name": "Keyboard", "price": "45.0"},
    {"name": "", "price": 20},           # Пустое имя → ошибка
    {"name": "Monitor", "price": -150},  # Отрицательная цена → ошибка
    {"name": "USB Cable"},               # Нет цены → ошибка
]

filtered_lst = list(filter(filt, raw_products))
print(filtered_lst)


class ProductError(Exception):
    def __init__(self, prod, message='Product error occured!'):
        self.prod = prod
        self.message = message
        super().__init__(self.message)


class MissingFieldError(ProductError):
    def __init__(self, prod, field):
        super().__init__(prod, f'Missing prod {prod} field {field} error!')


class NegativePriceError(ProductError):
    def __init__(self, prod,  price):
        super().__init__(prod, f'You entered negative price {price} in prod {prod}!')


class EmptyNameError(ProductError):
    def __init__(self, prod):
        super().__init__(prod, f'Empty name in prod {prod}!')


class BadPriceTypeError(ProductError):
    def __init__(self, prod):
        super().__init__(prod, f'Incorrect type of price in prod {prod}!')


def normalize(prod):
    if not isinstance(prod, dict):
        raise ProductError(prod, 'Product must be dict!')

    if 'name' not in prod or 'price' not in prod:
        raise MissingFieldError(prod, "name")

    if not isinstance(prod['price'], (int, float)):
        try:
            prod['price']=float(prod["price"])
        except TypeError:
            raise BadPriceTypeError(prod)
        

    if prod['name'].strip() == '':
        raise EmptyNameError(prod)

    if prod['price'] < 0:
        raise NegativePriceError(prod, "price")
    
    return {'name': prod['name'], 'price': prod['price']}

def safe_normalize(prod):
    try:
        return normalize(prod)
    except ProductError:
        return None

    


# print(normalize(raw_products[3]))

valid_products = list(filter(lambda x: x is not None, map(safe_normalize, raw_products)))
print(valid_products)
summ = reduce(lambda acc, x: acc + x['price'], valid_products, 0.0)
average_price = summ/len(valid_products)
max_price = reduce(lambda max, x: x if x['price'] > max['price'] else max, valid_products)
print(max_price)

sorted_catalog_up = sorted(valid_products, key=lambda x: x['price'])
sorted_catalog_dwn = sorted(valid_products, key=lambda x: x['price'], reverse=True)
print(sorted_catalog_up)
print(sorted_catalog_dwn)