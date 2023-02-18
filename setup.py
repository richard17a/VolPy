"""
setup module docstring
"""

from setuptools import setup, find_packages
setup(
    name='volpy',
    version='0.0.1',
    author='Richard Anslow',
    author_email='r.anslow@outlook.com',
    url='https://github.com/richard17a/VolPy',
    license='GNU License',
    packages=['volpy', 'volpy.velocities'],
    description='An example of building Python package.',
    install_requires=[
    #'python>=3.6.0',
    #'pandas>=0.10.0'
    ]
)
