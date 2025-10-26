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
