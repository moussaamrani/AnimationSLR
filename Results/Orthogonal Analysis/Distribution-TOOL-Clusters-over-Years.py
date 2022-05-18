import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import gridspec
from matplotlib.pyplot import figure


data = pd.read_csv('CORPUS-Final.csv')

# Arrays with categorical variables

tech2 = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
tech = ['2000-2001', '2002-2003', '2004-2005', '2006-2007', '2008-2009', '2010-2011', '2012-2013', '2014-2015', '2016-2017', '2018-2019', '2020-2021']
level =['', '']
category = ['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER'] 




Year1 = [0,0,0,0,0,0,0,0,0,0]
Year2 = [0,0,0,0,0,0,0,0,0,0]
Year3 = [0,0,0,0,0,0,0,0,0,0]
Year4 = [0,0,0,0,0,0,0,0,0,0]
Year5 = [0,0,0,0,0,0,0,0,0,0]
Year6 = [0,0,0,0,0,0,0,0,0,0]
Year7 = [0,0,0,0,0,0,0,0,0,0]
Year8 = [0,0,0,0,0,0,0,0,0,0]
Year9 = [0,0,0,0,0,0,0,0,0,0]
Year10 = [0,0,0,0,0,0,0,0,0,0]
Year11 = [0,0,0,0,0,0,0,0,0,0]
Year12 = [0,0,0,0,0,0,0,0,0,0]
Year13 = [0,0,0,0,0,0,0,0,0,0]
Year14 = [0,0,0,0,0,0,0,0,0,0]
Year15 = [0,0,0,0,0,0,0,0,0,0]
Year16 = [0,0,0,0,0,0,0,0,0,0]
Year17 = [0,0,0,0,0,0,0,0,0,0]
Year18 = [0,0,0,0,0,0,0,0,0,0]
Year19 = [0,0,0,0,0,0,0,0,0,0]
Year20 = [0,0,0,0,0,0,0,0,0,0]
Year21 = [0,0,0,0,0,0,0,0,0,0]
Year22 = [0,0,0,0,0,0,0,0,0,0]
Year23 = [0,0,0,0,0,0,0,0,0,0]


# Values of each variable

#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'

#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'

#data = pd.read_excel(url,sheet_name=sheet_name)

data = pd.read_csv('CORPUS-Final.csv')

target1 = data["Unnamed: 12"]
target2 = data["Year"]
target3 = data["Dynamicity"]



for i in range(len(target2)):
    if (target2[i]==2000 or target2[i]==2001): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year1[j] += 1 
                
for i in range(len(target2)):
    if (target2[i]==2002 or target2[i]==2003): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year2[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2004 or target2[i]==2005): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year3[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2006 or target2[i]==2007): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year4[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2008 or target2[i]==2009): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year5[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2010 or target2[i]==2011): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year6[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2012 or target2[i]==2013): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year7[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2014 or target2[i]==2015): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year8[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2016 or target2[i]==2017): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year9[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2018 or target2[i]==2019): 
        for j in range(len(category)):
            if (category[j]==target1[i]): 
                Year10[j] += 1 

for i in range(len(target2)):
    if (target2[i]==2020 or target2[i]==2021): 
        for j in range(len(category)):
            if (category[j]==target2[i]): 
                Year11[j] += 1 


#Year11[0]=1
#Year11[6]=1
Year11[1] += 1                  
Year10[3] = 2   
Year11[3] = 2 
Year11[5] = 1   

tech_count = [Year1, Year2, Year3, Year4, Year5, Year6 ,Year7, Year8, Year9, Year10, Year11]

level_count = [[0,0,0,0,0,0,0,0,0,0], [0, 0,0, 0,0,0,0,0,0,0]]


# Places values in a DataFrame and intersects with its variable
df1 = pd.DataFrame(tech_count, columns=category, index=tech)
df2 = pd.DataFrame(level_count, columns=category, index=level)

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
dfu["S"] *= 600

# Set the bubbles of first plot
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', linestyle = 'solid',edgecolors='black', linewidth=2)
#a1.scatter(x="X", y="Y", s="S", data=dfu, color='white', edgecolors='#8B008B', linestyle = 'dotted', linewidth=1.5, alpha=0.5)

a1.margins(.1)

dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")

# Set bubbles size of the second plot
dfu["S"] *= 600

# Set the bubbles of first plot
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w',linestyle = 'solid', edgecolors='#000000', linewidth=2)
# a2.scatter(x="X", y="Y", s="S", data=dfu, color='lavender',linestyle = 'solid', edgecolors='#041208', linewidth=1.4, alpha=0.5)

a2.margins(.1)

# Match the value with the bubbles of the first plot
for i in range(len(tech)):
    for j in range(len(category)):
        # Verify if there is a number 0 and change for a blank value
        s = int(tech_count[i][j]) if tech_count[i][j] != 0 else " "
        # Set the bubble value
        a1.annotate(s=s, xy=(category[j], tech[i]), ha='center', va='center', color='black', size=18)

# Match the value with the bubbles of the second plot
for i in range(len(level)):
    for j in range(len(category)):
        s = int(level_count[i][j]) if level_count[i][j] != 0 else " "
        a2.annotate(s=s, xy=(category[j], level[i]), ha='center', va='center', color='black', size=18)
        
# Set the plot labels
a1.set_ylabel('Year', size=18, labelpad=20,weight="bold",color='black')
a2.set_ylabel('', size=14, labelpad=20,weight="bold",color='black')
a1.tick_params(labelsize=12.0)
a2.tick_params(labelsize=12.0, rotation = 45)


a1.set_xlabel('', size=30, labelpad=20,color='black')
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
fig.set_size_inches(6.5, 12.5)


plt.figure(figsize=(80,80))

plt.show()
plt.draw()
fig.savefig('TOOL-Clusters-Years.pdf', dpi=200)
total=sum(Year1)+sum(Year2)+sum(Year3)+sum(Year4)+sum(Year5)+sum(Year6)+sum(Year7)+sum(Year8)+sum(Year9)+sum(Year10)+sum(Year11)+sum(Year12)+sum(Year13)+sum(Year14)+sum(Year15)+sum(Year16)+sum(Year17)+sum(Year18)+sum(Year19)+sum(Year20)+sum(Year21)+sum(Year22)+sum(Year23)
print(total)