from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='taskify',
  version='1.0.0',
  description='A task runner',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='',
  author='Benjamin Darbonne',
  author_email="dev.darbonne.ben@gmail.com",
  license='MIT',
  classifiers=classifiers,
  keywords='tasks',
  packages=find_packages(),
  install_requires=['']
)