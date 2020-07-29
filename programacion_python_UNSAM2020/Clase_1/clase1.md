

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

while saldo > pago_mensual:
    saldo *= (1+tasa/12) 
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo -= pago_mensual + pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo -= pago_mensual
        total_pagado = total_pagado + pago_mensual
        
    mes += 1
        
        
total_pagado += saldo * (1+tasa/12)
saldo = 0
mes += 1

print("Total pagado: ", round(total_pagado, 0))
print("Meses", mes - 1)

```
\
**Salida**:\
**(...)** \
300 24440.802775242293 853232.9999999965 \
301 21858.529453472467 855917.1099999965 \
302 19265.496659528602 858601.2199999965 \
303 16661.659562276636 861285.3299999965 \
304 14046.973143786123 863969.4399999965 \
305 11421.392198551897 866653.5499999964 \
306 8784.87133271253 869337.6599999964 \
307 6137.364963265498 872021.7699999964 \
308 3478.8273172791037 874705.8799999964 \
309 809.2124311010998 877389.9899999964 \
310 809.2124311010998 877389.9899999964 \ 
Total pagado:  878203.0 \
Meses 310 \

### Ejercicio 1.13: [El volúmen de una esfera](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/03_Numeros.md#ejercicio-113-el-vol%C3%BAmen-de-una-esfera)

```{python}
## esfera.py 

r = float(input("¿Cuál es el radio de tu esfera? "))
pi = 3.1415926535897931
V= 4.0/3.0*pi* r**3

print('The volume of the sphere is: ',V)
```

**Salida**: The volume of the sphere is: 904.7786842338603.

### Ejercicio 1.18: [Geringoso rústico](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/01_Introduccion/04_Strings.md#ejercicio-118-geringoso-r%C3%BAstico)

```{python}

## geringoso.py
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
## inclusive.py
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



