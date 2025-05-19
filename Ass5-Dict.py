#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kaint
#
# Created:     19-05-2025
# Copyright:   (c) Kaint 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

std_dict = {"Sam" : 95, "alice" : 85, "Nick": 98}
name1 = input("Enter the student name :- ")
if name1 in std_dict:
    print("{}'s marks:".format(name1), std_dict[name1])
else:
    print("{} student not found".format(name1))