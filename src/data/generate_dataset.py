import os
import pandas as pd

from src.features.build_features import prepare_dataset_feture_vector


def load_dataset(product, index_column, underlyer='aapl.us.txt'):
    raw_data_path = os.path.join(os.path.pardir, 'data', 'raw', product)
    data_path = os.path.join(raw_data_path, underlyer)
    print('Opening file ', data_path)
    return pd.read_csv(data_path)  # ,index_col=index_column)


def generate_train_dataset(dataset, cut_date='2016-01-01'):
    return dataset[dataset.Date < cut_date]


def generate_test_dataset(dataset, cut_date='2016-01-01'):
    #    columns = [column for column in df.columns if column != 'Survived']
    # df[df.Survived == -888][columns]
    return dataset[dataset.Date > cut_date]


def generate_dataset(product='Stocks', underlyer='aapl.us.txt', cut_date='2016-01-01'):  # , index_column = 'Date'):
    dataset = load_dataset(product, underlyer)
    if (prepare_dataset_feture_vector):
        dataset = prepare_dataset_feture_vector(dataset)
    train_df = generate_train_dataset(dataset, cut_date)
    test_df = generate_test_dataset(dataset, cut_date)

    return (dataset, train_df, test_df)


def write_data(train_df, test_df):
    processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
    write_train_path = os.path.join(processed_data_path, 'train.csv')
    write_test_path = os.path.join(processed_data_path, 'test.csv')
    # train data
    train_df.to_csv(write_train_path)
    # test data
    test_df.to_csv(write_test_path)


if __name__ == '__main__':
    dataset, train_df, test_df = generate_dataset('Stocks', 'aapl.us.txt', '2016-01-01')
    write_data(train_df, test_df)
    
