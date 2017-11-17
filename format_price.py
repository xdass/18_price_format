from decimal import *


# проверка на отрицательное значение
# проверка на число(не строка)
# неверный формат числа (123.123.123)


def format_price(price):
    try:
        if isinstance(price, str):
            price = float(price)
        if float(price) < 0:
            raise ValueError
        if str(price).find('.') != -1:
            price = str(price)[:str(price).find('.') + 3]
            return '{:,}'.format(float(price)).replace(',', ' ')
        else:
            return '{:,}'.format(price).replace(',', ' ')
    except ValueError:
        return None


if __name__ == '__main__':
    price_1 = 1231233  # 1 231 233
    price_2 = 9999.999  # 9 999.99 ??
    price_3 = 3245.000000  # 3 245
    price_4 = -40000  # wrong
    price_5 = 'asdadads'  # wrong
    price_6 = '123123.12312312.123123'
    print(format_price(price_1))
    print(format_price(price_2))
    print(format_price(price_3))
    print(format_price(price_4))
    print(format_price(price_5))
    print(format_price(price_6))
