#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly=TRUE)
file <- args[1]
cat(paste("Processing: ", file, "\n"))

library(knitr)
opts_knit$set(base.dir = 'final') # base dir where to save figures

knit(file)
#knit2html(file)
