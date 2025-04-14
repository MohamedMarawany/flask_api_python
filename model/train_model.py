# train_model.py
# python model/train_model.py
from sklearn.linear_model import LogisticRegression  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split
import pickle
import warnings
warnings.filterwarnings("ignore")

# Load and split data
data = load_iris()  
Xtrain, Xtest, Ytrain, Ytest = train_test_split(data.data, data.target, test_size=0.3, random_state=4)  

# Create and train model
model = LogisticRegression(C=0.1, max_iter=20, fit_intercept=True, n_jobs=3, solver='liblinear')
model.fit(Xtrain, Ytrain)  

# Save model in the correct path
pkl_filename = "api/iris_model.pkl"  
with open(pkl_filename, 'wb') as file:  
    pickle.dump(model, file)

# Optional: Test the model
with open(pkl_filename, 'rb') as file:  
    pickle_model = pickle.load(file)

score = pickle_model.score(Xtest, Ytest)  
print("✅ Model trained and saved successfully.")
print("Test score: {0:.2f}%".format(100 * score))



# Based on the model:

# 0 = Setosa

# 1 = Versicolor

# 2 = Virginica