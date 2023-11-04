import pandas as pd
import numpy as np
import sys
from subprocess import run

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == '__main__':
    # Get the file path from the user.
    file_path = input("Enter the file path to the dataset: ")

    # Load the dataset.
    df = load_dataset(file_path)

    # # Print the dataset.
    print(df)
    run(['python', 'dpre.py', file_path], check=True)
