#!/usr/bin/env Rscript

library(tools)
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
origFile <- basename(opts$input)
rootName <- file_path_sans_ext(origFile)
mdFile <- paste(rootName, '.md', sep="")

files <- list.files(getwd())
index <- grep(mdFile, files)
invisible(
    file.rename(
         from=file.path(getwd(), files[index]),
         to=file.path(basedir, files[index])
    )
)

#knit2html(file)
