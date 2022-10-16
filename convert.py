
def temperature(n, var1, var2):
    # переведем в Цельсия вне зависимости от того, какая величина дана
    if var1 == "C":
        c = n
    elif var1 == "K":
        c = n - 273.15
    elif var1 == "F":
        c = (5 / 9) * n - 32
    #переведем цельсия в нужную величину
    if var2 == "C":
        res = c
    elif var2 == "K":
        res = c + 273.15
    elif var2 == "F":
        res = (9/5) * c + 32
    return round(res, 2)

def length(n, var1, var2):
    if var1 == "cm":
        cm = n
    elif var1 == "mm":
        cm = n * 10
    elif var1 == "km":
        cm = n * 100000
    elif var1 == "m":
        cm = n * 100
    elif var1 == "ft":
        cm = n * 30.48
    elif var1 == "ml":
        cm = n * 160934.4
    elif var1 == "yd":
        cm = n * 91.44
    elif var1 == "inch":
        cm = n * 2.54
    elif var1 == "dm":
        cm = n / 10
    #converting to the value that is needed
    if var2 == "cm":
        res = cm
    elif var2 == "m":
        res = cm * 100
    elif var2 == "km":
        res = cm * 10 ** (-5)
    elif var2 == "ft":
        res = cm * 0.032808
    elif var2 == "ml":
        res = cm * 6.21 * 10 ** (-6)
    elif var2 == "yd":
        res = cm * 0.0120936
    elif var2 == "inch":
        res = cm * 0.393701
    elif var2 == "dm":
        res = cm * 10
    elif var2 == "mm":
        res = cm / 10
    return round(res, 2)

def weigth(n, var1, var2):



def weight(n, var1, var2):
    if var1 == "kg" and var2 == "lbs": #ounces
        return round((n * 2.20462), 2)
    elif var1 == "gr" and var2 == "oz": #фунты
        return round((n * 0.035274), 2)



