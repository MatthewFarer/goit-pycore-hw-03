import random

def get_numbers_ticket(min, max, quantity):

# function to get unique number for a lottery with adjusted parameters

    # check if input data suits the prameters
    if (
        min < 1 or
        max > 1000 or
        min > max or
        quantity > (max - min +1) or
        quantity < 1
    ):
        return []
    

    unique_numbers = random.sample(range(min, max +1), quantity)

    return sorted(unique_numbers)


lottery_numbers = get_numbers_ticket(4, 98, 5)
print(f"Your lottery numbers: {lottery_numbers}")

lottery_numbers = get_numbers_ticket(110, 98, 4)
print(f"Your lottery numbers: {lottery_numbers}")
