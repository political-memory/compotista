from setuptools import setup, find_packages

setup(name='compotista',
      version='0.0.1',
      description='OpenShift App',
      packages=['compotista'],
      package_dir={'compotista': '.'},
      author='James Pic',
      author_email='jpic@yourlabs.org',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['django'],
     )
