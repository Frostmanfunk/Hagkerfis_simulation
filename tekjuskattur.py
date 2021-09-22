#!/usr/bin/env python
# coding: utf-8

# In[34]:


import math

class tekjuskattur_c:
    
    def __init__ (self, skattþrep = ([0.3145,(0,349_018)],[0.3795,(349_019,979_847)],[0.4625,(979_847,math.inf)])): # á eftir að ákveða parametrana
        self.skattþrep = skattþrep
    
    def personuafslattur_f (self, personuafslattur = 50_792, uppsafnadur_personuafslattur = 0):
        self.personuafslattur = personuafslattur
        self.uppsafnadur_personuafslattur = uppsafnadur_personuafslattur
        
    def stadgreidsla_f(self, laun = 0, lifeyrissjodur = 0.04): # hægt að bæta við séreignarsparnaði o.fl. seinna
        skattstofn = laun*(1-lifeyrissjodur)
        þrep = 0
        for i in range(3):
            if skattstofn > self.skattþrep[i][1][0]:
                þrep += 1
        i = 0
        stadgreidsla = 0
        while þrep > 0:
            try:
                if skattstofn >= self.skattþrep[i+1][1][0]:
                    stadgreidsla += (self.skattþrep[i][1][1] - self.skattþrep[i][1][0])*self.skattþrep[i][0]
                else:
                    stadgreidsla += (skattstofn - self.skattþrep[i][1][0])*self.skattþrep[i][0]
            except:
                stadgreidsla += (skattstofn - self.skattþrep[2][1][0])*self.skattþrep[2][0]
            i += 1
            þrep -= 1
        stadgreidsla -= self.personuafslattur + self.uppsafnadur_personuafslattur
        if stadgreidsla < 0:
            self.uppsafnadur_personuafslattur = self.personuafslattur
            try:
                self.endurgreidsla -= stadgreidsla
            except:
                self.endurgreidsla = -stadgreidsla
            return 0
        elif stadgreidsla < self.personuafslattur:
            self.uppsafnadur_personuafslattur = self.personuafslattur - stadgreidsla
            return stadgreidsla
        else:
            return stadgreidsla


# In[33]:


x = tekjuskattur_c()
x.personuafslattur_f()
heildar = 0
for i in range(12):
    d = x.stadgreidsla_f(300_000)
    print(f"einstaklingurinn borgaði {round(d):>5} kr í tekjuskatt í mánuði {i+1}")
    heildar += d
print(f"Einstaklingurinn borgaði {heildar - x.endurgreidsla} kr í tekjuskatt á árinu")
    

