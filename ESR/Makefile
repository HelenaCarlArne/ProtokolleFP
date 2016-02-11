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

plots: pc/plot.py matplotlibrc header-matplotlib.tex|pc
	@echo 'Python-Plots:'
	TEXINPUTS="$(call translate,$(pwd):)" python pc/plot.py
	@echo

Abgabe.pdf: build/main.pdf|build
	@cp build/main.pdf Abgabe.pdf
	@echo Success

pc/plot.pdf: pc/plot.py matplotlibrc header-matplotlib.tex|pc
	@echo 'Python-Plots:'
	TEXINPUTS="$(call translate,$(pwd):)" python pc/plot.py
	@echo

pc/plot.py:
	@echo "Plots-Ordner fehlt!"
	@echo "=> Kopiere aus Vorlage"
	@false

rawdata/*:
	@echo 'Bitte Rohdaten abspeichern und make erneut starten.'
	@mkdir -p rawdata
	@false

lit.bib programme.bib:
	@echo 'Es fehlen die Bibliothek-Daten!'
	@echo '=> Kopiere aus PeP-et-al-Vorlage, falls Projekt neu.'
	@false

matplotlibrc header-matplotlib.tex:
	@echo "Konfigurationsdateien fehlen!"
	@echo "=> Kopiere aus PeP-et-al-Vorlage"
	@false

header.tex:
	@echo "Die Header-Datei fehlt!"
	@echo "=> Kopiere aus Vorlage"
	@false

main.tex:
	@echo "Main.tex fehlt!"
	@false

content/*:
	@echo "Content-Vorlagen fehlen!"
	@echo "=> Kopiere aus Vorlage, falls Projekt neu."
	@false

graphics:
	@mkdir -p graphics

tables:
	@mkdir -p tables

.DELETE_ON_ERROR:
build/main.pdf: pc/plot.pdf graphics tables header.tex main.tex content/* lit.bib programme.bib|build
	@TEXINPUTS="$(call translate,build:)" lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex|grep -B 10 -e'no output PDF file produced' -e'LuaTeX' --color=auto
	@echo
	@BIBINPUTS=build: biber build/main.bcf|grep -i -e'biber' -e'error' -e'warn' --color=auto
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
	main.tex|grep  -e'reference' -e'LuaTeX' --color=auto

build:
	@mkdir -p build
	@echo 'Erstelle build-Ordner'
	@echo

again:
	@make clean
	@make all

clean:
	@rm -rf build
	@echo 'Entferne build-Ordner, Abgabe.pdf unberührt.'
