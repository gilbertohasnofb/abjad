from abjad.tools import iterate


def extract_meters_from_measures_in_expr(components):
   '''Extract ordered list of meter pairs from ``components``.

   Example::

      abjad> t = Staff([RigidMeasure((2, 8), macros.scale(2)),
         RigidMeasure((3, 8), macros.scale(3)),
         RigidMeasure((4, 8), macros.scale(4))])

      abjad> metertools.extract_meters_from_measures_in_expr(t[:])
      [(2, 8), (3, 8), (4, 8)]

   Useful as input to some rhythmic transforms.

   .. versionchanged:: 1.1.2
      renamed ``metertools.extract_meter_list( )`` to
      ``metertools.extract_meters_from_measures_in_expr( )``.
   '''
   from abjad.tools import componenttools

   ## make sure components is a Python list of Abjad components
   assert componenttools.all_are_components(components)

   ## create empty list to hold result
   result = [ ]

   ## iterate measures and store meter pairs
   for measure in iterate.measures_forward_in_expr(components):
      meter = measure.meter.effective
      pair = (meter.numerator, meter.denominator)
      result.append(pair)

   ## return result
   return result
