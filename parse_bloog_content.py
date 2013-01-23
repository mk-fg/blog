# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import itertools as it, operator as op, functools as ft
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile
from datetime import datetime
import os, sys, re, ast, iso8601, pyaml


def slugify(slug):
	for src, dst in [
			(br'[\\/]', '_'), (br'^\.+', '_'), (br'[\x00-\x1f]', '_'),
			(br':', '-_'), (br'<', '('), (br'>', ')'), (br'"', "'"), (br'\*', '+'),
			(br'[|!]', '-'), (br'[\?\*.]', '_'), (br'\.+$', '_'), (br'\s+$', ''), (br'\s', '_') ]:
		n = True
		if re.search(src, dst): raise ValueError # sanity check
		while n: slug, n = re.subn(src, dst, slug)
	return slug.strip('_+-')


def main(argv=None):
	import argparse
	parser = argparse.ArgumentParser(
		description='Decode appengine data dump for blog entries.')
	parser.add_argument('dump', help='Path appengine data dump.')
	optz = parser.parse_args(argv if argv is not None else sys.argv[1:])

	src = open(optz.dump).read().decode('utf-8')
	for article in it.ifilter(None, it.imap(op.methodcaller('strip'), src.split('-=||||||||||=-'))):
		permalink, published, title, tags, html, plain = article.split('-=|||=-')
		published = iso8601.parse_date(published)
		tags = ast.literal_eval(tags) if tags else list()
		with NamedTemporaryFile() as src:
			src.write(html.encode('utf-8'))
			src.flush()
			proc = Popen(['pandoc', '-f', 'html', '-t', 'rst', src.name], stdout=PIPE)
			md = proc.stdout.read()
			if proc.wait(): raise RuntimeError('pandoc failed')
		# ---
		# id: ambient-auth-visual-identity
		# tags: #design, TODO
		# title: Ambient Auth Visual Identity
		# ---
		path = '{}.{}.md'.format(published.strftime('%Y-%m-%d'), slugify(title))
		# open(path, 'w').write(
		# 	'---\n{}---\n'.format(pyaml.dumps(dict(created=




if __name__ == '__main__': main()
