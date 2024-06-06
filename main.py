import matplotlib.pyplot as plt
import numpy as np
import sympy
from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("")
x = symbols('x') # x es una variable simbólica que se usará en la función
fn = sympify(input("Ingresa Función: ")) # Definir quién es la función que nos interesa
f = lambdify(x, fn)

# Iniciar variables
a = float(input("Dame el valor inicial a: ")) # Ingresar valor inicial          Límite Superior
b = float(input("Dame el valor inicial b: ")) # Ingresar valor inicial          Límite Inferior
crit = float(input("Dame el criterio de paro: ")) # Ingresar criterio de tolerancia
i = 0 # Iniciar el contador
ea = 1 # Iniciar la variable de error
x_anterior = 0 # Iniciar la variable de x anterior

# Criterio inicial para verificar si la solución está en el intervalo seleccionado
if f(a) * f(b) < 0:
   
    # Imprime encabezados de tabla
    print("")
    print("{:^60}".format("Método de Bisección"))
    print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i", "a", "b", "xr", "ea(%)"))

    while ea > crit:
        xr = (a + b) / 2
        ea = abs((xr - x_anterior) / xr)
           
        if f(xr) * f(a) < 0:
            b = xr
        else:
            a = xr
           
        x_anterior = xr

        # Imprime valores de tabla
        print("{:^10} {:^10.3f} {:^10.3f} {:^10.3f} {:^10.3f}".format(i, a, b, xr, round(ea * 100, 3)))
        i = i + 1

    print(" ")
    print("El valor de x es", round(xr, 9), "con un error de", round(ea * 100, 9), "%")

    # Grafica la función e indicar el punto
    xpts = np.linspace(-10, 10) # Regresa un vector en numpy formado por n números con los mismos espacios
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(xr, 0, c="red")
    plt.annotate(round(xr, 9), xy=(xr, 0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()
else: # f(a) * f(b) >= 0
    # Si no hay raíz o bien se seleccionan 2 raíces en un intervalo
    print(" ")
    print("La función no tiene una raíz en el intervalo de " + "x = " + str(a) + " a x = " + str(b))
    print("Ingresar otros valores iniciales")

    # Grafica la función e indicar el punto
    xpts = np.linspace(-10, 10, 400)
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()
