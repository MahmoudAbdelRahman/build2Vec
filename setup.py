from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'Python package for building data embeddings'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name = 'build2vec',         # How you named your package folder (MyLib)
    version=VERSION,
    author="Mahmoud Abdelrahman",
    author_email="<arch.mahmoud.ouf111@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[            # I get to this in a second
          'gensim',
          'networkx',
          'geopandas',
          'tqdm',
      ],
    keywords=['graph', 'network', 'building', 'spatial', 'spatiotemporal', 'bim', 'gis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
