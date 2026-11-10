#1.Understanding The Dataset
#2.Data Preprocessing
df=df[["primary_energy_consumption","population","gdp","year"]].dropna()#required columns
X=df[["population","gdp","year"]]#features
y=df["primary_energy_consumption"]#target
#3.Model Training and Testing
#4.Model Evaluation
