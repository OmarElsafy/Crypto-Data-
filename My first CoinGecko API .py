#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install --upgrade pandas ')


# In[ ]:





# In[2]:


pip install pycoingecko


# In[3]:


from pycoingecko import CoinGeckoAPI


# In[4]:


get_ipython().system('pip install pandas')


# In[5]:


get_ipython().system('pip install seaborn ')


# In[6]:


get_ipython().system('pip install numpy')


# In[7]:


import pandas as pd 
import seaborn as sns
import numpy as np 


# In[ ]:





# In[8]:


cg = CoinGeckoAPI()


# In[9]:


cg.ping()


# In[10]:


cg.get_supported_vs_currencies()


# In[11]:


cg.get_price(ids='bitcoin', vs_currencies='usd')


# In[12]:


cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')


# In[13]:


cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd,eur')


# In[14]:


cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies=['usd', 'eur'])


# In[15]:


cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')


# In[16]:





# In[ ]:


cg.get_supported_vs_currencies()


# In[ ]:


cg.get_coins_list()


# In[ ]:


cg.get_coins_markets()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




