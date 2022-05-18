import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')


target = data["Animation Type"]

NbOffline = 0
NbOnline = 0
for i in range(len(target)):
    if (target[i]=="CUSTOM"): 
        NbOnline  += 1   
    if (target[i]=="PREDEF"): 
        NbOffline+= 1

        
        
print(NbOffline)
print(NbOnline)

TotalPub=NbOffline+ NbOnline

rateOffline= NbOffline/TotalPub
rateOnline= NbOnline/TotalPub

print(rateOffline)
print(rateOnline)

Tasks = [rateOnline,rateOffline]




my_labels = 'CUSTOM ', 'PREDEF'



my_colors = ['silver','lightblue']

#purple', 'black', 'pink', 'aqua'

my_explode = (0, 0)
plt.pie(Tasks, labels=my_labels, autopct='%1.1f%%', startangle=180, textprops={'fontsize': 25},colors=my_colors,explode=my_explode, wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="MA Type")


plt.savefig("Animation Features-MA-Type.pdf",dpi=600)
plt.show()