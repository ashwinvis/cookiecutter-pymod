Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   modules
   contributing
   {% if cookiecutter.create_thanks_file == 'y' -%}thanks
   {% endif -%}history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
