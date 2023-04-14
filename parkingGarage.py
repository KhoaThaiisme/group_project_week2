# Our code start here

class Garage():
    current_ticket = {}
    '''
        current_ticket: {
            {
                time: price
                paid: False/True
            }
        }
    '''

    def __init__(self, tickets = [20], parking_spaces = [20]):
        self.tickets = tickets
        self.parking_spaces = parking_spaces

        

    def currentTicket(self):
        pass


    def add(self):
        ticket = input('How long would you like to park in minutes? 15 minutes, 30 minutes, 1 hour, 2 hour, overnight? ')
        while True:
            self.tickets -= 1
            self.parking_spaces -= 1
            if ticket == '15 minutes':
                pass
            if ticket == '30 minutes':
                pass
            if ticket == '1 hour':
                pass
            if ticket == '2 hours':
                pass
            if ticket == 'overnight':
                pass
        if ticket not in self.current_ticket[ticket]:
            print('Thank you, have a nice day!')
            self.tickets += 1
            self.parking_spaces += 1
  

    def driver(self):
        while ticket:
            res = input('Would you like to park? ').lower()
            if res == 'yes':
                self.add()
            if res == 'no':
                pass
        

#    # def time_for_parking(self):
#     #    ticket = True
        

    
#         while ticket:
#             res_2 = input('How long would you like to park in minutes? 15 minutes, 30 minutes, 1 hour, 2 hour, overnight? ')
#             if res_2 == '15 minutes':
#                 pass
#             if res_2 == '30 minutes':
#                 pass
#             if res_2 == '1 hour':
#                 pass
#             if res_2 == '2 hours':
#                 pass
#             if res_2 == 'overnight':
#                 pass


