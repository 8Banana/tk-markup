import tkinter as tk


def _pairs(sequence):
    if len(sequence) % 2 != 0:
        raise ValueError("odd number of elements in " + repr(sequence))
    return zip(sequence[0::2], sequence[1::2])


def _to_dict(any_widget, string):
    return {k.lstrip("-"): v
            for k, v in _pairs(any_widget.tk.splitlist(string))}


def create_widget(widget_type, attributes, parent_widget=None):
    cls = getattr(tk, widget_type)

    widget = cls(parent_widget)

    for showing_option in ("pack", "grid", "place"):
        if showing_option in attributes:
            method = getattr(widget, showing_option)
            kwargs = _to_dict(widget, attributes.pop(showing_option))
            method(**kwargs)
            break
    else:
        # TODO: Add an option for creating widgets without showing them.
        #       This is not needed most of the time, but some things
        #       like Porcupine's tab manager do it.
        # TODO: Don't break if someone creates a custom class called
        #       Toplevel or a MyToplevel class that inherits from
        #       Toplevel.
        if widget_type not in {"Tk", "Toplevel"}:
            raise RuntimeError(repr(widget) + " isn't packed, gridded "
                               "or placed")

    widget.config(**attributes)

    return widget
