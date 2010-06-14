from abjad import *


def test_tietools_get_tie_chain_duration_preprolated_01( ):
   '''Return sum of preprolated durations of leaves in tie chain.'''

   notes = leaftools.make_notes(0, [(5, 16)])
   assert tietools.get_tie_chain_duration_preprolated(notes[0].tie.chain) == \
      Rational(5, 16)


def test_tietools_get_tie_chain_duration_preprolated_02( ):
   '''Works on trivial tie chains.'''

   t = Note(0, (1, 4))
   assert tietools.get_tie_chain_duration_preprolated(t.tie.chain) == \
      Rational(1, 4)
