"""
main.py
-------
Main entry point for the OpenSpace Classifier project.
Contains a simple example flow that instantiates OpenSpace, assigns a team,
prints the seating plan and saves it to a file.

"""

from utils.openspace import OpenSpace

def main():
    """ Run the seat assignment program using a built-in `new_collegues` list.
    This function constructs a sample `new_collegues` list, creates an OpenSpace with
    6 tables of 4 seats each, shuffles and assigns the team members, displays
    the result, and writes the seating plan to "Seating_plan.txt."""

    new_collegues = ["Aleksei","Amine","Anna","Astha","Brigitta",        #list of collegues to be assigne to each seat of the tables
                 "Bryan","Ena","Esra","Faranges","Frédéric",
                 "Hamideh","Héloïse","Imran","Intan K.",
                 "Jens","Kristin","Michiel","Nancy","Pierrick",
                 "Sandrine","Tim","Viktor","Welederufeal","Živile"]

    output_file = "Seating_plan.txt"
    open_space = OpenSpace(number_of_tables = 6 , seats_per_table = 4 )
    open_space.organize(new_collegues)
    open_space.display()
    open_space.store(output_file)

if __name__ == "__main__":
    main()
