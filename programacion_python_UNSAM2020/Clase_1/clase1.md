

# Clase 1: Introduccion

**Aquí encontrará la resolución de los ejercicios de la clase 1.**. 

[Clase original aquí](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/01_Python.md) 

## Ejercicios

### Ejercicio 1.5: [La pelota que rebota](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/02_Hello_world.md#ejercicio-15-la-pelota-que-rebota)
```{python}
## rebotes.py
altura = 100
salto = 3/5
i = 0

while i < 10:
    i = i + 1
    altura = altura * 3/5
    print(round(altura, 4))
```


**Salida**:\
60.0 \
36.0 \
21.6 \
12.96 \
7.776 \
4.6656 \
2.7994 \
1.6796 \
1.0078 \
0.6047 


### Ejercicio 1.11: [Bonus](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/03_Numeros.md#ejercicio-111-bonus)
```{python}
# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        mes = mes + 1
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        print(mes -1, round(total_pagado, 2), round(saldo, 2))
    else:
        mes = mes + 1
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        print(mes -1, round(total_pagado, 2), round(saldo, 2))

print("Total pagado: ", round(total_pagado, 1))
print("Meses", mes-1)
```
\
**Salida**:\
1 2684.11 499399.22 \
2 5368.22 498795.94 \
3 8052.33 498190.15 \
4 10736.44 497581.83 \
5 13420.55 496970.98 \
6 16104.66 496357.58  \
7 18788.77 495741.63 \
8 21472.88 495123.11 \
9 24156.99 494502.01 \
10 26841.1 493878.33 \
11 29525.21 493252.04 \
12 32209.32 492623.15 \
**(...)** \
300 853233.0 24440.8 \
301 855917.11 21858.53 \
302 858601.22 19265.5 \
303 861285.33 16661.66 \
304 863969.44 14046.97 \
305 866653.55 11421.39 \
306 869337.66 8784.87 \
307 872021.77 6137.36 \
308 874705.88 3478.83 \
309 877389.99 809.21 \
310 880074.1 -1871.53 \
Total pagado:  880074.1 

### Ejercicio 1.13: [El volúmen de una esfera](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/03_Numeros.md#ejercicio-113-el-vol%C3%BAmen-de-una-esfera)

```{python}
# el volúmen de una esfera 

r = float(input("¿Cuál es el radio de tu esfera? "))
pi = 3.1415926535897931
V= 4.0/3.0*pi* r**3

print('The volume of the sphere is: ',V)
```

**Salida**: The volume of the sphere is: 904.7786842338603.

### Ejercicio 1.18: [Geringoso rústico](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/04_Strings.md#ejercicio-118-geringoso-r%C3%BAstico)

```{python}
## ejercicio 1.18
cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:  
    if c == 'a':
        capadepenapa += 'apa'
    elif c == 'e':
        capadepenapa += 'epe'
    elif c == 'i':
        capadepenapa += 'ipi'
    elif c == 'o':
        capadepenapa += 'opo'
    elif c == 'u':
        capadepenapa += 'upu'
    else: 
        capadepenapa += c 
print(capadepenapa)
```

**Salida**: Geperipingoposopo

### Ejercicio 1.29: [Traductor (rústico) al lenguaje inclusivo](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/05_Listas.md#ejercicio-129-traductor-r%C3%BAstico-al-lenguaje-inclusivo)

```{python}
## 1
frase = input('escribe la oración aquí: ')

palabras = frase.split()

frase_t =''
for palabra in palabras:  
    if palabra[-2:] == 'os':
        frase_t += palabra[:-2] + palabra[-2:].replace('o', 'e') + " "
    else:
        frase_t += palabra + " "

print(frase_t)

```
\
**Salidas**:
1. Les hermanes sean unides porque ésa es la ley primera .
2. ¿cómo transmitir a les otres el infinito, Aleph?
3. 'Todos, y tu también'. 


**¿Qué falla en esta última?**
Python no diferencia los caracteres entre una cadena, lo que significa que, para el lenguaje, no importa si es una palabra o una puntuación, por lo que la coma se considera parte del objeto "todos".



