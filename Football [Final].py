
# coding: utf-8

# In[6]:


splt = input()


# In[8]:

beg = 0
end = 7
val = splt[beg:end]

for x in range(len(splt)):
    if len(splt) < 7:
        break
    elif val == '1111111' or val == '0000000':
        print('YES')
        break
    elif val != '1111111':
        beg += 1
        end += 1
        val = splt[beg:end]
if val != '1111111' and val != '0000000':
    print('NO')

