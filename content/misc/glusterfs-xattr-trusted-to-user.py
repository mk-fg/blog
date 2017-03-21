#!/usr/bin/env python3

import itertools as it, operator as op, functools as ft
import os, sys, pathlib, logging


def patch_xattrs(path, dry_run=False):
	def patch_node(p):
		# getxattr/setxattr work weirdly for broken symlinks
		# glusterd produces these sometimes, seem to be expendable
		try: bugged = p.is_symlink() and not p.exists()
		except OSError: bugged = True
		if bugged:
			if not dry_run: p.unlink()
			return
		for k in os.listxattr(p, follow_symlinks=False):
			if not k.startswith('trusted.'): continue
			k_user = 'user.{}'.format(k[8:])
			v = os.getxattr(p, k, follow_symlinks=False)
			log.debug(f'patch: {p} :: {k} -> {k_user} [{v!r}]')
			if not dry_run: os.setxattr(p, k_user, v, follow_symlinks=False)
	for top, dirs, files in os.walk(path):
		p = pathlib.Path(top)
		patch_node(p)
		for fn in files: patch_node(p / fn)


def main(args=None):
	import argparse
	parser = argparse.ArgumentParser(
		description='Tool to copy trusted.* xattrs to user.* ones.')
	parser.add_argument('path', nargs='+',
		help='Path(s) to operate on recursively.')
	parser.add_argument('-n', '--dry-run', action='store_true',
		help='Do not change anything on fs, only navigate over it and run all the checks.')
	parser.add_argument('-d', '--debug', action='store_true', help='Verbose operation mode.')
	opts = parser.parse_args(sys.argv[1:] if args is None else args)

	global log
	logging.basicConfig(level=logging.DEBUG if opts.debug else logging.WARNING)
	log = logging.getLogger('main')

	paths = list(pathlib.Path(p).resolve() for p in opts.path)
	for p in paths: patch_xattrs(p, dry_run=opts.dry_run)

if __name__ == '__main__': sys.exit(main())
