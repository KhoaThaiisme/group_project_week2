

class ParkingGarage:
    def __init__(self):
        self.tickets = list(range(1, 21))
        self.parked_cars = {}

    def park_car(self):
        if not self.tickets:
            print("Sorry, the garage is full.")
            return
        ticket = self.tickets.pop(0)
        park_time = self.get_park_time()
        self.parked_cars[ticket] = (park_time, False)
        print(f"Your ticket number is {ticket}. You have parked for {park_time} minutes.")
        print(self.parked_cars)

    def get_park_time(self):
        while True:
            park_time = input("How long would you like to park? (15, 30, or 60 minutes): ")
            if park_time not in ["15", "30", "60"]:
                print("Invalid input. Please choose 15, 30, or 60 minutes.")
            else:
                return int(park_time)

    def pay_for_parking(self):
        ticket = self.get_ticket()
        if ticket not in self.parked_cars:
            print("Invalid ticket number.")
            return
        if self.parked_cars[ticket][1]:
            print("Your ticket has already been paid.")
            return
        payment = self.get_payment_amount(self.parked_cars[ticket][0])
        print(f"Your payment of ${payment} has been accepted. You have 15 minutes to leave.")
        self.parked_cars[ticket] = (self.parked_cars[ticket][0], True)

    def get_ticket(self):
        return int(input("Please enter your ticket number: "))


    def get_payment_amount(self, park_time):
        if park_time == 15:
            return 5
        elif park_time == 30:
            return 9
        elif park_time == 60:
            return 16
        else:
            return 0

    def leave_garage(self):
        ticket = self.get_ticket()
        if ticket not in self.parked_cars:
            print("Invalid ticket number.")
            return
        if not self.parked_cars[ticket][1]:
            self.pay_for_parking()
        print("Thank you, have a nice day!")
        self.tickets.append(ticket)
        del self.parked_cars[ticket]

    def start_parking(self):
        while True:
            action = input("What would you like to do? (park, pay, leave, or quit): ")
            if action == "park":
                self.park_car()
            elif action == "pay":
                self.pay_for_parking()
            elif action == "leave":
                self.leave_garage()
            elif action == "quit":
                print("Thank you, have a nice day!")
                break
            else:
                print("Invalid input. Please choose park, pay, leave, or quit.")

garage = ParkingGarage()
garage.start_parking()