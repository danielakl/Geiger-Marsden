import sys

# TODO: Find formula to determine the diameter of the nuclei.
# Probability of back scattering:
#        number of alpha particles deflected
# Ps = --------------------------------------------
#        total number of alpha particles send out
#
#
# Probability of area, wait what is this shit?
#        area of nuclei
# Pa = ------------------
#        area of atoms
#
#
# Probability of back scattering with relation to area of foil:
#
# n = number of nuclei
# A = area of foil
# r = radius of nuclei
#
#        n * area pr. nucleus       n * pi * r^2
# P = ------------------------- = ----------------
#                 A                      A
#
# r = sqrt((n * pi) / (A * P))

# Returns array, first element is what file is running.
print(sys.argv)

print(input("Write something: "))
