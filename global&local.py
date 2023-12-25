# var_global=4
# def func():
#     global var_global
#     var_global= 3
#     print(var_global)
 
# func()
# print(var_global)

var1=10  #global
def fun():
    var1=3
    print("fun1 ",var1)
    def fun2():
        nonlocal var1
        var1=4
        print("fun2 ",var1)
    
    fun2()
    print(var1)
fun()
print(var1) #global