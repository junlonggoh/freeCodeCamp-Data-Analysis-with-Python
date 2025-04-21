import pandas as pd

#Understanding the data
#df = pd.read_csv('adult.data.csv', header=0)
#df.info()
#df.head()
#df.shape()
#df['race'].value_counts()
#df['sex'].value_counts()
#df['education'].value_counts()
#df['salary'].value_counts()
#df['native-country'].value_counts()

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=0)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = (df['sex'] == 'Male')
    average_age_men = round(df[men]['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    num_bach_edu = df['education'].value_counts()['Bachelors']
    num_edu = df['education'].value_counts().sum()
    percentage_bachelors = round((num_bach_edu / num_edu) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # percentage with salary >50K
    num_high_edu_rich = df[higher_education]['salary'].value_counts()['>50K']
    num_high_edu = df[higher_education]['salary'].value_counts().sum()
    higher_education_rich = round((num_high_edu_rich / num_high_edu) * 100, 1)

    num_low_edu_rich = df[lower_education]['salary'].value_counts()['>50K']
    num_low_edu = df[lower_education]['salary'].value_counts().sum()
    lower_education_rich = round((num_low_edu_rich / num_low_edu) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_rich_min_workers = df.loc[df['hours-per-week'] == min_work_hours]['salary'].value_counts()['>50K']
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours].value_counts().sum()
    rich_percentage = round((num_rich_min_workers / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    num_rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    num_country = df['native-country'].value_counts()
    rich_perc_country = ((num_rich_country / num_country) * 100).sort_values(ascending = False)
    highest_earning_country = rich_perc_country.index[0]
    highest_earning_country_percentage = round(rich_perc_country.iloc[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    num_occ = rich_india['occupation'].value_counts().sort_values(ascending = False)
    top_IN_occupation = num_occ.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
