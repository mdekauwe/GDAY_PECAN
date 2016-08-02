#!/usr/bin/Rscript

# R interface script to talk to my python script to turn a netcdf file into
# an appropriate GDAY forcing file
#
# Martin De Kauwe, 3rd August 2015
wd <- getwd()
setwd(wd)

site = "US-NR1"
fpath = "met_data"
outfile_tag = "gday_met"
sub_daily = "False"

command = "python"
path2script = "generate_forcing_data.py"
args = c(site, fpath, outfile_tag, sub_daily)

# Add path to script as first arg
all_args = c(path2script, args)

all_args = paste(command, path2script, site, fpath, outfile_tag, sub_daily)
system(all_args)
