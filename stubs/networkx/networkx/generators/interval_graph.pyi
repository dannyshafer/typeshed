from collections.abc import Iterable, Sequence
from typing import TypeVar

from networkx.classes.graph import Graph
from networkx.utils.backends import _dispatchable

__all__ = ["interval_graph"]

_T = TypeVar("_T")

@_dispatchable
def interval_graph(intervals: Iterable[Sequence[_T]]) -> Graph[tuple[_T, ...]]: ...
