# Writing a definition that will identify and remove duplicated values

def identify_and_remove_duplicated_values (df):
    if df.duplicated().sum() > 0:
        df_cleaned = df.drop_duplicates(keep = 'first')
        print("-" * 50)
        print("Shape of data before removing duplicates:", df.shape)
        print("Shape of data after removing duplicates:", df_cleaned.shape)
        print("-" * 50)

        return df_cleaned
    else:
        print ('No duplicates found')

        return df