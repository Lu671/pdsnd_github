import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #month_list[]
    cities = ['chicago','new york city','washington']
    months =['january','february','march','april','may','june']
    days =['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter City: chicago, new york city, washington: ")
    while city.lower() not in cities:
         city = input ("Please Enter one of These: chicago, new york city, washington: ")       
    #print("City: ",city)
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_filterr = input("Would you like to filter the data by month? 'yes' OR 'no': ")
    if month_filterr == 'yes':
       month = input("Enter Month, January to June: ")
       while month.lower() not in months: 
         month = input ("Please Enter a Month From Junaray To June: ")
    else: 
        month = 'all'
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_filterr = input("Would you like to filter the data by day? 'yes' OR 'no': ")
    if day_filterr == 'yes':
       day = input("Enter Day: ")
       while day.lower() not in days:
         day = input ("Please Enter a day of week: ")   
    else:
        day = 'all'

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """"
   
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # prompt the user whether they would like want to see the raw data
    print_rows(df)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    common_month = df['month'].mode()[0]
    print("most common month: ",common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("most common day: ",common_day)

    # TO DO: display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("most common start hour: ",common_start_hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0] 
    print("most commonly used start station: ",start_station)
        

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("most commonly used end station: ",end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+['End Station']
    comb = df['combination'].mode()[0]
    print("most frequent combination of start station and end station trip:  ",comb)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTime = df['Trip Duration'].sum()
    print("Total travel Time: ",totalTime)


    # TO DO: display mean travel time
    meanTime = df['Trip Duration'].mean()
    print("Mean Travel Time: ",meanTime)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    #print (len(df.columns))
    if len(df.columns) == 10 :
        print ("washington.csv does not contains gender and birth year")
    else:
       #TO DO: Display counts of gender
       gender = df['Gender'].value_counts()
       print(gender)
       #TO DO: Display earliest, most recent, and most common year of birth
       print("Earliest Year Of Birth: ",df['Birth Year'].min())
       print("Most Recent Year Of Birth: ",df['Birth Year'].max())
       print("Most Common Year Of Birth: ",df['Birth Year'].mode()[0])
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def print_rows(df):
    # Displays raw data depends on the user input.
        #Number of rows to show
        x = 5
        #Number of rows in df
        n = df.count()[0]
        #print(n)
        try:
          prompt = int(input("Would you like to see raw data? Enter 1 = yes OR 0 = no: "))
          if prompt == 1:
            print(df.head(x))
            while prompt == 1 and x < n:
                prompt = int(input("Would you like to see MORE 5 raw data? "))
                x = x+5
                print(df.head(x))
        except:
            print ("Invaild input type")        
            
        
       
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
