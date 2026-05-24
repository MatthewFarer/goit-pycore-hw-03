from datetime import datetime

# function to calculate difference in days between today and input date
def get_days_from_today(date):
    
    try:

        # transform input date string to datetime format
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        today = datetime.today().date()
        
        # calculate the difference 
        days_difference = today - input_date
        
        return days_difference.days

    except ValueError:
        return "Invalid date format. Please Use YYYY-MM-DD"
    

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2026-10-09"))
print(get_days_from_today("15.14.2021"))