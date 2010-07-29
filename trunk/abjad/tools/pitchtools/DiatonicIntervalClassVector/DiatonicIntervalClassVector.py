from abjad.tools.pitchtools.get_harmonic_diatonic_intervals_in import \
   get_harmonic_diatonic_intervals_in
from abjad.tools.pitchtools.list_all_diatonic_interval_classes import \
   list_all_diatonic_interval_classes


class DiatonicIntervalClassVector(dict):
   '''.. versionadded:: 1.1.2

   Diatonic interval class vector. ::

      abjad> staff = Staff(macros.scale(5))

   Vector is not quatertone-aware.
   '''

   def __init__(self, expr): 
      self.all_dics = list_all_diatonic_interval_classes( )
      for dic in self.all_dics:
         self[dic] = 0
      for hdi in get_harmonic_diatonic_intervals_in(expr):
         dic = hdi.diatonic_interval_class
         self[dic] += 1

   ## OVERLOADS ##

   def __eq__(self, arg):
      if isinstance(arg, type(self)):
         if self._contents_string == arg._contents_string:
            return True
      return False

   def __ne__(self, arg):
      return not self == arg

   def __repr__(self):
      return '%s(%s)' % (self.__class__.__name__, self._contents_string)

   def __str__(self):
      return '{%s}' % self._contents_string

   ## PRIVATE ATTRIBUTES ##

   @property
   def _contents_string(self):
      parts = [ ]
      for dic in self.all_dics:
         count = self[dic]
         part = '%s: %s' % (dic, count)
         parts.append(part)
      contents_string = ', '.join(parts)
      return contents_string
