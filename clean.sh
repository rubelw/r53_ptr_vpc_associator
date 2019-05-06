#!/bin/bash

cd $(dirname ${0})

if [ -d r53_ptr_vpc_associator.egg-info ]; then rm -rf r53_ptr_vpc_associator.egg-info; fi
find . -name .ropeproject -type d | xargs rm -rf
find . -name "*.pyc" -type f | xargs rm -f
if [ -d build ]; then rm -rf build; fi
if [ -d dist ]; then rm -rf dist; fi
if [ -d .pytest_cache ]; then rm -rf .pytest_cache; fi
if [ -d .tox ]; then rm -rf .tox; fi
if [ -d .eggs ]; then rm -rf .eggs; fi
if [ -d test/pytestdebug.log ]; then rm test/pytestdebug.log; fi
if [ -d docs/_build ]; then rm -rf docs/_build; fi