LATEXMK ?= latexmk
PDFLATEX ?= pdflatex
LATEXMKFLAGS ?= -pdf -interaction=nonstopmode -halt-on-error

SECTION_TEX := $(wildcard sections/*.tex)
TABLE_TEX := $(wildcard tables/*.tex)
HELPER_TEX := $(wildcard helpers/*.tex)
STANDALONE_FIGURE_TEX := $(shell for f in figures/*.tex; do head -n 1 "$$f" | grep -qF '\documentclass' && printf '%s\n' "$$f"; done)
STANDALONE_FIGURE_PDFS := $(STANDALONE_FIGURE_TEX:.tex=.pdf)
STATIC_FIGURES := $(filter-out $(STANDALONE_FIGURE_PDFS),$(wildcard figures/*.pdf figures/*.png))

.PHONY: all paper abstract figures clean clean-figures distclean

all: figures paper abstract

paper: main.pdf

main.pdf: main.tex references.bib acmart.cls ACM-Reference-Format.bst \
	$(SECTION_TEX) $(TABLE_TEX) $(HELPER_TEX) \
	$(STANDALONE_FIGURE_PDFS) $(STATIC_FIGURES)
	$(LATEXMK) $(LATEXMKFLAGS) main.tex

abstract: extended-abstract.pdf

extended-abstract.pdf: extended-abstract.tex references.bib acmart.cls ACM-Reference-Format.bst
	$(LATEXMK) $(LATEXMKFLAGS) extended-abstract.tex

figures: $(STANDALONE_FIGURE_PDFS)

$(STANDALONE_FIGURE_PDFS): figures/%.pdf: figures/%.tex
	cd figures && $(LATEXMK) $(LATEXMKFLAGS) $(notdir $<)

clean: clean-figures
	$(LATEXMK) -c main.tex
	$(LATEXMK) -c extended-abstract.tex

clean-figures:
	@set -- $(STANDALONE_FIGURE_TEX); \
	for f do \
		(cd figures && $(LATEXMK) -c "$${f#figures/}"); \
	done

distclean: clean
	rm -f main.pdf extended-abstract.pdf $(STANDALONE_FIGURE_PDFS)
