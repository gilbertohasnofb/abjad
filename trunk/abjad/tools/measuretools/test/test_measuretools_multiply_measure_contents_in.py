from abjad import *


def test_measuretools_multiply_measure_contents_in_01( ):
   '''Spin one measure out three times.'''

   t = RigidMeasure((3, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
   measuretools.multiply_measure_contents_in(t, 3)

   r'''
   {
           \time 9/8
           c'8
           d'8
           e'8
           c'8
           d'8
           e'8
           c'8
           d'8
           e'8
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "{\n\t\\time 9/8\n\tc'8\n\td'8\n\te'8\n\tc'8\n\td'8\n\te'8\n\tc'8\n\td'8\n\te'8\n}"


def test_measuretools_multiply_measure_contents_in_02( ):
   '''Spin multiples measures out twice each.'''

   t = Staff(RigidMeasure((2, 8), leaftools.make_repeated_notes(2)) * 3)
   pitchtools.diatonicize(t)
   
   r'''
   \new Staff {
           {
                   \time 2/8
                   c'8
                   d'8
           }
           {
                   \time 2/8
                   e'8
                   f'8
           }
           {
                   \time 2/8
                   g'8
                   a'8
           }
   }
   '''

   measuretools.multiply_measure_contents_in(t, 2)

   r'''
   \new Staff {
           {
                   \time 4/8
                   c'8
                   d'8
                   c'8
                   d'8
           }
           {
                   \time 4/8
                   e'8
                   f'8
                   e'8
                   f'8
           }
           {
                   \time 4/8
                   g'8
                   a'8
                   g'8
                   a'8
           }
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Staff {\n\t{\n\t\t\\time 4/8\n\t\tc'8\n\t\td'8\n\t\tc'8\n\t\td'8\n\t}\n\t{\n\t\t\\time 4/8\n\t\te'8\n\t\tf'8\n\t\te'8\n\t\tf'8\n\t}\n\t{\n\t\t\\time 4/8\n\t\tg'8\n\t\ta'8\n\t\tg'8\n\t\ta'8\n\t}\n}"
