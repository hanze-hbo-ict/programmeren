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
# een paar seconden zolang er geen notebooks zijn veranderd. De pagina's worden
# over HTTP geserveerd en niet als bestand geopend, want Mermaid laadt als
# ES-module vanaf een CDN en dat weigert een browser op een file://-pagina.
review:
	@test -n "$(PR)" || (echo "Gebruik: make review PR=<nummer>"; exit 1)
	gh pr checkout $(PR)
	@$(MAKE) --no-print-directory html
	@# Uit master lezen: na de checkout staat het script niet meer in de werkboom
	@# als de branch ouder is dan het script zelf.
	@git show master:tools/open_changed.py | uv run python -

terug:
	git checkout master
