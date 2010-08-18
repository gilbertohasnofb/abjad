from abjad.components._Leaf import _Leaf
from abjad.tools.componenttools.get_nth_component_in_expr import get_nth_component_in_expr


def get_nth_leaf_in_expr(expr, n = 0):
   r'''.. versionadded:: 1.1.2

   Return leaf `n` in `expr`. ::

      abjad> staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 3)
      abjad> macros.diatonicize(staff)
      abjad> f(staff)
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

   ::

      abjad> for n in range(6):
      ...     leaftools.get_nth_leaf_in_expr(t, n)
      ... 
      Note(c', 8)
      Note(d', 8)
      Note(e', 8)
      Note(f', 8)
      Note(g', 8)
      Note(a', 8)

   Read backwards for negative values of `n`. ::

      abjad> leaftools.get_nth_leaf_in_expr(t, -1)
      Note(a', 8)
      
   .. note:: Because this function returns as soon as it finds instance
      `n` of `klasses`, it is more efficient to call
      ``leaftools.get_nth_leaf_in_expr(expr, 0)`` than ``expr.leaves[0]``.
      It is likewise more efficient to call
      ``leaftools.get_nth_leaf_in_expr(expr, -1)`` than ``expr.leaves[-1]``.

   .. todo:: implement ``iterate.yield_leaves(expr, i = 0, j = None)``
      as a generalization of, and companion to, this function.

   .. versionchanged:: 1.1.2
      renamed ``iterate.get_nth_leaf( )`` to ``leaftools.get_nth_leaf_in_expr( )``.

   .. versionchanged:: 1.1.2
      renamed ``iterate.get_nth_leaf_in( )`` to
      ``leaftools.get_nth_leaf_in_expr( )``.

   .. versionchanged:: 1.1.2
      renamed ``iterate.get_nth_leaf_in_expr( )`` to
      ``leaftools.get_nth_leaf_in_expr( )``.
   '''

   return get_nth_component_in_expr(expr, _Leaf, n)
