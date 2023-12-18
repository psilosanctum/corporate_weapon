import pandas as pd
import datetime as dt
from datetime import datetime
import matplotlib.pyplot as plt  
import matplotlib.ticker as ticker
pd.set_option('display.max_columns', None)

def manipulateData():
    try:
        print("Begin data manipulation...")
        # Import file containing raw data
        path = "data/raw/epoch_data.csv"

        # Create DF
        df = pd.read_csv(path)

        # Create empty lists to append converted time
        new_start_time = []
        new_end_time = []
        year_start = []
        year_end = []

        # Iterate over DF to convert timestamps
        for i, r in df.iterrows():
            start = dt.datetime.fromtimestamp(int(r['start_time'])).strftime('%Y-%m-%d')
            start2 = dt.datetime.fromtimestamp(int(r['start_time'])).strftime('%Y')
            new_start_time.append(start)
            year_start.append(start2)
            end = dt.datetime.fromtimestamp(int(r['end_time'])).strftime('%Y-%m-%d')
            end2 = dt.datetime.fromtimestamp(int(r['start_time'])).strftime('%Y')
            new_end_time.append(end)
            year_end.append(end2)

        new_df = df.copy()
        new_df = new_df.drop(['start_time', 'end_time'], axis=1)
        # Replace old timestamps with converted timestamps
        new_df['start_time'] = new_start_time
        new_df['end_time'] = new_end_time
        new_df['year_start'] = year_start
        new_df['year_end'] = year_end
        # print(new_df)

        # Calculate Annual Transactions & Fees DF
        yearly_tx_fees_df = new_df[['year_end', 'tx_count', 'fees']]
        yearly_tx_fees_df = yearly_tx_fees_df.groupby('year_end').sum().reset_index()
        yearly_tx_fees_df[['tx_count', 'fees']] = yearly_tx_fees_df[['tx_count', 'fees']].astype(int)
        # yearly_tx_fees_df.to_csv('data/processed/sum_yearly_tx_and_fees.csv', index=False)
        # print(yearly_tx_fees_df)

        # Transactions Over Time DF
        transactions_over_time_df = new_df[['epoch', 'tx_count']]
        # print(transactions_over_time_df)
        # transactions_over_time_df.to_csv('data/processed/transactions_over_time.csv', index=False)
        print("Data manipulation successful!")
    
    except:
        print("Data manipulation failed!")


# manipulateData()