from abjad import *
from abjad.tools import pitcharraytools
import py.test
py.test.skip('fix me: partitioning function somewhere not working as expected.')


def test_pitcharraytools_make_empty_pitch_array_from_list_of_pitch_lists_01( ):

   score = Score([ ])
   score.append(Staff(macros.scale(6)))
   score.append(Staff(macros.scale(3, Duration(1, 4))))
   score.append(Staff(macros.scale(6)))

   r'''
   \new Score <<
           \new Staff {
                   c'8
                   d'8
                   e'8
                   f'8
                   g'8
                   a'8
           }
           \new Staff {
                   c'4
                   d'4
                   e'4
           }
           \new Staff {
                   c'8
                   d'8
                   e'8
                   f'8
                   g'8
                   a'8
           }
   >>
   '''

   pitch_array = pitcharraytools.make_empty_pitch_array_from_list_of_pitch_lists(score)

   '''
   [ ] [ ] [ ] [ ] [ ] [ ]
   [     ] [     ] [     ]
   [ ] [ ] [ ] [ ] [ ] [ ]
   '''

   assert pitch_array[0].cell_widths == (1, 1, 1, 1, 1, 1)
   assert pitch_array[1].cell_widths == (2, 2, 2)
   assert pitch_array[2].cell_widths == (1, 1, 1, 1, 1, 1)


def test_pitcharraytools_make_empty_pitch_array_from_list_of_pitch_lists_02( ):

   score = Score([ ])
   score.append(Staff(macros.scale(4)))
   score.append(Staff(macros.scale(2, Duration(1, 4))))
   score.append(Staff(tuplettools.FixedDurationTuplet((2, 8), "c'8 d'8 e'8") * 2))

   r'''
   \new Score <<
           \new Staff {
                   c'8
                   d'8
                   e'8
                   f'8
           }
           \new Staff {
                   c'4
                   d'4
           }
           \new Staff {
                   \times 2/3 {
                           c'8
                           d'8
                           e'8
                   }
                   \times 2/3 {
                           c'8
                           d'8
                           e'8
                   }
           }
   >>
   '''

   pitch_array = pitcharraytools.make_empty_pitch_array_from_list_of_pitch_lists(score)

   '''
   [     ] [     ] [     ] [     ]
   [             ] [             ]
   [ ] [     ] [ ] [ ] [     ] [ ]
   '''

   assert pitch_array[0].cell_widths == (2, 2, 2, 2)
   assert pitch_array[1].cell_widths == (4, 4)
   assert pitch_array[2].cell_widths == (1, 2, 1, 1, 2, 1)
