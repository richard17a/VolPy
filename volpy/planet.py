"""
An abstract planet object
"""

from astropy import constants as const # pylint: disable=import-error
import numpy as np # pylint: disable=import-error


class Planet():
    """
    Planet docstring
    """

    def __init__(self,
                 mass: float,
                 radius: float,
                 semimajor_axis: float):

        self.mass = mass
        self.radius = radius
        self.semimajor_axis = semimajor_axis

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
            raise TypeError("Mass attribute of Planet object must be a float.")
        if isinstance(mass, float):
            self._mass = mass

    @property
    def radius(self):
        """
        Docstring
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """
        Docstring
        """
        if not isinstance(radius, float):
            raise TypeError("Radius attribute of Planet object must be a float.")
        if isinstance(radius, float):
            self._radius = radius

    @property
    def semimajor_axis(self):
        """
        Docstring
        """
        return self._semimajor_axis

    @semimajor_axis.setter
    def semimajor_axis(self, semimajor_axis):
        """
        Docstring
        """
        if not isinstance(semimajor_axis, float):
            raise TypeError("Semi-major axis attribute of Planet object must be a float.")
        if isinstance(semimajor_axis, float):
            self._semimajor_axis = semimajor_axis

    def calculate_escape_velocity(self):
        """
        Docstring
        """
        v_esc = np.sqrt( (2 * const.G.value * self.mass * const.M_sun.value) /
                     (self.radius * const.au.value))

        return v_esc
