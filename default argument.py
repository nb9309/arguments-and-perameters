def fun_name(name,age,sal,cun='india'):

    print('\t{}\t{}\t{}\t{}'.format(name,age,sal,cun))

print('\tname\tage\tsal\tcountry')
fun_name('naresh',21,50000)
fun_name('suresh',23,40000)
fun_name('chandu',22,35000)

'''def fun_name(age,sal,cun='india',name): # default parameter must come in last only 

    print('\t{}\t{}\t{}\t{}'.format(name,age,sal,cun))

print('\tname\tage\tsal\tcountry')
fun_name('naresh',21,50000)
fun_name('suresh',23,40000)
fun_name('chandu',22,35000)

output = syntax error'''