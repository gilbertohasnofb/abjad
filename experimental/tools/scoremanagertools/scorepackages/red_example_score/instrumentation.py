# -*- encoding: utf-8 -*-
from abjad import *


instrumentation=instrumenttools.InstrumentationSpecifier(
	performers=instrumenttools.PerformerInventory([
		instrumenttools.Performer(
			name='hornist',
			instruments=instrumenttools.InstrumentInventory([
				instrumenttools.FrenchHorn(),
				])
			),
		instrumenttools.Performer(
			name='trombonist',
			instruments=instrumenttools.InstrumentInventory([
				instrumenttools.TenorTrombone(),
				])
			),
		instrumenttools.Performer(
			name='violinist',
			instruments=instrumenttools.InstrumentInventory([
				instrumenttools.Violin(),
				])
			),
		instrumenttools.Performer(
			name='cellist',
			instruments=instrumenttools.InstrumentInventory([
				instrumenttools.Cello(),
				])
			),
		instrumenttools.Performer(
			name='pianist',
			instruments=instrumenttools.InstrumentInventory([
				instrumenttools.Piano(),
				])
			),
		instrumenttools.Performer(
			name='percussionist',
			instruments=instrumenttools.InstrumentInventory([])
			),
		])
	)