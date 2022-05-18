import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')


Venue= data["Venue Type"]
freq1 = data.groupby(['Venue Type']).count() 
print(freq1)

freq2 = data.groupby(['Dynamicity', 'Year']).size() 
print(freq2)





my_labels = 'Academic','Industrial'



data = pd.read_csv('CORPUS-Final.csv')




Venue= data["Venue Type"]
freq1 = data.groupby(['Venue Type']).count() 
print(freq1)

freq2 = data.groupby(['Dynamicity', 'Year']).size() 
print(freq2)


data = pd.read_csv('CORPUS-Final.csv')

target = data["Orientation"]

Nboffline = 0
Nbonline = 0
for i in range(len(target)):
    if (target[i]=="ACA"): 
        Nbonline  += 1   
    if (target[i]=="INDUS"): 
        Nboffline+= 1

        
        
print(Nboffline)
print(Nbonline)

TotalPub=Nboffline+ Nbonline

rateoffline= Nboffline/TotalPub*100
rateonline= Nbonline/TotalPub*100

print(rateoffline)
print(rateonline)

Tasks = [rateonline,rateoffline]


my_colors = ['lightblue','silver']

      #       'lightblue','lightsteelblue','silver'
#purple', 'black', 'pink', 'aqua'

my_explode = (0, 0.0)
plt.pie(Tasks, labels=my_labels,  textprops={'fontsize': 25}, autopct='%1.1f%%', startangle=180, colors=my_colors,explode=my_explode, wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="Orientation")


plt.savefig("Distribution-over-Orientation.pdf",dpi=600)
plt.show()