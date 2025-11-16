# The python script in this file makes the various parts of a model astrolabe.
#
# Copyright (C) 2010-2024 Dominic Ford <https://dcford.org.uk/>
#
# This code is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# this file; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

# ----------------------------------------------------------------------------

"""
This is the top level script for drawing all the parts needed to build astrolabes which work at a range of
different latitudes. They are rendered in PDF, SVG and PNG image formats.

Additionally, we use LaTeX to build a summary document for each latitude, which includes all of the parts needed
to build an astrolabe for that latitude, and instructions as to how to put them together.
"""

import argparse
import os
import pathlib
import subprocess
import time
from typing import Dict, Union

from . import latex_template, text
from .climate import Climate
from .graphics_context import CompositeComponent, GraphicsPage
from .mother_back import MotherBack
from .mother_front import MotherFront
from .rete import Rete
from .rule import Rule
from .settings import fetch_command_line_arguments


def make(args):
    output_dir: pathlib.Path = args.output_dir
    dir_parts: pathlib.Path = output_dir / "astrolabe_parts"
    dir_out: pathlib.Path = output_dir / "astrolabes"

    for d in [dir_parts, dir_out]:
        d.mkdir(parents=True, exist_ok=True)

    language: str
    for language in args.languages:
        astrolabe_type: str
        for astrolabe_type in args.astrolabe_types:
            latitude: float
            for latitude in args.latitudes:
                img_format: str
                for img_format in args.img_formats:
                    # Boolean flag for which hemisphere we're in
                    southern: bool = latitude < 0

                    # A dictionary of common substitutions
                    subs: Dict[str, Union[str, float]] = {
                        "dir_parts": dir_parts,
                        "dir_out": dir_out,
                        "abs_lat": abs(latitude),
                        "ns": "S" if southern else "N",
                        "astrolabe_type": astrolabe_type,
                        "lang": language,
                        "lang_short": (
                            "" if language == "en" else "_{}".format(language)
                        ),
                    }

                    settings: Dict[str, Union[str, float]] = {
                        "language": language,
                        "astrolabe_type": astrolabe_type,
                        "latitude": latitude,
                        "theme": args.theme,
                    }

                    # Render the parts of the astrolabe that do not change with geographic location
                    mother_front_filename: pathlib.Path = (
                        dir_parts
                        / "mother_front_{abs_lat:02d}{ns}_{lang}_{astrolabe_type}".format(
                            **subs
                        )
                    )
                    MotherFront(settings=settings).render_to_file(
                        filename=mother_front_filename,
                        img_format=img_format,
                    )

                    mother_back_filename: pathlib.Path = (
                        dir_parts
                        / "mother_back_{abs_lat:02d}{ns}_{lang}_{astrolabe_type}".format(
                            **subs
                        )
                    )
                    MotherBack(settings=settings).render_to_file(
                        filename=mother_back_filename, img_format=img_format
                    )

                    rete_filename: pathlib.Path = (
                        dir_parts
                        / "rete_{abs_lat:02d}{ns}_{lang}_{astrolabe_type}".format(
                            **subs
                        )
                    )
                    Rete(settings=settings).render_to_file(
                        filename=rete_filename,
                        img_format=img_format,
                    )

                    rule_filename: pathlib.Path = (
                        dir_parts
                        / "rule_{abs_lat:02d}{ns}_{lang}_{astrolabe_type}".format(
                            **subs
                        )
                    )
                    Rule(settings=settings).render_to_file(
                        rule_filename,
                        img_format=img_format,
                    )

                    # Render the climate of the astrolabe
                    Climate(settings=settings).render_to_file(
                        filename="{dir_parts}/climate_{abs_lat:02d}{ns}_{lang}_{astrolabe_type}".format(
                            **subs
                        ),
                        img_format=img_format,
                    )

                    # Make combined mother and climate
                    mother_front_combi_filename: pathlib.Path = (
                        dir_parts
                        / "mother_front_combi_{abs_lat:02d}{ns}_{lang}_{astrolabe_type}".format(
                            **subs
                        )
                    )
                    CompositeComponent(
                        settings=settings,
                        components=[
                            MotherFront(settings=settings),
                            Climate(settings=settings),
                        ],
                    ).render_to_file(
                        filename=mother_front_combi_filename,
                        img_format=img_format,
                    )

                    doc = latex_template.template.format(
                        latitude=r"${abs_lat:d}^\circ${ns}".format(**subs),
                        mother_back=mother_back_filename.absolute(),
                        mother_front=mother_front_combi_filename.absolute(),
                        rule=rule_filename.absolute(),
                        rete=rete_filename.absolute(),
                    )
                    with open(
                        "{dir_out}/astrolabe_{abs_lat:02d}{ns}_{lang}_{astrolabe_type}.tex".format(
                            **subs
                        ),
                        "w",
                    ) as f:
                        f.write(doc)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--latitudes",
        dest="latitudes",
        type=int,
        default=[52],
        nargs="*",
        help="The latitude to create a astrolabe for.",
    )
    parser.add_argument(
        "--types",
        dest="astrolabe_types",
        choices=["full", "simplified"],
        default=["full"],
        nargs="*",
        help="The astrolabe type to create.",
    )
    parser.add_argument(
        "--languages",
        dest="languages",
        choices=text.text.keys(),
        default=["en"],
        nargs="*",
        help="The language to create a astrolabe for.",
    )
    parser.add_argument(
        "--formats",
        dest="img_formats",
        choices=GraphicsPage.supported_formats(),
        default=["png"],
        nargs="*",
        help="The image format to create.",
    )
    parser.add_argument(
        "--output-dir",
        dest="output_dir",
        default="output",
        type=pathlib.Path,
        help="Dirname for output.",
    )
    parser.add_argument(
        "--theme",
        dest="theme",
        choices=["default", "dark"],
        default="default",
        help="Color theme to be used in the astrolabe.",
    )
    args = parser.parse_args()

    return make(args)


if __name__ == "__main__":
    import sys

    sys.exit(main() == False)
