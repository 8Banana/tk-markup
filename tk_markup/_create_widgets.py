import tkinter as tk


def _pairs(sequence):
    if len(sequence) % 2 != 0:
        raise ValueError("odd number of elements in " + repr(sequence))
    return zip(sequence[0::2], sequence[1::2])


def _to_dict(any_widget, string):
    if not isinstance(any_widget, tk.Tk):
        any_widget = any_widget.tk

    return {k.lstrip("-"): v for k, v in _pairs(any_widget.splitlist(string))}


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
        # TODO: Are there situations in which you don't want to show a widget?
        if widget_type != "Tk":
            raise RuntimeError(repr(widget) + " is not being displayed!")

    widget.config(**attributes)

    return widget
