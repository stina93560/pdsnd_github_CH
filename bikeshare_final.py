# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:07:43 2022

@author: stina
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city= ' '
    while True:
        city = input('Would you like to see chicago, new york city or washington? ').lower()
        if city in cities:
            break
    
        else:
            print ('\n',"Valid city inputs Only")
            continue

    month= ' '
    while True:
        month = input('Enter a month: ').lower()
        if month in months:
            break
    
        else:
            print ('\n',"Valid month inputs Only")
            continue

    day= ' '
    while True:
        day = input('Enter a day of the week: ').lower()
        if day in days:
            break
    
        else:
            print ('\n',"Valid day inputs Only")
            continue

# return the city month and day information 
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

   
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month:', popular_month)

    # TO DO: display the most common day of week
    #df['day'] =pd.to_datetime(df['Start Time']).dt.day
    #popular_day = df['day'].value_counts(ascending=True)
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Start Day:', popular_day)  

    # TO DO: display the most common start hour
    #df['hour'] =pd.to_datetime(df['Start Time']).dt.hour
    #popular_hour = df['hour'].value_counts(ascending=True)
    popular_hour = df['hour'].mode()[0]    
    print('Most Frequent Start Hour:', popular_hour) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startStation = df['Start Station'].mode()[0]   
    print('Most Frequent Start Station:', popular_startStation) 

    # TO DO: display most commonly used end station
    
    popular_startEnd = df['End Station'].mode()[0]   
    print('Most Frequent End Station:', popular_startEnd) 

    # TO DO: display most frequent combination of start station and end station trip
    df['stationCombo'] = df['Start Station'] + ' and ' + df['End Station']
    popular_combo = df['stationCombo'].mode()[0]
    print('Most Frequent Station Combination:', popular_combo) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Sum Trip Duration:', total_travel) 

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean Trip Duration:', mean_travel) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts(ascending=True)
    print('Counts of user types\n', user_types)

    # TO DO: Display counts of gender
    
   
    if "Gender" in df.columns:       
        gender_types = df['Gender'].value_counts(ascending=True)
        print('Counts of Genders', gender_types)
    
    else:
        print('No Gender Content for this city')
              
         

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if "Birth Year" in df.columns:
        minyear = df['Birth Year'].min()
        print('Earliest month:', minyear)

        maxyear = df['Birth Year'].max()
        print('Most Recent month:', maxyear)  

        Frequent_year = df['Birth Year'].mode()[0]
        print('Most Frequent Start month:', Frequent_year) 
       
    else:
        print('No Birth Year Content for this city')

     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Asks user if they want to see 5 rows of data. If they say yes then display data.
    Then ask if they'd like to see the next 5 rows of data. Keep asking until they enter no.

     """
    print('Now Lets look at some raw data!')
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        
        view_data = input("Do you wish to continue?: ").lower()
        if view_data != 'yes':
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
