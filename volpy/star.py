"""
Module containing the Star class.
"""

class Star():
    """
    A class representing a star.

    Attributes:
        mass (float): The mass of the star.
    """

    def __init__(self,
                 mass: float):
        """
        Initialize a star object with a given mass.

        Args:
            mass (float): The mass of the star.
        """

        self.mass = mass

    @property
    def mass(self):
        """
        Get the mass of the star.

        Returns:
            float: The mass of the star.
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """
        Set the mass of the star.

        Args:
            mass (float): The mass of the star.

        Raises:
            TypeError: If the mass is not of type float.
        """
        if not isinstance(mass, float):
            raise TypeError("Mass attribute of Star object must be a float.")
        if isinstance(mass, float):
            # Store the mass in the private variable _mass
            self._mass = mass


    @property
    def radius(self):
        """
        Calculate and get the radius of the star.

        Returns:
            float: The radius of the star.
        """
        # Calculate and return the radius based on the mass
        return self.mass ** 0.8
