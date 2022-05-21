#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import itertools
from scipy.stats import mode
from collections import Counter


# In[5]:


class FiniteField:
    def __init__(self, n,m):
        l = [4,3,2,1,0]
        self.n = n
        self.m = m
        self.elements = np.array(list(itertools.product(l, repeat=self.n + self.m)))
        self.M = self.elements[np.where(self.elements[:,0:self.n].sum(axis=1)!=self.n)]
        self.M = self.M[np.where(self.M[:,self.n:].sum(axis=1)!=self.m)]
        
    def get_coverage(self, alpha):
        cosets = []
        alpha_1 = alpha[:self.n]
        alpha_2 = alpha[self.n:]
        for i in range(self.n):
            for j in range(self.m):

                a = Counter(alpha)
                elem = a.most_common()[-1][0]
                if(elem == 1):
                    subspace = self.elements[np.where((self.elements[:,np.where(alpha==elem)[0]].sum(axis=1)==alpha.sum()))[0]]
                else:
                    subspace = self.elements[np.where((self.elements[:,np.where(alpha==elem)[0]].sum(axis=1)==0))[0]]

                coset = np.logical_xor(subspace, alpha).astype(int)
                cosets.append(coset)

                alpha_2 = np.roll(alpha_2, 1)
                alpha = np.concatenate([alpha_1, alpha_2])
            alpha_1 = np.roll(alpha_1, 1)
            alpha = np.concatenate([alpha_1, alpha_2])

        return cosets


# In[12]:


f = FiniteField(2,3)


# In[24]:


f.get_coverage(np.array([0,3,3,0,4]))


# In[14]:


np.unique(np.vstack(f.get_coverage(np.array([0,3,3,0,4]))),axis=0)


# In[22]:


np.vstack(f.get_coverage).shape


# In[ ]:




