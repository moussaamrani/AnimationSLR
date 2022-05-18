import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import gridspec
from matplotlib.pyplot import figure


data = pd.read_csv('CORPUS-Final.csv')

# Arrays with categorical variables
Dynamicity = ['ONLINE', 'OFFLINE']
animIntent = ['DEBUG',  'UNDERSTAND', 'EDUCATE']
MTLtype = ['GBT','MP','GPPL','GPML','LOGIC','ALGEBRAIC']


ONLINEIntent = [0,0,0,0,0,0]
OFFLINEIntent = [0, 0,0,0,0,0]

DebuggingMTL = [0,0,0,0,0,0]
UnderstandingMTL = [0, 0,0,0,0,0]
EducationalMTL = [0, 0,0,0,0,0]



#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'

#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'

#data = pd.read_excel(url,sheet_name=sheet_name)

target1 = data["MTL Type"]
target2 = data["Unnamed: 15"]
target3 = data["Dynamicity"]

target4 = data["Unnamed: 14"]
target5 = data["Unnamed: 16"]


for i in range(len(target3)):
    if (target3[i]=="ONLINE"): 
        for j in range(len(MTLtype)):
            if (MTLtype[j]==target1[i]): 
                ONLINEIntent[j] += 1 
    if (target3[i]=="OFFLINE"): 
        for j in range(len(MTLtype)):
            if (MTLtype[j]==target1[i]): 
                OFFLINEIntent[j] += 1 



for i in range(len(target2)):
    if (target2[i]=="DEBUG" or  target4[i]=="DEBUG" or target5[i]=="DEBUG"): 
        for j in range(len(MTLtype)):
            if (MTLtype[j]==target1[i]): 
                DebuggingMTL[j] += 1 
    if (target2[i]=="UNDERSTAND" or  target4[i]=="UNDERSTAND" or target5[i]=="UNDERSTAND"): 
        for j in range(len(MTLtype)):
            if (MTLtype[j]==target1[i]): 
                UnderstandingMTL[j] += 1 
    if (target2[i]=="EDUCATE" or  target4[i]=="EDUCATE" or target5[i]=="EDUCATE"): 
        for j in range(len(MTLtype)):
            if (MTLtype[j]==target1[i]): 
                EducationalMTL[j] += 1 
                




# Values of map Dynamicity
Dynamicity_count = [ONLINEIntent, OFFLINEIntent]
print(sum(ONLINEIntent)+ sum(OFFLINEIntent))
animIntent_count = [DebuggingMTL, UnderstandingMTL, EducationalMTL]

# Places values in a DataFrame and intersects with its variable
df1 = pd.DataFrame(Dynamicity_count, columns=MTLtype, index=Dynamicity)
df2 = pd.DataFrame(animIntent_count, columns=MTLtype, index=animIntent)

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

a1.margins(.3)

dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")

# Set bubbles size of the second plot
dfu["S"] *= 400

# Set the bubbles of first plot
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w',linestyle = 'solid', edgecolors='#000000', linewidth=2)
# a2.scatter(x="X", y="Y", s="S", data=dfu, color='lavender',linestyle = 'solid', edgecolors='#041208', linewidth=1.4, alpha=0.5)

a2.margins(.3)

# Match the value with the bubbles of the first plot
for i in range(len(Dynamicity)):
    for j in range(len(MTLtype)):
        # Verify if there is a number 0 and change for a blank value
        s = int(Dynamicity_count[i][j]) if Dynamicity_count[i][j] != 0 else " "
        # Set the bubble value
        a1.annotate(s=s, xy=(MTLtype[j], Dynamicity[i]), ha='center', va='center', color='black', size=20)

# Match the value with the bubbles of the second plot
for i in range(len(animIntent)):
    for j in range(len(MTLtype)):
        s = int(animIntent_count[i][j]) if animIntent_count[i][j] != 0 else " "
        a2.annotate(s=s, xy=(MTLtype[j], animIntent[i]), ha='center', va='center', color='black', size=22)
        
# Set the plot labels
a1.set_ylabel('Dynamicity', size=16, labelpad=20,weight="bold")
a2.set_ylabel('Animation Intent', size=16, labelpad=20,weight="bold")
a1.tick_params(labelsize=18.0)
a2.tick_params(labelsize=18.0)


a1.set_xlabel('', size=20, labelpad=20)
a2.set_xlabel('MTL Type', size=18, labelpad=20,weight="bold")


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
fig.savefig('MTL-Type-Dynamicity-MA-Intents.pdf', dpi=200)