
# coding: utf-8

# In[7]:


val1 = input().lower()
val2 = input().lower()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for x in range(len(val1)):
    if val1 == val2:
        print(0)
        break
    elif val1 != val2:
        if val1[x] != val2[x]:
            a = alphabet.index(val1[x])
            b = alphabet.index(val2[x])
            if a < b:
                print(-1)
                break
            elif a > b:
                print(1)
                break

