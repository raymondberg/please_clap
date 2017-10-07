from setuptools import setup

setup(
  name='please_clap',
  version='0.1.0',
  description='A Python Module to help through those tough times',
  url='http://github.com/raymondberg/please_clap',
  author='Raymond Berg',
  author_email='dev@raymondberg.com',
  license='MIT',
  packages=['please_clap'],
  package_data={
    'please_clap': ['*.wav']
  },
  install_requires=[
    'simpleaudio',
  ],
  scripts=['bin/please-clap'],
  zip_safe=False
)

