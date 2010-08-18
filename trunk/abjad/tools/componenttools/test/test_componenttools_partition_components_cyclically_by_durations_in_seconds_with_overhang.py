from abjad import *


def test_componenttools_partition_components_cyclically_by_durations_in_seconds_with_overhang_01( ):
   '''Read durations cyclically.
   If components remain, do append final part.'''

   t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
   macros.diatonicize(t)
   tempo_spanner = spannertools.TempoSpanner(t[:])
   tempo_indication = tempotools.TempoIndication(Rational(1, 4), 60)
   tempo_spanner.tempo_indication = tempo_indication

   r'''
   \new Staff {
         \time 2/8
         \tempo 4=60
         c'8
         d'8
         \time 2/8
         e'8
         f'8
         \time 2/8
         g'8
         a'8
         \time 2/8
         b'8
         c''8
         %% tempo 4=60 ends here
   }
   '''

   groups = \
      componenttools.partition_components_cyclically_by_durations_in_seconds_exactly_with_overhang(
      t.leaves, [1.5])

   "[[Note(c'', 8), Note(b', 8), Note(a', 8)], [Note(g', 8), Note(f', 8), Note(e', 8)], [Note(d', 8), Note(c', 8)]]"

   assert len(groups) == 3
   assert groups[0] == list(t.leaves[:3])
   assert groups[1] == list(t.leaves[3:6])
   assert groups[2] == list(t.leaves[6:8])
