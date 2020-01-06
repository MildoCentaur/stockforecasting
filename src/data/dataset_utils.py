import os
import pandas as pd


def load_dataset(subfolder='', file='aapl.us.txt', data_type='raw', index_column=0):
    data_path = os.path.join(os.path.pardir, os.path.pardir, 'data', data_type, subfolder, file)
    print('Opening file ', data_path)
    df = pd.read_csv(data_path, index_col=index_column)
    print('%d missing values found' % df.isnull().sum().sum())
    return df


def write_dataset(dataset,filename_extension):
    processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
    dataset_path = os.path.join(processed_data_path, 'dataset_' + filename_extension + '.csv')
    dataset.to_csv(dataset_path)
