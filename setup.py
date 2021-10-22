from distutils.core import setup
setup(
  name = 'build2vec',         # How you named your package folder (MyLib)
  packages = ['build2vec'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python package for building data embeddings',   # Give a short description about your library
  author = 'Mahmoud Abdelrahman',                   # Type in your name
  author_email = 'arch.mahmoud.ouf111@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/MahmoudAbdelRahman/build2Vec',   # Provide either the link to your github or to your website
  keywords = ['graph', 'embeddings', 'building', 'bim', 'gis', 'gnn'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'gensim',
          'networkx',
          'geopandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Building developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)