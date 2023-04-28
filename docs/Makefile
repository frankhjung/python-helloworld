# Minimal makefile for Sphinx documentation

SPHINXBUILD	= sphinx-build
SPHINXOPTS	= -v
SOURCEDIR	= $(PWD)
OUTPUTDIR	= $(PWD)/../target/docs

.PHONY: html
%: html
	@$(SPHINXBUILD) $(SPHINXOPTS) "$(SOURCEDIR)" "$(OUTPUTDIR)"