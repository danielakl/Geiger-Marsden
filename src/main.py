import math
import sys
from random import uniform

from atom.Gold import Gold

from geometry.Volume import Volume
from material.Foil import Foil


def execute_experiment(alpha_particles=0, foil=Foil()):
    """
    Execute the experiment.
    :param alpha_particles: The amount of alpha particles to fire at the foil
    :param foil: The foil to fire at
    :return: An array, first element is how many particles hit a nucleus, the second element is the calculated radius of
    the nucleus of the atoms the foil consist off.
    """

    # Calculate how much of the foil is gold nuclei.
    foil_nucleus_area = foil.get_atoms() * Gold.nucleusArea

    # Firing alpha particles
    hits = 0
    for i in range(0, alpha_particles):
        random = uniform(0, foil.volume.get_area())  # Random hit on foil, high = miss, low = hit.
        if random <= foil_nucleus_area:  # A particle hits if the random roll was low enough to hit the nucleus area
            hits = hits + 1

    return hits, math.sqrt((foil.volume.get_area() * hits / alpha_particles) / (math.pi * foil.get_atoms()))


# Default values
alphaCount = 1000000
width = 0.2
height = 0.2

# Process command line arguments.
argSize = len(sys.argv)
if argSize >= 4:
    try:
        height = round(abs(float(sys.argv[3])), 2)
    except ValueError:
        print("Invalid command line argument given for 'height of gold foil', was '" + sys.argv[3]
              + "' but expected a number.")
if argSize >= 3:
    try:
        width = round(abs(float(sys.argv[2])), 2)
    except ValueError:
        print("Invalid command line argument given for 'width of gold foil', was '" + sys.argv[2]
              + "' but expected a number.")
if argSize >= 2:
    try:
        alphaCount = abs(int(sys.argv[1]))
    except ValueError:
        print("Invalid command line argument given for 'number of alpha particles', was '" + sys.argv[1]
              + "' but expected a number.")
if argSize == 1:
    print("Start this program with command line arguments to change default variables.\n"
          "Arguments can be:\n"
          "1. Number of alpha particles to fire.\n"
          "2. Width of gold foil in meters.\n"
          "3. Height of gold foil in meters.")

# Define foil to use.
foil = Foil(Volume(width, height, 0.003), Gold)

# Print values used.
print("\nRunning experiment with the following variables.\n"
      "Alpha particles:", alphaCount, "\n"
      "Width:", str(width), "m.\n"
      "Height:", str(height), "m.\n"
      "Surface area of gold foil:", round(foil.volume.get_area(), 4), "meters squared.")

# Execute experiment.
result = execute_experiment(alphaCount, foil)

# Print result
print("\nResults:")
print(result[0], "of", alphaCount, "alpha particles hit a gold nucleus.")
print(str(round(result[0] / (alphaCount - result[0]), 4)) + "% of particles hit.")
print("The calculated radius of a gold nucleus is:", str(result[1]), "m.")
print("The actual radius of a gold nucleus is:", str(Gold.nucleusRadius), "m")
