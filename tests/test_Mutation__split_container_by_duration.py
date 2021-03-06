import abjad


def test_Mutation__split_container_by_duration_01():
    """
    Split one container in score.
    Adds tie after split.
    """

    staff = abjad.Staff()
    staff.append(abjad.Container("c'8 d'8"))
    staff.append(abjad.Container("e'8 f'8"))
    leaves = abjad.select(staff).leaves()
    abjad.beam(leaves[:2])
    abjad.beam(leaves[-2:])
    abjad.slur(leaves)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                )
                ]
            }
        }
        """
    ), print(format(staff))

    abjad.Mutation._split_container_by_duration(staff[0], abjad.Duration(1, 32))

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'32
                [
                (
                ~
            }
            {
                c'16.
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                )
                ]
            }
        }
        """
    ), print(format(staff))

    assert abjad.wellformed(staff)


def test_Mutation__split_container_by_duration_02():
    """
    Split in-score container at split offset with non-power-of-two denominator.
    Does not tie leaves after split.
    """

    staff = abjad.Staff()
    staff.append(abjad.Container("c'8 d'8"))
    staff.append(abjad.Container("e'8 f'8"))
    leaves = abjad.select(staff).leaves()
    abjad.beam(leaves[:2])
    abjad.beam(leaves[-2:])
    abjad.slur(leaves)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                )
                ]
            }
        }
        """
    ), print(format(staff))

    abjad.Mutation._split_container_by_duration(staff[0], abjad.Duration(1, 5))

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
            }
            {
                \times 4/5 {
                    d'16.
                    ~
                    d'16
                    ]
                }
            }
            {
                e'8
                [
                f'8
                )
                ]
            }
        }
        """
    ), print(format(staff))

    assert abjad.wellformed(staff)
