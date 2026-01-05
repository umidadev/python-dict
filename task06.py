car = {
  'brand': 'Chevrolet',
  'model': 'Cobalt',
  'color': 'white'
 }

key = input('key: ')

value = car.get(key, 'topilmadi')
print(value)