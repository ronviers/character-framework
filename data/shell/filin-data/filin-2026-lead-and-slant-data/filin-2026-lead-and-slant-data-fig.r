library(ggplot2)
library(ggpubr);
library(dplyr)
noshita.etal.df <-read.csv("noshita-etal-merged.csv", header=TRUE);
newkrk.doyle.df <-read.csv("newkrk-doyle-data.csv", header=TRUE);

habitat.names <- c("M"="Marine","L"="Land","F"="Freshwater");
noshita.etal.df$habitat.factor <- as.factor(habitat.names[noshita.etal.df$habitat]);
newkrk.doyle.df$stage.factor <- as.factor(c("Adult","Embryo")[1+(newkrk.doyle.df$is.embryo)]);

nwkrkdoyl.size <- 2
scatterpoint.size <- 3
scatterpoint.opacity <- 1.00
boundary.curve.opacity <- 0.5
panel.label.font <- list(size=16,family="Arial");
habitat.legend.lab <- "Habitat"
expansion.xlab <- "Expansion rate, \ud835\udefe" #gamma
expansion.axis.breaks = c(0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8);

pbasetheme <- theme_bw() + 
	theme(legend.title=element_text(size=11, face="bold"), 
		  legend.text=element_text(size=11, face="plain"), 
		  legend.position="none", 
		  axis.title.x = element_text(family = "Sans", 
									  face = "plain", size = 12, color = "black",
									  margin=margin(0.25,0.0,0,0,"cm")),
		  axis.title.y = element_text(family = "Sans", 
									  face = "plain", size = 12, color = "black", 
									  margin=margin(0.0,0.25,0,0,"cm"))
	  ); 

pPalleteFill <- scale_fill_brewer(type="seq",palette="Set3");
pPalleteColor <-	scale_color_discrete(type=c("red","black"),
									  breaks=c("Embryo","Adult"),
									  na.translate=FALSE);

pbase1 <- ggplot() + 
	scale_x_log10() + scale_y_log10() + 
	scale_shape_manual(values=c(22,24,25,21,23,8,25,9,8,10,1)) + 
	scale_x_log10(breaks=expansion.axis.breaks, 
				  labels = scales::label_number(drop0trailing=TRUE)) + 
	pbasetheme + pPalleteFill + pPalleteColor + 
	xlab(expansion.xlab) + 
	labs(fill=habitat.legend.lab,shape=habitat.legend.lab, 
	     color=expression(atop(bolditalic("L. saxatilis"),bold("stage")))) + 
	guides(color=NULL,
		   fill=guide_legend(order=1, override.aes = list(size = 3)), 
		   shape=guide_legend(order=1,theme=pbasetheme, 
							  override.aes = list(size = 3.5))) + 
	theme(legend.justification = c(0.5, 1.0),
			legend.margin = margin(t=10,r=10,unit="pt"));
	
p.beta <- pbase1 +  
	scale_y_log10(breaks=c(0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 2.0, 4.0, 8.0, 10.0), 
				  labels = scales::label_number(drop0trailing=TRUE)) + 
	ylab("Apical semiangle, tan \ud835\udefd") + 
	geom_point(data=noshita.etal.df, 
		mapping=aes(x=expansion,y=tan.beta,shape=habitat.factor,fill=habitat.factor,color=NULL),
		size=scatterpoint.size, alpha=scatterpoint.opacity) + 

	geom_function(fun=function(x) sinh(pi*x), color="black") + 
	geom_function(fun=function(x) pi*x/sqrt(1+x^2), 
				  color="gray", linewidth=1.5, alpha=boundary.curve.opacity) + 
	geom_function(fun=function(x) 2.0*sinh(pi*x), color="black") + 
	geom_function(fun=function(x) 0.5*pi*x/sqrt(1+x^2), 
				  color="gray", linewidth=1.5, alpha=boundary.curve.opacity) + 
	geom_function(fun=function(x) 0.5*sinh(pi*x), color="black") + 
	geom_function(fun=function(x) 2.0*pi*x/sqrt(1+x^2), 
				  color="gray", linewidth=1.5, alpha=boundary.curve.opacity) + 
	geom_vline(xintercept = 0.2, color="orange", linewidth = 1.5, alpha=0.5, lty="dashed" ) + 
	geom_point(data=newkrk.doyle.df,
		mapping=aes(x=expansion,y=tan.beta,color=stage.factor, fill=NULL, shape=NULL),
		shape=20, size=nwkrkdoyl.size, stroke=2, show.legend=F);

p.lambda <- pbase1 +  
	scale_y_log10(breaks=c(0.01, 0.02, 0.03, 0.05, 0.1, 0.2, 0.32, 0.4, 0.6, 0.8, 1.0), 
				  labels = scales::label_number(drop0trailing=TRUE)) + 
	ylab("Lead angle, tan \uD835\uDF06") + #lambda
	geom_point(data=noshita.etal.df, 
		mapping=aes(x=expansion,
			y=tan.lead,
			shape=habitat.factor,fill=habitat.factor, color=NULL), 
		size=scatterpoint.size, alpha=scatterpoint.opacity) + 
	geom_function(fun=function(x) x/sqrt(1+x^2)/sinh(pi*x), color="black") + 
	geom_function(fun=function(x) 1/pi, 
				  color="gray", linewidth=1.5, alpha=boundary.curve.opacity) +
	geom_function(fun=function(x) 0.5*x/sqrt(1+x^2)/sinh(pi*x), color="black") + 
	geom_function(fun=function(x) 0.5/pi, 
				  color="gray", linewidth=1.5, alpha=boundary.curve.opacity) +
	geom_function(fun=function(x) 2.0*x/sqrt(1+x^2)/sinh(pi*x), color="black") + 
	geom_function(fun=function(x) 2.0/pi, 
				  color="gray", linewidth=1.5, alpha=boundary.curve.opacity) +
	geom_vline(xintercept = 0.2, color="orange", linewidth = 1.5, alpha=0.5, lty="dashed" ) + 
	geom_point(data=newkrk.doyle.df,
		mapping=aes(x=expansion,
			y=tan.lead,
			color=stage.factor, fill=NULL, shape=NULL),
		shape=20, size=nwkrkdoyl.size, stroke=2, show.legend=F);

p <- ggarrange(p.beta, p.lambda,
		ncol=2, nrow=1, 
		widths=c(1,1),
		common.legend=T, 
		labels=c("A","B"),
		font.label=panel.label.font, 
		hjust=c(-4.5, -4.5), 
		vjust=+2);

print(p);
cairo_ps("datafig-slantnote.eps", height=5, width=9); print(p);dev.off();
cairo_pdf("datafig-slantnote.pdf", height=5, width=9); print(p);dev.off();

