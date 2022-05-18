import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import gridspec
from matplotlib.pyplot import figure


data = pd.read_csv('CORPUS-Final.csv')

# Arrays with categorical variables

MTLtype =  ['GBT','MP','GPPL','GPML','LOGIC','ALGEBRAIC']

TOOLCluster = ['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER'] 
MTLCluster =['FSM','REWRITE','KERMETA','PN','XTEND/JAVA','B','VARIOUS','OTHER']

#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'

#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'

#data = pd.read_excel(url,sheet_name=sheet_name)





print(data.groupby(['MTL Type','CLUSTER']).count())

target1 = data["MTL Type"]

target2 = data["CLUSTER"]


print(target1)
MP = [0, 0,0,0,0,0,0,0]

GBT = [0,0,0,0,0,0,0,0]
GPPL = [0, 0,0,0,0,0,0,0]
GPML = [0,0,0,0,0,0,0,0]
LOGIC = [0, 0,0,0,0,0,0,0]
ALGEBRAIC = [0, 0,0,0,0,0,0,1]

for i in range(len(target1)):
    if (target1[i]=="GBT"):
        for j in range(len(MTLCluster)): 
            if (target2[i]==MTLCluster[j]): 
             GBT[j] += 1          
    if (target1[i]=="MP"):
        for j in range(len(MTLCluster)): 
            if (target2[i]==MTLCluster[j]): 
             MP[j] += 1  
    if (target1[i]=="GPPL"):
        for j in range(len(MTLCluster)): 
            if (target2[i]==MTLCluster[j]): 
             GPPL[j] += 1  
    if (target1[i]=="GPML"):
        for j in range(len(MTLCluster)): 
            if (target2[i]==MTLCluster[j]): 
             GPML[j] += 1 
    if (target1[i]=="LOGIC"):
        for j in range(len(MTLCluster)): 
            if (target2[i]==MTLCluster[j]): 
             LOGIC[j] += 1 
             print(i," ",target1[i],"-",target2[i], "-",MTLCluster[j])
              
    if (target1[i]=="ALGEBRAIC"):
        for j in range(len(MTLCluster)): 
            if (target2[i]==MTLCluster[j]): 
             ALGEBRAIC[j] += 1 
             print(i," ",target1[i],"-",target2[i], "-",MTLCluster[j])
                  
print("================================")
   

#GBT = [0,11,0,0,0,0,0,0]
#MP = [0, 0,5,0,0,0,1,2]
#GPPL = [0, 0,0,0,3,0,0,1]
#GPML = [3,0,0,7,0,1,1,0]
#LOGIC = [0, 0,0,0,0,6,0,0]
#ALGEBRAIC = [0, 0,0,0,0,0,0,1]
TOPCASED = [0, 0,0,0,0,0,0,0]
GEMOC = [0, 0,0,0,0,0,0,0]
ATOMPM = [0, 0,0,0,0,0,0,0]
MEEDUSE =[0, 0,0,0,0,0,0,0]
VMTS = [0, 0,0,0,0,0,0,0]
RMT =[0, 0,0,0,0,0,0,0]
DiaMeta = [0, 0,0,0,0,0,0,0]
TROPIC = [0, 0,0,0,0,0,0,0]
GenGED = [0, 0,0,0,0,0,0,0]
OTHER  = [0, 0,0,0,0,0,0,0]

         
# Values of map MTLtype
MTLtype_count = [GBT,MP,GPPL,GPML,LOGIC,ALGEBRAIC]

TOOLCluster_count = [TOPCASED,GEMOC,ATOMPM,MEEDUSE,VMTS,RMT,DiaMeta,TROPIC,GenGED,OTHER ]

# Places values in a DataFrame and intersects with its variable
df1 = pd.DataFrame(MTLtype_count, columns=MTLCluster, index=MTLtype)
df2 = pd.DataFrame(TOOLCluster_count, columns=MTLCluster, index=TOOLCluster)

# Create a figure and the subplots that will compose the Plot
# sharex argument shares the axis X
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(11,6.5))

plt.rcParams["figure.figsize"] = [11,6.5]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 3

dfu = df1.unstack().reset_index()
dfu.columns = list("XYS")

# Set bubbles size of the first plot
dfu["S"] *= 400

# Set the bubbles of first plot
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', linestyle = 'solid',edgecolors='black', linewidth=2)
#a1.scatter(x="X", y="Y", s="S", data=dfu, color='white', edgecolors='#8B008B', linestyle = 'dotted', linewidth=1.5, alpha=0.5)

a1.margins(.1)

dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")

# Set bubbles size of the second plot
dfu["S"] *= 400

# Set the bubbles of first plot
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w',linestyle = 'solid', edgecolors='#000000', linewidth=2)
# a2.scatter(x="X", y="Y", s="S", data=dfu, color='lavender',linestyle = 'solid', edgecolors='#041208', linewidth=1.4, alpha=0.5)

a2.margins(.1)

# Match the value with the bubbles of the first plot
for i in range(len(MTLtype)):
    for j in range(len(MTLCluster)):
        # Verify if there is a number 0 and change for a blank value
        s = int(MTLtype_count[i][j]) if MTLtype_count[i][j] != 0 else " "
        # Set the bubble value
        a1.annotate(s=s, xy=(MTLCluster[j], MTLtype[i]), ha='center', va='center', color='black', size=20)

# Match the value with the bubbles of the second plot
for i in range(len(TOOLCluster)):
    for j in range(len(MTLCluster)):
        s = int(TOOLCluster_count[i][j]) if TOOLCluster_count[i][j] != 0 else " "
        a2.annotate(s=s, xy=(MTLCluster[j], TOOLCluster[i]), ha='center', va='center', color='black', size=22)
        
# Set the plot labels
a1.set_ylabel('MTL Type ', size=16, labelpad=20,weight="bold", color="black")
a2.set_ylabel('MTL Cluster', size=16, labelpad=20,weight="bold",color="black")
a1.tick_params(labelsize=12.0, color="black")
a2.tick_params(labelsize=12.0, color="black",rotation=30)


a1.set_xlabel('', size=20, labelpad=20)
a2.set_xlabel('MTL Cluster', size=18, labelpad=20,weight="bold",color='black')


a1.set_axisbelow(True)
a2.set_axisbelow(True)
# Set the lines of grid. Can be: dashed, dotted
a1.grid(ls='dotted',color='black')
a2.grid(ls='dotted',color='black')


# Change shape with marker
#plt.scatter(x, y, s=z*4000, marker="D")



# Plot the graph and save it
plt.tight_layout()
fig = plt.gcf()

fig.set_size_inches(6.5, 7.5)


plt.show()
plt.draw()
fig.savefig('MTL-Type-over-Clusters-MTL.pdf', dpi=200)
print(sum(GBT)+sum(MP)+sum(GPPL)+sum(GPML)+sum(LOGIC)+sum(ALGEBRAIC))

