from setuptools import setup, find_packages

setup(
  name='Tado',
  version='0.1',
  author='Max Rosin',
  packages=find_packages(),
  install_requires=[
    'Click',
  ],
  entry_points={
    'console_scripts': [
      'tado = libtado.__main__:main'
    ]
  }
)
