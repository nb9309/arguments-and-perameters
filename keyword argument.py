def fun_name(name,age,sal,cnt='india'):

    print('\t{}\t{}\t{}\t{}'.format(name,age,sal,cnt))

print('\tname\tage\tsal\tcountry')
fun_name('naresh',21,22000)
fun_name('suresh',22,20000)
fun_name(sal=40000,age=22,name='chandu',cnt='russia')
fun_name(age=22,name='sai',sal = 56000)
fun_name('shruthi',sal=90000,age=22)   # first preference gives to positional arguments