from abjad.tools import check
from abjad.tools.spannertools.get_contained import get_contained


def get_covered(components):
   '''Return unordered set of  spanners completely contained
      within the time bounds of thread-contiguous components.

      Compare 'covered' spanners with 'contained' spanners.
      Compare 'covered' spanners with 'dominant' spanners.'''

   check.assert_components(components, contiguity = 'thread') 

   if not len(components):
      return set([ ])

   first, last = components[0], components[-1]
   components_begin = first.offset.score
   components_end = last.offset.score + last.duration.prolated

   result = get_contained(components)
   for spanner in list(result):
      if spanner.begin < components_begin or \
         components_end < spanner.end:
         result.discard(spanner)
   
   return result  
