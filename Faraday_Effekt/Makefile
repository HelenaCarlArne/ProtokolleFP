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

plots: pc/plot.py matplotlibrc header-matplotlib.tex|data
	@echo 'Python-Plots:'
	TEXINPUTS="$(call translate,$(pwd):)" python pc/plot.py
	@echo

again:
	@make clean
	@make all

clean:
	@rm -rf build
	@echo 'Entferne build-Ordner'

#purge:
#	@ls | grep -v -e"Makefile" | xargs rm -rf
#	@rm -rf build
#	@clear

build:
	@mkdir -p build

data:
	@mkdir -p data
		

pc/plot.pdf: pc/plot.py data matplotlibrc header-matplotlib.tex
	@echo 'Python-Plots:'
	TEXINPUTS="$(call translate,$(pwd):)" python pc/plot.py
	@echo

pc/plot.py:
	@echo "Plots-Ordner fehlt!"
	@echo "=> Kopiere aus CAT-Vorlage"
	@mkdir -p pc
	@cp ../LaTeX/pc/* pc/
	@echo


lit.bib:
	@echo 'Es fehlen die Bibliothek-Daten!'
	@echo '=> Kopiere aus PeP-et-al-Vorlage'
	@cp -n ../LaTeX/latex-template/lit.bib lit.bib
	@echo

programme.bib:
	@echo 'Es fehlen die Bibliothek-Daten!'
	@echo '=> Kopiere aus PeP-et-al-Vorlage'
	@cp -n ../LaTeX/latex-template/programme.bib programme.bib
	@echo

matplotlibrc header-matplotlib.tex:
	@echo "Konfigurationsdateien fehlen!"
	@echo "=> Kopiere aus PeP-et-al- und CAT-Vorlage"
	@cp -n ../LaTeX/header-matplotlib.tex ./header-matplotlib.tex
	@cp -n ../LaTeX/latex-template/matplotlibrc ./matplotlibrc
	@echo

header.tex:
	@echo "Die Header-Datei fehlt!"
	@echo "=> Kopiere aus CAT-Vorlage"
	@cp -n ../LaTeX/header.tex header.tex
	@echo

main.tex: 
	@echo
	@echo 'Es fehlt die main.tex!'
	@echo '=> Kopiere aus PeP-et-al-Vorlage'
	@cp -n ../LaTeX/latex-template/main.tex main.tex
	@echo

content/*:
	@echo "Content-Vorlagen fehlen!"
	@echo "=> Kopiere aus CAT-Vorlage"
	@mkdir -p content
	@cp -n ../LaTeX/content/* content/
	@echo
	
graphics:
	@mkdir -p graphics

tables:
	@mkdir -p tables


.DELETE_ON_ERROR:
Abgabe.pdf: main.tex content/* header.tex  lit.bib programme.bib pc/plot.pdf graphics tables|build
	@TEXINPUTS="$(call translate,build:)" lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex|grep -B 12 -e'no output PDF file produced' -e'LuaTeX' --color=auto
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
	@mv build/main.pdf Abgabe.pdf
	@make clean
	@echo Success
