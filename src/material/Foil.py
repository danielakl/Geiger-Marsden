from atom.Gold import Gold
from geometry.Volume import Volume

AVOGADRO = 6.02214179e23


class Foil:
    def __init__(self, volume=Volume(), element=Gold):
        """
        Constructor for foil.
        :param volume: the volume of the foil.
        :param element: the element the foil is made of.
        """
        self.volume = volume
        self.element = element

    def get_mass(self):
        """
        Calculate the mass of the foil.
        :return: the mass of the foil in grams.
        """
        return self.volume.get_volume() * self.element.density

    def get_atoms(self):
        """
        Calculate the amount of atoms in the foil.
        :return: the amount of atoms.
        """
        return int((self.get_mass() / self.element.atomicWeight) * AVOGADRO)
