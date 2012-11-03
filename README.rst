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

Tips
=======

Reset auto-completion by choosing *SublimeCodeIntel: Reset* in command browser (CMD + SHIFT + P) [OSX].

Force auto-completion dialog: CMD + P [OSX].

Credits
=======

Based on the ``mkcodeintel`` script available in optilude's SublimeTextMisc_ repository.

``codeintel-path`` option and much better documentation by Mikko Ohtamaa .

.. _SublimeCodeIntel: https://github.com/Kronuz/SublimeCodeIntel

.. _SublimeText: http://www.sublimetext.com/2

.. _SublimeTextMisc: https://github.com/optilude/SublimeTextMisc

