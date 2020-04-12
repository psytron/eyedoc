from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("docker",  ["docker"]),
    #   ... all your modules that need be compiled ...
]
setup(
    name = 'SwarmWatch',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)