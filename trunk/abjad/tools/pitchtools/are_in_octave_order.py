def are_in_octave_order(pcs, pitches):
   '''True if `pcs` all appear
   in octave-relative order in `pitches`. ::

      abjad> pcs = [2, 7, 10]
      abjad> pitches = [6, 9, 12, 13, 14, 19, 22, 27, 28, 29, 32, 35]
      abjad> pitchtools.are_in_octave_order(pcs, pitches)
      True

   .. todo:: extend ``pitchtools.are_in_octave_order( )`` to work on 
      Abjad pitch instances.
   '''

   pcsStartIndex = [p % 12 for p in pitches].index(pcs[0] % 12)
   pcsTransposition = pitches[pcsStartIndex] - pcs[0]
   transposedPCs = [p + pcsTransposition for p in pcs]
   return set(transposedPCs).issubset(set(pitches))
