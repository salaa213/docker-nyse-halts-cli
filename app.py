import pandas as pd
from time import sleep
import os
    
def main():
    while True == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        datas = pd.read_csv('https://www.nyse.com/api/trade-halts/current/download')
        print(datas)
        sleep(10)

main()
