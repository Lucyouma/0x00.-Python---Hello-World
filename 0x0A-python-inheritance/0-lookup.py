#!/usr/bin/python3

"""Defines a lookup function of an object attribute."""


def lookup(obj):
    """Return a list of available attributes of an object."""
    return (dir(obj))
