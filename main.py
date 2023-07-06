from envis import Envis

if __name__ == '__main__':

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
