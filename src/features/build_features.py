import pandas as pd


def prepare_dataset_feture_vector(df):
    # Feature vector

    df_tomorrow = generate_tomorrow_dataset(df)
    df_yesterday = generate_yesterday_dataset(df)
    # concatenate yesterday - today and tomorrow
    df = pd.concat([df_yesterday, df, df_tomorrow], axis=1, sort=False)

    # eliminate nan values from before yesterday and after tomorrow
    df = df[1:-2]

    return (df
            .assign(Date=lambda x: pd.to_datetime(x.Date))
            .assign(Average_High_Low=lambda x: (x.High + x.Low) / 2)
            .assign(Average_Day=lambda x: (x.Open + x.Close) / 2)
            .assign(Diff_Close_Open=lambda x: (x.Close - x.Open) / x.Open)
            .assign(Diff_Tomorrow_Open=lambda x: (x.Tomorrow_Open - x.Open) / x.Open)
            .assign(Diff_Today_Open=lambda x: (x.Open - x.Yesterday_Open) / x.Yesterday_Open)
            .assign(Diff_Today_Close=lambda x: (x.Close - x.Yesterday_Close) / x.Yesterday_Close)
            .assign(Diff_Today_Volume=lambda x: (x.Volume - x.Yesterday_Volume) / x.Yesterday_Volume)
            .assign(Diff_Today_High=lambda x: (x.High - x.Yesterday_High) / x.Yesterday_High)
            .assign(Diff_Today_Low=lambda x: (x.Low - x.Yesterday_Low) / x.Yesterday_Low)
            )


def generate_tomorrow_dataset(today_dataset):
    df_tomorrow = today_dataset[['Date', 'Open']].copy()
    df_tomorrow = df_tomorrow[1:]
    df_tomorrow.columns = ['Tomorrow_Date', 'Tomorrow_Open']
    print('Generate new Column')
    df_tomorrow['aux_index'] = df_tomorrow.index - 1
    print('seteo la columna como indice')
    df_tomorrow.set_index('aux_index', inplace=True, drop=True)

    return df_tomorrow


def generate_yesterday_dataset(today_dataset):
    df_yesterday = today_dataset[['Date', 'Open', 'Close', 'Volume', 'Low', 'High']].copy()
    df_yesterday.columns = ['Yesterday_Date', 'Yesterday_Open', 'Yesterday_Close', 'Yesterday_Volume', 'Yesterday_Low',
                            'Yesterday_High']
    print('Generate new Column')
    df_yesterday['aux_index'] = df_yesterday.index + 1
    print('seteo la columna como indice')
    df_yesterday.set_index('aux_index', inplace=True, drop=True)

    return df_yesterday

