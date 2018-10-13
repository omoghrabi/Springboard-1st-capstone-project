import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/omarmoghrabi/Desktop/data/WA_Fn-UseC_-Telco-Customer-Churn 2.csv")
df.head()
df.columns = df.columns.str.capitalize()

df.columns

df.head()
df.info()

# no Nan values exist
df.describe()

# no outliers or weird data

# checking for duplicated data with cutomer id
df.duplicated().sum()

# checking for duplicated data without cutomer id

df.drop(columns="Customerid").duplicated().sum()

# furhter investigating duplicated data
df_new = df.drop(columns="Customerid")
idx = df_new.index[df_new.duplicated()]

df_test = df_new.iloc[idx]
df_test[df_test.Seniorcitizen == 1]
df_dup = df_new[(df_new.duplicated())]
df_dup
df_dup[df_dup.Internetservice == "DSL"]
sns.set()


sns.barplot(x="tenure",y="Churn",hue="gender",data=df)
 sns.barplot(x="MultipleLines",y="MonthlyCharges",hue="Churn",data=df)
 sns.barplot(x="PaymentMethod",y="MonthlyCharges",hue="Churn",data=df)
sns.barplot(x="MonthlyCharges",y="Churn",hue="MultipleLines",data=df)
sns.factorplot(x="Internetservice", hue="Churn", col="Multiplelines",data=df, kind="count")
df.columns

sns.countplot(x="Churn",hue="InternetService",data=df)
sns.countplot(x="Churn",hue="TechSupport",data=df)
sns.countplot(x="Churn",hue="PaymentMethod",data=df)
sns.countplot(x="Churn",hue="OnlineSecurity",data=df)
sns.countplot(x="Churn",hue="Contract",data=df)
