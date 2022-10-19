
def temperature(n, var1, var2):
    c = 0
    res = 0
    if var1 == "c":
        c = n
    elif var1 == "k":
        c = n - 273.15
    elif var1 == "f":
        c = (n - 32) / 1.8
    if var2 == "c":
        res = c
    elif var2 == "k":
        res = c + 273.15
    elif var2 == "f":
        res = (9/5) * c + 32
    return round(res, 10)


def length(n, var1, var2):
    cm = 0
    res = 0
    if var1 == "cm":
        cm = n
    elif var1 == "mm":
        cm = n / 10
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
    if var2 == "cm":
        res = cm
    elif var2 == "m":
        res = cm / 100
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
        res = cm * 10
    return round(res, 10)


def weight(n, var1, var2):
    kg = 0
    res = 0
    if var1 == "kg":
        kg = n
    elif var1 == "gr":
        kg = n / 1000
    elif var1 == "oz":
        kg = n * 0.02835
    elif var1 == "lbs":
        kg = n * 0.453592
    elif var1 == "stone":
        kg = n * 6.350295
    elif var1 == "cwt british":
        kg = n * 50.6
    elif var1 == "cwt usa":
        kg = n * 45.359229
    elif var1 == "n":
        kg = n * 0.101972
    if var2 == "kg":
        res = kg
    elif var2 == "gr":
        res = kg * 1000
    elif var2 == "oz":
        res = kg * 35.27396
    elif var2 == "lbs":
        res = kg * 2.204623
    elif var2 == "stone":
        res = kg * 0.157473
    elif var2 == "cwt british":
        res = kg * 0.019684
    elif var2 == "cwt usa":
        res = kg * 0.022046
    elif var2 == "n":
        res = kg * 9.806652
    return round(res, 10)
