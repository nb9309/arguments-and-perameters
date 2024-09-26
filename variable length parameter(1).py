def fun_name(name,age,sal,*param,cnt='india'):

    print('\tname = {}\tage = {}\tsal = {}\tparam = {}\tcountry = {}'.format(name,age,sal,param,cnt))


fun_name('naresh',21,22000,1.3,6.5,7.8)
#fun_name('suresh',22,20000,cnt='america',1.2,6.7,8)
fun_name('suresh',22,20000,1.2,6.7,8,cnt='america')
fun_name(sal=40000,age=22,name='chandu',1.2,2.2,3.4,cnt='russia')
fun_name(age=22,name='sai',sal = 56000)
fun_name('shruthi',sal=90000,age=22)   # first preference gives to positional arguments