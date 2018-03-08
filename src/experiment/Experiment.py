class Experiment:
    def __init__(self, distance_to_foil, distance_to_detector, foil):
        """
        Construct the experiment.
        :param distance_to_foil: the distance from the alpha particle emitter to
                the foil.
        :param distance_to_detector: the distance from the foil to the detector
                detecting the alpha particles.
        :param foil: the foil used to shoot alpha particles through.
        """
        self.distance_to_foil = distance_to_foil
        self.distance_to_detector = distance_to_detector
        self.foil = foil
