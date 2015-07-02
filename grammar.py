#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import graken, Parser


__version__ = (2015, 7, 2, 2, 19, 18, 3)

__all__ = [
    'grammarParser',
    'grammarSemantics',
    'main'
]


class grammarParser(Parser):
    def __init__(self, whitespace=None, nameguard=None, **kwargs):
        super(grammarParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=None,
            **kwargs
        )

    @graken()
    def _letter_(self):
        self._pattern(r'[a-zA-Z]')

    @graken()
    def _digit_(self):
        self._pattern(r'[0-9]')

    @graken()
    def _number_(self):
        self._pattern(r'[0-9]+')

    @graken()
    def _sign_(self):
        with self._choice():
            with self._option():
                self._token('+')
            with self._option():
                self._token('-')
            self._error('expecting one of: + -')

    @graken()
    def _int_(self):
        with self._group():
            self._pattern(r'[i+]?[0-9]+')
        self.ast['int'] = self.last_node

        self.ast._define(
            ['int'],
            []
        )

    @graken()
    def _float_(self):
        with self._group():
            self._pattern(r'[-+]?[0-9]*\.[0-9]+')
        self.ast['float'] = self.last_node

        self.ast._define(
            ['float'],
            []
        )

    @graken()
    def _string_(self):
        with self._group():
            self._pattern(r'"[^"\r\n]*"')
        self.ast['string'] = self.last_node

        self.ast._define(
            ['string'],
            []
        )

    @graken()
    def _literal_(self):
        with self._choice():
            with self._option():
                self._string_()
            with self._option():
                self._float_()
            with self._option():
                self._int_()
            self._error('no available options')

    @graken()
    def _import_(self):
        self._token('import')
        self._space_()
        self._import_id_()
        self.ast['import_'] = self.last_node

        self.ast._define(
            ['import'],
            []
        )

    @graken()
    def _import_id_(self):
        self._pattern(r'[^ ]+')

    @graken()
    def _cmd_(self):
        self._cmd_name_()
        self.ast['cmd'] = self.last_node
        with self._optional():
            with self._optional():
                self._param_list_()
            self.ast['args'] = self.last_node

        self.ast._define(
            ['cmd', 'args'],
            []
        )

    @graken()
    def _cmd_name_(self):
        self._pattern(r'[a-zA-Z0-9_]+')

    @graken()
    def _param_list_(self):

        def block0():
            self._space_()
            self._param_()
            self.ast.setlist('@', self.last_node)
        self._closure(block0)

    @graken()
    def _param_(self):
        self._literal_()

    @graken()
    def _comment_(self):
        with self._group():
            self._token('#')
            self._pattern(r'.*')
            self.ast['comment'] = self.last_node

        self.ast._define(
            ['comment'],
            []
        )

    @graken()
    def _expr_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._import_()
                with self._option():
                    self._cmd_()
                self._error('no available options')
        self.ast['action'] = self.last_node

        self.ast._define(
            ['action'],
            []
        )

    @graken()
    def _line_(self):
        with self._choice():
            with self._option():
                with self._optional():
                    self._space_()
                self._expr_()
                self.ast.setlist('@', self.last_node)
                with self._optional():
                    self._space_()
                with self._optional():
                    self._comment_()
                    self.ast.setlist('@', self.last_node)
            with self._option():
                with self._optional():
                    self._space_()
                with self._optional():
                    self._comment_()
                    self.ast.setlist('@', self.last_node)
            self._error('no available options')

    @graken()
    def _root_(self):

        def block0():
            self._line_()
            self.ast.setlist('@', self.last_node)
            self._eol_()
        self._closure(block0)
        with self._optional():
            self._line_()
            self.ast.setlist('@', self.last_node)
        self._check_eof()

    @graken()
    def _space_(self):

        def block0():
            with self._choice():
                with self._option():
                    self._token(' ')
                with self._option():
                    self._token('\t')
                self._error('expecting one of: \t  ')
        self._positive_closure(block0)

    @graken()
    def _eol_(self):
        with self._choice():
            with self._option():
                self._token('\n')
            with self._option():
                self._token('\r\n')
            self._error('expecting one of: \n \r\n')


class grammarSemantics(object):
    def letter(self, ast):
        return ast

    def digit(self, ast):
        return ast

    def number(self, ast):
        return ast

    def sign(self, ast):
        return ast

    def int(self, ast):
        return ast

    def float(self, ast):
        return ast

    def string(self, ast):
        return ast

    def literal(self, ast):
        return ast

    def import_(self, ast):
        return ast

    def import_id(self, ast):
        return ast

    def cmd(self, ast):
        return ast

    def cmd_name(self, ast):
        return ast

    def param_list(self, ast):
        return ast

    def param(self, ast):
        return ast

    def comment(self, ast):
        return ast

    def expr(self, ast):
        return ast

    def line(self, ast):
        return ast

    def root(self, ast):
        return ast

    def space(self, ast):
        return ast

    def eol(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = grammarParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in grammarParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for grammar.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )