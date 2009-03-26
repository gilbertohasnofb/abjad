from abjad.helpers.assess_components import assess_components
from abjad.helpers.components_switch_parent_to import \
   _components_switch_parent_to
from abjad.helpers.container_contents_scale import container_contents_scale
from abjad.helpers.get_parent_and_indices import get_parent_and_indices
from abjad.helpers.is_measure_list import _is_measure_list
from abjad.helpers.make_best_meter import _make_best_meter
from abjad.measure.rigid.measure import RigidMeasure
from abjad.meter.meter import Meter


def measures_fuse(measure_list):
   '''Fuse measures in measure_list.
      Calculate best new time signature.

      Better than naive spanner handling.'''

   assert _is_measure_list(measure_list)

   if len(measure_list) == 0:
      return None

   if len(measure_list) == 1:
      return measure_list[0]

   parent, parent_index, stop_index = get_parent_and_indices(measure_list)

   old_denominators = [x.meter.effective.denominator for x in measure_list]
   new_duration = sum([x.meter.effective.duration for x in measure_list])

   new_meter = _make_best_meter(new_duration, old_denominators)

   music = [ ]
   for measure in measure_list:
      multiplier = ~new_meter.multiplier * measure.meter.effective.multiplier
      measure_music = measure[:]
      container_contents_scale(measure_music, multiplier)
      music += measure_music

   _components_switch_parent_to(music, None)
   new_measure = RigidMeasure(new_meter, music)
   _components_switch_parent_to(measure_list, None)
   parent.insert(parent_index, new_measure)

   ## TODO: this is probably pretty good code to encapsulate for later use

   for i, measure in enumerate(measure_list):
      for spanner in list(measure.spanners.attached):
         spanner_index = spanner.index(measure)
         #spanner[spanner_index] = new_measure
         spanner._components[spanner_index] = new_measure
         new_measure.spanners._add(spanner)
         subsequent_measures = measure_list[i:]
         for subsequent_measure in subsequent_measures:
            if subsequent_measure in spanner:
               spanner.remove(subsequent_measure)

   return new_measure 
