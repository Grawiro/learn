# import only this var or function if import from * 
__all__=['var_2']

# if _ before dont import this if import from *
_var_1 = 'no import'
var_2 = 'import'
var_3 = 'no import'

# do this only if this module is not import
if __name__ == "__main__":
    print('this is a main module')