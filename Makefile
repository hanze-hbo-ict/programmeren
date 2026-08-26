# Minimal makefile for Sphinx documentation

SPHINXBUILD   = uv run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help html clean livehtml review terug

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  html            to make standalone HTML files"
	@echo "  clean           to remove build artifacts"
	@echo "  livehtml        to auto-rebuild on changes"
	@echo "  review PR=<nr>  to check out a pull request, build it and open the changed pages"
	@echo "  terug           to return to master after a review"

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(SOURCEDIR)/.jupyter_cache

livehtml:
	uv run sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html --open-browser

# Een pull request bekijken zoals hij eruitziet, niet zoals de diff hem toont.
# De notebookcache staat buiten git en overleeft een branchwissel, dus dit duurt
# een paar seconden zolang er geen notebooks zijn veranderd.
review:
	@test -n "$(PR)" || (echo "Gebruik: make review PR=<nummer>"; exit 1)
	gh pr checkout $(PR)
	@$(MAKE) --no-print-directory html
	@uv run python tools/open_changed.py

terug:
	git checkout master
