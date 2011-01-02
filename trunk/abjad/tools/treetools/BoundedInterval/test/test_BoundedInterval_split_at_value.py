from fractions import Fraction
from abjad.tools.treetools.BoundedInterval import BoundedInterval


def test_BoundedInterval_split_at_value_01( ):
    '''BoundedInterval.split_at_value returns a new BoundedInterval instance.'''
    i1 = BoundedInterval(3, 23)
    splits = i1.split_at_value(13)
    assert splits[0].signature == (3, 13)
    assert splits[1].signature == (13, 23)
    
def test_BoundedInterval_split_at_value_02( ):
    '''A split point at or outside the BoundedInterval bounds returns the original BoundedInterval.'''
    i1 = BoundedInterval(3, 23)
    splits = i1.split_at_value(3)
    assert i1 == splits[0]
    splits = i1.split_at_value(23)
    assert i1 == splits[0]
    splits = i1.split_at_value(-1000)
    assert i1 == splits[0]
    splits = i1.split_at_value(1000)
    assert i1 == splits[0]

def test_BoundedInterval_split_at_value_03( ):
    '''BoundedIntervals can be split by Fractions.'''
    i1 = BoundedInterval(3, 23)
    splits = i1.split_at_value(Fraction(46, 13))
    assert splits[0].signature == (3, Fraction(46, 13))
    assert splits[1].signature == (Fraction(46, 13), 23)
