# -*- coding: utf-8 -*-
"""Module ga4gh.drs.entrypoint.py
Main entrypoint into the drs client program, all sub-groups and and sub-commands
are added to the main entrypoint here 
"""

import click
from ga4gh.drs.cli.parsing.get import get
from ga4gh.drs.cli.parsing.schemes import schemes

@click.group()
def main():
    """Placeholder main method, subgroups/subcommands added to main via click"""

    pass

main.add_command(get)
main.add_command(schemes)
