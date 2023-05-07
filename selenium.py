#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install selenium')


# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time


# In[ ]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[ ]:


#Question 1


# In[ ]:


driver.get('https://www.naukri.com/')


# In[ ]:


des=driver.find_element(By.CLASS_NAME,'suggestor-input')


# In[ ]:


des.send_keys('Data Analyst')


# In[ ]:


loc=driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
loc.send_keys('Banglore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[ ]:


title=[]
location=[]
company_name=[]
exp_required=[]


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title.append(i.text)
    
title    


# In[ ]:


loc_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in loc_tags[0:10]:
    location.append(i.text)
    
location    


# In[ ]:


location


# In[ ]:


name_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in name_tags[0:10]:
    company_name.append(i.text)
    
company_name    


# In[ ]:


exp_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in exp_tags[0:10]:
    exp_required.append(i.text)
    
exp_required    


# In[ ]:


df=pd.DataFrame(columns=['Title','Location','Company Name','Experience Required'])
df["Title"]=title
df['Location']=location
df['Company Name']=company_name
df['Experience Required']=exp_required
df


# In[ ]:


#Question 2


# In[ ]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[ ]:


driver.get('https://www.naukri.com/')


# In[ ]:


des=driver.find_element(By.CLASS_NAME,'suggestor-input ')
des.send_keys('DataScientist')


# In[ ]:


loc=driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
loc.send_keys('Banglore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[ ]:


title=[]
location=[]
company_name=[]
exp_required=[]


# In[ ]:


title_tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title.append(i.text)


# In[ ]:


title


# In[ ]:



loc_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in loc_tags[0:10]:
  location.append(i.text)
  
location    


# In[ ]:


name_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in name_tags[0:10]:
    company_name.append(i.text)
    
company_name  


# In[ ]:


exp_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in exp_tags[0:10]:
    exp_required.append(i.text)
    
exp_required    


# In[ ]:


df=pd.DataFrame(columns=['Title','Location','Company Name','Experience Required'])
df["Title"]=title
df['Location']=location
df['Company Name']=company_name
df['Experience Required']=exp_required
df


# In[ ]:


#Question 3


# In[ ]:


df=pd.DataFrame(columns=['Title','Company Name','Location','Experience Required'])


# In[ ]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[ ]:


driver.get('http://www.naukri.com/')


# In[ ]:


des=driver.find_element(By.CLASS_NAME,'suggestor-input ')
des.send_keys('DataScientist')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[ ]:


loc=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[4]/div[2]').click()


# In[ ]:


sal=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[1]/label/p/span[1]').click()


# In[ ]:


title=[]
title_tag=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article/div[1]/div[1]/a')
print(title_tag.text)
title.append(title_tag.text)


# In[ ]:


cname=[]
name=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article/div[1]/div[1]/div/a[1]')
name=name.text
cname.append(name)


# In[ ]:


cexp=[]
exp=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article/div[1]/ul/li[1]/span[1]')
cexp.append(exp.text)


# In[ ]:


cloc=[]
loc=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article/div[1]/ul/li[3]/span')
cloc.append(loc.text)


# In[ ]:


df["Title"]=title
df['Location']=cloc
df['Company Name']=cname
df['Experience Required']=cexp
df


# In[ ]:


#Question 4


# In[39]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[40]:


driver.get('http://www.flipkart.com/')


# In[41]:


product=driver.find_element(By.CLASS_NAME,'_3704LK')
product.send_keys('Sunglasses')


# In[43]:


button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
button.click()


# In[47]:


start=0

end=3
brand=[]
price=[]
desc=[]
n=1
for page in range(start,end):

    brands=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    desc_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')

    for i in brands:
        if(n<=100):
            brand.append(i.text)
            n+=1
        else:
            break

        
        
len(brand)        


# In[50]:


start=0

end=3

desc=[]
n=1
for page in range(start,end):

   
    desc_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
   

    for i in desc_tags:
        if(n<=100):
            desc.append(i.text)
            n+=1
        else:
            break

        
        
len(desc)        


# In[49]:


start=0

end=3

price=[]

n=1
for page in range(start,end):

    
    price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')

    for i in price_tags:
        if(n<=100):
            price.append(i.text)
            n+=1
        else:
            break

        
        
len(price)        


# In[94]:


len(name)


# In[ ]:





# In[ ]:


#Question 5


# In[51]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[52]:


driver.get('https://www.flipkart.com/apple-iphone-11-black-128-gb/p/itm8244e8d955aba?pid=MOBFWQ6BKRYBP5X8&lid=LSTMOBFWQ6BKRYBP5X8IBG6BS&marketplace=FLIPKART&q=iphone11&store=tyy%2F4io&srno=s_1_3&otracker=search&otracker1=search&fm=organic&iid=aa96cc0c-b96c-46f3-958b-f2ce060fb957.MOBFWQ6BKRYBP5X8.SEARCH&ppt=hp&ppn=homepage&ssid=vfzeqgc7cw0000001683352837906&qH=d6db477051465f9a')


# In[53]:


click=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[7]/div/a/div')
click.click()


# In[56]:


start=0

end=10

review=[]
n=1
for page in range(start,end):

   
    review_tags=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
   

    for i in review_tags:
        if(n<=100):
            review.append(i.text)
            n+=1
        else:
            break

        
        
review        


# In[58]:


start=0

end=10

freview=[]
n=1
for page in range(start,end):

   
    freview_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
   

    for i in freview_tags:
        if(n<=100):
            freview.append(i.text)
            n+=1
        else:
            break

        
        
len(freview)        


# In[59]:


start=0

end=10

rating=[]
n=1
for page in range(start,end):

   
    rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
   

    for i in rating_tags:
        if(n<=100):
            rating.append(i.text)
            n+=1
        else:
            break

        
        
len(rating)        


# In[ ]:





# In[ ]:


#Question 6


# In[78]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[79]:


driver.get('http://www.flipkart.com/')


# In[80]:


product=driver.find_element(By.CLASS_NAME,'_3704LK')
product.send_keys('Sneakers')


# In[81]:


button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
button.click()


# In[84]:


name=[]
n=1
while(n<=100):
    tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in tags:
        if(n<=100):
            name.append(i.text)
            n+=1
        else:
            break
    else:
        next=driver.find_element(By.CLASS_NAME,'_1LKTO3')
        next.click
        continue
name


# In[85]:


len(name)


# In[86]:


des=[]
n=1
while(n<=100):
    tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in tags:
        if(n<=100):
            n+=1
            des.append(i.text)
        else:
            break
    else:
        next=driver.find_element(By.CLASS_NAME,'_1LKTO3')
        next.click
        continue
len(des)      


# In[87]:


price=[]
n=1
while(n<=100):
    tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in tags:
        if(n<=100):
            n+=1
            price.append(i.text)
        else:
            break
            
    else:
        next=driver.find_element(By.CLASS_NAME,'_1LKTO3')
        next.click
        continue
        
len(price)        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Question 7


# In[ ]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[ ]:


driver.get('https://www.amazon.in/')


# In[ ]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys('Laptop')


# In[ ]:


button=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div')
button.click()


# In[ ]:


cpu=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/span[12]/li/span/a/span').click()


# In[ ]:


title=[]
title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags[0:10]:
    title.append(i.text)
    
title    


# In[ ]:


len(title)


# In[ ]:


ratings=[]
rat_tags=driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]')
for i in rat_tags:
    ratings.append(i.text)
    
    
ratings


# In[ ]:


len(ratings)


# In[ ]:


price=[]
price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags[0:10]:
    price.append(i.text)
    
    
price    


# In[ ]:





# In[ ]:





# In[ ]:


#Question 8


# In[4]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[5]:


driver.get('https://www.azquotes.com/')


# In[6]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a').click()


# In[ ]:


quote=[]
tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tags[0:1000]:
    quote.append(i.text)
quote   


# In[ ]:


len(quote)


# In[7]:


quote=[]
n=1
while(n<=1000):
    tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in tags:
        n+=1
        quote.append(i.text)
    else:
        next=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
        next.click()
        continue


# In[8]:


len(quote)


# In[9]:


author=[]
n=1
while(n<=1000):
    tags=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in tags:
        n+=1
        author.append(i.text)
    else:
        next=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
        next.click()
        continue
        


# In[10]:


len(author)


# In[16]:



typ=[]
n=1
while(n<=1000):
    tags=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in tags:
        n+=1
        typ.append(i.text)
        
    else:
        next=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
        next.click()
        continue
        


# In[17]:


len(typ)


# In[ ]:





# In[ ]:


#Question 9


# In[2]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[3]:


driver.get('https://www.jagranjosh.com/')


# In[4]:


gk=driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[3]/a')
gk.click()


# In[5]:


search=driver.find_element(By.CLASS_NAME,'search_expend')
search.click()


# In[6]:


lis=driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div[4]/div/div/div/form/div[2]/div/input[1]')
lis.send_keys('Prime Ministers of India')


# In[7]:


search=driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div[4]/div/div/div/form/div[2]/div/input[2]')
search.click()


# In[8]:


click=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[2]/h2/a')
click.click()


# In[12]:


while(True):
    row=driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr')
    for rows in row[1:]:
        print(driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[2].text')," ")
        print(driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[3].text')," ")
        print(driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[4].text')," ")
        print("\n")
    else:
        break
        


# In[16]:


table=driver.find_element(By.CLASS_NAME,'table-box')
rows=table.find_elements(By.TAG_NAME,'tr')
data=[]
for row in rows:
    cells=row.find_elements(By.TAG_NAME,'td')
    row_data=[]
    for cell in cells[2:]:
        row_data.append(cell.text)
        print(cell.text,"\n")
    data.append(row_data)
   


# In[ ]:





# In[ ]:


#Question 10


# In[9]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[10]:


driver.get('https://www.motor1.com/')


# In[18]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[3]/div/div/div/form/input')
search.send_keys('Most expensive 50 cars')


# In[19]:


click=driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
click.click()


# In[20]:


s=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a')
s.click()


# In[37]:


car_name=[]
tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in tags[0:50]:
    car_name.append(i.text)
    
    


# In[39]:


car_name


# In[40]:


len(car_name)


# In[44]:


price=[]
tag=driver.find_elements(By.TAG_NAME,'strong')
for i in tag[0:50]:
    price.append(i.text)
    
price    


# In[45]:


df=pd.DataFrame(columns=['Car Name','Price'])
df['Car Name']=car_name
df['Price']=price
df


# In[ ]:




