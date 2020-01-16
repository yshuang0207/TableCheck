
import pandas as pd
import numpy as np
import time

def load_data():
    start = time.time()
    df = pd.read_excel('sample2.xlsx', sheet_name='20191222(含)以前入會之會員名單', converters={'MobilePhone': str})
    #df = pd.read_excel('sample.xlsx')
    end = time.time()
    print('read excel ' + str(end - start))
    return df

# Check phone number is valid
def check_phone(df):
    phones = df['MobilePhone']
    return phones.str.contains('^9\d{8}') & (phones.str.len() == 9)

def list_incorrect_phones(df):
    result = df.loc[df['MobilePhoneValid'] == False]
    print(result['MobilePhone'])

def main():
    tStart = time.time()
    df = load_data()
    #print(df)
    #print(type(df['Email'][0]))

    phones_check = check_phone(df)
    df['MobilePhoneValid'] = phones_check
    #print(df['MobilePhoneValid'])

    list_incorrect_phones(df)

    tEnd = time.time()
    print(tEnd - tStart)


if __name__ == "__main__":
    print("Check table")
    main()