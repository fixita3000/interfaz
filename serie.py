"""
    en un circuito en serie se tienen 3 resistencia
    r1=15 ohm
    r2=20ohm
    r3=x
    la ressitencia total es de 60 ohm
    cual es el valor de r3?
    rt= r1+r2+r3
    60=15+20+x
    60-35=x
    25ohm=43
"""

import sympy
r3=sympy.symbols("r3")
resistencia_total =15+20+r3
solucion = sympy.solve(resistencia_total)
print(f"la resistencia 3 es igual a:{solucion [0]}ohm")
