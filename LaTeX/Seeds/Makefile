#
# General Voraussetzung: ex. im Ordner.
#

# Windows-freundliche Übersetzung in MSys2/Cydwin
ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: Abgabe.pdf

Abgabe.pdf: build/main.pdf|build
	@cp build/main.pdf Abgabe.pdf
	@echo Success

pc/plot.pdf: pc/plot.py rawdata/* matplotlibrc header-matplotlib.tex|pc
	@echo 'Python-Plots:'
	TEXINPUTS="$(call translate,$(pwd):)" python pc/plot.py
	@echo

pc/plot.py: rawdata/*
	@echo "Plots-Ordner fehlt!"
	@echo "=> Kopiere aus CAT-Vorlage"
	@mkdir -p pc
	@cp ../LaTeX/pc/* pc/
	@echo

rawdata/*:
	@echo 'Es fehlen die Rohdaten! Als Initialisierung bitte Rohdaten abspeichern und make erneut starten.'
	@mkdir -p rawdata
	@false

lit.bib programme.bib:
	@echo 'Es fehlen die Bibliothek-Daten!'
	@echo '=> Kopiere aus PeP-et-al-Vorlage'
	@cp ../LaTeX/latex-template/lit.bib lit.bib
	@cp ../LaTeX/latex-template/programme.bib programme.bib
	@echo

matplotlibrc header-matplotlib.tex:
	@echo "Konfigurationsdateien fehlen!"
	@echo "=> Kopiere aus PeP-et-al-Vorlage"
	@cp ../LaTeX/latex-template/header-matplotlib.tex ./header-matplotlib.tex
	@cp ../LaTeX/latex-template/matplotlibrc ./matplotlibrc
	@echo

header.tex:
	@echo "Die Header-Datei fehlt!"
	@echo "=> Kopiere aus CAT-Vorlage"
	@cp ../LaTeX/header.tex header.tex
	@echo

main.tex: 
	@echo "Main.tex fehlt!""
	@false

content/*:
	@echo "Content-Vorlagen fehlen!"
	@echo "=> Kopiere aus CAT-Vorlage"
	@mkdir -p content
	@cp ../LaTeX/content/* content/
	@echo

graphics:
	@mkdir -p graphics

tables:
	@mkdir -p tables

.DELETE_ON_ERROR:
build/main.pdf: pc/plot.pdf graphics/* tables/* header.tex main.tex content/* lit.bib programme.bib|build 
	@echo 'LaTeX:'
	@TEXINPUTS="$(call translate,build:)" lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex|grep -i -A1 -e'!' -e'error'  -e'main.pdf' 
	@echo
	@BIBINPUTS=build: biber build/main.bcf|grep -i -e'biber' -e'err' -e'error' -e'warn'
	@echo
	@lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex>/dev/null
	@lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex|grep -i -e'!'-e'error' -e'warning' -e'biber' -e'rerunfilecheck'

build:
	@mkdir -p build
	@echo 'Erstelle build-Ordner'
	@echo

clean:
	@rm -rf build
	@echo 'Entferne build-Ordner, Abgabe.pdf unberührt.'

purge:
	@ls | grep -v -e"main.tex" -e"Makefile" | xargs rm -rf
	@rm -rf build
	@echo 'Alles weg.'
