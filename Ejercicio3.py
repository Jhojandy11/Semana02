'''
 Objetivo: En la Universidad "Del Futuro", se necesita un programa con las siguientes caracteristicas.
# Nombre; Jhojandy Azariel Michue Izquierdo
# Fecha: 29/03/2025

Ingresos
 Deberá ingresar un monto
 Descuentos 
     Deberá ingresar un monto
Neto a pagar
  Deberá calcular la suma Total de ingresos - Total de Descuentos

  Se debe ingresar la cantidad de días laborados
'''


# Entrada

MontoDeIngreso=float(input("digite el ingreso: "))

diasNolaborados=int(input("Digite la cantidad de dias no laborados: ")) 

#Proceso

diaslaborados =  30 - diasNolaborados
pagopordia= MontoDeIngreso / 30

netoPagar= diaslaborados * pagopordia

print("El neto a pagar es: ",netoPagar)
