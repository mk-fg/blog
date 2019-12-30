PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

DEBUG=0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif


help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate htmls in output dir   '
	@echo '   make clean                       remove generated files             '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make sync                        push data up to the mothership     '
	@echo '                                                                       '


html: | clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver:
	@cgrc -ru pelican apps-misc -- $(PELICAN) -ql --autoreload -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) &>/dev/null &
	@sleep 1 && { cgrc -rcu pelican || echo 'Pelican server is running in the background.'; }

stopserver:
	@cgrc -lru pelican | xargs kill
	@echo 'Stopped Pelican server.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

sync: publish
	$(BASEDIR)/sync.sh

appengine: sync

.PHONY: html help clean regenerate serve devserver stopserver publish appengine sync
