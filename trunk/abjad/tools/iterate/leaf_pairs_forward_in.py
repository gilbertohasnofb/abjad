from abjad.tools import listtools
from abjad.tools.iterate.vertical_moments_forward_in import \
   vertical_moments_forward_in


def leaf_pairs_forward_in(expr):
   r'''.. versionadded:: 1.1.2

   Iterate left-to-right, top-to-bottom leaf pairs in `expr`. ::

      abjad> score = Score([ ])
      abjad> notes = construct.scale(4) + [Note(7, (1, 4))]
      abjad> score.append(Staff(notes))
      abjad> notes = [Note(x, (1, 4)) for x in [-12, -15, -17]]
      abjad> score.append(Staff(notes))
      abjad> score[1].clef.forced = Clef('bass')

   ::

      abjad> f(score)
      \new Score <<
              \new Staff {
                      c'8
                      d'8
                      e'8
                      f'8
                      g'4
              }
              \new Staff {
                      \clef "bass"
                      c4
                      a,4
                      g,4
              }
      >>

   ::

      abjad> for pair in iterate.leaf_pairs_forward_in(score):
      ...      pair
      set([Note(c', 8), Note(c, 4)])
      (Note(c', 8), Note(d', 8))
      (Note(c, 4), Note(d', 8))
      (Note(d', 8), Note(e', 8))
      (Note(d', 8), Note(a,, 4))
      (Note(c, 4), Note(e', 8))
      (Note(c, 4), Note(a,, 4))
      set([Note(e', 8), Note(a,, 4)])
      (Note(e', 8), Note(f', 8))
      (Note(a,, 4), Note(f', 8))
      (Note(f', 8), Note(g', 4))
      (Note(f', 8), Note(g,, 4))
      (Note(a,, 4), Note(g', 4))
      (Note(a,, 4), Note(g,, 4))
      set([Note(g', 4), Note(g,, 4)])

   .. note:: the function yields vertical pitch pairs as (unordered)
      sets but horizontal and diagonal pitch pairs as (ordered) pairs.
      Calling code can easily distinguish harmonic and melodic
      output from this function.
   '''

   vertical_moments = vertical_moments_forward_in(expr)
   for moment_1, moment_2 in listtools.pairwise(vertical_moments):
      for pair in listtools.get_unordered_pairs(moment_1.start_leaves):
         yield pair
      pairs = listtools.pairs_from_to(moment_1.leaves, moment_2.start_leaves)
      for pair in pairs: 
         yield pair
   else:
      for pair in listtools.get_unordered_pairs(moment_2.start_leaves):
         yield pair
