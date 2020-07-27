## inclusive.py
## frase = input('escribe la oración aquí: ')

## palabras = frase.split()

## frase_t =''
## for palabra in palabras:  
##    if palabra[-2:] == 'os':
##        frase_t += palabra[:-2] + palabra[-2:].replace('o', 'e') + " "
##    else:
##       frase_t += palabra + " "

## print(frase_t)

## inclusive.py - Parte 1
frase = 'Los hermanos sean unidos porque ésa es la ley primera'

palabras = frase.split()

frase_t =''
for palabra in palabras:  
    if palabra[-2:] == 'os':
        frase_t += palabra[:-2] + palabra[-2:].replace('o', 'e') + " "
    else:
        frase_t += palabra + " "

print(frase_t)

## inclusive.py - Parte 2
frase = '¿cómo transmitir a los otros el infinito Aleph?'

palabras = frase.split()

frase_t =''
for palabra in palabras:  
    if palabra[-2:] == 'os':
        frase_t += palabra[:-2] + palabra[-2:].replace('o', 'e') + " "
    else:
        frase_t += palabra + " "

print(frase_t)

## inclusive.py - Parte 3
frase = 'Todos, tu también'

palabras = frase.split()

frase_t =''
for palabra in palabras:  
    if palabra[-2:] == 'os':
        frase_t += palabra[:-2] + palabra[-2:].replace('o', 'e') + " "
    else:
        frase_t += palabra + " "

print(frase_t)

# In[ ]:




