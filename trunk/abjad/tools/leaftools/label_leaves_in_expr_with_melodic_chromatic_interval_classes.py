from abjad.components._Leaf import _Leaf
from abjad.components.Note import Note
from abjad.tools import componenttools
from abjad.tools import threadtools


def label_leaves_in_expr_with_melodic_chromatic_interval_classes(expr, markup_direction = 'up'):
   r""".. versionadded:: 1.1.2

   Label the melodic chromatic interval class of every leaf in `expr`. ::

      abjad> staff = Staff(notetools.make_notes([0, 25, 11, -4, -14, -13, 9, 10, 6, 5], [Rational(1, 8)]))
      abjad> leaftools.label_leaves_in_expr_with_melodic_chromatic_interval_classes(staff)
      abjad> f(staff)
      \new Staff {
              c'8 ^ \markup { +1 }
              cs'''8 ^ \markup { -2 }
              b'8 ^ \markup { -2 }
              af8 ^ \markup { -10 }
              bf,8 ^ \markup { +1 }
              b,8 ^ \markup { +10 }
              a'8 ^ \markup { +1 }
              bf'8 ^ \markup { -4 }
              fs'8 ^ \markup { -1 }
              f'8
      }
   """

   for note in componenttools.iterate_components_forward_in_expr(expr, Note):
      thread_iterator = threadtools.iterate_thread_forward_from_component(note, _Leaf)
      try:
         thread_iterator.next( )
         next_leaf = thread_iterator.next( )
         if isinstance(next_leaf, Note):
            mdi = note.pitch - next_leaf.pitch
            mci = mdi.melodic_chromatic_interval
            mcic = mci.interval_class
            #note.markup.up.append(mcic)
            markup_list = getattr(note.markup, markup_direction)
            markup_list.append(mcic)
      except StopIteration:
         pass
