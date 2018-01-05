from __future__ import division, print_function, absolute_import


def validate_func(x, allow_none=True):
    if not (allow_none and x is None) and hasattr(x, '__call__'):
        raise ValueError("'%s' must be a function." % x.__name__)
