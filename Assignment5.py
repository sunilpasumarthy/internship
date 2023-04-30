#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#QUESTION 1
wiki=requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup=BeautifulSoup(wiki.content)


# In[8]:


h=[]
for i in soup.find_all('span',class_='mw-headline'):
    h.append(i.text)
h=pd.DataFrame(h)

h


# In[29]:


#QUESTION 2
imdb=requests.get('https://www.imdb.com/list/ls055386972/')
soup=BeautifulSoup(imdb.content,'html.parser')


# In[30]:


name=[]
for i in soup.find_all('h3',class_='lister-item-header'):
    for b in i.find_all('a'):
        name.append(b.text)
name   
imdb_movies=pd.DataFrame(name,columns=["Name"])
imdb_movies


# In[31]:


rating=[]
for i in soup.find_all('div',class_='ipl-rating-star small'):
    for a in i.find_all('span',class_='ipl-rating-star__rating'):
        rating.append(a.text)
rating    
imdb_movies['Rating']=rating
imdb_movies
            


# In[35]:


year=[]
for i in soup.find_all('span',class_='lister-item-year text-muted unbold'):
   
    year.append(i.text.strip(')'))

year   
imdb_movies['Year']=year
imdb_movies


# In[ ]:


#Question 9


# In[36]:


page=requests.get('https://www.dineout.co.in/hyderabad-restaurants/welcome-back')


# In[37]:


soup=BeautifulSoup(page.content,'html.parser')


# In[38]:


import pandas as pd


# In[39]:


#name of the restaurant
name=[]
for i in soup.find_all('a',class_='restnt-name ellipsis'):
    name.append(i.text)
name=pd.DataFrame(name)
name


# In[40]:


#location
loc=[]
for i in soup.find_all('div',class_='restnt-loc ellipsis'):
    loc.append(i.text)
loc=pd.DataFrame(loc)    
loc


# In[42]:


#Ratings
rating=[]
for i in soup.find_all('div',class_=['restnt-rating rating-4','restnt-rating rating-3','restnt-rating rating-5']):
    rating.append(i.text)
rating=pd.DataFrame(rating)
rating


# In[43]:


cuisine=[]
for i in soup.find_all('div',class_='collapse filter-options-wrap in'):
    for j in i.find_all('li'):
        cuisine.append(j.text)
cuisine        


# In[55]:


url=[]
img_url=[]
url=soup.find_all('img',class_='no-img')
for a in url:
    img_url.append(a['data-src'])
img_url=pd.DataFrame(img_url,columns=['URL'])
img_url


# In[56]:


#Question 8
req=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup=BeautifulSoup(req.content)

name=[]
for i in soup.find_all('h2',class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg'):
    name.append(i.text)
paper=pd.DataFrame(name,columns=['Name'])
paper


# In[57]:


author=[]
for i in soup.find_all('span',class_='sc-1w3fpd7-0 dnCnAO'):
    author.append(i.text)
paper['Author']=author
paper


# In[58]:


date=[]
for i in soup.find_all('span',class_='sc-1thf9ly-2 dvggWt'):
    date.append(i.text)
paper['Published Date']=date
paper


# In[78]:


url=[]
l=[]
l=soup.find_all('li',class_='sc-9zxyh7-1 sc-9zxyh7-2 kOEIEO hvoVxs')
for i in l:
    for j in i.find_all('a'):
        print(j['href'])
        url.append(j['href'])

paper['URL']=url
paper
    


# In[79]:


#Question 7
req=requests.get('https://www.cnbc.com/world/?region=world')
soup=BeautifulSoup(req.content)


# In[80]:


head=[]
for i in soup.find_all('a',class_='LatestNews-headline'):
    head.append(i.text)
News=pd.DataFrame(head,columns=['Head Line'])
News


# In[82]:


time=[]
for i in soup.find_all('span',class_='LatestNews-wrapper'):
    time.append(i.text)
News['Time']=time 
News


# In[96]:



url=[]
for i in soup.find_all('a',class_='LatestNews-headline'):
    url.append(i['href'])
News['Link']=url
News


# In[100]:


#Question 4
req=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
soup=BeautifulSoup(req.content)


# In[101]:


name=[]
for i in soup.find_all('div',class_='presidentListing'):
    for a in i.find_all('h3'):
        name.append(a.text)
name 
presidents=pd.DataFrame()
presidents['name']=name
presidents


# In[114]:


term=[]
for i in soup.find_all('div',class_="presidentListing"):

    term.append(i.get_text().strip("\n").split("\n")[1])
presidents['Term_of_service']=term
presidents


# In[115]:


#Question 5
req=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup=BeautifulSoup(req.content)


# In[72]:


import numpy as np


# In[83]:


df=pd.DataFrame(columns=["Name",'Matches','Points','Rating'])
df
df1=pd.DataFrame(columns=["Name",'Matches','Points','Rating'])
df1


# In[84]:


team=soup.find('span',class_='u-hide-phablet')
print(team.text)
team=team.text


# In[85]:


matches=soup.find('td',class_='rankings-block__banner--matches')
print(matches.text)
matches=matches.text


# In[86]:


points=soup.find('td',class_='rankings-block__banner--points')
points.text
points=points.text
points


# In[87]:


rating=soup.find('td',class_='rankings-block__banner--rating u-text-right')
rating=(rating.text.strip('\n').split('\n'))[0]

rating


# In[88]:


df=df.append({'Name':team,'Matches':matches,'Points':points,'Rating':rating},ignore_index=True)
df


# In[89]:


name=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__team'):
    for j in i.find_all('span',class_='u-hide-phablet'):
        name.append(j.text)
        
name
df1["Name"]=name
df1


# In[93]:


matches=[]
points=[]
for i in soup.find_all('tr',class_='table-body'):
    j=i.find_all('td',class_='table-body__cell u-center-text')
    if(j!=[]):
        
        matches.append(j[0].text)
        points.append(j[1].text)
        
df1["Matches"]=matches
df1['Points']=points
df1


# In[95]:


df=pd.concat([df,df1])
df


# In[116]:


#Batsmen
req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)


# In[117]:


df=pd.DataFrame(columns=["Team",'Rating'])
df
df1=pd.DataFrame(columns=["Team",'Rating'])
df1


# In[119]:


team=soup.find('div',class_='rankings-block__banner--name-large')
team=team.text.strip('[')
rating=soup.find('div',class_='rankings-block__banner--rating')
rating=rating.text.strip('[')


# In[120]:


df=df.append({'Team':team,'Rating':rating},ignore_index=True)
df


# In[121]:


name=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    name.append(i.text.strip('\n'))
name 
rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
    rating.append(i.text)
rating    
df1['Rating']=rating
df1['Team']=name
df1


# In[ ]:





# In[122]:


df=pd.concat([df,df1])
df


# In[ ]:





# In[ ]:





# In[133]:


#All_rounder
req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-rounder')
soup=BeautifulSoup(req.content)


# In[134]:


df=pd.DataFrame(columns=['Team','Rating'])
df1=pd.DataFrame(columns=['Team','Rating'])


# In[135]:


team=soup.find('div',class_='rankings-block__banner--name-large')
print(team.text.strip('['))
team=team.text.strip('[')
rating=soup.find('div',class_='rankings-block__banner--rating')
print(rating.text.strip('['))
rating=rating.text.strip('[')


# In[136]:


df=df.append({'Team':team,'Rating':rating},ignore_index=True)
df


# In[137]:


team=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    team.append(i.text.strip('\n'))
team 
rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
    rating.append(i.text)
rating    
df1['Rating']=rating
df1['Team']=team
df1


# In[138]:


df=pd.concat([df,df1])
df


# In[139]:


#Question 6
req=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup=BeautifulSoup(req.content)


# In[178]:


df=pd.DataFrame(columns=['Team','Matches','Points','Rating'])
df1=pd.DataFrame(columns=['Team','Matches','Points','Rating'])


# In[179]:


team=soup.find('span',class_='u-hide-phablet')
team=team.text
print(team)


# In[180]:


points=soup.find('td',class_='rankings-block__banner--points')
points=points.text.strip('\n')
print(points)
matches=soup.find('td',class_='rankings-block__banner--matches')
matches=matches.text
print(matches)
rating=soup.find('td',class_='rankings-block__banner--rating u-text-right')
rating=rating.text.strip('\n')
print(rating)


# In[181]:


df=df.append({'Team':team,'Matches':matches,'Points':points,'Rating':rating},ignore_index=True)
df


# In[182]:


team=[]
for i in soup.find_all('span',class_='u-hide-phablet')[1:]:
    team.append(i.text)
team
df1['Team']=team
df1


# In[183]:


matches=[]
points=[]
for i in soup.find_all('tr',class_='table-body'):
    j=i.find_all('td',class_='table-body__cell u-center-text')
    if(j!=[]):
        
        matches.append(j[0].text)
        points.append(j[1].text)
        
df1["Matches"]=matches
df1['Points']=points
df1


# In[185]:


rating=[]
for i in soup.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text)
df1['Rating']=rating    
df1


# In[186]:


df=pd.concat([df,df1])
df


# In[149]:


#Batting
req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)


# In[150]:


df=pd.DataFrame(columns=['Team','Rating'])
df1=pd.DataFrame(columns=['Team','Rating'])


# In[151]:


team=soup.find('div',class_='rankings-block__banner--name-large')
team=team.text
team


# In[152]:


rating=soup.find('div',class_='rankings-block__banner--rating')
rating=rating.text
rating


# In[154]:


team=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    team.append(i.text.strip('\n'))
df1['Team']=team    
df1


# In[155]:


rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
    rating.append(i.text)
df1['Rating']=rating    
df1


# In[156]:


df=pd.concat([df,df1])
df


# In[327]:


#All_rounder
req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling')
soup=BeautifulSoup(req.content)


# In[157]:


df=pd.DataFrame(columns=['Team','Rating'])
df1=pd.DataFrame(columns=['Team','Rating'])


# In[158]:


team=soup.find('div',class_='rankings-block__banner--name-large')
team=team.text
print(team)
rating=soup.find('div',class_='rankings-block__banner--rating')
rating=rating.text
print(rating)


# In[159]:


df=df.append({'Team':team,'Rating':rating},ignore_index=True)
df


# In[160]:


team=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    team.append(i.text.strip('\n'))
df1['Team']=team    
df1


# In[161]:


rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
    rating.append(i.text)
df1['Rating']=rating    
df1


# In[162]:


df=pd.concat([df,df1])
df


# In[ ]:




