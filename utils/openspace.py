import random
from table import Table
from seat import Seat  
class OpenSpace():
    def __init__(self, number_of_tables, seats_per_table=4):

        """
        Initialize the OpenSpace with a given number of tables and seats per table.
        Args: 
             number_of_tables(int): Number of tables in the open space.
             seats_per_table(int) : Number of seats peer table

        """
        self.number_of_table = number_of_tables
        self.tables =[Table(seats_per_table) for _ in range(number_of_tables=6)]
   
   
    def organize(self, names):

        """
        Randomly assigns people to available seats in the open space.
        Args:
             names(list): List of names to assign to seats.4

          """    
        random.shuffle(names)    #   Randomize seating
        all_seats = []
        for table in self.tables:
            for seat in table.seats:
                all_seats.append(seat)
        for seat in all_seats:
            seat.remove_occupant()
        for name, seat in zip(names,all_seats):
            seat.set_occupant(name)
    def display(self):
         """
         Print a readable representation of all tables and their occupants.

         """
         for i , table in enumerate(self.tables, start = 1):
            occupants = [seat.occupant if not seat.free else "Empty" for seat in table.seats]
            print(f"Table {i}: {', '.join(occupants)}")
    def store(self, Seating_plan):
     
          """
         Store the current seat distribution into a file called 'seating_plan'.

         Args:
         filename (str): The name of the file to store seating arrangement.
         """
          with open("Seating_plan.txt", "w") as file:
            for i, table in enumerate(self.tables, start=1):
               occupants = [seat.occupant if not seat.free else "Empty" for seat in table.seats]
            file.write(f"Table {i}: {', '.join(occupants)}\n")
            print(f"Seating arrangement saved to '{filename}' successfully!")
