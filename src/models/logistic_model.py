import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

import src.models.prediction_utils as utils

X_train, y_train, result_train_df = utils.create_train_matrix('dataset_feature_vector.csv')
X_test, y_test, result_test_df = utils.create_test_matrix('dataset_feature_vector.csv')

#Create model/estimator
logistic_model = LogisticRegression(random_state=0, solver='liblinear')

#This takes several minutes
parameters = {'C':[1.0, 10.0, 50.0, 100.0, 1000.0], 'penalty' : ['l1','l2'],'class_weight' : ['balanced',None], 'solver' : ['liblinear','saga'], 'max_iter' : [100,1000,10000]}
logistic_model_grid = GridSearchCV(logistic_model, param_grid=parameters, cv=3)
#Train every posible variation of the model
with ignore_warnings(category=ConvergenceWarning):
    logistic_model_grid.fit(X_train, y_train)

#Get the best    
print ('Best parameters for logistic model grid'.logistic_model_grid.best_params_)
print ('Best score : {0:.2f}'.format(logistic_model_grid.best_score_))
print ('Score for logistic regression - version 2 : {0:.2f}'.format(logistic_model_grid.score(X_test, y_test)))

utils.get_model_metrics(logistic_model_grid, y_test, X_test, 'Logistic model grid')
utils.compare_prediction_visual(utils.create_predictions_dataset(result_test_df, logistic_model_grid, X_test), result_test_df, 'Logistic Grid')


