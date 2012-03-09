from abc import ABCMeta
from abc import abstractproperty


class _ImmutableAbjadObject(object):
    '''.. versionadded:: 2.8
    
    Abstract base class for system-global functionality.

    _MutableAbjadObject and _ImmutableAbjadObject differ only in the implementation of __slots__.
    '''
    
    ### CLASS ATTRIBUTES ###

    __metaclass__ = ABCMeta
    __slots__ = ()

    ### READ-ONLY ATTRIBUTES ###

    @property
    def class_name(self):
        return type(self).__name__
