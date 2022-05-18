import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')

target = data["Unnamed: 12"]

TOPCASED= 0
GEMOC= 0
ATOMPM= 0
MEEDUSE= 0
VMTS= 0
RMT= 0
DiaMeta= 0
TROPIC= 0
GenGED= 0
OTHER= 0


for i in range(len(target)):
    if (target[i]=="TOPCASED"): 
        TOPCASED   += 1   
    if (target[i]=="GEMOC"): 
        GEMOC += 1 
    if (target[i]=="ATOMPM"): 
        ATOMPM += 1 
    if (target[i]=="MEEDUSE"): 
        MEEDUSE += 1 
    if (target[i]=="VMTS"): 
        VMTS += 1 
    if (target[i]=="RMT"): 
        RMT += 1 
    if (target[i]=="DiaMeta"): 
        DiaMeta += 1 
    if (target[i]=="TROPIC"): 
        TROPIC += 1 
    if (target[i]=="GenGED"): 
        GenGED += 1 
    if (target[i]=="OTHER"): 
        OTHER += 1  

print("------------")

        
#TOPCASED= 2
#GEMOC= 7
#ATOMPM= 5
#MEEDUSE= 4
#VMTS= 3
#RMT= 3
#DiaMeta= 2
#TROPIC= 3
#GenGED= 2
#OTHER= 11

Total= GEMOC+ ATOMPM+ MEEDUSE+ VMTS+ RMT+ DiaMeta+ TROPIC+ GenGED+ OTHER+TOPCASED
print(Total)
r1= TOPCASED/Total*100
r2= GEMOC/Total*100
r3= ATOMPM/Total*100
r4= MEEDUSE/Total*100
r5= VMTS/Total*100
r6= RMT/Total*100
r7= DiaMeta/Total*100
r8= TROPIC/Total*100
r9= GenGED/Total*100
r10= OTHER/Total*100




Ratio = [r1, r2,r3,r4,r5,r6,r7,r8,r9,r10]

print(Ratio)

print(sum(Ratio))



my_labels = 'TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER'




my_colors =  ['#ccda62','#e69191','#ffb84d','lavender','#bdff00','#ffec52','#f8e5d8','#43bccd','olive','peru']

#purple', 'black', 'pink', 'aqua'

my_explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
plt.pie(Ratio, labels=my_labels, autopct='%1.1f%%', startangle=180, colors=my_colors,explode=my_explode,  textprops={'fontsize': 14},wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="MTL Cluster")


plt.savefig("Distribution-Clusters-Tools.pdf",dpi=600)
plt.show()