from setuptools import setup
setup(name='solcast',
      version='0.2.1',
      description='Client library for the Solcast API',
      license='MIT',
      url='https://github.com/cjtapper/solcast-py',
      author='Chris Tapper',
      author_email='cj.tapper@gmail.com',
      packages=['solcast', 'solcast.utils'],
      install_requires=[
          'requests',
          'isodate',
      ]
     )
