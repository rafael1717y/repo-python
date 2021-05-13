TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print('There are {} tickets remaining'.format(tickets_remaining))
    name = input("What is your name? ")
    number_of_tickets = input(("Hello {}. How many tickets do you want to buy?".format(name)))
    try:
        number_of_tickets = int(number_of_tickets)
        if (number_of_tickets > tickets_remaining):
            raise ValueError("There are only {} tickets remainging".format(tickets_remaining))
    except ValueError as err:
        print(f"Oh no, we ran into a issue. {err} Please try again! ")
    else:
        amount_due = calculate_price(number_of_tickets)
        print("The total due is {}.".format(amount_due))

        question = input('Do you want to proceed? Y/N ')
        if question.lower() == "y":
            print("SOLD")
            # TODO: Gather credit card information and process it.
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you {}".format(name))

# Notify user that the tickets are sold out.
print("Sorry the tickets are sold out !!!!!")


