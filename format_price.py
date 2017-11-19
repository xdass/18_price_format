import sys


def format_price(price):
    try:
        if isinstance(price, str):
            price = float(price)
        if float(price) < 0:
            raise ValueError
        if float(price).is_integer():
            return '{:,.0f}'.format(price).replace(',', ' ')
        else:
            price = str(price)[:str(price).find('.') + 3]
            return '{:,}'.format(float(price)).replace(',', ' ')
    except ValueError:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        raw_price = sys.argv[1].strip('\'')
        print(format_price(raw_price))
