import pandas as pd


def make_dim_counterparty(input_df1, input_df2):
    """
    This function takes 2 dataframes of counterparty
    and address as input.
    Joins dataframes on address_id and renames
    columns to appropriate end table column names
    and returns single formatted dataframe.

    Args:
        `input_df1`: address dataframe
        `input_df2`: counterparty dataframe
    ---------------------------

    Returns:
        Formatted dataframe

    Errors:
        Raises no errors.
    """
    df2 = input_df2.copy()
    df1 = input_df1.copy()
    df2.rename(columns={"address_id": "legal_address_id"}, inplace=True)
    df2.rename(columns={"address_line_1":
                        "counterparty_legal_address_line_1"}, inplace=True)
    df2.rename(columns={"address_line_2":
                        "counterparty_legal_address_line_2"}, inplace=True)
    df2.rename(columns={"district":
                        "counterparty_legal_district"}, inplace=True)
    df2.rename(columns={"city": "counterparty_legal_city"}, inplace=True)
    df2.rename(columns={"postal_code":
                        "counterparty_legal_postal_code"}, inplace=True)
    df2.rename(columns={"country": "counterparty_legal_country"}, inplace=True)
    df2.rename(columns={"phone":
                        "counterparty_legal_phone_number"}, inplace=True)

    df_counterp = pd.merge(df1, df2, how='inner', on='legal_address_id')
    filtered_merge = df_counterp[['counterparty_id',
                                  'counterparty_legal_name',
                                  'counterparty_legal_address_line_1',
                                  'counterparty_legal_address_line_2',
                                  'counterparty_legal_district',
                                  'counterparty_legal_city',
                                  'counterparty_legal_postal_code',
                                  'counterparty_legal_country',
                                  'counterparty_legal_phone_number']]

    return filtered_merge
