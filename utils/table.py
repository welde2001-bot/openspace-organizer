<<<<<<< HEAD
class Seat:
    """
    Represents a seat with an occupant status.
    """
    def __init__(self) -> None:
        """
        Initializes a Seat object with free status and no occupant.
        """
        self.free = True
        self.occupant = ""

    def set_occupant(self, name: str):
        """
        Sets the occupant of the seat if it is free.
        Args:
            name (str): The name of the person to occupy the seat.
        """
        if self.free == True:
            self.occupant = name
            self.free = False
        else:
            print("Seat is already occupied.")
            return None
    def remove_occupant(self) -> str:
        """
        Removes the occupant from the seat if it is occupied.
        Returns:
            str: The name of the removed occupant, or None if the seat was already free.
        """
        if self.free == False:
            name = self.occupant
            self.occupant = ""
            return name
        else:
            print("Seat is already free.")
            return None


                             #Step 2: Build a Table
#from seat import SEAT

class Table():
    def __init__(self, capacity=4):
        """Create a table with a given number of seats."""
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity = 4)]  # make a list of Seat objects
        
        #super().__init__()
    def has_free_spot(self):
        """Check if any seat is still available."""
        for seat in self.seats:
            if seat.free:
                return True
        # If no seat was free
        return False

    def assign_seat(self, name: str):
        """Assign a person to the first free seat at this table."""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                print(f"{name} was assigned a seat.")
                return True
        # If no seat was found free
        print("No free seats at this table.")
        return False

    def left_capacity(self):
        """Count how many seats are still empty."""
        free_seats = 0
        for seat in self.seats:
            if seat.free:
                free_seats += 1
        print(f"Number of empty seats: {free_seats}")
        return free_seats
    class Openspace:
        def __init__(self, tables, numbers_of_tables):
            self.tables = tables
            self.numbers_of_tables = numbers_of_tables
            

=======
"""
table.py
--------
Contains the Seat and Table classes for OpenSpace seat management.
"""

class Seat:

    """Represents a single seat in the open space."""
    
    def __init__(self):
         """
        Initialize a Seat instance as free and without an occupant.
        """
         self.free = True
         self.occupant = None

    def set_occupant(self, name: str):

        """
        Assign an occupant to the seat if it is free.

        Parameters
        ----------
        name : str
            The name of the person to assign to this seat.
            """
        
        if self.free:
            self.occupant = name
            self.free = False
        else:
            print(f" Seat already occupied by {self.occupant}.")

    def remove_occupant(self):

        """Free the seat if currently occupied."""
        
        if not self.free:
            self.occupant = None
            self.free = True
        else:
            return True    #Return True if the Seat is already free.


class Table:

    """Represents a table with several seats."""
    
    def __init__(self, capacity: int):

        """
        Create a Table with `capacity` Seat instances.
        """
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self) -> bool:

        """Check if there is at least one available seat."""
        
        return any(seat.free for seat in self.seats)

    def left_capacity(self) -> int:

        """
        Count how many seats at the table are free.

        Returns
        -------
        int
            Number of free seats at this table.
        """
        
        return sum(1 for seat in self.seats if seat.free)
>>>>>>> 4ce2fc2c56218c38a4df6541e50062536c89208b
