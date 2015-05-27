#!/usr/bin/env Rscript

library(optparse)
library(knitr)

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

opts_knit$set(base.dir=opts$outdir) # base dir where to save figures

# perform the rendering
invisible(knit(opts$input))

# move the output file to location of the original input directory
basedir <- dirname(opts$input)
files <- list.files(getwd())
index <- grep(".md", files)
invisible(file.rename(file.path(getwd(), files[index]),
         file.path(basedir, files[index])))

#knit2html(file)
