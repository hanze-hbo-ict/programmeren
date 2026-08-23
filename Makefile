# Minimal makefile for Sphinx documentation

SPHINXBUILD   = uv run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help html clean livehtml

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  clean      to remove build artifacts"
	@echo "  livehtml   to auto-rebuild on changes"

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(SOURCEDIR)/.jupyter_cache

livehtml:
	uv run sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html --open-browser
