import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import csv
import random
raw_data = pd.read_csv('UNSW_NB15_testing-set.csv')
#raw_data.head()

data_train = 'output_data_60.csv'
data_test = 'output_data_40.csv'

split_ratio = 0.4  # 40%

data = []


with open('UNSW_NB15_testing-set.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  
    for row in csv_reader:
        data.append(row)

random.shuffle(data)


split_point = int(len(data) * split_ratio)

data_40 = data[:split_point]
data_60 = data[split_point:]


with open(data_train, 'w', newline='') as csv_file_1:
    csv_writer_1 = csv.writer(csv_file_1)
    csv_writer_1.writerows(data_40)

with open(data_test, 'w', newline='') as csv_file_2:
    csv_writer_2 = csv.writer(csv_file_2)
    csv_writer_2.writerows(data_60)

print(f"{len(data_40)} rows saved to {data_train}")
print(f"{len(data_60)} rows saved to {data_test}")


model = RandomForestClassifier(n_estimators=30, random_state=10, criterion='entropy',max_depth=25)

data = raw_data.copy()

x_train = data['name']
y_train = data['id']
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
