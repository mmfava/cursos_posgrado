#!/usr/bin/env python
# coding: utf-8

# In[2]:


# tablamult.py

column = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
inicio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print ("           ", f'{0:>10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>10} {6:>10} {7:>10} {8:>10} {9:>10}')
print ("       ", "-------------------------------------------------------------------------------------------------------------------")

for i in range(10):
    print(f'{i:>10d}: {inicio[0]:>10} {inicio[1]:>10d} {inicio[2]:>10d} {inicio[3]:>10d} {inicio[4]:>10d} {inicio[5]:>10d} {inicio[6]:>10d} {inicio[7]:>10d} {inicio[8]:>10d} {inicio[9]:>10d}')
    inicio = (inicio[0] + 0, inicio[1] + 1, 
              inicio[2] + 2, inicio[3] + 3, 
              inicio[4] + 4, inicio[5] + 5, 
              inicio[6] + 6, inicio[7] + 7,
              inicio[8] + 8, inicio[9] + 9)

