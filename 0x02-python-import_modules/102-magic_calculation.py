import importlib.util

def magic_calculation(a, b):
    if a < b:
        spec = importlib.util.spec_from_file_location("magic_calculation_102", "./magic_calculation_102.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        add = getattr(module, "add")
        sub = getattr(module, "sub")
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

