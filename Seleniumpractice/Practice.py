from random import random



Company = 'Infosys' + \
          '31' + \
          'Limited'
print(Company)

print("Stefan Salvatore"[5:])

a = "  PYTHON PROGRAM  "
print(a.lstrip('P'))

try:
    print(10 * (1 / 10))
    print(203 / 0)
    print(var * 33)

except(ZeroDivisionError, NameError):
    print('Error')
