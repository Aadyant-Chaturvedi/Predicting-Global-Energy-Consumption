#1. Understanding Dataset
#2. Data Preprocessing
#3. Model Training & Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)
pd.DataFrame(pred).to_csv("output/Predicted_Values.csv")
pd.DataFrame(y_test).to_csv("output/test_Values.csv")
#4.Model Evaluation
