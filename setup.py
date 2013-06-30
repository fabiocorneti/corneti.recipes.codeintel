import os
from setuptools import setup, find_packages

version = '0.3'

try:
    README = open(os.path.join(os.path.dirname(__file__), "README.rst"), "rt").read()
except IOError:
    README = ''

tests_require = ['zope.testing', 'zc.buildout']


setup(name='corneti.recipes.codeintel',
      version=version,
      description="A Sublime Text 2 / SublimeCodeIntel auto-completion data generator for buildout",
      long_description=README,
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
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='collective.recipe.pip.tests.test_docs.test_suite',
      install_requires=['setuptools', 'zc.buildout', 'zc.recipe.egg', 'simplejson'],
      entry_points={'zc.buildout': ['default = corneti.recipes.codeintel:CodeintelRecipe']},
      )
