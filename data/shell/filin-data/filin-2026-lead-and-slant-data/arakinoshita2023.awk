BEGIN {
	OFS = ",";
	PI = 3.141592653589793238462643383279502884;
	INTEGERNUMBER = "[0-9]+(\.0+)?"
	REALNUMBER = "([0-9]+\.[0-9]*|\.[0-9]+)"
	REPOSITORY = "(SUM|SHIN|BPBM|SPMN|UMUT)"
	HABITAT = "(M|F|L)"
	GENUS = "([A-Z][a-z]+|Gen\.)"
	SPECIES = "([a-z]+|sp\.)"
	headerLine = "genus,species,subfamily,family,subclass,habitat,W,Traup,D,Delta,Gamma"
	fileHeader = headerLine;
	sub("subfamily,","",fileHeader);
	nNames = split(headerLine,arrayNames,",");
	for (i in arrayNames) {
		datalineArray[arrayNames[i]][1] = 1;
	}
	Index="";
}

NR<=3 { next }

/^[[:blank:]]*$/ { next }

NF==1 && $1 ~ /Subclass/ {
	Index="subclass"	
	next
}

NF==1 && $1 ~ "Familiy" {
	Index="family"	
	next
}

NF==1 && $1~/Subfamiliy/ {
	Index="subfamily"	
	next
}

NF==1 && $1~/habitat/ {
	Index="habitat"	
	next
}

NF==1 && $1 ~ /^W$/ {
	Index="W"	
	next
}

NF==1 && $1 ~ /^T$/ {
	Index="Traup"	
	next
}

NF==1 && $1 ~ /^D$/ {
	Index="D"	
	next
}

NF==1 && $1 ~ /^Δ$/ {
	Index="Delta"	
	next
}

NF==1 && $1 ~ /^Γ$/ {
	Index="Gamma"	
	next
}

NF==1 && $1 ~ /^Species$/ {
	Index="species"	
	next
}

Index=="species" && NF>1 && $1 ~ GENUS && $2 ~ SPECIES {
	genusName=$1;
	if (genusName=="Gen\.") 
		speciesName=$0;
	else
		speciesName = $2 (NF>2 ? " "$3 : "");

	datalineArray["genus"][1]++ 
	datalineArray["genus"][datalineArray["genus"][1]]=genusName
	datalineArray["species"][1]++ 
	datalineArray["species"][datalineArray["species"][1]]=speciesName
		
}

Index && NF==1 && Index != "species" {
	datalineArray[Index][1]++ 
	datalineArray[Index][datalineArray[Index][1]]=$1
}

END {
	print fileHeader
	for (j = 2; j<=datalineArray["species"][1]; j++) {
		print datalineArray["genus"][j],datalineArray["species"][j],\
			  datalineArray["family"][j],datalineArray["subclass"][j],\
			  datalineArray["habitat"][j],\
			  datalineArray["W"][j],datalineArray["Traup"][j],\
			  datalineArray["D"][j],datalineArray["Delta"][j],\
			  datalineArray["Gamma"][j];
	}
}

