a = 5
b = 6
def first_func():
    if a < b:
        print(str(a) + " меньше " + str(b))
    else:
        print(str(a) + " больше " + str(b))

c = first_func()

km = 1.60934
def miles_to_kms(mile):
    return mile * km
d = miles_to_kms(5)
print(d)

def is_even(a):
    e = a % 2
    if e == 0:
        print("Переданное число " + str(a) + " является четным")
    else:
        print("Переданное число " + str(a) + " является нечетным")
#   return e

is_even(7)
#
print(e)