import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'september', 'october', 'november', 'december')


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

# get user input for city (chicago, new york city, washington).
    while True:
        city = input("Please chose the city to analyst data: \n Chicago, New York City or Washington ?\n").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Sorry, try again.\n")
            continue
        else:
            break
# get user input for filtr by (month, day, washington).
    while True:
        filtr = input("Please chose the filtr: \n month, day, both\n").lower()
        if filtr not in ('month', 'day', 'both'):
            print("Sorry, you did something wrong. Try again.\n")
            continue
        else:
            break
# get user input for month if filtr both (all, january, february, ... , june)
    if filtr in ('both'):
        while True:
                month = input("Which month do you like to see? \n Type all or name of the single month.\n").lower()
                if month not in ('all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'september', 'october', 'november', 'december'):
                    print("Sorry, you did something wrong. Try again!")
                    continue
                else:
                    break
# get user input for day if filtr both (all, monday, tuesday, ... sunday)
        while True:
                day = input("Which day do you like to see?\n Type all or name of single day.\n").lower()
                if day not in ('all','monday', 'thursday', 'wendsday', 'thursday', 'freiday', 'saturday', 'sunday'):
                    print("Sorry, you did something wrong. Try again\n")
                    continue
                else:
                    break
# get user input for month (all, january, february, ... , june)
    if filtr in ('month'):
        while True:
            day = 'all'
            month = input("Which month do you like to see? \n Type all or name of the single month. ").lower()
            if month not in ('all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'september', 'october', 'november', 'december'):
                print("Sorry, you did something wrong. Try again")
                continue
            else:
                break

 # get user input for day of week (all, monday, tuesday, ... sunday)
    if filtr in ('day'):
        while True:
            month = 'all'
            day = input("Which day?\n").lower()
            if day not in ('all','monday', 'thursday', 'wendsday', 'thursday', 'freiday', 'saturday', 'sunday'):
                print("Sorry, try again\n")
                continue
            else:
                break

    return city, month, day

    print('Hello! Let\'s explore some US bikeshare data!')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):


    #Load csv file
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #filtr data by inputs
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':

        months = MONTH_DATA
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts()
    common_month = df['month'].value_counts()
    common_day_of_week = df['day'].value_counts()

    print('Most frequent start hour:\n', popular_hour.head(1))
    print('Most frequent month: ', common_month.head(1))
    print('Most common day of week: ', common_day_of_week.head(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonly_used_start_station = df['Start Station'].value_counts()

    # display most commonly used end station
    commonly_used_end_station = df['End Station'].value_counts()

    # display most frequent combination of start station and end station trip
    commonly_used_start_ends_combination = df['Start Station'] + ' - ' + df['End Station']
    commonly_used_start_ends_combination = commonly_used_start_ends_combination.value_counts()
    print('Most commonly used start station: ', commonly_used_start_station.head(1))
    print('Most commonly used end station: ', commonly_used_end_station.head(1))
    print('Most frequent combination of start and end station: ', commonly_used_start_ends_combination.head(1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()


    print('Total travel time: ', total_time )
    print('Mean travel time: ', mean_travel_time)

    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].unique()
    count_types = df['User Type'].value_counts()
    print('Type of users: {} \n Count of users: \n{}'.format(user_types, count_types))

    # Display counts of gender
    counts_of_gender = df['Gender'].value_counts()
    print('Counts of gender:\n ', counts_of_gender)

    # Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = df['Birth Year'].min()
    most_recent_year_of_birth = df['Birth Year'].max()
    most_common_year_of_birth = df['Birth Year'].value_counts()
    print('Earliest year of birth: ', earliest_year_of_birth)
    print('Most recent year of birth: ', most_recent_year_of_birth)
    print('Most common year of birth: ', most_common_year_of_birth.head(1),'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
