<<<<<<< HEAD
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
=======
"""
openspace.py
-------------
OpenSpace class which manages multiple tables and assigns team members randomly.

    This module depends on the Table/Seat definitions from utils.table and uses
    utils.file_utils for persisting the seating plan.
    """

import random
from utils.table import Table
from utils.file_utils import save_seating_plan

class OpenSpace:
    """ OpenSpace class which manages multiple tables and assigns team members randomly.

    This module depends on the Table/Seat definitions from utils.table and uses
    utils.file_utils for persisting the seating plan.
    """
    def __init__(self, number_of_tables: int, seats_per_table: int):
        
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]
    def organize(self, names: list):
        """Randomly assign team members to seats. The method will first shuffle the provided `names` list in-place,
        then map each name to the next available Seat. If there are more
        names than seats, only the first N names (where N is total seats)
        are assigned; extra names are ignored. If there are fewer names than
        seats, remaining seats stay empty.
        """
        random.shuffle(names)
        all_seats = [seat for table in self.tables for seat in table.seats]

        # Clear existing occupants
        for seat in all_seats:
            seat.remove_occupant()

        # Assign new occupants
        for name, seat in zip(names, all_seats):
            seat.set_occupant(name)

    def display(self):
        """
        Print a human-readable seating plan to stdout.
        The method prints the table index and the comma-separated occupants
        for each table. Empty seats are represented as the string "Empty".
        """
        print("\n Current Seating Plan:\n")
        for i, table in enumerate(self.tables, start=1):
            occupants = [seat.occupant if not seat.free else "Empty" for seat in table.seats]
            print(f"Table {i}: {', '.join(occupants)}")

    def store(self, filename: str):
        """
        Save current arrangement to file.
        """
        save_seating_plan(filename, self.tables)
>>>>>>> 4ce2fc2c56218c38a4df6541e50062536c89208b
