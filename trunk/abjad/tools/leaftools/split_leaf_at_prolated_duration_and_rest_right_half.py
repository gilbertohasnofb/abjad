from abjad.rest import Rest


def split_leaf_at_prolated_duration_and_rest_right_half(
   leaf, prolated_duration):
   r'''.. versionadded:: 1.1.2

   Split `leaf` at `prolated_duration` and rest right half::


      abjad> t = Staff(macros.scale(4))
      abjad> Slur(t[:])
      Slur(c'8, d'8, e'8, f'8)
      abjad> f(t)
      \new Staff {
         c'8 (
         d'8
         e'8
         f'8 )
      }

   ::

      abjad> leaftools.split_leaf_at_prolated_duration_and_rest_right_half(t.leaves[1], (1, 32))
      ([Note(d', 32)], [Note(d', 16.)])

   ::

      abjad> f(t)
      \new Staff {
         c'8 (
         d'32
         r16.
         e'8
         f'8 )
      }

   Return list of leaves to left of `prolated_durration`
   together with list of leaves to right of `prolated_duration`.

   .. todo:: implement 
      ``leaftools.split_leaf_at_prolated_duration_and_rest_left_half( )``.

   .. versionchanged:: 1.1.2
      renamed ``leaftools.shorten( )`` to
      ``leaftools.split_leaf_at_prolated_duration_and_rest_right_half( )``.
   '''

   from abjad.tools.componenttools.split_component_at_prolated_duration_and_do_not_fracture_crossing_spanners import split_component_at_prolated_duration_and_do_not_fracture_crossing_spanners

   left, right = split_component_at_prolated_duration_and_do_not_fracture_crossing_spanners(leaf, prolated_duration)
   for leaf in right:
      Rest(leaf)

   return left, right
