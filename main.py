# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:10:06 2019

@author: Yoavkt
"""

import numpy as np
import pandas as pd 
import seaborn as sns
import os
import matplotlib.pyplot as plt

data_folder = r'C:\CODE\Flatiron_project\data'
df_pd = pd.read_csv(os.path.join(data_folder,'Patient_Diagnosis.csv')
                    ,dtype={'diagnosis_code':np.float,'patient_id':np.int,
                    'diagnosis':str},parse_dates=['diagnosis_date'])
df_pt = pd.read_csv(os.path.join(data_folder,'Patient_Treatment.csv'),
                    parse_dates=['treatment_date'],
                    dtype={'drug_code':str,'patient_id':np.int})


# Here we are cheking (though told) that there are no nan values.
for df,nm in zip([df_pd,df_pt],['Patient_Diagnosis','Patient_Treatment']):
    for col in df_pd.columns:
        print(nm,col,'No nan values:',np.sum(df_pd[col].isnull())==0)
        
# Here we are cheking (though told) that there are no nan values.
for df,nm in zip([df_pd,df_pt],['Patient_Diagnosis','Patient_Treatment']):
    for col in df_pd.columns:
        print(nm,col,'Possible values',df_pd[col].unique())

# now we are checking if all patients recived a treatment
untreated_patients = [v for v in df_pd['patient_id'].unique()  if v not in df_pt['patient_id'].unique()]
unaccount_treatments = [v for v in df_pt['patient_id'].unique() if v not in df_pd['patient_id'].unique()]
print('Number of untreated patients',len(untreated_patients))
print('Number of treatments without patients',len(unaccount_treatments))


### figure 1
f,(ax1,ax2) = plt.subplots(2,1)
sns.countplot(data=df_pd,ax=ax1,x='diagnosis_code',hue='diagnosis').set_title('Patients per diagnosis code')
g = sns.countplot(data=df_pt,ax=ax2,x='patient_id',hue='drug_code')
g.set_xticklabels(g.get_xticklabels(),rotation=90)

df_pd['first_line'] = np.nan
for v in df_pd.iterrows():
    df_pd.loc[v[0],'start_date'] =df_pt.loc[(df_pt['patient_id']==v[1]['patient_id']),'treatment_date'].min()
    df_pd.loc[v[0],'end_date'] =df_pt.loc[(df_pt['patient_id']==v[1]['patient_id']),'treatment_date'].max()
    df_pd.loc[v[0],'diag_num'] =  len(df_pd.loc[df_pd['patient_id']==v[1]['patient_id'],'diagnosis'].unique())
    if (df_pt.loc[df_pt['patient_id']==v[1]['patient_id'],['treatment_date','drug_code']].shape[0]>0):
        df_pd.loc[v[0],'first_line'] = df_pt.loc[df_pt['patient_id']==v[1]['patient_id'],['treatment_date','drug_code']].sort_values(by='treatment_date',ascending=True)['drug_code'].values[0]
### figure 2
f,ax = plt.subplots(1,1)

f,ax = plt.subplots()
df_pd.loc[:,'diag_num'].value_counts().plot(kind='bar',ax=ax)


df_pd['Days_diff'] = df_pd['start_date'] -  df_pd['diagnosis_date']
df_pd['Days_diff_n'] = [v.days for v in df_pd['Days_diff']]
df_pd['Days_treat'] = df_pd['end_date'] -  df_pd['start_date']
df_pd['Days_treat_n'] = [v.days for v in df_pd['Days_treat']]

df_pd_single_diag = df_pd.loc[(df_pd['diag_num']==1) & (df_pd['Days_diff_n']<df_pd['Days_diff_n'].quantile(.98))
& (df_pd['Days_diff_n']>0),:]
f,ax = plt.subplots(1,1)
ax = sns.boxplot(x="diagnosis", y="Days_diff_n", data=df_pd_single_diag,ax=ax)


df_pt['new ind'] = [str(v)+str(v2) for v,v2 in zip(df_pt['patient_id'],df_pt['drug_code'])]
df_pt.sort_values(by='treatment_date',ascending=True)
tmp = df_pt.drop_duplicates(  subset=['new ind'])

for v in df_pd_single_diag['patient_id']:
    tmp.loc[tmp['patient_id']==v,'diagnosis'] = df_pd_single_diag.loc[df_pd_single_diag['patient_id']==v,'diagnosis'].values[0]
    tmp.loc[(tmp['patient_id']==v) & (tmp['diagnosis']=='Breast Cancer'),'ord'] = np.argsort(tmp.loc[(tmp['patient_id']==v) & (tmp['diagnosis']=='Breast Cancer'),'treatment_date'])
    tmp.loc[(tmp['patient_id']==v) & (tmp['diagnosis']=='Colon Cancer'),'ord'] = np.argsort(tmp.loc[(tmp['patient_id']==v) & (tmp['diagnosis']=='Colon Cancer'),'treatment_date'])

tmp = tmp.loc[tmp['ord'].notnull(),:]


g = sns.catplot(x="ord", hue="diagnosis", col="drug_code",
                 data=tmp, kind="count",
                 height=4, aspect=.7);
f,ax = plt.subplots(1,1)
df_pd['first_line'].value_counts().plot(kind='bar',ax=ax)     

f,ax = plt.subplots(1,1)
df_pd_tmp = df_pd.loc[(df_pd['Days_treat_n']<df_pd['Days_treat_n'].quantile(.95))
& (df_pd['Days_treat_n']>0),:]
ax = sns.boxplot(x="diagnosis", y="Days_treat_n", data=df_pd_tmp,ax=ax)
from scipy import stats
stats.ttest_ind(df_pd.loc[df_pd['first_line']=='A','Days_treat_n'],df_pd.loc[df_pd['first_line']=='B','Days_treat_n'])
