"""
Module docstring
"""

class Star():
    """
    Star docstring
    """

    def __init__(self,
                 mass: float):

        self.mass = mass

    @property
    def mass(self):
        """
        Docstring
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """
        Docstring
        """
        if not isinstance(mass, float):
            raise TypeError("Mass attribute of Star object must be a float.")
        if isinstance(mass, float):
            self._mass = mass


    @property
    def radius(self):
        """
        Docstring
        """
        return self.mass ** 0.8
