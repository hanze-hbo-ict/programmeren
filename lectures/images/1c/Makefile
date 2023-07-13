DOT=dot

DOTS=$(wildcard *.dot)
PNGS=$(DOTS:.dot=.png)
SVGS=$(DOTS:.dot=.svg)
OPTS := -Gdpi=100 -Nfontname=Helvetica -Efontname=Helvetica

diagrams: $(PNGS) $(SVGS)

%.png: %.dot
	$(DOT) "-Tpng" $(OPTS) "$<" -o "$@"

%.svg: %.dot
	$(DOT) "-Tsvg" $(OPTS) "$<" -o "$@"

clean:
	rm $(PNGS) $(SVGS)