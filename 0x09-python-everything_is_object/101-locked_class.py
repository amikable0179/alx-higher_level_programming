#!/usr/bin/python3
"""blocked class module"""


class LockedClass:
    """object prevents dynamic attribute except firstname"""

    __slots__ = ['first_name']
