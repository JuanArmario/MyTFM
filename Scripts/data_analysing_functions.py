import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def nulls_percentage(dataset):
    """
    Prints the percentage of null values, the number of unique values, and the data type for each column in the dataset.

    Args:
        dataset (pd.DataFrame): The dataset to analyze.

    Returns:
        None
    """
    for column in dataset.columns:
        null_percentage = "{:.1%}".format(np.mean(dataset[column].isnull()))
        print(
            column,
            ",",
            null_percentage,
            "nulls",
            ",",
            dataset[column].nunique(),
            "unique values,",
            dataset[column].dtype,
        )


def nulls_percentage_in_column(column):
    """
    Prints the percentage of null values, the number of unique values, and the data type for a given column.

    Args:
        column (pd.Series): The column to analyze.

    Returns:
        None
    """
    null_percentage = "{:.1%}".format(np.mean(column.isnull()))
    print(
        column.name,
        ",",
        null_percentage,
        "nulls",
        ",",
        column.nunique(),
        "unique values,",
        column.dtype,
    )


def get_columns_with_percentage_or_higher(dataset, min_percentage, max_percentage):
    """
    Identifies and prints columns with a percentage of null values within a specified range.

    Args:
        dataset (pd.DataFrame): The dataset to analyze.
        min_percentage (float): Minimum percentage threshold.
        max_percentage (float): Maximum percentage threshold.

    Returns:
        None
    """
    for column in dataset.columns:
        null_percentage = "{:.1%}".format(np.mean(dataset[column].isnull()))
        if (
            float(null_percentage.replace("%", "")) > min_percentage
            and float(null_percentage.replace("%", "")) < max_percentage
        ):
            print(
                column,
                ",",
                null_percentage,
                "nulls",
                ",",
                dataset[column].nunique(),
                "unique values,",
                dataset[column].dtype,
            )


def set_gender_characteristics_value(dataset, characteristics_list, gender):
    """
    Sets the default value of specified characteristics based on gender.

    Args:
        dataset (pd.DataFrame): The dataset to modify.
        characteristics_list (list): List of characteristic columns to modify.
        gender (str): Gender value to filter by.

    Returns:
        None
    """
    for characteristic in characteristics_list:
        dataset.loc[dataset["sex"] == gender, characteristic] = 0


def boxplot_for_list(dataset, characteristics_list):
    """
    Generates a boxplot for each characteristic in the provided list.

    Args:
        dataset (pd.DataFrame): The dataset containing the characteristics.
        characteristics_list (list): List of columns to visualize.

    Returns:
        None
    """
    for characteristic in characteristics_list:
        plt.boxplot(dataset[characteristic].dropna(), vert=False)
        plt.title(characteristic)
        plt.show()


def impute_missing_values(df):
    """
    Imputes missing values in a DataFrame.
    - Uses the median for numerical columns.
    - Uses the mode for categorical columns.
    - Drops specific columns before imputation.

    Args:
        df (pd.DataFrame): DataFrame with missing values.

    Returns:
        pd.DataFrame: DataFrame with imputed values.
    """
    df_imputed = df.copy()

    # Drop specific columns
    df_imputed = df_imputed.drop(columns=["liver_topography", "plco_id", "build"])

    # Impute missing values in numerical columns with the median
    for col in df_imputed.select_dtypes(include=["number"]).columns:
        median_value = df_imputed[col].median()
        df_imputed[col].fillna(median_value, inplace=True)

    # Impute missing values in categorical columns with the mode
    for col in df_imputed.select_dtypes(include=["object", "category"]).columns:
        mode_value = df_imputed[col].mode()[0]  # Take the first mode value
        df_imputed[col].fillna(mode_value, inplace=True)

    return df_imputed