==================================================
SublimeCodeIntel configuration recipe for buildout
==================================================

This recipe generates a configuration file for SublimeCodeIntel_, a SublimeText_ plugin .

To use it, add a codeintel configuration section to your ``buildout.cfg`` file and the corresponding part::

    [buildout]
    parts =
        django
        codeintel

    ...

    [codeintel]
    recipe = corneti.recipes.codeintel
    eggs = ${django:eggs}
    extra-paths =
        ${django:location}
        ${django:extra-paths}

Setting .codeintel folder
===========================

SublimeCodeIntel will pick up auto-completion information from ``.codeintel``
folder from your Sublime Text project root.

By default, this recipe generates the folder in the buildout root.
You can specify optional ``codeintel-path`` if you want to generate
``.codeintel`` in some other location.

Example how to create CodeIntel information inside ``src/`` folder.
Usually ``src/`` is used for all Python eggs you are currently developing yourself i.e.
essentially all of your project codebase::

    [codeintel]
    recipe = corneti.recipes.codeintel
    eggs = ${instance:eggs}
    codeintel-path = ${buildout:directory}/src/.codeintel

This will generate file ``src/.codeintel/config`` which will list all your eggs
used by ``[instance]`` in your *buildout.cfg*.

Now you can open your ``src/`` folder as project in Sublime with perfect auto-completion support::

    subl src

... or just open src/ folder using *File > Open folder*.

(`See how to configure Sublime Text 2 commaline commands <http://opensourcehacker.com/2012/05/11/sublime-text-2-tips-for-python-and-web-developers/>`_)


We'll start by creating a buildout that uses the recipe::

We form a config which uses paths for every language supported::

    >>> from corneti.recipes.codeintel import CodeintelRecipe
    >>> extra_info = "\n".join(map(lambda x: r"""
    ... {0}-path = /some/bin/{0}
    ... {0}-extra-paths = /some/{0}/path
    ...                   /some/{0}/path2
    ... """.format(x.lower()), CodeintelRecipe.SUPPORTED_LANGUAGES))
    >>> write('buildout.cfg',
    ... r"""
    ... [buildout]
    ... parts = codeintel
    ... newest = false
    ...
    ... [codeintel]
    ... recipe = corneti.recipes.codeintel
    ... eggs = zc.buildout
    ... {0}
    ... """.format(extra_info))

Running the buildout gives us::

    >>> print system(buildout)
    Installing codeintel.

We see the folder with codeintel config is created::

    >>> print ls('.')
    d  .codeintel
    ...

    >>> print ls('./.codeintel')
    -  config
    ...

We check the contents of the config::

    >>> import os
    >>> import simplejson
    >>> import pprint
    >>> contents = open(os.path.join('.codeintel', 'config')).read()
    >>> contents_json = simplejson.loads(contents)
    >>> '/some/python/path' in contents_json['Python']['pythonExtraPaths']
    True
    >>> '/some/python/path2' in contents_json['Python']['pythonExtraPaths']
    True
    >>> len(contents_json['Python']['pythonExtraPaths'])
    4

We check that every lang is present in config::

    >>> contents_json.keys() == CodeintelRecipe.SUPPORTED_LANGUAGES
    True

Let's check the usage with only one additional language::

    >>> write('buildout.cfg',
    ... r"""
    ... [buildout]
    ... parts = codeintel
    ... newest = false
    ...
    ... [codeintel]
    ... recipe = corneti.recipes.codeintel
    ... eggs = zc.buildout
    ... javascript-extra-paths = /some
    ... """)

    >>> print system(buildout)
    Uninstalling codeintel.
    Installing codeintel.

    >>> contents = open(os.path.join('.codeintel', 'config')).read()
    >>> contents_json = simplejson.loads(contents)

    >>> len(contents_json) == 2
    True

    >>> contents_json['JavaScript']
    {'javascriptExtraPaths': ['/some']}


Tips
=======

Reset auto-completion by choosing *SublimeCodeIntel: Reset* in command browser (CMD + SHIFT + P) [OSX].

Force auto-completion dialog: CMD + P [OSX].

Testing
=======

To test this recipe, bootstrap the included buildout, build it and execute the test section::

    $ python bootstrap.py
    $ bin/buildout -v
    $ bin/buildout test

If the first command gives you a setuptools dependency error, try the following variant to use distribute::

    $ python bootstrap.py -d
    $ bin/buildout -v
    $ bin/buildout test

Credits
=======

Based on the ``mkcodeintel`` script available in optilude's SublimeTextMisc_ repository.

``codeintel-path`` option and much better documentation by Mikko Ohtamaa .

.. _SublimeCodeIntel: https://github.com/Kronuz/SublimeCodeIntel

.. _SublimeText: http://www.sublimetext.com/2

.. _SublimeTextMisc: https://github.com/optilude/SublimeTextMisc

