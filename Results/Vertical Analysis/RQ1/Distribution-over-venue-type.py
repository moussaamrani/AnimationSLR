import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')

target = data["Venue Type"]

NbConf = 0
NbWSHOP = 0
NbWJOUR = 0
for i in range(len(target)):
    if (target[i]=="CONF"): 
        NbConf += 1   
    if (target[i]=="WSHOP"): 
        NbWSHOP += 1
    if (target[i]=="JOUR"): 
        NbWJOUR += 1
        
        
        
print(NbWSHOP)
print(NbWJOUR)

TotalPub=NbConf+ NbWJOUR+ NbWSHOP

rateCONF= NbConf/TotalPub*100
rateWSHOP= NbWSHOP/TotalPub*100
rateJOUR= NbWJOUR/TotalPub*100
Tasks = [rateCONF,rateWSHOP,rateJOUR]

print(rateCONF)
print(rateWSHOP)
print(rateJOUR)
print(rateWSHOP+rateCONF+rateJOUR)

my_labels = 'Conference','Workshop','Journal'




my_colors = ['#ea8b3e','#8b3eea','#ffcc00']

#purple', 'black', 'pink', 'aqua'

my_explode = (0, 0, 0)
plt.pie(Tasks, labels=my_labels,  textprops={'fontsize': 18}, autopct='%1.1f%%', startangle=180, colors=my_colors,explode=my_explode, wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})


# ax.pie(frac, colors=colors ,labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14})

# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')




plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="Pub. Venue")


plt.savefig("Distribution-over-venue-type.pdf",dpi=600)
plt.show()

######################## = Venue  