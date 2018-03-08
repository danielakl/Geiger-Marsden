class Area:
    def __init__(self, width=1.0, height=1.0):
        """
        Constructor for area.
        :param width: the width of the object in meters
        :param height: the height of the object in meters
        """
        self.width = width
        self.height = height

    def get_area(self):
        """
        Calculate the area in meters squared.
        :return: the meters squared
        """
        return self.width * self.height
