# data/disability-adjusted_life_year.csv
import os

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


for dirname, _, filenames in os.walk('data/disability-adjusted_life_year.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# Reading the csv file
df=pd.read_csv('/kaggle/input/top-25-economies-leading-cause-of-dalys-death/data.csv')

import matplotlib.pyplot as plt
import seaborn as sns


# getting the head of the csv
df.head()
""" To print to stdout """
# print(df.head())

df.isnull().sum()

# Plotting the graph
df.groupby('YEAR')['DEATHS'].sum().plot.bar()
plt.title('DEATHS')

df.groupby('YEAR')['DALY'].sum().plot.bar()
plt.title('DALY')

sns.heatmap(df.corr(),annot=True)

pd.DataFrame(df.groupby(['YEAR','COUNTRY_CODE'])['DEATHS'].sum())

df_00_19=df[df['YEAR'].isin([2000,2019])]
df1_d=pd.DataFrame(df.groupby(['YEAR','COUNTRY_CODE'])['DEATHS'].sum())
df1_d=df1_d.reset_index()
df1_da=pd.DataFrame(df.groupby(['YEAR','COUNTRY_CODE'])['DALY'].sum())
df1_da=df1_da.reset_index()


""" Economic Death Numbers """

import matplotlib.pyplot as plt
import plotly_express as px
fig = px.choropleth(df1_d,locations='COUNTRY_CODE',color='DEATHS',scope='world',color_continuous_scale=px.colors.sequential.GnBu,
                    animation_frame='YEAR',range_color=(50000,10000000),title='Top 25 Economics Countries Death Numbers',height=800
    )
fig.show()
