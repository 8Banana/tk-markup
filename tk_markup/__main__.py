#!/usr/bin/env python3
import argparse

import bs4

from ._create_widgets import create_widget


def create_element(root, parent=None):
    if root.name is None:
        return

    widget = create_widget(root.name, root.attrs, parent)
    children = []

    for child in getattr(root, "children", ()):
        children.append(create_element(child, widget))

    return (widget, children)


def main():
    argp = argparse.ArgumentParser()

    argp.add_argument("file", type=argparse.FileType("r"),
                      help="The XML file to parse.")

    argv = argp.parse_args()

    with argv.file:
        soup = bs4.BeautifulSoup(argv.file.read(), "xml")

    root = create_element(soup.find("Tk"))
    root[0].mainloop()


if __name__ == "__main__":
    main()
