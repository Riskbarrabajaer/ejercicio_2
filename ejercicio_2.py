vivienda = 2_000_000
sueldo = int(input("ingrese sueldo"))
def calcular_mensualidad (pie1, años):
    return (vivienda - pie1) * años
def calcular_descuento(entrada1):
    return (entrada1 / 100) * vivienda
 
if sueldo >= 80_000:
    pie = 15
    meses = 120
 
elif sueldo < 80_000:
    pie = 30
    meses = 84

pie_inicial = calcular_descuento(pie)    
print(f"pie a paga pagar {pie_inicial}clp")
print(f"mensualidad {calcular_mensualidad(pie_inicial, meses)}clp")
print(f"durante {meses // 12} años")




    