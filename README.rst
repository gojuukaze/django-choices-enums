django-choices-enums
====================

The enum type used for Django choices enables Django’s choices to
support code prompts!!

用于django choices的枚举类型，使得django的choices支持代码提示！！

依赖
====

-  python3+

Installation
============

::

   pip install django-choices-enums

Usage
=====

.. code:: python

   from django_choices_enums import DjangoChoicesEnum

   class TypeChoices(DjangoChoicesEnum):
       Created = (1,'created')
       Finished = (2,'finished')

   class Foo(models.Model):
       type = models.IntegerField(choices=TypeChoices.to_django_choices())

use enum like this:

.. code:: python

   f = Foo.create(type=TypeChoices.Created)

get all values:

.. code:: python

   print(TypeChoices.all_values())
   # Out: [1, 2]