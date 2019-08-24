import numpy as np
import pandas as pd 
df = pd.read_csv('./final_dataset.csv')
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle
# Features
gender = list(df['gender'])
for i in range(len(gender)):
	if gender[i] == 'M':
		gender[i] = 0
	else:
		gender[i] = 1
# Male - 0 , Female - 1

school_level = list(df['StageID'])
for i in range(len(school_level)):
	if school_level[i] == "lowerlevel":
		school_level[i] = 0
	elif school_level[i] == "MiddleSchool":
		school_level[i] = 1
	else:
		school_level[i] = 2
# Class 0-4 - 0 , 5-8 - 1, 9-12 - 2

doubts_aksed = list(df['raisedhands'])

discussion = list(df['Discussion'])

parent = list(df['ParentschoolSatisfaction'])
for i in range(len(parent)):
	if parent[i] == 'Good':
		parent[i] = 1
	else:
		parent[i] = 0
# Good - 1, Bad - 0

absent = list(df['StudentAbsenceDays'])
for i in range(len(absent)):
	if absent[i] == 'Under-7':
		absent[i] = 0
	else:
		absent[i] = 1
# Absent More Than 10% - 1, Less Than 10% - 0

result = list(df['Class'])
for i in range(len(result)):
	if result[i] == 'L':
		result[i] = 0
	elif result[i] == 'M':
		result[i] = 1
	else:
		result[i] = 2
# Results 0,1,2

labels = result

features = list()
for i in range(len(doubts_aksed)):
	features.append([school_level[i],doubts_aksed[i],discussion[i],parent[i],absent[i]])

# Fraction Of Training Data
fac = 0.8
features_train = features[:int(fac*len(features))]
features_test = features[int(fac*len(features)):]
labels_train = labels[:int(fac*len(labels))]
labels_test = labels[int(fac*len(labels)):]

sc = StandardScaler()

sc.fit(features_train)


features_train_std = sc.transform(features_train)
features_test_std = sc.transform(features_test)

svm = SVC(kernel='linear', C=2.0, random_state=0)
svm.fit(features_train_std, labels_train)

pickle.dump(svm,open('trained_model.sav','wb'))

loaded_model = pickle.load(open('trained_model.sav','rb'))

labels_pred = loaded_model.predict(features_test_std)
print('Misclassified samples: %d' % (labels_test != labels_pred).sum())
print(len(features_test))
