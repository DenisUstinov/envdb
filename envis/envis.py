import os


class Envis:
    def __init__(self):
        self.env_dict = {}

    def create_variable(self, name, **kwargs):
        if len(kwargs) != 1:
            raise ValueError("Only one keyword argument should be provided.")

        key, value = kwargs.popitem()
        if key == 'str':
            self.env_dict[name] = value
        elif key == 'int':
            self.env_dict[name] = f'int={value}'
        elif key == 'float':
            self.env_dict[name] = f'float={value}'
        elif key == 'bool':
            self.env_dict[name] = f'bool={value}'
        elif key == 'dict':
            self.env_dict[name] = f'dict={str(value)}'
        elif key == 'i':
            self.env_dict[name] = f'i={value}'
        else:
            raise ValueError("Invalid keyword argument.")

        os.environ[name] = self.env_dict[name]

    def get_variable(self, name):
        if name in self.env_dict:
            value = self.env_dict[name]
            if value.startswith('int='):
                return int(value[4:])
            elif value.startswith('float='):
                return float(value[6:])
            elif value.startswith('bool='):
                return bool(value[5:])
            elif value.startswith('dict='):
                return eval(value[5:])
            elif value.startswith('i='):
                return self._process_increment_variable(name, int(value[2:]))
            else:
                return value
        else:
            return os.environ.get(name, None)

    def _process_increment_variable(self, name, step=1):
        if name in self.env_dict:
            value = self.env_dict[name]
            if value.startswith('int='):
                current_value = int(value[4:])
                new_value = current_value + step
                self.env_dict[name] = f'int={new_value}'
                os.environ[name] = self.env_dict[name]
                return new_value
        return None
