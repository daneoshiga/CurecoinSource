SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: requirements

objects = $(wildcard requirements/*.in)
outputs := $(objects:.in=.txt)

# Linting and Formatting ######################################################

lint:
	pre-commit run -a -v

# Dependency Management #######################################################

requirements: $(outputs)

%.txt: %.in
	pip-compile -v --output-file $@ $<

# SAM
sam_build:
	sam build --use-container --docker-network host --debug
