# What?

This is a library that automatically fixes the field names of a wrapped object.

It throws an `AttributeError` if it cannot find a field with a similar name.

**Warning**: dunder methods do not work properly.

# Why?

For fun.

# How?

Install it from PyPI:

    pip install fixed_that_for_you

Use the `Fixer` class to wrap an object and the `unwrap` function to unwrap it.

Example:

    from fixed_that_for_you import Fixer, unwrap
    l = Fixer([2, 1])
    l.srt()
    assert unwrap(l) == [1, 2]
