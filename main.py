# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:10:06 2019

@author: Yoavkt
"""

import numpy as np
import pandas as pd 
import seaborn as sns
import os

data_folder = r'C:\CODE\Flatiron_project\data'
df_pd = pd.read_csv(os.path.join(data_folder,'Patient_Diagnosis.csv'),
                    index_col='patient_id',dtype={'diagnosis_code':np.float,
                    '':str},parse_dates=['diagnosis_date'])
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


sns.countplot(data=df_pd,x='diagnosis_code',hue='diagnosis').set_title('Patients per diagnosis code')
g = sns.countplot(data=df_pt,x='patient_id',hue='drug_code')
g.set_xticklabels(g.get_xticklabels(),rotation=90)


for v in df_pd.index:
    df_pd.loc[v,'start_date'] =df_pt.loc[df_pt['patient_id']==v,'treatment_date'].min()

df_pd['Days_diff']  =df_pd['start_date'] -  df_pd['diagnosis_date']
