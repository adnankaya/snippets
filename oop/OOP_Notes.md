# Object Oriented Programming

### What is it ?

- OOP is a computer programming design philosophy or methodology.
- It organizes and models software design around data, or objects rather than functions and logic.
- OOP combines a group of data attributes with functions or methods into a unit called an **object**.
- An object is referred to as a data field that has unique attributes (properties) and behaviors (functions, methods).
- Properties are the state of the object. Behaviors are the actions our object take. Behaviors often modify the properties of object.
- Pillars of OOP are abstraction, encapsulation, inheritance and polymorphism.
- An **object** has attributes and functions.
- A **class** is a blueprint or template of an object.

### Why do we use it?

- OOP allows to break the program into the small pieces. So the problems will be solved easily.
- OOP systems can be easily upgraded from small to large systems.
- OOP increases programmer productivity, quality of software and decreases maintenance cost.
- We can build the programs from standard working modules that communicate each other, rather than having to start writing the code from scratch.
- It makes large-scale applications much simpler because it's a great way to reduce dependencies.

### When do we use it ?

- OOP is about encapsulating mutable state and is therefore more appropriate for interactive applications, GUI's and API's exposing mutable state.
- You have multiple programmers who don't need to understand each component.
- There is a lot of code that could be shared and reused
- The project is expected to change often and be added to over time
- Different sections can benefit from different resources like data source and hardware.

### How we use it ?

- In OOP when we model a problem in terms of objects we create abstract definitions representing the types of object we want to have in our system. 

- For example if we were modeling a school, we might want to have objects representing professors. Every professor has some properties in common: they all have name and a subject they teach. Also every professor can do certain things. For example they can all grade a paper and they can introduce themselves to their students at the start of the year.

- So `Professor` could be a **class** in our system and the definition of the class lists data(attributes, properties) and methods that every professor has.

- In pseudocode a  `Professor` class could be written like this

- ```
  class Professor
  	properties:
  		name
  		teaches
  	methods:
  		grade(paper)
  		introduce_self()
  ```

- On its own, a class doesn't do anything. It's kind of template(blueprint) for creating concrete objects of that type.

- Each concrete professor we create is called **instance** of `Professor` class. 

- > **An object is referred to as an instance of the class**

- The process of creating an instance is performed by a special function called a **constructor**.

### Example of usage

- https://github.com/adnankaya/snippets/blob/master/oop_hr/main.py



##### Resources

- https://www.javatpoint.com/what-is-object-oriented-programming
- https://stackoverflow.com/questions/24270/whats-the-point-of-oop
- https://www.geeksforgeeks.org/benefits-advantages-of-oop/
- https://www.indeed.com/career-advice/career-development/what-is-object-oriented-programming
- https://realpython.com/lessons/what-object-oriented-programming-oop/
- https://softwareengineering.stackexchange.com/a/325825
- https://teamtreehouse.com/community/when-to-use-oop-over-procedural-coding