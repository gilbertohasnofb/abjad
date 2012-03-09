from abc import ABCMeta
from abjad.mixins._ImmutableAbjadObject import _ImmutableAbjadObject


class _StrictComparator(_ImmutableAbjadObject):
    '''Mix-in abstract base class to confer strict comparison behavior
    to any custom class. Note that this class will be unnecessary
    in some future release because Python 3.0 implements strict
    comparison behavior by default.
    '''

    ### CLASS ATTRIBUTES ###

    __metaclass__ = ABCMeta
    __slots__ = ()

    ### OVERLOADS ###

    def __eq__(self, arg):
        return id(self) == id(arg)

    def __ge__(self, arg):
        raise NotImplementedError('\n\tGreater-equal not implemented on "{!r}".'.format(arg))

    def __gt__(self, arg):
        raise NotImplementedError('\n\tGreater-than not implemented on "{!r}".'.format(arg))

    def __le__(self, arg):
        raise NotImplementedError('\n\tLess-equal not implemented on "{!r}".'.format(arg))

    def __lt__(self, arg):
        raise NotImplementedError('\n\tLess-than not implemented on "{!r}".'.format(arg))

    def __ne__(self, arg):
        return not self == arg

    def __nonzero__(self):
        return True
