PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py


help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   make appengine                   push data up to the mothership     '
	@echo '                                                                       '


html: | clean $(OUTPUTDIR)/index.html update_legacy_links
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

update_legacy_links:
	awk\
		'match($$0,/^\s*<!-- legacy-link: (.*) -->\s*$$/,a) {sub(/^output\//, "", FILENAME); print a[1], FILENAME}'\
		output/*/*/*/*.html | sort -u | ./dynamic/legacy_redirect.py

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

devserver:
	$(BASEDIR)/develop_server.sh restart >/dev/null 2>&1

publish_build:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

publish: | publish_build update_legacy_links

appengine: publish
	cd ~/hatch/gapp && ./appcfg.py update pelican-blog

.PHONY: html update_legacy_links help clean regenerate serve devserver publish publish_build appengine
