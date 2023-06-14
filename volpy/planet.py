"""
Module containing the Planet class.
"""

from astropy import constants as const # pylint: disable=import-error
import numpy as np # pylint: disable=import-error


class Planet():
    """
    A class representing a planet.

    Attributes:
        mass (float): The mass of the planet.
        radius (float): The radius of the planet.
        semimajor_axis (float): The semi-major axis of the planet's orbit.
    """

    def __init__(self,
                 mass: float,
                 radius: float,
                 semimajor_axis: float):
        """
        Initialize a planet object with given mass, radius, and semi-major axis.

        Args:
            mass (float): The mass of the planet.
            radius (float): The radius of the planet.
            semimajor_axis (float): The semi-major axis of the planet's orbit.
        """

        self.mass = mass
        self.radius = radius
        self.semimajor_axis = semimajor_axis

    @property
    def mass(self):
        """
        Get the mass of the planet.

        Returns:
            float: The mass of the planet.
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """
        Set the mass of the planet.

        Args:
            mass (float): The mass of the planet.

        Raises:
            TypeError: If the mass is not of type float.
        """
        if not isinstance(mass, float):
            raise TypeError("Mass attribute of Planet object must be a float.")
        if isinstance(mass, float):
            # Store the mass in the private variable _mass
            self._mass = mass

    @property
    def radius(self):
        """
        Get the radius of the planet.

        Returns:
            float: The radius of the planet.
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """
        Set the radius of the planet.

        Args:
            radius (float): The radius of the planet.

        Raises:
            TypeError: If the radius is not of type float.
        """
        if not isinstance(radius, float):
            raise TypeError("Radius attribute of Planet object must be a float.")
        if isinstance(radius, float):
            self._radius = radius

    @property
    def semimajor_axis(self):
        """
        Get the semi-major axis of the planet's orbit.

        Returns:
            float: The semi-major axis of the planet's orbit.
        """
        return self._semimajor_axis

    @semimajor_axis.setter
    def semimajor_axis(self, semimajor_axis):
        """
        Set the semi-major axis of the planet's orbit.

        Args:
            semimajor_axis (float): The semi-major axis of the planet's orbit.

        Raises:
            TypeError: If the semi-major axis is not of type float.
        """
        if not isinstance(semimajor_axis, float):
            raise TypeError("Semi-major axis attribute of Planet object must be a float.")
        if isinstance(semimajor_axis, float):
            self._semimajor_axis = semimajor_axis

    def calculate_escape_velocity(self):
        """
        Calculate the escape velocity of the planet.

        Returns:
            float: The escape velocity of the planet.
        """
        v_esc = np.sqrt( (2 * const.G.value * self.mass * const.M_sun.value) /
                     (self.radius * const.au.value))

        return v_esc
