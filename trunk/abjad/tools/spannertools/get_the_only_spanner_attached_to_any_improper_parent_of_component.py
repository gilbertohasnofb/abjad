def get_the_only_spanner_attached_to_any_improper_parent_of_component(
    component, spanner_classes=None):
    r'''.. versionadded:: 1.1

    Get the only spanner attached to any improper parent `component`:

    ::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> beam = spannertools.BeamSpanner(staff.select_leaves())
        >>> slur = spannertools.SlurSpanner(staff.select_leaves())
        >>> trill = spannertools.TrillSpanner(staff)
        >>> f(staff)
        \new Staff {
            c'8 [ ( \startTrillSpan
            d'8
            e'8
            f'8 ] ) \stopTrillSpan
        }

    ::

        >>> print spannertools.get_the_only_spanner_attached_to_any_improper_parent_of_component(
        ...     staff)
        TrillSpanner({c'8, d'8, e'8, f'8})

    Raise missing spanner error when no spanner attached to `component`.

    Raise extra spanner error when more than one spanner attached to `component`.

    Return a single spanner.

    .. note:: function will usually be called with `spanner_classes` 
              specifier set.
    '''
    from abjad.tools import spannertools

    # get spanners and count spanners
    spanners = \
        spannertools.get_spanners_attached_to_any_improper_parent_of_component(
            component, spanner_classes=spanner_classes)
    count = len(spanners)

    # raise or return
    if count == 0:
        raise MissingSpannerError
    elif count == 1:
        return spanners.pop()
    else:
        raise ExtraSpannerError
