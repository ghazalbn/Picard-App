# فاطمه زهرا بخشنده
from sympy import *
import re

# starts app
print('\nWelcome to Picard App!')
print('-'*22)
while 1:
    # Getting inputs
    x0 = int(input('\nenter x0: '))
    y0 = int(input('enter y0: '))
    # this code below lets you enter y' without * between variables. also you can use ^ as power sign
    d = input('enter y\'(a function of x & y): ').lower().replace('^', '**')
    while re.search("[0-9xy)][tsclexy]", d):
        r = re.findall("[0-9xy)][sclexy]", d)[0]
        d = d.replace(r,f'{r[0]}*{r[1]}')
    n = int(input('enter a positive number for picard: '))

    # Computing Picard
    x = Symbol('x')
    picard = y0
    for i in range(n):
        picard = y0 + integrate(d.replace('y',f'({picard})'), (x, x0, x))
    print(f'\npicard({n}) = ', str(picard).replace('**','^'))
    print('-'*63)

    # Quit App
    if input('\nDo you want to quit? (Enter N if you want try another picard): ') not in ['n', 'N']:
        print(f"\nGood Luck \U0001F44B")
        break
