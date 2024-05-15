dict = {
    'Apple' : '130',
    'Avacado' : '50',
    'Banana' : '110',
    'Cantaloupe' : '50',
    'Grapefruit' : '60'
}

inp = input('Item: ').title()
if inp in dict:
    print(f'Calories: {dict[inp]}')