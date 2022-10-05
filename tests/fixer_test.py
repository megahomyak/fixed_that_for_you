import pytest
from fixed_that_for_you import Fixer, unwrap
from dataclasses import dataclass


@dataclass
class Foo:
    bar: int
    blah: int

    def quux(self, n):
        return self.bar + n


def test_getting():
    foo = Fixer(Foo(1, 2))
    assert foo.bar == 1
    assert foo.baz == 1
    assert foo.blak == 2
    assert foo.quux(3) == 4
    assert foo.quux(n=3) == 4
    with pytest.raises(AttributeError):
        foo.jazz


def test_setting():
    foo = Fixer(Foo(1, 2))
    foo.blak += 2
    assert foo.blak == 4
    with pytest.raises(AttributeError):
        foo.jazz = 54
