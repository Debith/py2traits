PyTraits
========

Comprehensive trait support for Python

Support:
  * Python 3.x
  * Python 2.7+
  * Python 2.6 and lower (NestedDict is based on normal dict,
                          thus ordering is not guaranteed)

About Traits
------------

Traits are classes which contain methods that can be used to extend
other classes, similar to mixins, with exception that traits do not use
inheritance. Instead, traits are composed into other classes. That is;
methods, properties and internal state is copied to master object. 

The point is to improve code reusability by dividing code into simple 
building blocks that can be then combined into actual classes.

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
    - [X] Instances
 - Supported Trait Types
    - [X] Classes
    - [X] Instances
    - [X] Methods
    - [X] Functions
      - [X] as instance methods
      - [X] as classmethods
      - [X] as staticmethods
    - [X] Properties
 - [X] Singleton
 - [X] NestedDict
 - Examples
    - [X] Class
       - [X] Unbound method in Python 2.x
       - [X] Bound method in Python 2.x
       - [X] Method in Python 3.x
       - [X] Property as part of class
       - [ ] Property cherry-picking
       - [X] Function
         - [X] Instance method         
         - [X] Class method
         - [X] Static method
       - [ ] Conflicts
          - [ ] symmetric sum
          - [ ] override
          - [ ] alias
          - [ ] exclude
       - [X] Multiple traits
    - [X] Instance
       - [X] Unbound method in Python 2.x
       - [X] Bound method in Python 2.x
       - [X] Method in Python 3.x
       - [X] Property as part of class
       - [ ] Property cherry-picking
       - [X] Function
         - [X] Instance method         
         - [X] Class method
         - [X] Static method
       - [ ] Conflicts
          - [ ] symmetric sum
          - [ ] override
          - [ ] alias
          - [ ] exclude
       - [X] Multiple traits

Composition of Traits
---------------------

Traits are classes that are not supposed to run stand alone (nothing stops to make them work
like that though). Traits are classes that are composed (by copying functions and properties)
into other classes. Advantage is that there is no inheritance happening and so there are no
typical problems occurring with normal inheritance. For instance, diamond inheritance is not
possible as everything is copied to target class and all conflicting methods and properties
needs to be resolved during composition.

In Python, this kind of approach is handy with metaclasses, since metaclasses have very strict
requirements for inheritance.

This library goes bit further than extending just classes. It's possible to also compose traits
into instances of classes, in which case, composition only affects single instance, not whole
class. Also, this library allows cherrypicking methods and properties from other classes and 
composing them to target objects. If anything, it at least enables possibility for highly 
creative ways to reuse your code.


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

0.6 Restructuring into library
  - Added support for py.test
  - Preparing to support tox
  - Improved multiple examples and renamed them to make more sense
  - Removed the need of having two separate code branches for different Python versions

0.5 Instances can now be extended with traits in Python 3.x
  - Instance support now similar to classes
  - Added more examples

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
