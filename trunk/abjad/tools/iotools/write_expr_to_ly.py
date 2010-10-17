from abjad.cfg.cfg import ABJADPATH
from abjad.tools.iotools._insert_expr_into_lily_file import _insert_expr_into_lily_file
import os


def write_expr_to_ly(expr, file_name, template = None):
   '''Write `expr` to `file_name`::

      abjad> note = Note(0, (1, 4))
      abjad> write_expr_to_ly(note, '/home/user/foo.ly')
   
   Write `expr` to `file_name` with `template`::

      abjad> note = Note(0, (1, 4))
      abjad> write_expr_to_ly(note, '/home/user/foo.ly', 'paris')

   .. versionchanged:: 1.1.2
      renamed ``io.write_ly( )`` to
      ``io.write_expr_to_ly( )``.
   '''

   file_name = os.path.expanduser(file_name)
   if not file_name.endswith('.ly'):
      file_name += '.ly'
   try:
      outfile = open(file_name, 'w')
      lily_file = _insert_expr_into_lily_file(expr)
      if template is not None:
         if not template.endswith('.ly'):
            template += '.ly'
         full_path_to_template = os.path.join(ABJADPATH, 'templates', template)
         lily_file.file_initial_system_includes.append(full_path_to_template)
      outfile.write(lily_file.format)
      outfile.close( )
   except IOError:
      print 'ERROR: cound not open file %s' % file_name
      dirname = os.path.dirname(file_name)
      if dirname:
         print 'Make sure "%s" exists in your system.' % dirname

   print 'LilyPond input file written to %s' % os.path.basename(file_name)
