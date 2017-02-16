from setuptools import setup, find_packages

setup(
  name='libtado',
  version='2.0.0.dev1',
  author='Max Rosin',
  author_email='libtado@hackrid.de',
  description='A library (and a command line client) to control your Tado Smart Thermostat.',
  url='https://github.com/ekeih/libtado',
  license='GPLv3+',
  packages=find_packages(),
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3',
  ],
  install_requires=[
    'click',
    'requests'
  ],
  entry_points={
    'console_scripts': [
      'tado = libtado.__main__:main'
    ]
  }
)
