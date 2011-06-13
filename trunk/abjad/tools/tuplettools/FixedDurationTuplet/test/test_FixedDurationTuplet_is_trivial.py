from abjad import *


def test_FixedDurationTuplet_is_trivial_01( ):
   '''True when tuplet ratio equals one.'''

   t = tuplettools.FixedDurationTuplet((2, 8), "c'8 d'8 e'8")
   assert not t.is_trivial


def test_FixedDurationTuplet_is_trivial_02( ):
   '''True when tuplet ratio equals one.'''

   t = tuplettools.FixedDurationTuplet((2, 8), macros.scale(2))
   assert t.is_trivial
