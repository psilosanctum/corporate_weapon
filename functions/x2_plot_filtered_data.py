import pandas as pd
import matplotlib.pyplot as plt  
import matplotlib.ticker as ticker
pd.set_option('display.max_columns', None)

def plotTransactions():
    try:
        print("Beginning transactions line plot...")
        path = 'data/processed/transactions_over_time.csv'
        df = pd.read_csv(path)
        # print(df)

        fig = plt.figure(figsize=(10,6))
        ax = fig.add_subplot(111)
        ax.plot(df['epoch'], df['tx_count'])
        ax.xaxis.set_major_locator(ticker.MultipleLocator(25)) # set BIG ticks
        ax.yaxis.set_major_locator(ticker.MultipleLocator(100000)) # set BIG ticks
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        ax.set_ylim(0, 1600000)
        ax.set_xlim(0, 455)
        plt.xlabel('Epoch') 
        plt.ylabel('Transactions') 
        plt.title('Transactions Over Time') 
        plt.savefig('figures/line_transactions.png')
        # plt.show()
        print("Transactions line graph saved!")
    
    except:
        print("Transactions line graph not saved!")


def plotYearly():
    try:
        print("Beginning transactions bar graph...")
        path = 'data/processed/sum_yearly_tx_and_fees.csv'
        df = pd.read_csv(path)
        # print(df)

        fig = plt.figure(figsize=(10,6))
        ax = fig.add_subplot(111)
        ax.bar(df['year_end'], df['tx_count'])
        # ax.xaxis.set_major_locator(ticker.MultipleLocator(25)) # set BIG ticks
        # ax.yaxis.set_major_locator(ticker.MultipleLocator(100000)) # set BIG ticks
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        ax.set_ylim(0, 35000000)
        plt.xlabel('Epoch') 
        plt.ylabel('Transactions') 
        plt.title('Transactions By Year') 
        plt.savefig('figures/bar_transactions.png')
        # plt.show()
        print("Transactions bar graph saved!")

    except:
        print("Transactions bar graph not saved!")

# plotTransactions()
# plotYearly()