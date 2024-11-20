# Concepts in Object Oriented Programming

## Class

- Template (blueprint) for the creation of an object

### Attribute (Parameter) 

- Descriptions of an object. (First name, last name, class, etc.)
- Two different types of attributes:
- Instance attribute (applies to a specific instance)
- Class level attribute (applies to every object within a class)

### `__init__` (Initializer)
- Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created

### Methods (Action)
- Instance method:
    - method that can be performed on the object
- Class method: 
    - allows us to create and modify class level data
- Static method: 
    - does not have access to class or instance attributes but performs action within the class
- Magic method:
    - reserved methods that perform a specific task (`__str__`)