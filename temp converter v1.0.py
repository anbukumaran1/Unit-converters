import time
print("""
╔════╗╔═══╗╔═╗╔═╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗╔╗ ╔╗╔═══╗╔═══╗    ╔═══╗╔═══╗╔═╗ ╔╗╔╗  ╔╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗
║╔╗╔╗║║╔══╝║║╚╝║║║╔═╗║║╔══╝║╔═╗║║╔═╗║║╔╗╔╗║║║ ║║║╔═╗║║╔══╝    ║╔═╗║║╔═╗║║║╚╗║║║╚╗╔╝║║╔══╝║╔═╗║║╔╗╔╗║║╔══╝║╔═╗║
╚╝║║╚╝║╚══╗║╔╗╔╗║║╚═╝║║╚══╗║╚═╝║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║║╚══╗    ║║ ╚╝║║ ║║║╔╗╚╝║╚╗║║╔╝║╚══╗║╚═╝║╚╝║║╚╝║╚══╗║╚═╝║
  ║║  ║╔══╝║║║║║║║╔══╝║╔══╝║╔╗╔╝║╚═╝║  ║║  ║║ ║║║╔╗╔╝║╔══╝    ║║ ╔╗║║ ║║║║╚╗║║ ║╚╝║ ║╔══╝║╔╗╔╝  ║║  ║╔══╝║╔╗╔╝
 ╔╝╚╗ ║╚══╗║║║║║║║║   ║╚══╗║║║╚╗║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗║╚══╗    ║╚═╝║║╚═╝║║║ ║║║ ╚╗╔╝ ║╚══╗║║║╚╗ ╔╝╚╗ ║╚══╗║║║╚╗
 ╚══╝ ╚═══╝╚╝╚╝╚╝╚╝   ╚═══╝╚╝╚═╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝╚═══╝    ╚═══╝╚═══╝╚╝ ╚═╝  ╚╝  ╚═══╝╚╝╚═╝ ╚══╝ ╚═══╝╚╝╚═╝
                                                                                                              
                                                                                                              

""")
print("=======================================================================================================================================================")
print("""
1.Celsius
2.Fahrenheit
3.Kelvin
4.Rankine
""")
q1 = int(input("Enter a quantity you want to convert  : "))
q2 = int(input("Enter a quantity you want to convert into : "))
if q1 ==1 and q2 ==2:
    a = int(input("Enter degree in celsius to covert to fahrenheit   : "))
    print(a*33.8)
elif q1 ==1 and q2 ==3:
    a = int(input("Enter degree in celsius to covert to kelvin   : "))
    print(a*274.15)
elif q1 ==1 and q2 ==4:
    a = int(input("Enter degree in celsius to covert to rankine  : "))
    print(a*493.47)
elif q1 ==2 and q2 ==1:
    a = int(input("Enter degree in fahrenheit to covert to celsius  : "))
    print(a*-17.2222222)
elif q1 ==2 and q2 ==3:
    a = int(input("Enter degree in fahrenheit to covert to kelvin  : "))
    print(a*255.927778)
elif q1 ==2 and q2 ==4:
    a = int(input("Enter degree in fahrenheit to covert to rankine : "))
    print(a*460.67)
elif q1 ==3 and q2 ==1:
    a = int(input("Enter degree in kelvin to covert to celsius  : "))
    print(a*-272.15)
elif q1 ==3 and q2 ==2:
    a = int(input("Enter degree in kelvin to covert to fahrenheit  : "))
    print(a*-457.87)
elif q1 ==3 and q2 ==4:
    a = int(input("Enter degree in kelvin to covert to rankine : "))
    print(a*1.8) 
elif q1 ==4 and q2 ==1:
    a = int(input("Enter degree in rankie to covert to celsius  : "))
    print(a*-272.594444)
elif q1 ==4 and q2 ==2:
    a = int(input("Enter degree in rankie to covert to fahrenheit  : "))
    print(a*-458.67)
elif q1 ==4 and q2 ==3:
    a = int(input("Enter degree in rankie to covert to kelvin : "))
    print(a*0.55555556) 
else:
    print("INVALID. ENTER A CORRECT VALUE ")
print("=======================================================================================================================================================")
time.sleep(100000)