#!/bin/sh

jupyter nbconvert $1 --to slides --post serve --ServePostProcessor.port=8080
