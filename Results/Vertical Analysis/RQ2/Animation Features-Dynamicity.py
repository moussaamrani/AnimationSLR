import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'

#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'

#data = pd.read_excel(url,sheet_name=sheet_name)

data = pd.read_csv('CORPUS-Final.csv')

target = data["Dynamicity"]

nbOffline = 0
NbOnline = 0
for i in range(len(target)):
    if (target[i]=="ONLINE"): 
        NbOnline  += 1   
    if (target[i]=="OFFLINE"): 
        nbOffline+= 1

        
        
print(nbOffline)
print(NbOnline)

TotalPub=nbOffline+ NbOnline

rateOffline= nbOffline/TotalPub*100
rateOnline= NbOnline/TotalPub*100

print(rateOffline)
print(rateOnline)

Tasks = [rateOffline,rateOnline]


my_labels = 'Offline','Online'




my_colors = ['silver','lightblue']


my_explode = (0, 0)
plt.pie(Tasks, labels=my_labels, autopct='%1.1f%%', textprops={'fontsize': 20}, startangle=180, colors=my_colors,explode=my_explode, wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


plt.title('Animation Features: Dynamicity')
plt.title('')
plt.axis('equal')

plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="Dynamicity")


plt.savefig("Animation Features-Dynamicity.pdf",dpi=600)
plt.show()