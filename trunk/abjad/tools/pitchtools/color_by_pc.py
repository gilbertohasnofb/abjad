from abjad.exceptions import MissingPitchError
from abjad.exceptions import ExtraPitchError
from abjad.scm import Color
from abjad.tools.pitchtools.get_pitch import get_pitch as \
   pitchtools_get_pitch


def color_by_pc(pitch_carrier):
   r'''Color `pitch_carrier` by pitch-class.

   ::

      abjad> t = Note(0, (1, 4))
      abjad> pitchtools.color_by_pc(t)
      abjad> print t.format
      \once \override NoteHead #'color = #(x11-color 'red)
      c'4
   
   Pitch-class colors are these.

   * 0: red
   * 1: MediumBlue
   * 2: orange
   * 3: LightSlateBlue
   * 4: ForestGreen
   * 5: MediumOrchid
   * 6: firebrick
   * 7: DeepPink
   * 8: DarkOrange
   * 9: IndianRed
   * 10: CadetBlue
   * 11: SeaGreen
   * 12: LimeGreen
   '''
   
   pitch = pitchtools_get_pitch(pitch_carrier)
   color = _pc_number_to_color(pitch.pc.number)
   if color is not None:
      pitch_carrier.note_head.color = color


def _pc_number_to_color(pc):
   
   pc_number_to_color = {
      0: Color('red'),
      1: Color('MediumBlue'),
      2: Color('orange'),
      3: Color('LightSlateBlue'),
      4: Color('ForestGreen'),
      5: Color('MediumOrchid'),
      6: Color('firebrick'),
      7: Color('DeepPink'),
      8: Color('DarkOrange'),
      9: Color('IndianRed'),
     10: Color('CadetBlue'),
     11: Color('SeaGreen'),
     12: Color('LimeGreen')}

   return pc_number_to_color.get(pc, None)
