============
IsoUnidecode
============


This is a package for conversion and transliteration of unicode into ascii or
iso-8859-1 strings. This is mostly a port of Perl Text::Unidecode_ to Python
with additional support for iso8859-1.

.. _Unidecode: http://cpansearch.perl.org/src/SBURKE/Text-Unidecode-0.04/README


This package provides one function - unidecode() which tries to represent
input unicode object as an 'ascii' or 'iso8859-1' string replacing characters
unavailable in the target encoding with similar characters or their
transliteration.

It works with different agree of success for different lanugages. It works
quite good for European languages, works ok for Russian, and works to some
extent for Arabic, Hindi.

Unidecode even produces something for Chinese and Japanese - but I am not
really sure that such results are any good at all.

There are some additional fixes (not present in Text::Unidecode) in iso8859-1
conversion table article which enable unidecode to convert unicode string in
any European language into iso8859-1.


Example usage
-------------

Ascii conversion::

    >>> from isounidecode import unidecode
    >>> unidecode(u"Programmes de publicité - Solutions d'entreprise")
    "Programmes de publicite - Solutions d'entreprise"

    >>> unidecode(u"Транслитерирует и русский")
    'Translitieriruiet i russkii'

iso8859-1 conversion::

    >>> from isounidecode import unidecode
    >>> unidecode(u"Programmes de publicité - Solutions d'entreprise", 'iso8859-1')
    "Programmes de publicit\xe9 - Solutions d'entreprise"


Another Unidecode package
-------------------------

There exists another unidecode_ python package. Which was registered first on
PyPI. I learned about the existence of that package only when I ran "python
setup.py register". 

I created this package a couple of years ago - at that time there was no other
unidecode packages. I made this package and completely forgot about its
existencse unitil it suddenly came in handy recently.

So I decided to add readme, and upload it to PYPI. Now I know there's another
unidecode package, so I am renaming this package into "isounidecode".


