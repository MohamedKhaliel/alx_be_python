from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ",current_date)
    return current_date
display_current_datetime()

number_of_days = input("Enter the number of days to add to the current date: ")

def calculate_future_date(number_of_days):
    future_date = datetime.datetime.now() + datetime.timedelta(days=int(number_of_days))
    return future_date.strftime("%Y-%m-%d %H:%M:%S")
print("Future date: ", calculate_future_date(number_of_days))
