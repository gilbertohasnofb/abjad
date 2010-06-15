from abjad import *


def test_layout_insert_measure_padding_rest_01( ):

   t = Staff(AnonymousMeasure(leaftools.make_first_n_notes_in_ascending_diatonic_scale(2)) * 2)

   r'''
   \new Staff {
           {
                   \override Staff.TimeSignature #'stencil = ##f
                   \time 1/4
                   c'8
                   d'8
                   \revert Staff.TimeSignature #'stencil
           }
           {
                   \override Staff.TimeSignature #'stencil = ##f
                   \time 1/4
                   c'8
                   d'8
                   \revert Staff.TimeSignature #'stencil
           }
   }
   '''
   
   layout.insert_measure_padding_rest(t, Rational(1, 32), Rational(1, 64))   

   r'''
   \new Staff {
           {
                   \override Staff.TimeSignature #'stencil = ##f
                   \time 19/64
                   r32
                   c'8
                   d'8
                   r64
                   \revert Staff.TimeSignature #'stencil
           }
           {
                   \override Staff.TimeSignature #'stencil = ##f
                   \time 19/64
                   r32
                   c'8
                   d'8
                   r64
                   \revert Staff.TimeSignature #'stencil
           }
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Staff {\n\t{\n\t\t\\override Staff.TimeSignature #'stencil = ##f\n\t\t\\time 19/64\n\t\tr32\n\t\tc'8\n\t\td'8\n\t\tr64\n\t\t\\revert Staff.TimeSignature #'stencil\n\t}\n\t{\n\t\t\\override Staff.TimeSignature #'stencil = ##f\n\t\t\\time 19/64\n\t\tr32\n\t\tc'8\n\t\td'8\n\t\tr64\n\t\t\\revert Staff.TimeSignature #'stencil\n\t}\n}"


def test_layout_insert_measure_padding_rest_02( ):
   '''Works when measures contain stacked voices.'''

   measure = DynamicMeasure(Voice(leaftools.make_repeated_notes(2)) * 2)
   measure.parallel = True
   t = Staff(measure * 2)
   pitchtools.diatonicize(t)
   
   r'''
   \new Staff {
           <<
                   \time 1/4
                   \new Voice {
                           c'8
                           d'8
                   }
                   \new Voice {
                           e'8
                           f'8
                   }
           >>
           <<
                   \time 1/4
                   \new Voice {
                           g'8
                           a'8
                   }
                   \new Voice {
                           b'8
                           c''8
                   }
           >>
   }
   '''

   layout.insert_measure_padding_rest(t, Rational(1, 32), Rational(1, 64))

   r'''
   \new Staff {
           <<
                   \time 19/64
                   \new Voice {
                           r32
                           c'8
                           d'8
                           r64
                   }
                   \new Voice {
                           r32
                           e'8
                           f'8
                           r64
                   }
           >>
           <<
                   \time 19/64
                   \new Voice {
                           r32
                           g'8
                           a'8
                           r64
                   }
                   \new Voice {
                           r32
                           b'8
                           c''8
                           r64
                   }
           >>
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Staff {\n\t<<\n\t\t\\time 19/64\n\t\t\\new Voice {\n\t\t\tr32\n\t\t\tc'8\n\t\t\td'8\n\t\t\tr64\n\t\t}\n\t\t\\new Voice {\n\t\t\tr32\n\t\t\te'8\n\t\t\tf'8\n\t\t\tr64\n\t\t}\n\t>>\n\t<<\n\t\t\\time 19/64\n\t\t\\new Voice {\n\t\t\tr32\n\t\t\tg'8\n\t\t\ta'8\n\t\t\tr64\n\t\t}\n\t\t\\new Voice {\n\t\t\tr32\n\t\t\tb'8\n\t\t\tc''8\n\t\t\tr64\n\t\t}\n\t>>\n}"


def test_layout_insert_measure_padding_rest_03( ):
   '''Set splice = True to extend edge spanners over newly insert rests.'''

   t = DynamicMeasure(leaftools.make_first_n_notes_in_ascending_diatonic_scale(2))
   Beam(t[:])
   label.measure_numbers(t)
   layout.insert_measure_padding_rest(
      t, Rational(1, 32), Rational(1, 64), splice = True)

   r'''
   % start measure 1
   {
           \time 19/64
           r32 [
           c'8
           d'8
           r64 ]
   }
   % stop measure 1
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "% start measure 1\n{\n\t\\time 19/64\n\tr32 [\n\tc'8\n\td'8\n\tr64 ]\n}\n% stop measure 1"
