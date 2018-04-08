class Volume:
    def __init__(self, width=1.0, height=1.0, depth=1.0):
        """
        Constructor for volume.
        :param width: the width of the object in meters
        :param height: the height of the object in meters
        :param depth: the depth of the object in meters
        """
        self.width = width
        self.height = height
        self.depth = depth

    def get_area(self):
        """
        Calculate the area in meters squared.
        :return: the meters squared
        """
        return self.width * self.height

    def get_volume(self):
        """
        Calculate the volume in cubic meters.
        :return: the cubic meters
        """
        return self.width * self.height * self.depth
