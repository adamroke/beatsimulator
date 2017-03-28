#! /usr/bin/env python

import sys, os, glob, subprocess, urllib
import distutils, distutils.command.clean, distutils.dir_util
from .gen_external import generate_external, header, output_path

if __name__ == "__main__":
    if len(sys.argv) >= 2:

        with open("808_config.txt") as f:
        config = f.readlines()
        config = [x.strip("\n") for x in content]

        python ./python/demos/demo_notes.py sys.argv[1] 44100 >> tempconf1.txt

        with open("kick_config.txt") as f:
        config = f.readlines()
        config = [x.strip("\n") for x in content]

        python ./python/demos/demo_notes.py sys.argv[1] 44100 >> tempconf2.txt

        with open("hs_config.txt") as f:
        config = f.readlines()
        config = [x.strip("\n") for x in content]

        python ./python/demos/demo_notes.py sys.argv[1] 44100 >> tempconf3.txt

        with open("ot_config.txt") as f:
        config = f.readlines()
        config = [x.strip("\n") for x in content]

        python ./python/demos/demo_notes.py sys.argv[1] 44100 >> tempconf4.txt
