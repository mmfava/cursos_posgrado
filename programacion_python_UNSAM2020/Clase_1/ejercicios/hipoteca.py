#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[ ]:




