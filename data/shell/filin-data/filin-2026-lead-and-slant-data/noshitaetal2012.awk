BEGIN {
	OFS = ",";
	PI = 3.141592653589793238462643383279502884;
	INTEGERNUMBER = "[0-9]+(\.0+)?"
	REALNUMBER = "([0-9]+\.[0-9]*|\.[0-9]+)"
	REPOSITORY = "(SUM|SHIN|BPBM|SPMN|UMUT)"
	HABITAT = "(M|F|L)"
	FAMILY = "[A-Z][a-z]+dae"
	GENUS = "[A-Z][a-z]+"
	SPECIES = "[a-z]+"
	print "genus","species","family","repo","habitat","W","Traup","D","Delta","Gamma","OneOverLambda","E"
	resetArray();
	family="";
}

NF==1  && $1 ~ "^"REPOSITORY"$" {
	repo = $1
}	

NF==1  && $1 ~ "^"HABITAT"$" {
	habitat = $1
}	

NF==1  && $1 ~ "^"FAMILY"$" {
	familybuffer = $1
	if (!family) family=familybuffer
}	

NF==2  && $1 ~ "^"REPOSITORY"$" {
	repo = $1
	habitat = $2
}

(NF==2 || NF==3) && $1 ~ GENUS && $2 ~ SPECIES {
	if (species) printDataline()
	resetArray()
	genus = $1 
	species = $2 (NF==3 ? " "$3 : "")
}

{#Main, hopefully for number datums
	for (i=1; i<=NF; ++i) {
		if ($i ~ REALNUMBER) {
			dataLine[datumIndex] = $i;	
			datumIndex++;
		}
	}
}

END {
	printDataline()
}

function printDataline() {
	gsub(/^[[:space:]]+/,"",species);
	gsub(/[[:space:]]+$/,"",species);
	gsub(/^[[:space:]]+/,"",genus);
	gsub(/[[:space:]]+$/,"",genus);
	print genus,species,family,repo,habitat,\
			 dataLine[1],dataLine[2],dataLine[3],dataLine[4],\
			 dataLine[5],dataLine[6],dataLine[7]
}

function resetArray() {
	species="";
	genus="";
	repo="";
	family=familybuffer;
	habitat="";
	for (i=1; i<=7; ++i) 
		dataLine[i] = "NA";	
	datumIndex = 1;
}
