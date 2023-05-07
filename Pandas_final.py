
import pandas as pd
import matplotlib.pyplot

def pandas(self, file):
    """
    Reads a guest list in the form ofCSV file using pandas and performs various analyses on the data.

    Args:
        file (str): The path to the CSV file.

    Returns:
        None
    """
    df = pd.read_csv(file)

    # RSVP Guest List
    guestlist_df = df.loc[:, ['First Name', 'Last Name', 'RSVP Status']]
    print(guestlist_df)
    print(df['Dietary Restriction'].unique())
     #gender count bar graph
    sex_df = df['Sex'].value_counts()
    print(sex_df)
    sex_df.plot.bar(x=['Male', 'Female'], y=sex_df)

    #age group bar graph
    children = df['Age'] <= 12
    teenagers = (df['Age'] > 12) & (df['Age'] <= 21)
    adults = df['Age'] > 21

    age_groups = ['Children', 'Teenagers', 'Adults']
    age_counts = [len(df[children]), len(df[teenagers]), len(df[adults])]
    age_counts_df = pd.df({'Age Group': age_groups, 'Count': age_counts})
    age_counts_df.plot.bar(x='Age Group', y='Count')