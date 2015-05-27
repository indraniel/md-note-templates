#!/usr/bin/env Rscript

library(optparse)

opts.list <- list(
    make_option(c("-o", "--outdir"), action="store", 
                type="character", default="final",
                help="The output directory to place the figures [default: 'final']"),

    make_option(c("-i", "--input"), action="store", 
                type="character", default=NA,
                help="The input markdown file to process")
)

opts <- parse_args(OptionParser(option_list=opts.list))

cat(paste("Input File: ", opts$input, "\n"))
cat(paste("Output Figure Directory: ", opts$outdir, "\n"))

library(knitr)
opts_knit$set(base.dir = opts$outdir) # base dir where to save figures

knit(opts$input)
#knit2html(file)
