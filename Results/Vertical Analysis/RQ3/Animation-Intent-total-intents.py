import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')

target1 = data["Unnamed: 14"]
target2 = data["Unnamed: 15"]
target3 = data["Unnamed: 16"]

NbUND = 0
NbDEBUG = 0
NbEDUCATE=0
for i in range(len(target1)):
    if (target1[i]=="DEBUG"): 
        NbDEBUG  += 1   
    if (target1[i]=="UNDERSTAND"): 
        NbUND+= 1
    if (target1[i]=="EDUCATE"): 
        NbEDUCATE+= 1
      
for i in range(len(target2)):
    if (target2[i]=="DEBUG"): 
        NbDEBUG  += 1   
    if (target2[i]=="UNDERSTAND"): 
        NbUND+= 1
    if (target2[i]=="EDUCATE"): 
        NbEDUCATE+= 1
        
for i in range(len(target3)):
    if (target3[i]=="DEBUG"): 
        NbDEBUG  += 1   
    if (target3[i]=="UNDERSTAND"): 
        NbUND+= 1
    if (target3[i]=="EDUCATE"): 
        NbEDUCATE+= 1
        
print(NbUND)
print(NbDEBUG)
print(NbEDUCATE)

TotalPub=NbUND+ NbDEBUG+NbEDUCATE

rateUND= NbUND/TotalPub*100
rateDEBUG= NbDEBUG/TotalPub*100
rateEDUCATE= NbEDUCATE/TotalPub*100

print(rateUND)
print(rateDEBUG)

print(rateEDUCATE)


#Distribution = [57.75,38.03,4.23]
Distribution = [rateDEBUG,rateUND,rateEDUCATE]

Distribution = [NbDEBUG,NbUND,NbEDUCATE]
#Venue= data["Venue Type"]
#freq1 = data.groupby(['Venue Type']).count() 
#print(freq1)

#freq2 = data.groupby(['Venue Type', 'Year']).size() 
#print(freq2)


my_labels = 'DEBUG', 'UNDERSTAND', 'EDUCATE'


my_colors = ['silver','lightblue','#9f6dd1']

#purple', 'black', 'pink', 'aqua'

my_explode = (0, 0, 0)
plt.pie(Distribution, labels=my_labels, autopct='%1.1f%%', startangle=180 ,  textprops={'fontsize': 22}, colors=my_colors,explode=my_explode, wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="",edgecolor="black")

import pylab as plot
params = {'legend.fontsize': 18,
          'legend.handlelength': 2}
plot.rcParams.update(params)


plt.savefig("Animation-intent-Total.pdf",dpi=600)
plt.show()