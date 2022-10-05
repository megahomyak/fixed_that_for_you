from difflib import SequenceMatcher


class Fixer:

    def __init__(self, inner):
        object.__setattr__(self, "_inner", inner)

    def __getattribute__(self, name):
        return getattr(
            object.__getattribute__(self, "_inner"),
            object.__getattribute__(self, "_get_matching_field_name")(name),
        )

    def _get_matching_field_name(self, requested_field_name):
        field_info = max(
            (
                (
                    SequenceMatcher(
                        None, requested_field_name, existing_field_name
                    ).ratio(),
                    existing_field_name
                )
                for existing_field_name in dir(
                    object.__getattribute__(self, "_inner")
                )
            ), key=lambda f: f[0]
        )
        if field_info[0] > 0.5:
            return field_info[1]
        raise AttributeError

    def __setattr__(self, name, value):
        setattr(
            object.__getattribute__(self, "_inner"),
            object.__getattribute__(self, "_get_matching_field_name")(name),
            value,
        )


def unwrap(fixer):
    return object.__getattribute__(fixer, "_inner")


__all__ = ["Fixer", "unwrap"]
