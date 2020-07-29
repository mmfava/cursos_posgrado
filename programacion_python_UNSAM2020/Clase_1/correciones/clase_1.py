## hipoteca.py

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
        print(mes, saldo, total_pagado)
    else:
        saldo -= pago_mensual
        total_pagado = total_pagado + pago_mensual
        print(mes, saldo, total_pagado)

    mes += 1
        
print(mes, saldo, total_pagado)       
total_pagado += saldo * (1+tasa/12)
saldo = 0
mes += 1

print("Total pagado: ", round(total_pagado, 0))
print("Meses", mes - 1)

#%%
## geringonso.py

cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
    capadepenapa += c
    if c in "aeiou":
        capadepenapa += 'p'
        capadepenapa += c

print("{} -> {}". format(cadena, capadepenapa))

#%%
## 

