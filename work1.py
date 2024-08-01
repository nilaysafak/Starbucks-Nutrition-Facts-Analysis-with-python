import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



sns.set_style("darkgrid")
df = pd.read_csv("starbucks.csv",index_col=0)
x = df.head()
#print(x)

y = df.info()
#print(y)

z = df.describe()
print(z)

a = df["item"].nunique()
#print(a)

b= df["item"].unique()
#print(b)

c = df["type"].unique()
print(c)

d = df.groupby("type")["item"].count().plot()
plt.title("Ürün Türleri")
plt.text(2,47,"Ürün Kategori Yelpazesi",bbox=dict(facecolor="yellow",alpha=0.5))
plt.show()

sns.countplot(x="type",data=df,palette="Set1")
plt.title("Ürün sayıları")
plt.show()


sns.catplot(kind="bar",x="type",y="calories",data=df,palette="muted", height=4, aspect=1.5)
plt.title("Kalori değerleri")
plt.tight_layout()
plt.show()


sns.catplot(kind="bar",x="type",y="protein",data=df,palette="muted", height=4, aspect=1.5)
plt.title("Protein değerleri")
plt.tight_layout()
plt.show()


sns.catplot(kind="bar",x="type",y="carb",data=df,palette="muted", height=4, aspect=1.5)
plt.title("Karbonhidrat değerleri")
plt.tight_layout()
plt.show()


sns.catplot(kind="bar",x="type",y="fiber",data=df,palette="muted", height=4, aspect=1.5)
plt.title("Lif değerleri")
plt.tight_layout()
plt.show()


sns.displot(x="calories",data=df,color="red",kde=True)
plt.title("kalori grafiği")
plt.tight_layout()
plt.show()


sns.displot(x="fat",data=df,color="purple",kde=True)
plt.title("yağ grafiği")
plt.tight_layout()
plt.show()