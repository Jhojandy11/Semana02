# Entrada

MontoDeIngreso=float(input("digite el ingreso: "))
Descuento=int(input("digite el descuento: "))
diasNolaborados=int(input("Digite la cantidad de dias no laborados: ")) 

#Proceso

diaslaborados =  30 - diasNolaborados
pagopordia= MontoDeIngreso / 30

netoPagar= diaslaborados * pagopordia - Descuento

print("El neto a pagar es: ",netoPagar)
