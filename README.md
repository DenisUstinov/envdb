# Envis

Envis is a Python library that provides a convenient way to interact with environment variables through a Python program. It allows you to create and retrieve environment variables with various data types, including strings, integers, floats, booleans, dictionaries, and variables with incremental values.

## Installation

You can install Envis using pip:

```bash
pip install git+https://github.com/DenisUstinov/envis.git --use-pep517
```

## Usage

Here's how you can use Envis in your Python program:

```python
from envis import Envis

# Create an instance of the Envis class
env = Envis()

# Create environment variables
env.set_var('MY_STRING', str='Hello, World!')
env.set_var('MY_INTEGER', int=42)
env.set_var('MY_FLOAT', float=3.14)
env.set_var('MY_BOOL', bool=True)
env.set_var('MY_DICT', dict={'key': 'value'})
env.set_var('MY_INCREMENT', i=1)

# Retrieve environment variables
my_string = env.get_var('MY_STRING')
my_integer = env.get_var('MY_INTEGER')
my_float = env.get_var('MY_FLOAT')
my_bool = env.get_var('MY_BOOL')
my_dict = env.get_var('MY_DICT')
my_increment = env.get_var('MY_INCREMENT')

print(my_string)  # Output: Hello, World!
print(my_integer)  # Output: 42
print(my_float)  # Output: 3.14
print(my_bool)  # Output: True
print(my_dict)  # Output: {'key': 'value'}
print(my_increment)  # Output: 1
```

## API Reference

### Envis Class
```python
set_var(name, **kwargs)
```

Creates an environment variable with the specified name and data type. The keyword arguments determine the data type and value of the variable.

Supported keyword arguments:

* str: String value for the variable.
* int: Integer value for the variable.
* float: Float value for the variable.
* bool: Boolean value for the variable.
* dict: Dictionary value for the variable.
* i: Incremental value for the variable. The step value can be specified (default: 1).
* get_var(name)

Retrieves the value of the specified environment variable.

If the variable was created using set_var, it returns the stored value.
If the variable exists in the environment, it returns the value from the environment.
If the variable doesn't exist, it returns None.
_process_increment_variable(name, step=1)

Processes the incremental variable by incrementing its value by the specified step. This method is called internally when retrieving an incremental variable value.

## License

This project is licensed under the MIT License.
