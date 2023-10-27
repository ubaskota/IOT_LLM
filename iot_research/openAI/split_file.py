import pandas as pd
import sys
from sklearn.model_selection import train_test_split


def split_csv(input_csv, output_test_csv):

    df = pd.read_csv(input_csv)

    _, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Save the test data to a new CSV file
    test_df.to_csv(output_test_csv, index=False)

    print("Test data saved to", output_test_csv)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_csv_file> <output_test_csv_file>")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    output_test_csv_file = sys.argv[2]

    split_csv(input_csv_file, output_test_csv_file)
