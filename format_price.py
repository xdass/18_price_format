import sys


def format_price(price):
    try:
        if isinstance(price, str):
            price = float(price)
        if float(price) < 0:
            return None
        if float(price).is_integer():
            return '{:,.0f}'.format(price).replace(',', ' ')
        else:
            integer, decimal = str(price).split('.')
            prepared_price = '{}.{}'.format(integer, decimal[:2])
            return '{:,}'.format(float(prepared_price)).replace(',', ' ')
    except ValueError:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        raw_price = sys.argv[1].strip('\'')
        print(format_price(raw_price))
    price_1 = 1231233  # 1 231 233
    price_2 = 9999.99999  # 9 999.99 ??
    price_3 = 3245.000000  # 3 245
    price_4 = -40000  # wrong
    price_5 = 'asdadads'  # wrong
    price_6 = '123123.12312312.123123'
    price_7 = '12312'
    price_8 = 5555.3511
    print(format_price(price_1))
    print(format_price(price_2))
    print(format_price(price_3))
    print(format_price(price_4))
    print(format_price(price_5))
    print(format_price(price_6))
    print(format_price(price_7))
    print(format_price(price_8))