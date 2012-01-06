from setuptools import setup, find_packages
import sys, os

version = '0.1.3'

setup(name='corneti.recipes.codeintel',
      version=version,
      description="A buildout recipe that generates a configuration file for SublimeCodeIntel",
      long_description="""A buildout recipe that generates a configuration file for SublimeCodeIntel""",
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Framework :: Buildout',
            'Framework :: Buildout :: Recipe',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Text Editors'
      ],
      keywords='sublimetext sublimecodeintel editor buildout recipe',
      author='Fabio Corneti',
      author_email='info@corneti.com',
      url='https://github.com/fabiocorneti/corneti.recipes.codeintel',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['corneti', 'corneti.recipes'],
      include_package_data=True,
      zip_safe=False,
      install_requires = ['setuptools', 'zc.buildout', 'zc.recipe.egg',], 
      entry_points = { 'zc.buildout' : ['default = corneti.recipes.codeintel:CodeintelRecipe'] },
      )
