#!/usr/bin/env python3
import argparse
import pprint

import bs4


def create_element(root, parent=None):
    if root.name is None:
        return

    yield (root.name, parent)

    for child in getattr(root, "children", ()):
        yield from create_element(child, root)


def main():
    argp = argparse.ArgumentParser()

    argp.add_argument("filename",
                      help="The XML file to parse.")

    argv = argp.parse_args()

    with open(argv.filename) as xml_file:
        soup = bs4.BeautifulSoup(xml_file.read(), "xml")

    root = create_element(soup.find("Tk"))

    pprint.pprint(list(root))


if __name__ == "__main__":
    main()
