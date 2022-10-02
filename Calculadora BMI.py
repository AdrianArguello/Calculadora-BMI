def cuerpo (altura, peso):
	return round ((peso / altura**2),2)


a = float (input("introduzca su altura en metros:"))
p = float (input("introduzca su peso en kilogramos"))

print ("bienvenido")

bmi = cuerpo (a, p)
print ("Tu BMI es: ", bmi)

if bmi <= 18.5:
	print ("Estas bajo de peso")
elif 18.5 < bmi <= 24.9:
	print("Estas en un peso normal")
elif 25 < bmi <= 29.9:
	print("Tienes exceso de peso")
else:
	print("Eres obeso")