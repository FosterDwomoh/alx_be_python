from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"current date and time:{formatted_date}")

    def calculate_future_date():
        try:
            num_days = int(input("Enter the number of days to add tp the current date:"))
            current_date = datetime.datetime.now()
            future_date = current_date + datetime.timedelta(days=num_days)
            formatted_future_date = future_date.strftime("%Y-%m-%d")
            print(f"future date after {num_days} days: {formatted_future_date}")
        except valueError:
            print("Invalid input. Please enter a valid integer number of days.")
            def main():
                display_current_datetime()
                calculate_future_date()
                if_name_=="_main_":
                    main()
