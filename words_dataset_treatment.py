import pandas as pd

# Implementation of the routine explored in the file evaluate_datasets.ipynb

def treat_dataset(dataset: pd.DataFrame)  -> pd.DataFrame:
    """Remove unwanted entries from dataset"""

    dataset = dataset.copy(deep=True)

    # Filter the words with 5 letters
    dataset = dataset[dataset["words"].str.len()==5]

    # Make all words lower case
    dataset["words"] = dataset["words"].str.lower()

    # Remove words with hyphen, ', ö, î, è, ï, ª, º, .
    dataset = dataset.drop(dataset[dataset["words"].str.contains("-")].index)   
    dataset = dataset.drop(dataset[dataset["words"].str.contains("'")].index)
    dataset = dataset.drop(dataset[dataset["words"].str.contains("ö")].index)
    dataset = dataset.drop(dataset[dataset["words"].str.contains("î")].index)
    dataset = dataset.drop(dataset[dataset["words"].str.contains("è")].index)
    dataset = dataset.drop(dataset[dataset["words"].str.contains("ï")].index)
    dataset = dataset.drop(dataset[dataset["words"].str.contains("ª")].index)
    dataset = dataset.drop(dataset[dataset["words"].str.contains("º")].index)
    dataset = dataset.drop(dataset[dataset["words"].str.contains(".", regex=False)].index)

    # Replace accented characters for not accented ones
    dataset["words"] = dataset["words"].str.replace("[áÁâÂãÃàÀ]","a", regex=True)
    dataset["words"] = dataset["words"].str.replace("[éÉêÊ]","e", regex=True)
    dataset["words"] = dataset["words"].str.replace("[íÍ]","i", regex=True)
    dataset["words"] = dataset["words"].str.replace("[óÓôÔõÕ]","o", regex=True)
    dataset["words"] = dataset["words"].str.replace("[úÚüÜ]","u", regex=True)
    dataset["words"] = dataset["words"].str.replace("ç","c")

    # Remove duplicated entries
    dataset.drop_duplicates(inplace=True)

    return dataset

if __name__ == "__main__":
    words_dataset = pd.read_csv("resources\\palavras.txt", header=None, names=["words"])
    words_dataset = treat_dataset(words_dataset)

    print(words_dataset)