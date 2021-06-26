import pandas as pd

def create_list_of_values(df, label_col, value_col):

    """
    Create a list of values.

    params:
    * df: Pandas dataframe.
    * label_col: String. Column name to be used as label.
    * value_col: String. Column name to be used as value.
    """

    lov = []
    unique_values = df.drop_duplicates([label_col, value_col])

    for idx, row in unique_values.iterrows():
        lov.append({"label": row[label_col], "value": row[value_col]})

    return lov


def filter_df(df, filter_cols):
    """
    Filter a dataset based on a list of filtering columns.

    * df: Pandas dataframe.
    * filter_cols: List of maps. Filters to be used to filter the dataframe.
    """

    filters = []

    for column, value in filter_cols.items():

        if value:
            df = df[df[column] == value]

    return df
