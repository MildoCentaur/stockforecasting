import pandas as pd
from src.data.dataset_utils import load_dataset, write_dataset
from src.features.feature_data import prepare_feture_vector


def process_dataset(product='Stocks', underlyer='aapl.us.txt'):
    dataset = load_dataset(product, underlyer, 'raw', index_column=False)
    dataset = prepare_feture_vector(dataset)
    write_dataset(dataset,'feature_vector')
    return dataset
    
    
def generate_train_dataset(dataset, split_date='2016-01-01'):
    return dataset[(dataset.Date < split_date) & (dataset.Date > pd.to_datetime('2013-01-01'))]


def generate_test_dataset(dataset, split_date='2016-01-01'):
    return dataset[dataset.Date > split_date]

if __name__ == '__main__':
    dataset = process_dataset('Stocks', 'aapl.us.txt')
