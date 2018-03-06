rub = 1
euro = 69.70
dollar = 56.50	
yena = 0.54
v = [rub, euro, dollar, yena]
t = ['в рублях', 'в долларах', 'в евро', 'в йенах']

def convert(money, ind):
    return [t[ind], str(round(money / v[ind], 3))]
# курс на 6.03.18
