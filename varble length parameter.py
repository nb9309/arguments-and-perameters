# type of variable length parameter is tuple
def fun_name(a,b,c,d):
    print(a,b,c,d)
fun_name(10,20,30,40)

def fun_name(a,b,c):
    print(a,b,c)
fun_name(10,20,30)

def fun_name(a,b):
    print(a,b)
fun_name(10,20)

def fun_name(a):
    print(a)
fun_name(10)

def fun_name():
    print()
fun_name()
print('-'*50)
print('--------or---------')

def fun_name(*val):
    print(val)

fun_name(10,20,30,40)
fun_name(10,20,30)
fun_name(10,20)
fun_name(10)
fun_name()

print('--------or----------')

def fin_name(*val):
    for i in val:
        print(i,end=' ')
    print('\t\t\t\t\t\ttype of val is {}, length of val is {}'.format(type(val),len(val)))
    print()

fin_name(10,20,30,40)
fin_name(10,20,30)
fin_name(10,20)
fin_name(10)
fin_name()

