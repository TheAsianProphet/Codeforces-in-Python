
# coding: utf-8

# In[8]:


def word_cptl(word):
    first_letter = word[0].upper()
    final = first_letter + word[1:]
    return final

a = word_cptl(input())
print(a)
    

