#!/usr/bin/env Rscript

install.packages('devtools', repos="http://cran.wustl.edu")

library(devtools)

install_github("yihui/knitr", ref="master")
install_github("alexcb/rjson/rjson", ref="master")
install_github("hadley/ggplot2", ref="master")
install_github("trevorld/optparse", ref="master")
