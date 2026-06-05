popnum <- 1:5; 
is.embryo <- rep(TRUE,5); 

adults.T <- c(1.08, 1.27, 1.50, 1.45, 1.49);
adults.W <- c(2.45, 2.07, 1.83, 1.89, 1.94);
adults.S <- c(0.79, 0.78, 0.75, 0.71, 0.72);

embryos.T <- c(0.76, 0.75, 0.84, 0.80, 0.90);
embryos.W <- c(2.76, 2.71, 2.64, 2.55, 2.42); 
embryos.S <- c(0.74, 0.74, 0.73, 0.71, 0.70); 

embryos.expansion <- log(embryos.W)/2/pi 
adults.expansion <- log(adults.W)/2/pi
embryos.tan.lead <- embryos.expansion/sqrt(1+embryos.expansion^2) * embryos.T*2;
adults.tan.lead <-  adults.expansion/sqrt(1+adults.expansion^2) * adults.T*2;

embryos.sin.beta <- sin(atan(1.0/embryos.T/2.0));
adults.sin.beta <- sin(atan(1.0/adults.T/2.0));
embryos.cot.spiral <- embryos.expansion/embryos.sin.beta;
adults.cot.spiral <- adults.expansion/adults.sin.beta; 

newkrk.doyle.df <- data.frame(pop = rep(popnum,2), 
	is.embryo=c(is.embryo,!is.embryo),
	T=c(embryos.T,adults.T), W=c(embryos.W,adults.W), S=c(embryos.S, adults.S),
	expansion=c(embryos.expansion,adults.expansion),
	tan.lead=c(embryos.tan.lead,adults.tan.lead),
	tan.beta=c(1/2/embryos.T,1/2/adults.T),
	sin.beta=c(embryos.sin.beta,adults.sin.beta),
	cot.spiral=c(embryos.cot.spiral,adults.cot.spiral));

write.csv(newkrk.doyle.df,"newkrk-doyle-data.csv", row.names=FALSE);
