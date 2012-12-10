lilypond_version = "2.16.1"

grob-interfaces = {
    "Accidental": [
        "accidental-interface",
        "font-interface",
        "grob-interface",
        "inline-accidental-interface",
        "item-interface",
    ],
    "AccidentalCautionary": [
        "accidental-interface",
        "font-interface",
        "grob-interface",
        "inline-accidental-interface",
        "item-interface",
    ],
    "AccidentalPlacement": [
        "accidental-placement-interface",
        "grob-interface",
        "item-interface",
    ],
    "AccidentalSuggestion": [
        "accidental-interface",
        "accidental-suggestion-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "script-interface",
        "self-alignment-interface",
        "side-position-interface",
    ],
    "Ambitus": [
        "ambitus-interface",
        "axis-group-interface",
        "break-aligned-interface",
        "grob-interface",
        "item-interface",
    ],
    "AmbitusAccidental": [
        "accidental-interface",
        "break-aligned-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "side-position-interface",
    ],
    "AmbitusLine": [
        "ambitus-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
    ],
    "AmbitusNoteHead": [
        "ambitus-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "ledgered-interface",
        "note-head-interface",
        "rhythmic-head-interface",
        "staff-symbol-referencer-interface",
    ],
    "Arpeggio": [
        "arpeggio-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "side-position-interface",
        "staff-symbol-referencer-interface",
    ],
    "BalloonTextItem": [
        "balloon-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "text-interface",
    ],
    "BarLine": [
        "bar-line-interface",
        "break-aligned-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "pure-from-neighbor-interface",
    ],
    "BarNumber": [
        "break-alignable-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
    ],
    "BassFigure": [
        "bass-figure-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "rhythmic-grob-interface",
        "text-interface",
    ],
    "BassFigureAlignment": [
        "align-interface",
        "axis-group-interface",
        "bass-figure-alignment-interface",
        "grob-interface",
        "spanner-interface",
    ],
    "BassFigureAlignmentPositioning": [
        "axis-group-interface",
        "grob-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "BassFigureBracket": [
        "enclosing-bracket-interface",
        "grob-interface",
        "item-interface",
    ],
    "BassFigureContinuation": [
        "figured-bass-continuation-interface",
        "grob-interface",
        "spanner-interface",
    ],
    "BassFigureLine": [
        "axis-group-interface",
        "grob-interface",
        "spanner-interface",
    ],
    "Beam": [
        "beam-interface",
        "font-interface",
        "grob-interface",
        "spanner-interface",
        "staff-symbol-referencer-interface",
        "unbreakable-spanner-interface",
    ],
    "BendAfter": [
        "bend-after-interface",
        "grob-interface",
        "spanner-interface",
    ],
    "BreakAlignGroup": [
        "axis-group-interface",
        "break-aligned-interface",
        "grob-interface",
        "item-interface",
    ],
    "BreakAlignment": [
        "axis-group-interface",
        "break-alignment-interface",
        "grob-interface",
        "item-interface",
    ],
    "BreathingSign": [
        "break-aligned-interface",
        "breathing-sign-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "text-interface",
    ],
    "ChordName": [
        "chord-name-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "rhythmic-grob-interface",
        "text-interface",
    ],
    "Clef": [
        "break-aligned-interface",
        "clef-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "pure-from-neighbor-interface",
        "staff-symbol-referencer-interface",
    ],
    "ClusterSpanner": [
        "cluster-interface",
        "grob-interface",
        "spanner-interface",
    ],
    "ClusterSpannerBeacon": [
        "cluster-beacon-interface",
        "grob-interface",
        "item-interface",
        "rhythmic-grob-interface",
    ],
    "CombineTextScript": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "side-position-interface",
        "text-interface",
        "text-script-interface",
    ],
    "CueClef": [
        "break-aligned-interface",
        "clef-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "pure-from-neighbor-interface",
        "staff-symbol-referencer-interface",
    ],
    "CueEndClef": [
        "break-aligned-interface",
        "clef-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "pure-from-neighbor-interface",
        "staff-symbol-referencer-interface",
    ],
    "Custos": [
        "break-aligned-interface",
        "custos-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "staff-symbol-referencer-interface",
    ],
    "DotColumn": [
        "axis-group-interface",
        "dot-column-interface",
        "grob-interface",
        "item-interface",
    ],
    "Dots": [
        "dots-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "staff-symbol-referencer-interface",
    ],
    "DoublePercentRepeat": [
        "break-aligned-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "percent-repeat-interface",
        "percent-repeat-item-interface",
    ],
    "DoublePercentRepeatCounter": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "percent-repeat-interface",
        "percent-repeat-item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
    ],
    "DoubleRepeatSlash": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "percent-repeat-interface",
        "percent-repeat-item-interface",
        "rhythmic-grob-interface",
    ],
    "DynamicLineSpanner": [
        "axis-group-interface",
        "dynamic-interface",
        "dynamic-line-spanner-interface",
        "grob-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "DynamicText": [
        "dynamic-interface",
        "dynamic-text-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "script-interface",
        "self-alignment-interface",
        "text-interface",
    ],
    "DynamicTextSpanner": [
        "dynamic-interface",
        "dynamic-text-spanner-interface",
        "font-interface",
        "grob-interface",
        "line-interface",
        "line-spanner-interface",
        "spanner-interface",
        "text-interface",
    ],
    "Episema": [
        "episema-interface",
        "font-interface",
        "grob-interface",
        "line-interface",
        "line-spanner-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "Fingering": [
        "finger-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
        "text-script-interface",
    ],
    "Flag": [
        "flag-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
    ],
    "FootnoteItem": [
        "balloon-interface",
        "font-interface",
        "footnote-interface",
        "grob-interface",
        "item-interface",
        "text-interface",
    ],
    "FootnoteSpanner": [
        "balloon-interface",
        "font-interface",
        "footnote-interface",
        "footnote-spanner-interface",
        "grob-interface",
        "spanner-interface",
        "text-interface",
    ],
    "FretBoard": [
        "chord-name-interface",
        "font-interface",
        "fret-diagram-interface",
        "grob-interface",
        "item-interface",
        "rhythmic-grob-interface",
    ],
    "Glissando": [
        "glissando-interface",
        "grob-interface",
        "line-interface",
        "line-spanner-interface",
        "spanner-interface",
        "unbreakable-spanner-interface",
    ],
    "GraceSpacing": [
        "grace-spacing-interface",
        "grob-interface",
        "spacing-options-interface",
        "spanner-interface",
    ],
    "GridLine": [
        "grid-line-interface",
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
    ],
    "GridPoint": [
        "grid-point-interface",
        "grob-interface",
        "item-interface",
    ],
    "Hairpin": [
        "dynamic-interface",
        "grob-interface",
        "hairpin-interface",
        "line-interface",
        "self-alignment-interface",
        "spanner-interface",
    ],
    "HorizontalBracket": [
        "grob-interface",
        "horizontal-bracket-interface",
        "line-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "InstrumentName": [
        "font-interface",
        "grob-interface",
        "self-alignment-interface",
        "side-position-interface",
        "spanner-interface",
        "system-start-text-interface",
    ],
    "InstrumentSwitch": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
    ],
    "KeyCancellation": [
        "break-aligned-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "key-cancellation-interface",
        "key-signature-interface",
        "pure-from-neighbor-interface",
        "staff-symbol-referencer-interface",
    ],
    "KeySignature": [
        "break-aligned-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "key-signature-interface",
        "pure-from-neighbor-interface",
        "staff-symbol-referencer-interface",
    ],
    "LaissezVibrerTie": [
        "grob-interface",
        "item-interface",
        "semi-tie-interface",
    ],
    "LaissezVibrerTieColumn": [
        "grob-interface",
        "item-interface",
        "semi-tie-column-interface",
    ],
    "LedgerLineSpanner": [
        "grob-interface",
        "ledger-line-spanner-interface",
        "spanner-interface",
    ],
    "LeftEdge": [
        "break-aligned-interface",
        "grob-interface",
        "item-interface",
    ],
    "LigatureBracket": [
        "grob-interface",
        "line-interface",
        "spanner-interface",
        "tuplet-bracket-interface",
    ],
    "LyricExtender": [
        "grob-interface",
        "lyric-extender-interface",
        "lyric-interface",
        "spanner-interface",
    ],
    "LyricHyphen": [
        "font-interface",
        "grob-interface",
        "lyric-hyphen-interface",
        "lyric-interface",
        "spanner-interface",
    ],
    "LyricSpace": [
        "grob-interface",
        "lyric-hyphen-interface",
        "spanner-interface",
    ],
    "LyricText": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "lyric-syllable-interface",
        "rhythmic-grob-interface",
        "self-alignment-interface",
        "text-interface",
    ],
    "MeasureGrouping": [
        "grob-interface",
        "measure-grouping-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "MelodyItem": [
        "grob-interface",
        "item-interface",
        "melody-spanner-interface",
    ],
    "MensuralLigature": [
        "font-interface",
        "grob-interface",
        "mensural-ligature-interface",
        "spanner-interface",
    ],
    "MetronomeMark": [
        "break-alignable-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "metronome-mark-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
    ],
    "MultiMeasureRest": [
        "font-interface",
        "grob-interface",
        "multi-measure-interface",
        "multi-measure-rest-interface",
        "rest-interface",
        "spanner-interface",
        "staff-symbol-referencer-interface",
    ],
    "MultiMeasureRestNumber": [
        "font-interface",
        "grob-interface",
        "multi-measure-interface",
        "self-alignment-interface",
        "side-position-interface",
        "spanner-interface",
        "text-interface",
    ],
    "MultiMeasureRestText": [
        "font-interface",
        "grob-interface",
        "multi-measure-interface",
        "self-alignment-interface",
        "side-position-interface",
        "spanner-interface",
        "text-interface",
    ],
    "NonMusicalPaperColumn": [
        "axis-group-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "paper-column-interface",
        "separation-item-interface",
        "spaceable-grob-interface",
    ],
    "NoteCollision": [
        "axis-group-interface",
        "grob-interface",
        "item-interface",
        "note-collision-interface",
    ],
    "NoteColumn": [
        "axis-group-interface",
        "grob-interface",
        "item-interface",
        "note-column-interface",
        "separation-item-interface",
    ],
    "NoteHead": [
        "font-interface",
        "gregorian-ligature-interface",
        "grob-interface",
        "item-interface",
        "ledgered-interface",
        "ligature-head-interface",
        "mensural-ligature-interface",
        "note-head-interface",
        "rhythmic-grob-interface",
        "rhythmic-head-interface",
        "staff-symbol-referencer-interface",
        "vaticana-ligature-interface",
    ],
    "NoteName": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "note-name-interface",
        "text-interface",
    ],
    "NoteSpacing": [
        "grob-interface",
        "item-interface",
        "note-spacing-interface",
        "spacing-interface",
    ],
    "OctavateEight": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
    ],
    "OttavaBracket": [
        "font-interface",
        "grob-interface",
        "horizontal-bracket-interface",
        "line-interface",
        "ottava-bracket-interface",
        "side-position-interface",
        "spanner-interface",
        "text-interface",
    ],
    "PaperColumn": [
        "axis-group-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "paper-column-interface",
        "separation-item-interface",
        "spaceable-grob-interface",
    ],
    "ParenthesesItem": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "parentheses-interface",
    ],
    "PercentRepeat": [
        "font-interface",
        "grob-interface",
        "multi-measure-rest-interface",
        "percent-repeat-interface",
        "spanner-interface",
    ],
    "PercentRepeatCounter": [
        "font-interface",
        "grob-interface",
        "percent-repeat-interface",
        "self-alignment-interface",
        "side-position-interface",
        "spanner-interface",
        "text-interface",
    ],
    "PhrasingSlur": [
        "grob-interface",
        "slur-interface",
        "spanner-interface",
    ],
    "PianoPedalBracket": [
        "grob-interface",
        "line-interface",
        "piano-pedal-bracket-interface",
        "piano-pedal-interface",
        "spanner-interface",
    ],
    "RehearsalMark": [
        "break-alignable-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "mark-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
    ],
    "RepeatSlash": [
        "grob-interface",
        "item-interface",
        "percent-repeat-interface",
        "percent-repeat-item-interface",
        "rhythmic-grob-interface",
    ],
    "RepeatTie": [
        "grob-interface",
        "item-interface",
        "semi-tie-interface",
    ],
    "RepeatTieColumn": [
        "grob-interface",
        "item-interface",
        "semi-tie-column-interface",
    ],
    "Rest": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "rest-interface",
        "rhythmic-grob-interface",
        "rhythmic-head-interface",
        "staff-symbol-referencer-interface",
    ],
    "RestCollision": [
        "grob-interface",
        "item-interface",
        "rest-collision-interface",
    ],
    "Script": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "script-interface",
        "side-position-interface",
    ],
    "ScriptColumn": [
        "grob-interface",
        "item-interface",
        "script-column-interface",
    ],
    "ScriptRow": [
        "grob-interface",
        "item-interface",
        "script-column-interface",
    ],
    "Slur": [
        "grob-interface",
        "slur-interface",
        "spanner-interface",
    ],
    "SostenutoPedal": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "piano-pedal-script-interface",
        "self-alignment-interface",
        "text-interface",
    ],
    "SostenutoPedalLineSpanner": [
        "axis-group-interface",
        "grob-interface",
        "piano-pedal-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "SpacingSpanner": [
        "grob-interface",
        "spacing-options-interface",
        "spacing-spanner-interface",
        "spanner-interface",
    ],
    "SpanBar": [
        "bar-line-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "span-bar-interface",
    ],
    "SpanBarStub": [
        "grob-interface",
        "item-interface",
        "pure-from-neighbor-interface",
    ],
    "StaffGrouper": [
        "grob-interface",
        "spanner-interface",
        "staff-grouper-interface",
    ],
    "StaffSpacing": [
        "grob-interface",
        "item-interface",
        "spacing-interface",
        "staff-spacing-interface",
    ],
    "StaffSymbol": [
        "grob-interface",
        "spanner-interface",
        "staff-symbol-interface",
    ],
    "StanzaNumber": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "side-position-interface",
        "stanza-number-interface",
        "text-interface",
    ],
    "Stem": [
        "grob-interface",
        "item-interface",
        "stem-interface",
    ],
    "StemStub": [
        "grob-interface",
        "item-interface",
    ],
    "StemTremolo": [
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
        "stem-tremolo-interface",
    ],
    "StringNumber": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "string-number-interface",
        "text-interface",
        "text-script-interface",
    ],
    "StrokeFinger": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "stroke-finger-interface",
        "text-interface",
        "text-script-interface",
    ],
    "SustainPedal": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "piano-pedal-interface",
        "piano-pedal-script-interface",
        "self-alignment-interface",
        "text-interface",
    ],
    "SustainPedalLineSpanner": [
        "axis-group-interface",
        "grob-interface",
        "piano-pedal-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "System": [
        "axis-group-interface",
        "grob-interface",
        "spanner-interface",
        "system-interface",
    ],
    "SystemStartBar": [
        "grob-interface",
        "side-position-interface",
        "spanner-interface",
        "system-start-delimiter-interface",
    ],
    "SystemStartBrace": [
        "font-interface",
        "grob-interface",
        "side-position-interface",
        "spanner-interface",
        "system-start-delimiter-interface",
    ],
    "SystemStartBracket": [
        "font-interface",
        "grob-interface",
        "side-position-interface",
        "spanner-interface",
        "system-start-delimiter-interface",
    ],
    "SystemStartSquare": [
        "font-interface",
        "grob-interface",
        "side-position-interface",
        "spanner-interface",
        "system-start-delimiter-interface",
    ],
    "TabNoteHead": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "note-head-interface",
        "rhythmic-grob-interface",
        "rhythmic-head-interface",
        "staff-symbol-referencer-interface",
        "tab-note-head-interface",
        "text-interface",
    ],
    "TextScript": [
        "font-interface",
        "grob-interface",
        "instrument-specific-markup-interface",
        "item-interface",
        "self-alignment-interface",
        "side-position-interface",
        "text-interface",
        "text-script-interface",
    ],
    "TextSpanner": [
        "font-interface",
        "grob-interface",
        "line-interface",
        "line-spanner-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "Tie": [
        "grob-interface",
        "spanner-interface",
        "tie-interface",
    ],
    "TieColumn": [
        "grob-interface",
        "spanner-interface",
        "tie-column-interface",
    ],
    "TimeSignature": [
        "break-aligned-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "pure-from-neighbor-interface",
        "time-signature-interface",
    ],
    "TrillPitchAccidental": [
        "accidental-interface",
        "font-interface",
        "grob-interface",
        "inline-accidental-interface",
        "item-interface",
        "side-position-interface",
        "trill-pitch-accidental-interface",
    ],
    "TrillPitchGroup": [
        "axis-group-interface",
        "font-interface",
        "grob-interface",
        "item-interface",
        "note-head-interface",
        "parentheses-interface",
        "side-position-interface",
    ],
    "TrillPitchHead": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "ledgered-interface",
        "pitched-trill-interface",
        "rhythmic-head-interface",
        "staff-symbol-referencer-interface",
    ],
    "TrillSpanner": [
        "font-interface",
        "grob-interface",
        "line-interface",
        "line-spanner-interface",
        "side-position-interface",
        "spanner-interface",
        "trill-spanner-interface",
    ],
    "TupletBracket": [
        "grob-interface",
        "line-interface",
        "spanner-interface",
        "tuplet-bracket-interface",
    ],
    "TupletNumber": [
        "font-interface",
        "grob-interface",
        "spanner-interface",
        "text-interface",
        "tuplet-number-interface",
    ],
    "UnaCordaPedal": [
        "font-interface",
        "grob-interface",
        "item-interface",
        "piano-pedal-script-interface",
        "self-alignment-interface",
        "text-interface",
    ],
    "UnaCordaPedalLineSpanner": [
        "axis-group-interface",
        "grob-interface",
        "piano-pedal-interface",
        "side-position-interface",
        "spanner-interface",
    ],
    "VaticanaLigature": [
        "font-interface",
        "grob-interface",
        "spanner-interface",
        "vaticana-ligature-interface",
    ],
    "VerticalAlignment": [
        "align-interface",
        "axis-group-interface",
        "grob-interface",
        "spanner-interface",
    ],
    "VerticalAxisGroup": [
        "axis-group-interface",
        "grob-interface",
        "hara-kiri-group-spanner-interface",
        "spanner-interface",
    ],
    "VoiceFollower": [
        "grob-interface",
        "line-interface",
        "line-spanner-interface",
        "spanner-interface",
    ],
    "VoltaBracket": [
        "font-interface",
        "grob-interface",
        "horizontal-bracket-interface",
        "line-interface",
        "side-position-interface",
        "spanner-interface",
        "text-interface",
        "volta-bracket-interface",
        "volta-interface",
    ],
    "VoltaBracketSpanner": [
        "axis-group-interface",
        "grob-interface",
        "side-position-interface",
        "spanner-interface",
        "volta-interface",
    ],
}
