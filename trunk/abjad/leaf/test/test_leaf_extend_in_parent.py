from abjad import *


def test_leaf_extend_in_parent_01( ):
   '''Extend leaves rightwards after leaf.'''

   t = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
   Beam(t[:])
   result = t[-1].extend_in_parent(leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))

   r'''
   \new Voice {
      c'8 [
      d'8
      e'8 ]
      c'8
      d'8
      e'8
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert result == t[-4:]
   assert t.format == "\\new Voice {\n\tc'8 [\n\td'8\n\te'8 ]\n\tc'8\n\td'8\n\te'8\n}"


def test_leaf_extend_in_parent_02( ):
   '''Extend leaf rightwards after interior leaf.'''

   t = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
   Beam(t[:])
   result = t[1].extend_in_parent([Note(2.5, (1, 8))])

   r'''
   \new Voice {
           c'8 [
           d'8
           dqs'8
           e'8 ]
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Voice {\n\tc'8 [\n\td'8\n\tdqs'8\n\te'8 ]\n}"
   assert result == t[1:3]
