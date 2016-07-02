from setuptools import setup

import autopython
import codecs

setup(
  name = 'autopython',
  version = autopython.__version__,
  license = 'GPLv3',

  description = 'Autoscripting for Python 3',
  long_description='Autoscripting Python for your presentations',

  packages = ['autopython'],
  scripts = ['bin/autopython'],
  
  install_requires = [
    'colorama',
    'Pygments',
  ],
  
  url = 'https://github.com/gosella/autopython',
  download_url = 'https://github.com/gosella/autopython',

  author = 'Germán Osella Massa',
  author_email = 'german.osella@nexo.unnoba.edu.ar',
  maintainer = 'Germán Osella Massa',
  maintainer_email = 'german.osella@nexo.unnoba.edu.ar',
  
  keywords = ['python3', 'presentation', 'autoscripting'],
  classifiers = [],
)
