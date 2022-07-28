# Load Sample Dataset:Iris Dataset
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Splitting Dataset:Training&Testing Set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=1)

# Training Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Evaluasi Model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy:{acc}')

# Pemanfaatan Trained Model
data_baru = [[5, 5, 3, 2],
             [2, 4, 3, 5]]

preds = model.predict(data_baru)
preds
pred_species = [iris.target_names[p]for p in preds]

print(f'Hasil Prediksi:{pred_species}')

# Dump&Load Trained Model
# Dumping Model Machine Learning menjadi file joblib
import joblib
joblib.dump(model,'iris_classifier_knn.joblib')
['iris_classifier_knn.joblib']

# Loading Model Machine Learning dari file joblib
production_model=joblib.load('iris_classifier_knn.joblib')