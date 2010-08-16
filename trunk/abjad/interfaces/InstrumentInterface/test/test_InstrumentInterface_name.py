from abjad import *


def test_InstrumentInterface_name_01( ):
   '''Instrument interface name manages the LilyPond
   instrumentName context setting.
   Works with strings.
   '''

   t = Staff(macros.scale(4))
   t.set.instrument_name = 'Violini I'

   r'''
   \new Staff \with {
      instrumentName = "Violini I"
   } {
      c'8
      d'8
      e'8
      f'8
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == '\\new Staff \\with {\n\tinstrumentName = "Violini I"\n} {\n\tc\'8\n\td\'8\n\te\'8\n\tf\'8\n}'


def test_InstrumentInterface_name_02( ):
   '''Works with Markup.'''

   t = Staff(macros.scale(4))
   t.set.instrument_name = Markup(r'\circle { V }')

   r'''
   \new Staff \with {
      instrumentName = \markup { \circle { V } }
   } {
      c'8
      d'8
      e'8
      f'8
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Staff \\with {\n\tinstrumentName = \\markup { \\circle { V } }\n} {\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"
