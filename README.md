# Price Formatter

This script format number like a price, e.g. 12341 convert to 12 341.<br>
Note: 
* The number with decimal number converted to price format with 2 decimal places,  cuts them as is, e.g. 3112.999 convert to 3 112.99
* If input number can't format to price format, script return None
# How to use
```bash
$python format_price.py 3245.000000
3 245
```
```bash
$python format_price.py 99999.999999
99 9999.99
```

#### You also use format price like a function in your project, just import format_price
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
