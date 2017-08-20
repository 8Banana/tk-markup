import tkinter as tk


def _pairs(sequence):
    if len(sequence) % 2 != 0:
        raise ValueError("odd number of elements in " + repr(sequence))
    return zip(sequence[0::2], sequence[1::2])


def _to_dict(string, any_widget):
    return dict(_pairs(any_widget.tk.splitlist(string)))


# all of these can be None, except class_name
def create_widget(parent_widget, class_name, pack_opts, grid_opts,
                  place_opts, config_opts):
    cls = getattr(tk, class_name):
    # TODO: validate cls?

    if parent_widget is None:
        # probably Tk
        widget = cls()
        widget.config(**config)
    else:
        config = dict(_pairs(parent_widget.tk.splitlist(config_opts)))
        widget = cls(parent_widget, **config)

    # tkinter raises an error if more than one of these is specified
    if pack_opts is not None:
        widget.pack(**_to_dict(pack_opts))
    if grid_opts is not None:
        widget.grid(**_to_dict(grid_opts))
    if place_opts is not None:
        widget.place(**_to_dict(place_opts)

    return widget
