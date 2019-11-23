# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
print(data)
#Code starts here 
data['Gender'].replace('-', 'Agender', inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar', figsize=(15,10))


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot(kind='pie', labels='Character Alignment')


# --------------
#Code starts here
#sc_df = data[['Strength', 'Combat']].copy()

#mean_strength = data['Strength'].mean()
#mean_combat = data['Combat'].mean()
#diff_strength = (data['Strength']-mean_strength)
#diff_combat = (data['Combat']-mean_combat)
#summation = (diff_strength*diff_combat).sum()
#sc_covariance = summation/len('Strength')
#a = (data['Strength']-mean_strength)**2
#sc_strength = (a.sum()/len(a))**(1/2)

#b = (data['Combat']-mean_combat)**2
#sc_combat = (b.sum()/len(b))**(1/2)

#sc_pearson = sc_covariance/(sc_strength*sc_combat)
#print(sc_pearson)

#IC_df = data[['Intelligence', 'Combat']].copy()

#mean_intelligence = data['Intelligence'].mean()
#mean_combat = data['Combat'].mean()
#diff_intelligence = (data['Intelligence']-mean_intelligence)
#diff_combat = (data['Combat']-mean_combat)
#summation = (diff_intelligence*diff_combat).sum()
#ic_covariance = summation/len('Intelligence')
#c = (data['Intelligence']-mean_intelligence)**2
#ic_intelligence = (c.sum()/len(c))**(1/2)

#d = (data['Combat']-mean_combat)**2
#ic_combat = (d.sum()/len(d))**(1/2)

#ic_pearson = sc_covariance/(ic_intelligence*ic_combat)
#print(ic_pearson)


sc_df = data[['Strength','Combat']].copy()
import pandas as pandas
import matplotlib.pyplot as plt
# Calulating Pearson correlation coefficient
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']].copy()
import pandas as pandas
import matplotlib.pyplot as plt
# Calulating Pearson correlation coefficient
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


























# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])



#print(super_best)
print(super_best_names)        



# --------------
#Code starts here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

ax_1.boxplot(super_best['Intelligence'])
plt.xlabel('Intelligence')
ax_2.boxplot(super_best['Speed'])
plt.xlabel('Speed')
ax_3.boxplot(super_best['Power'])
plt.xlabel('Power')


