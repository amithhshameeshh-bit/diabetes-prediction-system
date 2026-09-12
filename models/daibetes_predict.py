import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv('hospital.csv')
print(df.head(
))
x=df[[ "Age","Blood_Pressure","Blood_Sugar","BMI"]]
y=df["Diabetes"]
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("predicted value:",y_pred)
accuracy=accuracy_score(y_test,y_pred)
print("accuracy",accuracy*100,"%")
import pickle
pickle.dump(model,open("diabetes_model.pkl","wb")
            )
print("model saved successfully as 'diabetes_model.pkl")