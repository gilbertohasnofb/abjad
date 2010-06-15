from abjad import *


def test_measuretools_scale_measure_contents_in_01( ):
   '''Quadruple binary meter.
      Meter denominator adjust appropriately.'''

   t = RigidMeasure((3, 32), leaftools.make_first_n_notes_in_ascending_diatonic_scale(3, Rational(1, 32)))
   Beam(t[:])

   measuretools.scale_measure_contents_in(t, Rational(4))

   r'''
   {
           \time 3/8
           c'8 [
           d'8
           e'8 ]
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "{\n\t\\time 3/8\n\tc'8 [\n\td'8\n\te'8 ]\n}"


def test_measuretools_scale_measure_contents_in_02( ):
   '''Triple binary meter.'''

   t = RigidMeasure((3, 32), leaftools.make_first_n_notes_in_ascending_diatonic_scale(3, Rational(1, 32)))
   Beam(t[:])

   measuretools.scale_measure_contents_in(t, Rational(3))

   r'''
   {
           \time 9/32
           c'16. [
           d'16.
           e'16. ]
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "{\n\t\\time 9/32\n\tc'16. [\n\td'16.\n\te'16. ]\n}"


def test_measuretools_scale_measure_contents_in_03( ):
   '''Multiply binary measure by 2/3.'''

   t = RigidMeasure((3, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
   Beam(t[:])

   measuretools.scale_measure_contents_in(t, Rational(2, 3))

   r'''
   {
           \time 3/12
           \scaleDurations #'(2 . 3) {
                   c'8 [
                   d'8
                   e'8 ]
           }
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "{\n\t\\time 3/12\n\t\\scaleDurations #'(2 . 3) {\n\t\tc'8 [\n\t\td'8\n\t\te'8 ]\n\t}\n}"
