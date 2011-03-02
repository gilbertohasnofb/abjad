import copy
from abjad.core import _Immutable
from fractions import Fraction


class BoundedInterval(_Immutable):
   '''A low / high pair, carrying some metadata.'''

   __slots__ = ('data', 'high', 'low', )

   def __init__(self, *args, **kwargs):
      if len(args) == 1 and isinstance(args[0], BoundedInterval):
         low, high, data = args[0].low, args[0].high, args[0].data
      elif len(args) == 2:
         low, high, data = args[0], args[1], None
         if 'data' in kwargs:
            data = kwargs['data']
      elif len(args) == 3:
         low, high, data = args[0], args[1], args[2]
      assert isinstance(low, (int, Fraction))
      assert isinstance(high, (int, Fraction))
#        assert low <= high 
      assert low < high
      if data is not None:
         data = copy.copy(data)
      else:
         data = { }
      object.__setattr__(self, 'low', low)
      object.__setattr__(self, 'high', high)
      object.__setattr__(self, 'data', data)

   ## OVERLOADS ##

   def __repr__(self):
      return '%s(%s, %s, data = %s)' % \
         (self.__class__.__name__, \
         repr(self.low), \
         repr(self.high), \
         repr(self.data))

   ## PUBLIC ATTRIBUTES ##

   @property
   def centroid(self):
      '''Center point of low and high bounds.'''
      return Fraction(self.high + self.low) / 2

   @property
   def magnitude(self):
      '''High bound minus low bound.'''
      return self.high - self.low

   @property
   def signature(self):
      '''Tuple of low bound and high bound.'''
      return (self.low, self.high)

   ## PUBLIC METHODS ##

   def get_overlap_with_interval(self, interval):
      '''Return amount of overlap with `interval`.'''
      assert isinstance(interval, BoundedInterval)
      if not self.is_overlapped_by_interval(interval):
         return 0
      elif self.is_container_of_interval(interval):
         return interval.magnitude
      elif self.is_contained_by_interval(interval):
         return self.magnitude
      elif self.low < interval.low:
         return self.high - interval.low
      else:
         return interval.high - self.low

   def is_container_of_interval(self, interval):
      '''True if interval contains `interval`.'''
      assert isinstance(interval, BoundedInterval)
      if self.low <= interval.low and interval.high <= self.high:
         return True
      else:
         return False

   def is_contained_by_interval(self, interval):
      '''True if interval is contained by `interval`.'''
      assert isinstance(interval, BoundedInterval)
      if interval.low <= self.low and self.high <= interval.high:
         return True
      else:
         return False

   def is_overlapped_by_interval(self, interval):
      '''True if interval is overlapped by `interval`.'''
      assert isinstance(interval, BoundedInterval)
      if self.is_container_of_interval(interval):
         return True
      elif self.is_contained_by_interval(interval):
         return True
      elif self.low < interval.low < self.high:
         return True
      elif self.low == interval.low:
         return True
      elif self.high == interval.high:
         return True
      elif self.low < interval.high < self.high:
         return True
      else:
         return False

   def is_tangent_to_interval(self, interval):
      '''True if interval is tangent to `interval`.'''
      assert isinstance(interval, BoundedInterval)
      if self.high == interval.low or interval.high == self.low:
         return True
      else:
         return False

   def scale_by_rational(self, rational):
      assert isinstance(rational, (int, Fraction))
      assert 0 <= rational
      if rational != 1:
         new_magnitude = (self.high - self.low) * rational
         return self.__class__(BoundedInterval(self.low, self.low + new_magnitude, self.data))
      else:
         return self

   def scale_to_rational(self, rational):
      assert isinstance(rational, (int, Fraction))
      assert 0 <= rational
      if rational != self.magnitude:
         return self.__class__(BoundedInterval(self.low, self.low + rational, self.data))
      else:
         return self

   def shift_by_rational(self, rational):
      assert isinstance(rational, (int, Fraction))
      if rational != 0:
         return self.__class__(BoundedInterval(self.low + rational, self.high + rational, self.data))
      else:
         return self

   def shift_to_rational(self, rational):
      assert isinstance(rational, (int, Fraction))
      if rational != self.low:
         magnitude = self.high - self.low
         return self.__class__(BoundedInterval(rational, rational + magnitude, self.data))
      else:
         return self

   def split_at_rational(self, rational):
      assert isinstance(rational, (int, Fraction))
      if self.low < rational < self.high:
         return (self.__class__(BoundedInterval(self.low, rational, self.data)),
               self.__class__(BoundedInterval(rational, self.high, self.data)))
      else:
         return (self,)
