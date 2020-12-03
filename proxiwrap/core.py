"""Core functionality for the proxiwrap package."""

from typing import Type, List
from collections.abc import Callable


# Wrapper approach based on:
# https://gist.github.com/kyouko-taiga/de5ece0792d2f5fe8fb3

class WrapperBase(type):
    """WrapperBase base class."""

    # This metaclass is heavily inspired by the Object Proxying python recipe
    # (http://code.activestate.com/recipes/496741/). It adds special methods
    # to the wrapper class so it can proxy the wrapped class. In addition, it
    # adds a field __overrides__ in the wrapper class dictionary, containing
    # all attributes decorated to be overriden.

    _special_names = [
        '__abs__', '__add__', '__and__', '__call__', '__cmp__', '__coerce__',
        '__contains__', '__delitem__', '__delslice__', '__div__', '__divmod__',
        '__eq__', '__float__', '__floordiv__', '__ge__', '__getitem__',
        '__getslice__', '__gt__', '__hash__', '__hex__', '__iadd__',
        '__iand__', '__idiv__', '__idivmod__', '__ifloordiv__', '__ilshift__',
        '__imod__', '__imul__', '__int__', '__invert__', '__ior__', '__ipow__',
        '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__',
        '__le__', '__len__', '__long__', '__lshift__', '__lt__', '__mod__',
        '__mul__', '__ne__', '__neg__', '__oct__', '__or__', '__pos__',
        '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__',
        '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
        '__rfloorfiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__',
        '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
        '__rxor__', '__setitem__', '__setslice__', '__sub__', '__truediv__',
        '__xor__', 'next',
    ]

    def __new__(cls, classname, bases, attrs):
        def make_method(name):
            def method(self, *args, **kwargs):
                mtd = getattr(object.__getattribute__(self, "_wrapped"), name)
                return mtd(*args, **kwargs)
            return method

        for name in cls._special_names:
            attrs[name] = make_method(name)

        overrides = attrs.get('__overrides__', [])
        # overrides.extend(k for k,v in attrs.items() if isinstance(v, lazy))
        attrs['__overrides__'] = overrides
        return type.__new__(cls, classname, bases, attrs)


# ==== CachedExperimentRun class (including wrapper base class) ====


def build_proxy_class(
    classname: str,
    overrides: List[Callable],
):
    """Blah."""
    class Wrapper(metaclass=WrapperBase):
        """Wraps an object."""

        # This class acts as a proxy for the wrapped instance it is passed. All
        # access to its attributes are delegated to the wrapped class, except
        # those contained in __overrides__.

        __slots__ = ['_wrapped', '__weakref__']
        __override_names__ = [f.__name__ for f in overrides]
        __overrides__ = {f.__name__: f for f in overrides}

        def __init__(self, wrapped):
            object.__setattr__(self, '_wrapped', wrapped)

        def __getattribute__(self, attr):
            if attr in object.__getattribute__(self, '__override_names__'):
                return object.__getattribute__(self, '__overrides__')[attr]

            # If the requested attribute wasn't overriden, then we delegate to
            # the wrapped class.
            return getattr(object.__getattribute__(self, '_wrapped'), attr)

        def __setattr__(self, attr, value):
            setattr(object.__getattribute__(self, '_wrapped'), attr, value)

        def __nonzero__(self):
            return bool(object.__getattribute__(self, '_wrapped'))

        def __str__(self):
            return str(object.__getattribute__(self, '_wrapped'))

        def __repr__(self):
            return repr(object.__getattribute__(self, '_wrapped'))

        def _wrapped_obj(self):
            """Returns the wrapped object."""
            return object.__getattribute__(self, '_wrapped')

    Wrapper.__name__ = classname
    return Wrapper
