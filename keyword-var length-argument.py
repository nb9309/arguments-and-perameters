def fun_name(*para,name,age,sal,cnt='india',**param):
    print('\tpara = {}\tname = {}\tage = {}\tsal = {}\tcountry = {}\tparam = {}'.format(para,name,age,sal,cnt,param))
    print(type(param))
fun_name(1.2,5.6,7.8,sal=40000,age=22,name='chandu',cnt='russia',height=3,waiegt=4,heigh=5)