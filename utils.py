from importlib import import_module

VERBOSITY = 1


def log(msg, verbosity=2):
    if verbosity <= VERBOSITY:
        print(msg)


def load(path):
    module, klass = path.rsplit('.', 1)
    m = import_module(module)
    cls = getattr(m, klass)
    return cls
