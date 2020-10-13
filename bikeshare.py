import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters(city, month, day):

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Write a city name: Chicago, New York City or Washington!").lower()
        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue
        else:
            break

    while True:
        time = input("Do you want to filter as month, day, all or none?").lower()
        if time == 'month':
            month = input("Which month? January, February, March, April, May or June?").lower()
            day = 'all'
            break

        elif time == 'day':
            month = 'all'
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break

        elif time == 'all':
            month = input("Which month? January, February, March, April, May or June?").lower()
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break
        elif time == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("Wrong word! Please type it again. month, day, all or none?")
            break

    print(city)
    print(month)
    print(day)
    print('-' * 40)
    return city.lower(),month.lower(),day.lower()


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("No gender information available in this city.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("No birth year information available in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def duration_in_mins(datum, city):
    """
        Takes as input a dictionary containing info about a single trip (datum) and
        its origin city (city) and returns the trip duration in units of minutes.
        Washington is in terms of milliseconds while Chicago and NYC
        are in terms of seconds.
    """
    from datetime import datetime
    if city == 'New York City':
        duration = float(datum['tripduration']) / 60
    elif city == 'Chicago':
        duration = float(datum['tripduration']) / 60
    elif city == 'Washington':
        duration = float(datum['Duration (ms)']) / 60000
    return duration

tests = {'New York City': 13.9833, 'Chicago': 15.4333, 'Washington': 7.1231}
for city in tests:
    assert (abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001)


def time_of_trip(datum, city):

    from datetime import datetime
    if city == 'New York City':
        starttime = datum['starttime']
        d1 = datetime.strptime(starttime, '%m/%d/%Y %H:%M:%S')
        day_of_week=d1.strftime('%A')
        return (d1.month, d1.hour, day_of_week)
    elif city == 'Chicago':
        starttime = datum['starttime']
        d2 = datetime.strptime(starttime, '%m/%d/%Y %H:%M')
        day_of_week=d2.strftime('%A')
        return (d2.month, d2.hour, day_of_week)
    elif city == 'Washington':
        starttime = datum['Start date']
        d3 = datetime.strptime(starttime, '%m/%d/%Y %H:%M')
        day_of_week=d3.strftime('%A')
        return (d3.month, d3.hour, day_of_week)

tests = {'New York City': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}


for city in tests:
    assert time_of_trip(example_trips[city], city) == tests[city]
def data(df):
    raw_data = 0
    while True:
        answer = input("Wanna see the raw data? Yes or No").lower()
        if answer not in ['yes', 'no']:
            answer = input("Wrong word! Please type Yes or No.").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data: raw_data + 5])
            again = input("Wanna see more? Yes or No").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nDo you want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
