import pandas as pd
    
def main():
    datas = pd.read_csv('https://www.nyse.com/api/trade-halts/current/download')
    print(datas)

main()
