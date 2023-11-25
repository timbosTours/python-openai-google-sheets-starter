import importlib
from typing import Callable

def dynamic_import(module_name: str, function_name: str) -> Callable:
    """
    Dynamically imports a function from a module within the 'modules' package.

    This utility function allows for flexible importing of functions based on
    module and function names provided as strings. It is particularly useful
    for scenarios where the modules to import from are not known ahead of time
    and may change or be user-defined.

    Parameters:
    - module_name: The name of the module (without the 'modules.' prefix).
    - function_name: The name of the function to import from the module.

    Returns:
    The imported function object ready to be called with its required parameters.
    
    Raises:
    - AttributeError: If the specified function is not found within the given module.
    - ModuleNotFoundError: If the specified module is not found within the 'modules' package.
    """
    try:
        # Attempt to import the module from the 'modules' directory.
        # The module name is prefixed with 'modules.' to specify the correct package.
        print(f"Attempting to import module: modules.{module_name}")
        module = importlib.import_module(f"modules.{module_name}")
        print(f"Successfully imported module: modules.{module_name}")

        # Retrieve the function from the imported module.
        # If the function is not found, AttributeError will be raised.
        print(f"Attempting to retrieve function: {function_name} from module: modules.{module_name}")
        function = getattr(module, function_name)
        print(f"Successfully retrieved function: {function_name} from module: modules.{module_name}")

        return function
    except AttributeError:
        print(f"Error: Function {function_name} not found in module: modules.{module_name}")
        raise
    except ModuleNotFoundError:
        print(f"Error: Module modules.{module_name} not found")
        raise
