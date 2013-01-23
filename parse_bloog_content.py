#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import itertools as it, operator as op, functools as ft
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile
from datetime import datetime
import os, sys, re, ast, iso8601, pyaml

from lxml.html import (
	fromstring as lxml_fromstring,
	tostring as lxml_tostring )
from lxml.html.soupparser import fromstring as lxml_soup
from lxml.etree import (
	XMLSyntaxError as lxml_SyntaxError,
	ParserError as lxml_ParserError )


def slugify(slug):
	for src, dst in [
			(br'[\\/]', '_'), (br'^\.+', '_'), (br'[\x00-\x1f]', '_'),
			(br':', '-_'), (br'<', '('), (br'>', ')'), (br'"', "'"), (br'\*', '+'),
			(br'[|!]', '-'), (br'[\?\*.]', '_'), (br'\.+$', '_'), (br'\s+$', ''), (br'\s', '_') ]:
		n = True
		if re.search(src, dst): raise ValueError # sanity check
		while n: slug, n = re.subn(src, dst, slug)
	return slug.strip('_+-')


def process_html(html):
	rc, doc = 0, lxml_soup(html)
	for e in doc.xpath('//pre'):
		if not e.text: continue
		for br in e.iterfind('br'):
			assert br.getparent() is e
			if br.tail: e.text += '\n' + br.tail
			e.remove(br)
			rc += 1
	return lxml_tostring(doc)


def main(argv=None):
	import argparse
	parser = argparse.ArgumentParser(
		description='Decode appengine data dump for blog entries.')
	parser.add_argument('dump', help='Path appengine data dump.')
	parser.add_argument('dst_dir', help='Path to generate files in.')
	optz = parser.parse_args(argv if argv is not None else sys.argv[1:])

	src = open(optz.dump).read().decode('utf-8')
	for article in it.ifilter(None, it.imap(op.methodcaller('strip'), src.split('-=||||||||||=-'))):
		permalink, published, title, tags, html, plain = article.split('-=|||=-')
		published = iso8601.parse_date(published)
		tags = map(op.methodcaller('lower'), ast.literal_eval(tags) if tags else list())
		with NamedTemporaryFile() as src:
			src.write(process_html(html).encode('utf-8'))
			src.flush()
			proc = Popen(['pandoc', '-f', 'html', '-t', 'rst', src.name], stdout=PIPE)
			body = proc.stdout.read().decode('utf-8')
			if proc.wait(): raise RuntimeError('pandoc failed')
		slug = slugify(title)
		path = '{}.{}.rst'.format(published.strftime('%Y-%m-%d'), slug)
		with open(os.path.join(optz.dst_dir, path), 'w') as dst:
			dst.write('\n'.join(filter(None, [
				'{}\n{}\n'.format(title, '#'*len(title)),
				':date: {}'.format(published.strftime('%Y-%m-%d %H:%M')),
				tags and ':tags: {}'.format(', '.join(tags)),
				'\n', body ])).encode('utf-8'))


if __name__ == '__main__': main()
