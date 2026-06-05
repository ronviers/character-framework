20 June 2025, 25 April 2026
by Ido Filin

Data from Noshita et al. (2012) was obtained by scanning the
pages of their supplemental table into a text file with some
manual bugfixes. 

Data from Araki & Noshita (2023) was obtained by transforming
their supplementary pdf to a text file using the Linux tool
pdftotext, and doing some manual cleanup.

.txt files are then transformed to .csv format using awk scripts
and combined with an R-script to a single merged .csv
file: 
noshita-etal-merged.csv

Data from Newkirk & Doyle (1975) was copied from their Table 1,
and processed with an R-script to produce a .csv file:
newkrk-doyle-data.csv


References:

Araki A, Noshita K (2023).
Theoretical morphological analysis of differential morphospace
 occupation patterns for terrestrial and aquatic gastropods.
Evolution 77: 1864–1873.

Noshita K, Asami T, Ubukata T (2012).
Functional constraints on coiling geometry and aperture inclination in gastropods.
Paleobiology 38: 322–334.

Newkirk GF, Doyle RW (1975). Genetic analysis of shell-shape variation in Littorina saxatilis
on an environmental cline. Mar Biol 30: 227–237.

Filin I (2026). Lead and slant on the geometry of coiling in gastropods.
