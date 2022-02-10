import pandas as pd


class data_wrangler:
    def __init__(self):
        pass

    def remove_duplicates(self,raw_df):
        df_dup_removed=raw_df.remove_duplicates()
        return df_dup_removed

