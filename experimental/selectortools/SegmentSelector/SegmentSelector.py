from experimental.selectortools.BackgroundElementSelector import BackgroundElementSelector


class SegmentSelector(BackgroundElementSelector):
    r'''.. versionadded:: 1.0

    Select segment ``3``::

        >>> from experimental import *

    ::

        >>> selectortools.SegmentSelector(index=3)
        SegmentSelector(index=3)

    Select segment ``'red'``::

        >>> selectortools.SegmentSelector(index='red')
        SegmentSelector(index='red')

    Segment selectors are immutable.
    '''

    ### INITIALIZER ###

    def __init__(self, inequality=None, index=0):
        from experimental import specificationtools
        BackgroundElementSelector.__init__(self, 
            klass=specificationtools.Segment, inequality=inequality, index=index)

    ### READ-ONLY PROPERTIES ###

    @property
    def context_name(self):
        '''Return none.
        '''
        return

    @property
    def context_names(self):
        '''Return empty list.
        '''
        return []
