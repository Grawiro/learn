print('import file')

x=2

def show_x():
    print(x)

# import from local directory to_import_2
from . import file_to_import_relative
# import only var from this module
# from .file_to_import_relative import var
print(file_to_import_relative.var)
# import from above directory to_import_1
from .. import file_to_import_relative
# import from moduls
import file_to_import_relative