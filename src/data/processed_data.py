import pandas as pd
from src.data.dataset_utils import load_dataset, write_dataset
from src.features.feature_data import prepare_feture_vector


def process_dataset(product='Stocks', underlyer='aapl.us.txt'):
    dataset = load_dataset(product, underlyer, 'raw', index_column=False)
    dataset = prepare_feture_vector(dataset)
    write_dataset(dataset,'feature_vector')
    return dataset
    
    
def generate_train_dataset(dataset, split_date='2016-01-01'):
    dataset_aux = dataset[dataset.Date < split_date]
    result_df = pd.DataFrame()
    result_df['Label'] = dataset_aux.Label
    result_df['Index'] = dataset_aux.index
    dataset_aux = dataset_aux.drop(columns=['Tomorrow_Date', 'Tomorrow_Open', 'Label', 'Diff_Tomorrow_Open', 'Date', 'Yesterday_Date']) 
    return dataset_aux, result_df


def generate_train_dataset_lowerbound(dataset, split_date='2016-01-01', lower_bound = '2000-01-01'):
    dataset_aux = dataset[(dataset.Date < split_date) & (dataset.Date > lower_bound)]
    result_df = pd.DataFrame()
    result_df['Label'] = dataset_aux.Label
    result_df['Index'] = dataset_aux.index
    print(dataset_aux.columns)
    dataset_aux = dataset_aux.drop(columns=['Tomorrow_Date', 'Tomorrow_Open', 'Label', 'Diff_Tomorrow_Open', 'Date', 'Yesterday_Date'])
    return dataset_aux, result_df


def generate_test_dataset(dataset, split_date='2016-01-01'):
    dataset_aux = dataset[dataset.Date > split_date]
    result_df = pd.DataFrame()
    result_df['Label'] = dataset_aux.Label
    result_df['Index'] = dataset_aux.index

    dataset_aux = dataset_aux.drop(columns=['Tomorrow_Date', 'Tomorrow_Open', 'Label', 'Diff_Tomorrow_Open', 'Date', 'Yesterday_Date'])
    return dataset_aux, result_df

if __name__ == '__main__':
    dataset = process_dataset('Stocks', 'aapl.us.txt')
