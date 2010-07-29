from abjad.tools import iterate


def label_leaves_in_expr_with_leaf_numbers(expr, direction = 'below'):
   r'''Label the number of every leaf in `expr`, starting at 1.

   ::

      abjad> staff = Staff(macros.scale(4))
      abjad> leaftools.label_leaves_in_expr_with_leaf_numbers(staff)
      \new Staff {
              c'8 _ \markup { \small 1 }
              d'8 _ \markup { \small 2 }
              e'8 _ \markup { \small 3 }
              f'8 _ \markup { \small 4 }
      } 

   .. versionadded:: 1.1.2:
      new `direction` keyword parameter.

   .. versionchanged:: 1.1.2
      renamed ``label.leaf_numbers( )`` to
      ``leaftools.label_leaves_in_expr_with_leaf_numbers( )``.
   '''

   for i, leaf in enumerate(iterate.leaves_forward_in_expr(expr)):
      leaf_number = i + 1
      label = r'\small %s' % leaf_number
      if direction == 'below':
         leaf.markup.down.append(label)
      elif direction == 'above':
         leaf.markup.up.append(label)
      else:
         raise ValueError("must be 'above' or 'below'.")
