
from assignment3 import *


def test():
    in_file = "Misc/class/class_list"
    out_file = "Misc/class/new_list"
    
    main = Main()
    main.parse_file(in_file)
    students = main.get_students("76")
    main.write_to_file(students, out_file)
    
    
if __name__ == "__main__":
    test()
