n = float(input())
var1 = input()
var2 = input()

def temperature(n, var1, var2):
    if var1 == "C" and var2 == "F":
        return round((((9/5) * n + 32)), 2) #Celsius -> Fahrenheit
    elif var1 == "C" and var2 == "K":
        return round((n + 273.15), 2) #Celsius -> Kelvin
    elif var1 == "F" and var2 == "C":
        return round((5 / 9) * n - 32, 2) #Fahrenheit -> Celsius
    elif var1 == "K" and var2 == "C":
         return n - 273.15 #Kelvin -> Celsium
def temperature2(n, var1, var2):
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
def weigt(n, var1, var2):
    if var1 == "kg" and var2 == "lbs": #ounces
        return round((n * 2.20462), 2)
    elif var1 == "gr" and var2 == "oz": #фунты
        return round((n * 0.035274), 2)

def lenght(n, var1, var2):
    if var1 == "km" and var2 == "mile":
        return round((n * 1.60934), 2)
    elif var1 == "m" and var2 == "yd": #yards
        return round((n * 1.09361), 2)
    elif var1 == "m" and var2 == "ft": #футы
        return round((n / 0.3048), 2)
    elif var1 == "cm" and var2 == "inch":
        return round((n * 2.5400013716), 2)
