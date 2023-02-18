"""
Docstring
"""

import numpy as np 


def calculate_relative_velocity(tiss: float,
								M_star: float, 
								a_pl: float, 
								G: float, 
								AU: float, 
								M_solar: float):
	"""
	Docstring

	v_rel = v_kep * sqrt(3 - Tiss)

	"""

	if not isinstance(tiss, float):
		raise TypeError
	if not isinstance(M_star, float):
		raise TypeError
	if not isinstance(a_pl, float):
		raise TypeError
	if not isinstance(G, float):
		raise TypeError
	if not isinstance(AU, float):
		raise TypeError
	if not isinstance(M_solar, float):
		raise TypeError

	v_kep = np.sqrt((G * M_star * M_solar) / (a_pl * AU))
	v_rel = v_kep * np.sqrt(3 - tiss)

	return v_rel
