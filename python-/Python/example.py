import datetime

"""
This script creates an empty file.
"""

filename = datetime.datetime.now()
filename = filename.strftime("%Y-%m-%d-%H-%M-%S-%f" + ".txt")


#Create empty file
def create_File():
    with open(filename, "w") as file:
        file.write("") #Writing empty string

create_File()
