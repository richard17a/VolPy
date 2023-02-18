"""
Docstring
"""

from volpy.velocities.generate_vimp_dist import calculate_relative_velocity
import numpy as np
import pytest


def test_calculate_relative_velocity():

	v_rel_299 = calculate_relative_velocity(tiss=2.99,
										M_star=1.,
										a_pl=1.,
										G=6.67e-11,
										AU=1.496e11,
										M_solar=1.989e30)
	v_rel_3 = calculate_relative_velocity(tiss=3.,
										M_star=1.,
										a_pl=1.,
										G=6.67e-11,
										AU=1.496e11,
										M_solar=1.989e30)

	with pytest.raises(TypeError) as e_info:
		v_rel = calculate_relative_velocity(tiss=np.linspace(2., 3., 100),
											M_star=1.,
											a_pl=1.,
											G=6.67e-11,
											AU=1.496e11,
											M_solar=1.989e30)

	with pytest.raises(TypeError) as e_info:
		v_rel = calculate_relative_velocity(tiss=2.99,
											M_star=1,
											a_pl=1.,
											G=6.67e-11,
											AU=1.496e11,
											M_solar=1.989e30)

	with pytest.raises(TypeError) as e_info:
		v_rel = calculate_relative_velocity(tiss=2.99,
											M_star=1.,
											a_pl=1,
											G=6.67e-11,
											AU=1.496e11,
											M_solar=1.989e30)

	with pytest.raises(TypeError) as e_info:
		v_rel = calculate_relative_velocity(tiss=2.99,
											M_star=1.,
											a_pl=1,
											G=6.67e-11,
											AU='AU',
											M_solar=1.989e30)

	with pytest.raises(TypeError) as e_info:
		v_rel = calculate_relative_velocity(tiss=2.99,
											M_star=1,
											a_pl=1.,
											G=6.67e-11,
											AU=1.496e11,
											M_solar=1)

	assert v_rel_299, v_rel_3
	assert np.isclose(v_rel_299 / 1e3, 29.779 * np.sqrt(3 - 2.99), rtol=1e-4)
	assert v_rel_3 == 0
