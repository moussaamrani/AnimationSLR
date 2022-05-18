import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import gridspec
from matplotlib.pyplot import figure


data = pd.read_csv('CORPUS-Final.csv')

# Arrays with categorical variables
Dynamicity = ['ONLINE', 'OFFLINE']
AnimIntent = ['Debugging', 'Understanding', 'Educational']
TOOLS = ['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER'] 


ONLINEMLLang = [0,0,0,0,0,0,0,0,0,0]
OFFLINEMLLang =[0,0,0,0,0,0,0,0,0,0]

DebuggingMLLang = [0,0,0,0,0,0,0,0,0,0]
UnderstandingMLLang = [0,0,0,0,0,0,0,0,0,0]
EducationalMLLang = [0,0,0,0,0,0,0,0,0,0]


data = pd.read_csv('CORPUS-Final.csv')
target1 = data["Unnamed: 12"]
target2 = data["Unnamed: 15"]
target3 = data["Dynamicity"]

target4 = data["Unnamed: 14"]
target5 = data["Unnamed: 16"]


for i in range(len(target3)):
    if (target3[i]=="ONLINE"): 
        for j in range(len(TOOLS)):
            if (TOOLS[j]==target1[i]): 
                ONLINEMLLang[j] += 1 
    if (target3[i]=="OFFLINE"): 
        for j in range(len(TOOLS)):
            if (TOOLS[j]==target1[i]): 
                OFFLINEMLLang[j] += 1 



for i in range(len(target2)):
    if (target2[i]=="DEBUG" or  target4[i]=="DEBUG" or target5[i]=="DEBUG"): 
        for j in range(len(TOOLS)):
            if (TOOLS[j]==target1[i]): 
                DebuggingMLLang[j] += 1 
    if (target2[i]=="UNDERSTAND" or  target4[i]=="UNDERSTAND" or target5[i]=="UNDERSTAND"): 
        for j in range(len(TOOLS)):
            if (TOOLS[j]==target1[i]): 
                UnderstandingMLLang[j] += 1 
    if (target2[i]=="EDUCATE" or  target4[i]=="EDUCATE" or target5[i]=="EDUCATE"): 
        for j in range(len(TOOLS)):
            if (TOOLS[j]==target1[i]): 
                EducationalMLLang[j] += 1 



# Values of map Dynamicity
Dynamicity_count = [ONLINEMLLang, OFFLINEMLLang]

print(sum(ONLINEMLLang)+ sum(OFFLINEMLLang))

AnimIntent_count = [DebuggingMLLang, UnderstandingMLLang, EducationalMLLang]

# Places values in a DataFrame and intersects with its variable
df1 = pd.DataFrame(Dynamicity_count, columns=TOOLS, index=Dynamicity)
df2 = pd.DataFrame(AnimIntent_count, columns=TOOLS, index=AnimIntent)

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
dfu["S"] *= 380

# Set the bubbles of first plot
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', linestyle = 'solid',edgecolors='black', linewidth=2)
#a1.scatter(x="X", y="Y", s="S", data=dfu, color='white', edgecolors='#8B008B', linestyle = 'dotted', linewidth=1.5, alpha=0.5)

a1.margins(.3)

dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")

# Set bubbles size of the second plot
dfu["S"] *= 380

# Set the bubbles of first plot
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w',linestyle = 'solid', edgecolors='#000000', linewidth=2)
# a2.scatter(x="X", y="Y", s="S", data=dfu, color='lavender',linestyle = 'solid', edgecolors='#041208', linewidth=1.4, alpha=0.5)

a2.margins(.3)

# Match the value with the bubbles of the first plot
for i in range(len(Dynamicity)):
    for j in range(len(TOOLS)):
        # Verify if there is a number 0 and change for a blank value
        s = int(Dynamicity_count[i][j]) if Dynamicity_count[i][j] != 0 else " "
        # Set the bubble value
        a1.annotate(s=s, xy=(TOOLS[j], Dynamicity[i]), ha='center', va='center', color='black', size=18)

# Match the value with the bubbles of the second plot
for i in range(len(AnimIntent)):
    for j in range(len(TOOLS)):
        s = int(AnimIntent_count[i][j]) if AnimIntent_count[i][j] != 0 else " "
        a2.annotate(s=s, xy=(TOOLS[j], AnimIntent[i]), ha='center', va='center', color='black', size=18)
        
# Set the plot labels
a1.set_ylabel('Dynamicity', size=16, labelpad=20,weight="bold")
a2.set_ylabel('Animation Intent', size=16, labelpad=20,weight="bold")
a1.tick_params(labelsize=18.0)
a2.tick_params(labelsize=12.0,rotation = 0)


a1.set_xlabel('', size=10, labelpad=20)
a2.set_xlabel('TOOLS', size=16, labelpad=20,weight="bold")


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
plt.show()
plt.draw()
fig.savefig('MTL-Clusters-over-Dynamicity-MA-Intents.pdf', dpi=200)