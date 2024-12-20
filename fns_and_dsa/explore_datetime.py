from datetime import datetime, timedelta
def display_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

def calculate_future_date(days):
    now = datetime.now()
    future = timedelta(days=days)
    future_date = now + future
    return future_date.strftime("%Y-%m-%d")

def main():
    print(f"Current date and time: {display_current_datetime()}")
    days = int(input("Enter the number of days to add to the current date: "))
    print(f"Future date: {calculate_future_date(days)}")

if __name__=="__main__":
    main()
