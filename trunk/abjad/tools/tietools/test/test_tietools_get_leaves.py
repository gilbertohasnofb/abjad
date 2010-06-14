from abjad import *


def test_tietools_get_leaves_01( ):
   '''Leaves from nontrivial tie chain.'''

   notes = leaftools.make_notes(0, [(5, 32)])
   assert tietools.get_leaves(notes[0].tie.chain) == tuple(notes)


def test_tietools_get_leaves_02( ):
   '''Leaves from trivial tie chain.'''

   t = Note(0, (1, 4))
   assert tietools.get_leaves(t.tie.chain) == (t, )
