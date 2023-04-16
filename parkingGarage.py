# Our code start here

class Garage:
    current_ticket = {}
    '''
        current_ticket: {
            {
                price: price
                paid: False/True
            }
        }
    '''
    # parking = False
    def __init__(self, tickets = 20, parking_spaces = 20, price = 0, parking = False):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.price = price
        self.parking = parking

    def driver(self):
        while True:
            res = input('Would you like to park? ').lower()
            if res == 'yes':
                self.parking = True
                self.add()
            if res == 'no':
                break

    def leaving(self):
        leave = input('are you exiting? \n')
        while True:
            paid = True
            
            print('Thank you, have a nice day')
            
    

    def add(self):
        ticket = input('How long would you like to park in minutes? 15 minutes, 30 minutes, 1 hour, 2 hour, overnight? ')
        while True:
            self.tickets -= 1
            self.parking_spaces -= 1
            if ticket == '15 minutes':
                paying = input('Your choice of parking time of 15 minutes is $2 \n')
                if paying == 'paid':
                    self.current_ticket['price'] = 2
                    self.current_ticket['paid'] = True
                    print('Thank you, have a nice day')
                    break
            if ticket == '30 minutes':
                paying = input('Your choice of parking time of 30 minutes is $4 \n')
                if paying == 'paid':
                    self.current_ticket['price'] = 4
                    self.current_ticket['paid'] = True
                    print('Thank you, have a nice day')
                    break
            if ticket == '1 hour':
                paying = input('Your choice of parking time of 60 minutes is $5 \n')
                if paying == 'paid':
                    self.current_ticket['price'] = 5
                    self.current_ticket['paid'] = True
                    print('Thank you, have a nice day')
                    break
            if ticket == '2 hours':
                paying = input('Your choice of parking time of 2 hours is $9 \n')
                if paying == 'paid':
                    self.current_ticket['price'] = 9
                    self.current_ticket['paid'] = True
                    print('Thank you, have a nice day')
                    break
            if ticket == 'overnight':
                paying = input('Your choice of parking time of overnight is $20 \n')
                if paying == 'paid':
                    self.current_ticket['price'] = 20
                    self.current_ticket['paid'] = True
                    print('Thank you, have a nice day')
                    break
            # else: 
            #     self.current_ticket[ticket] = {
            #         'price': price,
            #         'paid': False
            #     }
            self.show()
    def show(self):
        print(self.current_ticket)
        print(f'current tickets left is {self.tickets}')
        print(f'current parking spots is {self.parking_spaces}')



new_parking = Garage();

new_parking.driver()




        # if ticket not in self.current_ticket[ticket]:
        #     print('Thank you, have a nice day!')
        #     self.tickets += 1
        #     self.parking_spaces += 1
  

        

#    # def time_for_parking(self):
#     #    ticket = True
        

    


