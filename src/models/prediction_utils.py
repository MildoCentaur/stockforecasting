import pandas as pd
import warnings
import sklearn
import datetime
import matplotlib.pyplot as plt     
from matplotlib.pyplot import figure
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.utils.multiclass import unique_labels

import src.data.dataset_utils as utils
import src.data.processed_data as process

def create_predictions_dataset(test_df, model, X_test):
    predictions = model.predict(X_test)
    df_predicted = pd.DataFrame({ 'Label' : predictions, 'Index' : test_df.index} )
    return df_predicted


def compare_prediction_visual(df_predicted, df_real,model_name='Unknown model'):
    fig = figure(num=None, figsize=(15, 4), dpi=80, facecolor='w', edgecolor='k')
    plt.subplot(121)
    title = model_name + ' ' +  'classification results'
    df_predicted.plot(kind='scatter', x='Index',y='Label',ax = plt.gca(),title=title)
    plt.subplot(122)
    df_real.plot(kind='scatter', x='Index',y='Label',ax = plt.gca() ,title='Real classification results')
    today = datetime.date.today()
    plt.savefig('{0}{1}.png'.format(model_name,today))


def get_model_metrics(model, y_test, X_test, model_name='Unknown model'):
    result = model.score(X_test, y_test)
    print ('Metrics for model: {}'.format(model_name))
    print ('\tScore: {1:.2f}'.format(model_name, result))
    print ('\tAccuracy: {0:.2f}'.format(accuracy_score(y_test, model.predict(X_test))))
    warnings.filterwarnings('ignore')
    print ('\tPrecision: {0:.2f}'.format(precision_score(y_test, model.predict(X_test))))
    print ('\tRecall: {0:.2f}'.format(recall_score(y_test, model.predict(X_test))))
    print ('\tPredicts {0:.2f}% time it the stock price goes up'.format(result*100, model_name))
    cm = confusion_matrix(y_test, model.predict(X_test))
    print( '\tConfusion matrix: \n\t{0} \n\t{1}'.format(cm[0], cm[1]))

    
def create_train_matrix(file, data_type='processed', predicted_variable='Label'):
    dataset = utils.load_dataset('',file, data_type)
    train_df, result_train_df = process.generate_train_dataset_lowerbound(dataset)
    X_train = train_df.values.astype('float')
    y_train = result_train_df[predicted_variable].ravel()
    print (y_train.shape)
    print (X_train.shape)
    
    return X_train, y_train, result_train_df


def create_test_matrix(file, data_type='processed', predicted_variable='Label'):
    dataset = utils.load_dataset('',file, data_type)
    test_df, result_test_df = process.generate_test_dataset(dataset)
    X_test = test_df.values.astype('float')
    y_test = result_test_df['Label'].ravel()
    print (y_test.shape)
    print (X_test.shape)
    
    return X_test, y_test, result_test_df


    
