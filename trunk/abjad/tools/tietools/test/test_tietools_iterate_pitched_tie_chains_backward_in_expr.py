from abjad import *


def test_tietools_iterate_pitched_tie_chains_backward_in_expr_01():

    staff = Staff('c ~ c r d ~ d r')

    tie_chains = list(tietools.iterate_pitched_tie_chains_backward_in_expr(staff))

    assert tie_chains[0] == tietools.TieChain(staff[3:5])
    assert tie_chains[1] == tietools.TieChain(staff[:2])
