from abjad.cfg.cfg import ABJADOUTPUT
from abjad.cfg.get_last_output import _get_last_output
from abjad.cfg.open_file import _open_file
from abjad.cfg.read_config_value import _read_config_value
import os


def pdf(target = -1):
   '''Open most recent Abjad-generated PDF.'''

   if isinstance(target, int) and target < 0:
      last_lilypond = _get_last_output( )
      if last_lilypond:
         last_number = last_lilypond.replace('.ly', '')
         target_number = int(last_number) + (target + 1)
         target_str = '%04d' % target_number
         target_pdf = os.path.join(ABJADOUTPUT, target_str + '.pdf')
      else:
         print 'Target PDF does not exist.'
   elif isinstance(target, int) and 0 <= target:
      target_str = '%04d' % target
      target_pdf = os.path.join(ABJADOUTPUT, target_str + '.pdf')
   elif isinstance(target, str):
      target_pdf = os.path.join(ABJADOUPUT, target)
   else:
      raise ValueError('can not get target pdf name from %s.' % target)

   if os.stat(target_pdf):
      pdfviewer = _read_config_value('pdfviewer')
      _open_file(target_pdf, pdfviewer)
   else:
      print 'Target PDF %s does not exist.' % target_pdf
