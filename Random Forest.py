import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

raw_data = pd.read_csv('UNSW_NB15_testing-set.csv')
#raw_data.head()

model = RandomForestClassifier(n_estimators=30, random_state=10, criterion='entropy',max_depth=25)

data = raw_data.copy()

x_train = data['name']
y_train = data['Performance']
x_test = data['']
y_test = data['']

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test)
print('accuracy:',accuracy)

report = classification_report(y_test, y_pred)
print('Classification report:\n', report)

conf_matrix = confusion_matrix(y_test, y_pred)
print('confusion_matrix:\n',conf_matrix)
