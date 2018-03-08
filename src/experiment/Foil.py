from atom.Gold import Gold
from geometry.Area import Area


class Foil:
    def __init__(self, area=Area(), element=Gold()):
        """
        Construct ultra thin sheet of a given element, with a given surface area.
        :param element: the element the foil is made of (default Gold)
        :param area: the surface area of the foil sheet. This is the area that
        will be bombarded with alpha particles.
        """
        self.element = element
        self.area = area
