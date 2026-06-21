

"""
Rule-Based Customer Segmentation and Revenue Prediction

This project analyzes a gaming company’s customer transaction data to build
level-based customer personas and estimate potential revenue for new users.

Main steps:
- Exploratory data analysis
- Customer aggregation by demographic features
- Creation of level-based personas
- Conversion of age into categorical groups
- Segmentation using quantiles (A–D)
- Revenue prediction for new customers based on persona

No machine learning models are used; the approach is fully rule-based.
"""


import pandas as pd
from pandas import set_option

pd.set_option('display.max_columns', 500)

df=pd.read_csv("persona.csv")


def general_info(dataframe):
    print("SHAPE")
    print(dataframe.shape)
    print("HEAD")
    print(dataframe.head())
    print("DESCRIBE")
    print(dataframe.describe().T)
    print("TAIL")
    print(dataframe.tail())
    print("COLUMNS")
    print(dataframe.columns)
    print("INDEX")
    print(dataframe.index)
    print("DTYPES")
    print(dataframe.dtypes)
    print("TOTAL NULL")
    print(dataframe.isnull().sum())
    print("NUMBER UNIQUE")
    print(dataframe.nunique())
    print("###########################")

general_info(df)



df["SOURCE"].nunique()
df["SOURCE"].value_counts()


df["PRICE"].nunique()

df["PRICE"].value_counts()
df.head()
df["COUNTRY"].value_counts()



df.groupby("COUNTRY")["PRICE"].sum()
df.head()
df["SOURCE"].value_counts()

df.groupby("COUNTRY")["PRICE"].mean()


df.groupby("SOURCE")["PRICE"].mean()

df.pivot_table("PRICE",["COUNTRY","SOURCE"],aggfunc="mean")

df.pivot_table("PRICE",["COUNTRY","SOURCE","AGE","SEX"],aggfunc="mean")


agg_df=df.pivot_table(["PRICE"],["COUNTRY","SOURCE","AGE","SEX"],aggfunc="mean")
agg_df=agg_df.sort_values("PRICE",ascending=False)

agg_df.head()

agg_df.reset_index(inplace=True)

agg_df.head()


df.head()
agg_df["NEW AGE"]=pd.cut(agg_df["AGE"],bins=[0,18,23,30,40,70],labels=['0_18', '19_23', '24_30', '31_40', '41_70'])





agg_df["customer_level_based"]=(agg_df["COUNTRY"].astype(str)+"_"+agg_df["SOURCE"].astype(str)+"_"+agg_df["SEX"].astype(str)+"_"+agg_df["NEW AGE"].astype(str))
#agg_df["customer_level_based"]=[ str(country)+"_"+str(source)+"_"+str(sex)+"_"+str(new_age) for country,source,sex,new_age in zip(agg_df["COUNTRY"],agg_df["SOURCE"],agg_df["SEX"],agg_df["NEW AGE"])]

agg_df=agg_df.groupby("customer_level_based").agg({"PRICE":"mean"})
agg_df.reset_index(inplace=True)

#agg_df["new segment"]=pd.cut(agg_df["PRICE"],[8,19,29,39,49,59],labels=['so cheap','cheap','middle','top middle','so expensive'])
agg_df["SEGMENT"]=pd.qcut(agg_df["PRICE"],4,['D','C','B','A'])


agg_df.head()

agg_df.loc[agg_df["customer_level_based"]=="tur_android_female_31_40",["customer_level_based","SEGMENT","PRICE"]]
agg_df.loc[agg_df["customer_level_based"]=="fra_ios_female_31_40",["customer_level_based","SEGMENT","PRICE"]]

def predict(age,source,country,sex,agg_df):
    if age<18:
        cat_age="0_18"
    elif age<=23:
        cat_age="19_23"
    elif age<=30:
        cat_age="24_30"
    elif age<=40:
        cat_age="31_40"
    else:
        cat_age="41_70"

    customer=f'{country}_{source}_{sex}_{cat_age}'
    #customer= country+"_"+source+"_"+sex+"_"+cat_age
    return agg_df.loc[agg_df["customer_level_based"]==customer,
    ["customer_level_based","SEGMENT","PRICE"]]

predict(35,"ios","fra","female",agg_df)