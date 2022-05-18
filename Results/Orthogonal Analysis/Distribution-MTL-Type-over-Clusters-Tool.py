import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import gridspec
from matplotlib.pyplot import figure


data = pd.read_csv('CORPUS-Final.csv')


# Arrays with categorical variables

MTLtype =  ['GBT','MP','GPPL','GPML','LOGIC','ALGEBRAIC']
level = ['','','','','','','','']
MTLCluster =['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER'] 



#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'

#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'

#data = pd.read_excel(url,sheet_name=sheet_name)



GBT = [0,0,3,0,3,0,2,0,2,1]
MP = [0, 6,0,0,0,0,0,0,0,2]
GPPL = [2, 1,2,0,0,0,0,0,0,0]
GPML = [0,0,0,2,0,3,0,3,0,4]
LOGIC = [0, 0,0,2,0,0,0,0,0,3]
ALGEBRAIC = [0, 0,0,0,0,0,0,0,0,1]

FSM = [0, 0,0,0,0,0,0,0,0,0]
REWRITE = [0, 0,0,0,0,0,0,0,0,0]
KERMETA = [0, 0,0,0,0,0,0,0,0,0]
PN = [0, 0,0,0,0,0,0,0,0,0]
XTENDJAVA = [0, 0,0,0,0,0,0,0,0,0]
B = [0, 0,0,0,0,0,0,0,0,0]
VARIOUS = [0, 0,0,0,0,0,0,0,0,0]
OTHER = [0, 0,0,0,0,0,0,0,0,0]
       
# Values of map MTLtype
MTLtype_count = [GBT,MP,GPPL,GPML,LOGIC,ALGEBRAIC]

level_count = [FSM,REWRITE,KERMETA,PN,XTENDJAVA,B,VARIOUS,OTHER ]



# Places values in a DataFrame and intersects with its variable
df1 = pd.DataFrame(MTLtype_count, columns=MTLCluster, index=MTLtype)
df2 = pd.DataFrame(level_count, columns=MTLCluster, index=level)

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
for i in range(len(level)):
    for j in range(len(MTLCluster)):
        s = int(level_count[i][j]) if level_count[i][j] != 0 else " "
        a2.annotate(s=s, xy=(MTLCluster[j], level[i]), ha='center', va='center', color='black', size=22)
        
# Set the plot labels
a1.set_ylabel('MTL Type', size=16, labelpad=20,weight="bold", color="black")
a2.set_ylabel('', size=16, labelpad=20,weight="bold",color="black")
a1.tick_params(labelsize=12.0, color="black",rotation=0)
a2.tick_params(labelsize=12.0, color="black",rotation=30)


a1.set_xlabel('', size=20, labelpad=20,color='black')
a2.set_xlabel('TOOL Cluster', size=18, labelpad=20,weight="bold",color='black')


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
fig.savefig('MTL-Type-Clusters-Tool.pdf', dpi=200, transparent=True)

print(sum(GBT)+sum(MP)+sum(GPPL)+sum(GPML)+sum(LOGIC)+sum(ALGEBRAIC))
