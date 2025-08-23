import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("===============-------------------===============")
data = pd.read_csv('CORPUS-Final.csv')

# Arrays with categorical variables
Dynamicity = ['ONLINE', 'OFFLINE']
animIntent = ['DEBUG', 'UNDERSTAND', 'EDUCATE']
MTLtype = ['GBT','MP','GPPL','GPML','LOGIC','ALGEBRAIC','META']  # Added META

# Initialize arrays with zeros (7 elements now for META)
ONLINEIntent = [0]*len(MTLtype)
OFFLINEIntent = [0]*len(MTLtype)

DebuggingMTL = [0]*len(MTLtype)
UnderstandingMTL = [0]*len(MTLtype)
EducationalMTL = [0]*len(MTLtype)

# Targets from data
target1 = data["MTL Type"]
target2 = data["Unnamed: 15"]
target3 = data["Dynamicity"]
target4 = data["Unnamed: 14"]
target5 = data["Unnamed: 16"]

# Count Dynamicity
for i in range(len(target3)):
    if target3[i] == "ONLINE": 
        for j in range(len(MTLtype)):
            if MTLtype[j] == target1[i]: 
                ONLINEIntent[j] += 1 
    if target3[i] == "OFFLINE": 
        for j in range(len(MTLtype)):
            if MTLtype[j] == target1[i]: 
                OFFLINEIntent[j] += 1 

# Count Animation Intent
for i in range(len(target2)):
    for j in range(len(MTLtype)):
        if MTLtype[j] == target1[i]:
            if target2[i]=="DEBUG" or target4[i]=="DEBUG" or target5[i]=="DEBUG": 
                DebuggingMTL[j] += 1 
            if target2[i]=="UNDERSTAND" or target4[i]=="UNDERSTAND" or target5[i]=="UNDERSTAND": 
                UnderstandingMTL[j] += 1 
            if target2[i]=="EDUCATE" or target4[i]=="EDUCATE" or target5[i]=="EDUCATE": 
                EducationalMTL[j] += 1 

# Values of map Dynamicity and Animation Intent
Dynamicity_count = [ONLINEIntent, OFFLINEIntent]
animIntent_count = [DebuggingMTL, UnderstandingMTL, EducationalMTL]

# Create DataFrames
df1 = pd.DataFrame(Dynamicity_count, columns=MTLtype, index=Dynamicity)
df2 = pd.DataFrame(animIntent_count, columns=MTLtype, index=animIntent)

# Create figure and subplots
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(11,6.5))

# First plot - Dynamicity
dfu = df1.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 400
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', linestyle='solid', edgecolors='black', linewidth=2)
a1.margins(.3)

# Second plot - Animation Intent
dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 400
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w', linestyle='solid', edgecolors='#000000', linewidth=2)
a2.margins(.3)

# Annotate Dynamicity plot
for i in range(len(Dynamicity)):
    for j in range(len(MTLtype)):
        text = str(int(Dynamicity_count[i][j])) if Dynamicity_count[i][j] != 0 else " "
        a1.annotate(text=text, xy=(MTLtype[j], Dynamicity[i]), ha='center', va='center', color='black', size=20)

# Annotate Animation Intent plot
for i in range(len(animIntent)):
    for j in range(len(MTLtype)):
        text = str(int(animIntent_count[i][j])) if animIntent_count[i][j] != 0 else " "
        a2.annotate(text=text, xy=(MTLtype[j], animIntent[i]), ha='center', va='center', color='black', size=22)

# Set labels and grid
a1.set_ylabel('Dynamicity', size=16, labelpad=20, weight="bold")
a2.set_ylabel('Animation Intent', size=16, labelpad=20, weight="bold")
a1.tick_params(labelsize=18.0)
a2.tick_params(labelsize=18.0)

a1.set_xlabel('')
a2.set_xlabel('MTL Type', size=18, labelpad=20, weight="bold")
a1.set_axisbelow(True)
a2.set_axisbelow(True)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# Show and save figure
plt.tight_layout()
fig = plt.gcf()
plt.show()
fig.savefig('MTL-Type-Dynamicity-MA-Intents-META.pdf', dpi=200)

print("Total counts:", sum(ONLINEIntent)+sum(OFFLINEIntent))
