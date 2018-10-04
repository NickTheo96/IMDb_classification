import pandas as pd
import glob
import os
import numpy as np


def main():
    list_of_files = glob.glob('Data_In/Train/neg/*.txt')

    a = pd.read_csv(list_of_files[0], dtype={'ID': object})
    b = pd.read_csv(list_of_files[1], dtype={'ID': object})

    a.to_csv('Data_Out/a.csv', index=1)
    b.to_csv('Data_Out/b.csv', index=2)

    print(a.shape)

    d = pd.concat([a, b], sort=False)
    d.to_csv('Data_Out/d.csv')


if __name__ == "__main__":
    main()
