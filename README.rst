===============================
Download recipe for zc.buildout
===============================

This recipe generates a configuration file for SublimeCodeIntel_, a SublimeText_ plugin .

Based on the ``mkcodeintel`` script available in optilude's SublimeTextMisc_ repository.

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

.. _SublimeCodeIntel: http://cheeseshop.python.org/pypi/corneti.recipes.codeintel

.. _SublimeText: http://www.sublimetext.com/2

.. _SublimeTextMisc: https://github.com/optilude/SublimeTextMisc