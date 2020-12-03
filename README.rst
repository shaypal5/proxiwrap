proxiwrap ᘯ
#######

.. |PyPI-Status| |Downloads| |PyPI-Versions| |Build-Status| |Codecov| |Codefactor| |LICENCE|

Dike helps you select pre-trained word embedding for your data.

.. |proxiwrap_icon| image:: https://github.com/shaypal5/proxiwrap/blob/cc5595bbb78f784a3174a07157083f755fc93172/proxiwrap.png
   :height: 87
   :width: 40 px
   :scale: 50 %
   
.. .. image:: https://github.com/shaypal5/proxiwrap/blob/b10a19a28cb1fc41d0c596df5bcd8390e7c22ee7/proxiwrap.png

.. code-block:: python

  from proxiwrap import select_embedding
  select_embedding(df['description'])

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install proxiwrap


Methodology
===========

``proxiwrap`` attempts to generate several metrics that might help capture the measure of representativeness/suitability of each embedding to your text data:

* **Vocabulary-based:**

  * The simple intersection between your data's vocabulary and that of the examined word embedding.
  * Vocabulary intersection weighted by word importance in your data; word importance can be given by various measures.
  * Count of missing word occurences.
  * Count of documents with at least 1/2/etc. missing words.

* **Information content:** Each document is projected into the embedding space by averaging the word vectors of the words it is composed off. Then, for each resulting projection of the entire corpus into the embedding space, the information content is estimated by presenting the number of dimension required by PCA to capture increasing thresholds of the information in the resulting space.


Use
===



Configuring proxiwrap
=================

Configure ``proxiwrap`` by populating the ``~/.config/proxiwrap/cfg.json`` file with the follosing possible configuration key-value pairs:

.. code-block:: python

  {
      "datadir": "/home/myuser/data/"  # directory where data and embedding files are downloaded to
  }

Corresponding environment variables which can be used for configuration:

* ``DIKE_DATADIR`` - Populate with the path to the directory where data and embedding files are downloaded to.



Supported embeddings
====================

gensim
------

* `word2vec-google-news-300 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/word2vec-google-news-300>`_ - Pre-trained vectors trained on a part of the Google News dataset (about 100 billion words). The model contains 300-dimensional vectors for 3 million words and phrases. Size: 1.6GB.

* `glove-twitter-200 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-200>`_ - Pre-trained 200-dimensinal glove vectors based on 2B tweets, 27B tokens, 1.2M vocab, uncased. Size: 759MB.

* `glove-twitter-100 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-100>`_ - Pre-trained 100-dimensional glove vectors based on 2B tweets, 27B tokens, 1.2M vocab, uncased. Size: 387MB.

* `glove-twitter-50 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-50>`_ - Pre-trained 50-dimensional glove vectors based on 2B tweets, 27B tokens, 1.2M vocab, uncased. Size: 200MB.

* `glove-twitter-25 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-25>`_ - Pre-trained 25-dimensional glove vectors based on 2B tweets, 27B tokens, 1.2M vocab, uncased. Size: 105MB.

* `glove-wiki-gigaword-300 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-300>`_ - Pre-trained 300-dimensional glove vectors based on Wikipedia 2014 + Gigaword, 5.6B tokens, uncased. Size: 376MB.

* `glove-wiki-gigaword-200 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-200>`_ - Pre-trained 200-dimensional glove vectors based on Wikipedia 2014 + Gigaword, 5.6B tokens, uncased. Size: 252MB.

* `glove-wiki-gigaword-100 <https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-100>`_ - Pre-trained 100-dimensional glove vectors based on Wikipedia 2014 + Gigaword, 5.6B tokens, uncased. Size: 128MB.


Contributing
============

Package author and current maintainer is `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/proxiwrap.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd proxiwrap
  pip install -e '.[test]'


Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd proxiwrap
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Created by `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com).

``proxiwrap`` is named after `Dike, the Greek goddess of justice <https://en.wikipedia.org/wiki/Dike_(mythology)>`_, as she is meant to help you make the right choice of pre-trained word embeddings. The symbol ᘯ was chosen for its visual similarity to the Libra symbol, the constellation representing Dike.


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/proxiwrap.svg
  :target: https://pypi.python.org/pypi/proxiwrap

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/proxiwrap.svg
   :target: https://pypi.python.org/pypi/proxiwrap

.. |Build-Status| image:: https://travis-ci.org/shaypal5/proxiwrap.svg?branch=master
   :target: https://travis-ci.org/shaypal5/proxiwrap

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://github.com/shaypal5/proxiwrap/blob/master/LICENSE

.. |Codecov| image:: https://codecov.io/github/shaypal5/proxiwrap/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/proxiwrap?branch=master

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/99e79faee7454a13a0e60219c32015ae
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/shaypal5/proxiwrap?utm_source=github.com&utm_medium=referral&utm_content=shaypal5/proxiwrap&utm_campaign=Badge_Grade_Dashboard

.. |Requirements| image:: https://requires.io/github/shaypal5/proxiwrap/requirements.svg?branch=master
   :target: https://requires.io/github/shaypal5/proxiwrap/requirements/?branch=master
   :alt: Requirements Status
     
.. |Codefactor| image:: https://www.codefactor.io/repository/github/shaypal5/proxiwrap/badge?style=plastic
   :target: https://www.codefactor.io/repository/github/shaypal5/proxiwrap
   :alt: Codefactor code quality

.. |Downloads| image:: https://pepy.tech/badge/proxiwrap
   :target: https://pepy.tech/project/proxiwrap
   :alt: PePy stats

.. .. test pypi
