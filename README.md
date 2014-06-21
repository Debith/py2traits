PyTraits
========

Comprehensive trait support for Python

Support:
  * Python 3.x (in short future)
  * Python 2.7+
  * Python 2.6 and lower (NestedDict is based on normal dict,
                          thus ordering is not guaranteed)

About Traits
------------

Traits are classes which contain methods that can be used to extend
other classes, similar to mixins. Idea is to improve code reusability
where code is divided into simple building blocks that can be then
combined into actual classes.

Read more from wikipedia: http://en.wikipedia.org/wiki/Traits_class

----------------------------------------------------------------

Features
========
 - Composition of Traits
    - [X] No conflicts
    - [ ] Symmertric Sum
    - [ ] Override
    - [ ] Alias
    - [ ] Exclusion
 - Supported Trait Targets
    - [X] Classes
    - [ ] Instances
 - Supported Trait Types
    - [X] Classes
    - [X] Instances
    - [X] Methods
    - [X] Functions
    - [X] Properties
 - [X] Singleton
 - [X] NestedDict
 - Examples
    - [X] Class
       - [X] Unbound method in Python 2.x
       - [X] Bound method in Python 2.x
       - [ ] Method in Python 3.x
       - [X] Property as part of class
       - [ ] Property directly
       - [ ] Function
       - [ ] Static method
       - [ ] Class method
       - [ ] Conflicts
          - [ ] symmetric sum
          - [ ] override
          - [ ] alias
          - [ ] exclude
       - [ ] Multiple traits
    - [ ] Instance
       - [ ] Unbound method in Python 2.x
       - [ ] Bound method in Python 2.x
       - [ ] Method in Python 3.x
       - [ ] Property as part of class
       - [ ] Property directly
       - [ ] Function
       - [ ] Static method
       - [ ] Class method
       - [ ] Conflicts
          - [ ] symmetric sum
          - [ ] override
          - [ ] alias
          - [ ] exclude
       - [ ] Multiple traits

Composition of Traits
---------------------

TBD

Supported Trait Targets
-----------------------

TBD

Supported Trait Types
---------------------

TBD

NestedDict - Dictionary for deep nested hierarchies
---------------------------------------------------

TBD

Singleton - Glorified global variable
-------------------------------------

TBD


History
=======

0.4 Completed function binding with examples in Python 2.x
  - Separate functions can now be bound to classes
    - Functions with 'self' as a first parameter will be acting as a method
    - Functions with 'cls' as a first parameter will be acting as classmethod
    - Other functions will be static methods.
  - Fixed an issue with binding functions

0.3 Trait extension support without conflicts for Python 2.x
  - Classes can be extended
  - Instances can be extended
  - Python 2.x supported

0.2 Apache License Updated
  - Added apache 2.0 license to all files
  - Set the character set as utf-8 for all files

0.1 Initial Version
  - prepared files for Python 2.x
  - prepared files for Python 3.x
