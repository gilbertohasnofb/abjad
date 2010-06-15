from abjad import *


def test_slur_interface_01( ):
   '''Abjad SlurInterface handles the LilyPond Slur grob.'''

   t = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(4))
   t.slur.color = 'red'

   r'''
   \new Voice \with {
           \override Slur #'color = #red
   } {
           c'8
           d'8
           e'8
           f'8
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Voice \\with {\n\t\\override Slur #'color = #red\n} {\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"
