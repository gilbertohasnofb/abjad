from abjad.component.slots import _ComponentFormatterSlotsInterface


class _LeafFormatterSlotsInterface(_ComponentFormatterSlotsInterface):

   def __init__(self, client):
      _ComponentFormatterSlotsInterface.__init__(self, client)
      
   ## PUBLIC ATTRIBUTES ##

   @property
   def slot_1(self):
      result = [ ]
      formatter = self.formatter
      leaf = formatter.leaf
      result.append(self.wrap(formatter, '_grace_body'))
      result.append(self.wrap(leaf.comments, 'before'))
      result.append(self.wrap(leaf.directives, 'before'))
      result.append(self.wrap(leaf.interfaces, 'overrides'))
      result.append(self.wrap(leaf.spanners, 'before'))
      result.append(self.wrap(leaf.interfaces, 'before'))
      return tuple(result)

   @property
   def slot_3(self):
      result = [ ]
      formatter = self.formatter
      leaf = formatter.leaf
      result.append(self.wrap(leaf.comments, 'opening'))
      result.append(self.wrap(leaf.directives, 'opening'))
      result.append(self.wrap(leaf.interfaces, 'opening'))
      result.append(self.wrap(formatter, '_agrace_opening'))
      return tuple(result)

   @property
   def slot_4(self):
      result = [ ]
      result.append(self.wrap(self.formatter, '_leaf_body'))
      return tuple(result)

   @property
   def slot_5(self):
      result = [ ]
      formatter = self.formatter
      leaf = formatter.leaf
      result.append(self.wrap(formatter, '_agrace_body'))
      result.append(self.wrap(leaf.directives, 'closing'))
      result.append(self.wrap(leaf.interfaces, 'closing'))
      result.append(self.wrap(leaf.comments, 'closing'))
      return tuple(result)

   @property
   def slot_7(self):
      result = [ ]
      formatter = self.formatter
      leaf = formatter.leaf
      result.append(self.wrap(leaf.interfaces, 'after'))
      result.append(self.wrap(leaf.spanners, 'after'))
      result.append(self.wrap(leaf.directives, 'after'))
      result.append(self.wrap(leaf.comments, 'after'))
      return tuple(result)
