csvfilename.2012 <- "noshitaetal2012.csv"
csvfilename.2023 <- "arakinoshita2023.csv"

# The following two system command calls should work on a Linux
# machine, but may be commented out, and the awk processing done
# manually, depending on operating system.
system(paste("awk -f noshitaetal2012.awk noshita-etal-2012-table-s1.txt > ", csvfilename.2012))
system(paste("awk -f arakinoshita2023.awk araki-noshita-2023-suppl.txt > ", csvfilename.2023))

# Read the generated per-study csv files
noshita.df <- read.csv(csvfilename.2012,header=T);
araki.df <- read.csv(csvfilename.2023,header=T);

# Merge the two datasets
araki.df$repo <- "NHMIC"
indices <- c("genus","species","family","habitat","repo","W","Traup","D","Delta","Gamma");
noshita.etal.df <- data.frame(rbind(noshita.df[,indices],araki.df[,indices]));

# Some more processing to merged dataset
noshita.etal.df$W <- as.numeric(noshita.etal.df$W); 
noshita.etal.df$Traup <- as.numeric(noshita.etal.df$Traup); 
noshita.etal.df$D <- as.numeric(noshita.etal.df$D); 
noshita.etal.df$Delta <- as.numeric(noshita.etal.df$Delta); 
noshita.etal.df$Gamma <- as.numeric(noshita.etal.df$Gamma); 

noshita.etal.df$expansion <- with(noshita.etal.df, log(W)/2/pi)
noshita.etal.df$T.centerline <- with(noshita.etal.df, 2*Traup)
noshita.etal.df$tan.lead <- with(noshita.etal.df, expansion/sqrt(1+expansion^2)*T.centerline)
noshita.etal.df$tan.beta <- with(noshita.etal.df, 1.0/T.centerline)
noshita.etal.df$sin.beta <- sin(atan(noshita.etal.df$tan.beta));
noshita.etal.df$cot.spiral <- with(noshita.etal.df, expansion/sin.beta)

write.csv(noshita.etal.df,"noshita-etal-merged.csv", row.names=FALSE);
