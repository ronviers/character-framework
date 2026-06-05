# line 12   - A) raw data obtained from procedure 1 - 6.
# line 155  - B) Procedure 6: Principal component analysis on EFA coeefficient.
# line 177  - C) Preparing data for procedure 7 and 8.
# line 212  - D) Procedure 7: scatter plots.
# line 633 - E) Procedure 8: cluster analysis.



################################################
################################################
##                                            ##
##A) raw data obtained from procedure 1 - 6.  ----
##                                            ##A
################################################
################################################
    ##############
    # Open files ----        
    ##############

####Set working directory - where the files were saved
christae_bor_5572_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_christae_bor_5572_surface_circle_no_peristome.001 NEFA.csv")
crassipupa_bor_5512_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_crassipupa_5512_surface_circle_no_peristome.001 NEFA.csv")
laidlawi_zma_136014_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_laidlawi_surface_circle_no_peristome.001 NEFA.csv")
vermiculum_rapat_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_vermiculum_rapat_surface_circle_start12_no_peristome.001 NEFA.csv")
laidl_rs_zma_136014_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_07112013 Retopo laidlawi surface circle no peristome_ half size NEFA.csv")
vermic_2X_rapat_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo vermiculum rapat surface circle_start12 no peristome 2X NEFA.csv")
chris_ob_bor_5572_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo christae bor 5572 surface circle no peristome 0.5XY2Z NEFA.csv")
chris_de_bor_5572_NEFA <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo christae bor 5572 surface circle no peristome 2XY0.5Z NEFA.csv")

christae_bor_5572_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_christae_bor_5572_surface_circle_no_peristome.001 perimeter.csv")
crassipupa_bor_5512_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_crassipupa_5512_surface_circle_no_peristome.001 perimeter.csv")
laidlawi_zma_136014_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_laidlawi_surface_circle_no_peristome.001 perimeter.csv")
vermiculum_rapat_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_vermiculum_rapat_surface_circle_start12_no_peristome.001 perimeter.csv")
laidl_rs_zma_136014_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_07112013 Retopo laidlawi surface circle no peristome_ half size perimeter.csv")
vermic_2X_rapat_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo vermiculum rapat surface circle_start12 no peristome 2X perimeter.csv")
chris_ob_bor_5572_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo christae bor 5572 surface circle no peristome 0.5XY2Z perimeter.csv")
chris_de_bor_5572_perimeter <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo christae bor 5572 surface circle no peristome 2XY0.5Z perimeter.csv")

christae_bor_5572_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_christae_bor_5572_surface_circle_no_peristome.001_q70.csv")
crassipupa_bor_5512_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_crassipupa_5512_surface_circle_no_peristome.001_q50.csv")
laidlawi_zma_136014_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_laidlawi_surface_circle_no_peristome.001_q70.csv")
vermiculum_rapat_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all 4 shell Retopo_vermiculum_rapat_surface_circle_start12_no_peristome.001_q60.csv")
laidl_rs_zma_136014_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_07112013 Retopo laidlawi surface circle no peristome_ half size_q70.csv")
vermic_2X_rapat_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo vermiculum rapat surface circle_start12 no peristome 2X_q50.csv")
chris_ob_bor_5572_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo christae bor 5572 surface circle no peristome 0.5XY2Z_q70.csv")
chris_de_bor_5572_torsion_curvature_ontogenyaxis <- read.csv("C:/Liew Thor Seng/PhD thesis/A practical guide to morphological analysis of 3D model/To be submit to PeerJ/all morphometric for 4 species/all_4_shell_06112013 Retopo christae bor 5572 surface circle no peristome 2XY0.5Z_q70.csv")

    ###############
    # Merge files ----        
    ###############
str(christae_bor_5572_NEFA)
str(christae_bor_5572_perimeter)
str(christae_bor_5572_torsion_curvature_ontogenyaxis)
summary(christae_bor_5572_NEFA)
summary(christae_bor_5572_perimeter)
summary(christae_bor_5572_torsion_curvature_ontogenyaxis)
all_morphometric_christae_bor_5572_temp1 <- merge(christae_bor_5572_NEFA,christae_bor_5572_perimeter,by="aperture")
all_morphometric_christae_bor_5572_temp2 <- merge(christae_bor_5572_torsion_curvature_ontogenyaxis,all_morphometric_christae_bor_5572_temp1,by="aperture")
label <- rep('christae', 760)
all_morphometric_christae_bor_5572 <- cbind(all_morphometric_christae_bor_5572_temp2,label)
str(all_morphometric_christae_bor_5572)

str(crassipupa_bor_5512_NEFA)
str(crassipupa_bor_5512_perimeter)
str(crassipupa_bor_5512_torsion_curvature_ontogenyaxis)
summary(crassipupa_bor_5512_NEFA)
summary(crassipupa_bor_5512_perimeter)
summary(crassipupa_bor_5512_torsion_curvature_ontogenyaxis)
all_morphometric_crassipupa_bor_5512_temp1 <- merge(crassipupa_bor_5512_NEFA,crassipupa_bor_5512_perimeter,by="aperture")
all_morphometric_crassipupa_bor_5512_temp2 <- merge(crassipupa_bor_5512_torsion_curvature_ontogenyaxis,all_morphometric_crassipupa_bor_5512_temp1,by="aperture")
label <- rep('crassipupa', 576)
all_morphometric_crassipupa_bor_5512 <- cbind(all_morphometric_crassipupa_bor_5512_temp2,label)
str(all_morphometric_crassipupa_bor_5512)

str(laidlawi_zma_136014_NEFA)
str(laidlawi_zma_136014_perimeter)
str(laidlawi_zma_136014_torsion_curvature_ontogenyaxis)
summary(laidlawi_zma_136014_NEFA)
summary(laidlawi_zma_136014_perimeter)
summary(laidlawi_zma_136014_torsion_curvature_ontogenyaxis)
all_morphometric_laidlawi_zma_136014_temp1 <- merge(laidlawi_zma_136014_NEFA,laidlawi_zma_136014_perimeter,by="aperture")
all_morphometric_laidlawi_zma_136014_temp2 <- merge(laidlawi_zma_136014_torsion_curvature_ontogenyaxis,all_morphometric_laidlawi_zma_136014_temp1,by="aperture")
label <- rep('laidlawi', 760)
all_morphometric_laidlawi_zma_136014 <- cbind(all_morphometric_laidlawi_zma_136014_temp2,label)
str(all_morphometric_laidlawi_zma_136014)

str(vermiculum_rapat_NEFA)
str(vermiculum_rapat_perimeter)
str(vermiculum_rapat_torsion_curvature_ontogenyaxis)
summary(vermiculum_rapat_NEFA)
summary(vermiculum_rapat_perimeter)
summary(vermiculum_rapat_torsion_curvature_ontogenyaxis)
all_morphometric_vermiculum_rapat_temp1 <- merge(vermiculum_rapat_NEFA,vermiculum_rapat_perimeter,by="aperture")
all_morphometric_vermiculum_rapat_temp2 <- merge(vermiculum_rapat_torsion_curvature_ontogenyaxis,all_morphometric_vermiculum_rapat_temp1,by="aperture")
label <- rep('vermiculum', 672)
all_morphometric_vermiculum_rapat <- cbind(all_morphometric_vermiculum_rapat_temp2,label)
str(all_morphometric_vermiculum_rapat)

str(laidl_rs_zma_136014_NEFA)
str(laidl_rs_zma_136014_perimeter)
str(laidl_rs_zma_136014_torsion_curvature_ontogenyaxis)
summary(laidl_rs_zma_136014_NEFA)
summary(laidl_rs_zma_136014_perimeter)
summary(laidl_rs_zma_136014_torsion_curvature_ontogenyaxis)
all_morphometric_laidl_rs_zma_136014_temp1 <- merge(laidl_rs_zma_136014_NEFA,laidl_rs_zma_136014_perimeter,by="aperture")
all_morphometric_laidl_rs_zma_136014_temp2 <- merge(laidl_rs_zma_136014_torsion_curvature_ontogenyaxis,all_morphometric_laidl_rs_zma_136014_temp1,by="aperture")
label <- rep('laidl_rs', 760)
all_morphometric_laidl_rs_zma_136014 <- cbind(all_morphometric_laidl_rs_zma_136014_temp2,label)
str(all_morphometric_laidl_rs_zma_136014)

str(vermic_2X_rapat_NEFA)
str(vermic_2X_rapat_perimeter)
str(vermic_2X_rapat_torsion_curvature_ontogenyaxis)
summary(vermic_2X_rapat_NEFA)
summary(vermic_2X_rapat_perimeter)
summary(vermic_2X_rapat_torsion_curvature_ontogenyaxis)
all_morphometric_vermic_2X_rapat_temp1 <- merge(vermic_2X_rapat_NEFA,vermic_2X_rapat_perimeter,by="aperture")
all_morphometric_vermic_2X_rapat_temp2 <- merge(vermic_2X_rapat_torsion_curvature_ontogenyaxis,all_morphometric_vermic_2X_rapat_temp1,by="aperture")
label <- rep('vermic_2X', 540)
all_morphometric_vermic_2X_rapat <- cbind(all_morphometric_vermic_2X_rapat_temp2,label)
str(all_morphometric_vermic_2X_rapat)

str(chris_ob_bor_5572_NEFA)
str(chris_ob_bor_5572_perimeter)
str(chris_ob_bor_5572_torsion_curvature_ontogenyaxis)
summary(chris_ob_bor_5572_NEFA)
summary(chris_ob_bor_5572_perimeter)
summary(chris_ob_bor_5572_torsion_curvature_ontogenyaxis)
all_morphometric_chris_ob_bor_5572_temp1 <- merge(chris_ob_bor_5572_NEFA,chris_ob_bor_5572_perimeter,by="aperture")
all_morphometric_chris_ob_bor_5572_temp2 <- merge(chris_ob_bor_5572_torsion_curvature_ontogenyaxis,all_morphometric_chris_ob_bor_5572_temp1,by="aperture")
label <- rep('chris_ob', 760)
all_morphometric_chris_ob_bor_5572 <- cbind(all_morphometric_chris_ob_bor_5572_temp2,label)
str(all_morphometric_chris_ob_bor_5572)

str(chris_de_bor_5572_NEFA)
str(chris_de_bor_5572_perimeter)
str(chris_de_bor_5572_torsion_curvature_ontogenyaxis)
summary(chris_de_bor_5572_NEFA)
summary(chris_de_bor_5572_perimeter)
summary(chris_de_bor_5572_torsion_curvature_ontogenyaxis)
all_morphometric_chris_de_bor_5572_temp1 <- merge(chris_de_bor_5572_NEFA,chris_de_bor_5572_perimeter,by="aperture")
all_morphometric_chris_de_bor_5572_temp2 <- merge(chris_de_bor_5572_torsion_curvature_ontogenyaxis,all_morphometric_chris_de_bor_5572_temp1,by="aperture")
label <- rep('chris_de', 760)
all_morphometric_chris_de_bor_5572 <- cbind(all_morphometric_chris_de_bor_5572_temp2,label)
str(all_morphometric_chris_de_bor_5572)


combined_all_morphometric_data_of_all_shells <- rbind(all_morphometric_christae_bor_5572, all_morphometric_crassipupa_bor_5512,all_morphometric_laidlawi_zma_136014,all_morphometric_vermiculum_rapat,all_morphometric_laidl_rs_zma_136014,all_morphometric_vermic_2X_rapat,all_morphometric_chris_ob_bor_5572,all_morphometric_chris_de_bor_5572) 
str(combined_all_morphometric_data_of_all_shells)
summary(combined_all_morphometric_data_of_all_shells)

##########################################################
##########################################################
##                                                      ##
## B) Procedure 6:                                      ## 
##    Principal component analysis on EFA coeefficient. ----
##                                                      ##
##########################################################
##########################################################

species <- combined_all_morphometric_data_of_all_shells[,48]
ontogeny_axis <- combined_all_morphometric_data_of_all_shells[,3]
aperture_size <- combined_all_morphometric_data_of_all_shells[,47]
NEFA_cooefficient_Of_all_shells <- combined_all_morphometric_data_of_all_shells[,12:41]
str(NEFA_cooefficient_Of_all_shells)

pca <- prcomp(NEFA_cooefficient_Of_all_shells)
#plot(pca)
summary(pca)
rot <- pca$r
round(rot*100)
pca_scores <- pca$x

##########################################################
##########################################################
##                                                      ##
## C) Preparing data for procedure 7 and 8              ----
##                                                      ##
##########################################################
##########################################################
Final_data_output <- 
  cbind((combined_all_morphometric_data_of_all_shells[,1:3]),
        as.numeric(format((combined_all_morphometric_data_of_all_shells[,9]), digit = 2)),
        as.numeric(format((combined_all_morphometric_data_of_all_shells[,10]), digit = 2)),
        (pca_scores[,1:3]),
        (combined_all_morphometric_data_of_all_shells[,47:48]))

str(Final_data_output)

write.table(Final_data_output, file = "Final_data_output.csv", sep = ",")
getwd()

library(rgl)
plot3d((Final_data_output[,4]), 
       (Final_data_output[,5]), 
       (Final_data_output[,9]), 
       size=1, type='s',
       col=c(rep("red",760),rep("yellow",576), rep("blue",760), rep("green",672), rep("dodgerblue",760), rep("darkgreen",540), rep("darkorange",760), rep("darkred",760)),
       xlab = "Curvature 1/mm", ylab = "Torsion 1/mm", zlab = "Aperture perimeter mm")

library(rgl)
plot3d((Final_data_output[,6]), 
       (Final_data_output[,5]), 
       (Final_data_output[,9]), 
       size=1, type='s',
       col=c(rep("red",760),rep("yellow",576), rep("blue",760), rep("green",672), rep("dodgerblue",760), rep("darkgreen",540), rep("darkorange",760), rep("darkred",760)),
       xlab = "PC1", ylab = "Torsion 1/mm", zlab = "Aperture perimeter mm")

##########################################################
##########################################################
##                                                      ##
## D) Procedure 7: scatter plots                        ----
##                                                      ##
##########################################################
##########################################################

    #################
    # Dataset       ----       
    #################

christae_time_series_all_morphometrics <- Final_data_output[1:760,]
crassipupa_time_series_all_morphometrics <- Final_data_output[761:1336,]
laidlawi_time_series_all_morphometrics <- Final_data_output[1337:2096,]
vermiculum_time_series_all_morphometrics <- Final_data_output[2097:2768,]
laidl_rs_time_series_all_morphometrics <- Final_data_output[2769:3528,]
vermic_2X_time_series_all_morphometrics <- Final_data_output[3529:4068,] 
chris_ob_time_series_all_morphometrics <- Final_data_output[4069:4828,] 
chris_de_time_series_all_morphometrics <- Final_data_output[4829:5588,] 

    #################
    # Scatter plots #        
    #################

par(mar=c(0.25,0.25, 0.01, 0.5),mfcol=c(6, 8))
#par(mar=c(2, 2, 0, 0.5),mfcol=c(6, 8))
#bottom, left, top and right margins 
plot(christae_time_series_all_morphometrics[,3],
     christae_time_series_all_morphometrics[,4],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",pch='.',cex=0.5,
     )
plot(christae_time_series_all_morphometrics[,3],
     christae_time_series_all_morphometrics[,5],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",pch='.',cex=0.5,
)
plot(christae_time_series_all_morphometrics[,3],
      christae_time_series_all_morphometrics[,9],
      #main="title", sub="subtitle",
      #xlab="X-axis label", ylab="y-axix label",
      xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
      ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",pch='.',cex=0.5,
)
plot(christae_time_series_all_morphometrics[,3],
      christae_time_series_all_morphometrics[,6],
      #main="title", sub="subtitle",
      #xlab="X-axis label", ylab="y-axix label",
      xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
      ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",pch='.',cex=0.5,
)
plot(christae_time_series_all_morphometrics[,3],
     christae_time_series_all_morphometrics[,7],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",pch='.',cex=0.5,
)
plot(christae_time_series_all_morphometrics[,3],
     christae_time_series_all_morphometrics[,8],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     pch='.',cex=0.5,
)

plot(crassipupa_time_series_all_morphometrics[,3],
     crassipupa_time_series_all_morphometrics[,4],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(crassipupa_time_series_all_morphometrics[,3],
     crassipupa_time_series_all_morphometrics[,5],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(crassipupa_time_series_all_morphometrics[,3],
     crassipupa_time_series_all_morphometrics[,9],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(crassipupa_time_series_all_morphometrics[,3],
     crassipupa_time_series_all_morphometrics[,6],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(crassipupa_time_series_all_morphometrics[,3],
     crassipupa_time_series_all_morphometrics[,7],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(crassipupa_time_series_all_morphometrics[,3],
     crassipupa_time_series_all_morphometrics[,8],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     yaxt = "n",pch='.',cex=0.5,
)

plot(laidlawi_time_series_all_morphometrics[,3],
     laidlawi_time_series_all_morphometrics[,4],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidlawi_time_series_all_morphometrics[,3],
     laidlawi_time_series_all_morphometrics[,5],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidlawi_time_series_all_morphometrics[,3],
     laidlawi_time_series_all_morphometrics[,9],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidlawi_time_series_all_morphometrics[,3],
     laidlawi_time_series_all_morphometrics[,6],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidlawi_time_series_all_morphometrics[,3],
     laidlawi_time_series_all_morphometrics[,7],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidlawi_time_series_all_morphometrics[,3],
     laidlawi_time_series_all_morphometrics[,8],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     yaxt = "n",pch='.',cex=0.5,
)

plot(vermiculum_time_series_all_morphometrics[,3],
     vermiculum_time_series_all_morphometrics[,4],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermiculum_time_series_all_morphometrics[,3],
     vermiculum_time_series_all_morphometrics[,5],
     ###main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermiculum_time_series_all_morphometrics[,3],
     vermiculum_time_series_all_morphometrics[,9],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermiculum_time_series_all_morphometrics[,3],
     vermiculum_time_series_all_morphometrics[,6],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermiculum_time_series_all_morphometrics[,3],
     vermiculum_time_series_all_morphometrics[,7],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermiculum_time_series_all_morphometrics[,3],
     vermiculum_time_series_all_morphometrics[,8],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     yaxt = "n",pch='.',cex=0.5,
)

plot(laidl_rs_time_series_all_morphometrics[,3],
     laidl_rs_time_series_all_morphometrics[,4],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidl_rs_time_series_all_morphometrics[,3],
     laidl_rs_time_series_all_morphometrics[,5],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidl_rs_time_series_all_morphometrics[,3],
     laidl_rs_time_series_all_morphometrics[,9],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidl_rs_time_series_all_morphometrics[,3],
     laidl_rs_time_series_all_morphometrics[,6],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidl_rs_time_series_all_morphometrics[,3],
     laidl_rs_time_series_all_morphometrics[,7],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(laidl_rs_time_series_all_morphometrics[,3],
     laidl_rs_time_series_all_morphometrics[,8],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     yaxt = "n",pch='.',cex=0.5,
)

plot(vermic_2X_time_series_all_morphometrics[,3],
     vermic_2X_time_series_all_morphometrics[,4],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermic_2X_time_series_all_morphometrics[,3],
     vermic_2X_time_series_all_morphometrics[,5],
     ###main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermic_2X_time_series_all_morphometrics[,3],
     vermic_2X_time_series_all_morphometrics[,9],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermic_2X_time_series_all_morphometrics[,3],
     vermic_2X_time_series_all_morphometrics[,6],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermic_2X_time_series_all_morphometrics[,3],
     vermic_2X_time_series_all_morphometrics[,7],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(vermic_2X_time_series_all_morphometrics[,3],
     vermic_2X_time_series_all_morphometrics[,8],
     ##main="title", sub="subtitle",
     ##xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     yaxt = "n",pch='.',cex=0.5,
)

plot(chris_ob_time_series_all_morphometrics[,3],
     chris_ob_time_series_all_morphometrics[,4],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_ob_time_series_all_morphometrics[,3],
     chris_ob_time_series_all_morphometrics[,5],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_ob_time_series_all_morphometrics[,3],
     chris_ob_time_series_all_morphometrics[,9],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_ob_time_series_all_morphometrics[,3],
     chris_ob_time_series_all_morphometrics[,6],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_ob_time_series_all_morphometrics[,3],
     chris_ob_time_series_all_morphometrics[,7],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_ob_time_series_all_morphometrics[,3],
     chris_ob_time_series_all_morphometrics[,8],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     yaxt = "n",pch='.',cex=0.5,
)

plot(chris_de_time_series_all_morphometrics[,3],
     chris_de_time_series_all_morphometrics[,4],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,4]))),(max(na.omit(Final_data_output[,4])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_de_time_series_all_morphometrics[,3],
     chris_de_time_series_all_morphometrics[,5],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,5]))),(max(na.omit(Final_data_output[,5])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_de_time_series_all_morphometrics[,3],
     chris_de_time_series_all_morphometrics[,9],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,9]))),(max(na.omit(Final_data_output[,9])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_de_time_series_all_morphometrics[,3],
     chris_de_time_series_all_morphometrics[,6],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,6]))),(max(na.omit(Final_data_output[,6])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_de_time_series_all_morphometrics[,3],
     chris_de_time_series_all_morphometrics[,7],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,7]))),(max(na.omit(Final_data_output[,7])))),
     xaxt = "n",yaxt = "n",pch='.',cex=0.5,
)
plot(chris_de_time_series_all_morphometrics[,3],
     chris_de_time_series_all_morphometrics[,8],
     #main="title", sub="subtitle",
     #xlab="X-axis label", ylab="y-axix label",
     xlim=c((min(na.omit(Final_data_output[,3]))),(max(na.omit(Final_data_output[,3])))), 
     ylim=c((min(na.omit(Final_data_output[,8]))),(max(na.omit(Final_data_output[,8])))),
     yaxt = "n",pch='.',cex=0.5,
)


##########################################################
##########################################################
##                                                      ##
## E) Procedure 8: cluster analysis                     ----
##                                                      ##
##########################################################
##########################################################

    ##############################################################
    # Restructuring continuous time series data to interval data ----
    # for cluster analysis (missing data NA was included         #
    ##############################################################

par(mfcol=c(6,8))
par(mar=c(2, 2, 0, 0.25),mfcol=c(6, 8))

christae_data <- Final_data_output[1:760,]
interval <- (max(christae_data[,3])-min(christae_data[,3]))/49
interval_list = min(christae_data[,3])
each_inverval = min(christae_data[,3])
while(each_inverval < (max(christae_data[,3]))){ 
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(christae_data[,3]-i)==min(abs(christae_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
christae_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  christae_interval_dataset_perimeter <- append(christae_interval_dataset_perimeter,christae_data[i,9])
}
christae_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  christae_interval_dataset_ontogeny_axis <- append(christae_interval_dataset_ontogeny_axis,christae_data[i,3])
}
christae_interval_dataset_curvature= vector()
for (i in interval_list_index){
  christae_interval_dataset_curvature <- append(christae_interval_dataset_curvature,christae_data[i,4])
}
christae_interval_dataset_torsion= vector()
for (i in interval_list_index){
  christae_interval_dataset_torsion <- append(christae_interval_dataset_torsion,christae_data[i,5])
}
christae_interval_dataset_PC1 = vector()
for (i in interval_list_index){
  christae_interval_dataset_PC1 <- append(christae_interval_dataset_PC1,christae_data[i,6])
}
christae_interval_dataset_PC2 = vector()
for (i in interval_list_index){
  christae_interval_dataset_PC2 <- append(christae_interval_dataset_PC2,christae_data[i,7])
}
christae_interval_dataset_PC3 = vector()
for (i in interval_list_index){
  christae_interval_dataset_PC3 <- append(christae_interval_dataset_PC3,christae_data[i,8])
}
plot(christae_interval_dataset_ontogeny_axis,christae_interval_dataset_perimeter)
plot(christae_interval_dataset_ontogeny_axis,christae_interval_dataset_curvature)
plot(christae_interval_dataset_ontogeny_axis,christae_interval_dataset_torsion)
plot(christae_interval_dataset_ontogeny_axis,christae_interval_dataset_PC1)
plot(christae_interval_dataset_ontogeny_axis,christae_interval_dataset_PC2)
plot(christae_interval_dataset_ontogeny_axis,christae_interval_dataset_PC3)
##
##
crassipupa_data <- Final_data_output[761:1336,]
interval <- (max(crassipupa_data[,3])-min(crassipupa_data[,3]))/49
interval_list = min(crassipupa_data[,3])
each_inverval = min(crassipupa_data[,3])
while(each_inverval < (max(crassipupa_data[,3]))-interval){ 
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(crassipupa_data[,3]-i)==min(abs(crassipupa_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
crassipupa_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  crassipupa_interval_dataset_perimeter <- append(crassipupa_interval_dataset_perimeter,crassipupa_data[i,9])
}
crassipupa_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  crassipupa_interval_dataset_ontogeny_axis <- append(crassipupa_interval_dataset_ontogeny_axis,crassipupa_data[i,3])
}
crassipupa_interval_dataset_curvature= vector()
for (i in interval_list_index){
  crassipupa_interval_dataset_curvature <- append(crassipupa_interval_dataset_curvature,crassipupa_data[i,4])
}
crassipupa_interval_dataset_torsion= vector()
for (i in interval_list_index){
  crassipupa_interval_dataset_torsion <- append(crassipupa_interval_dataset_torsion,crassipupa_data[i,5])
}
crassipupa_interval_dataset_PC1= vector()
for (i in interval_list_index){
  crassipupa_interval_dataset_PC1 <- append(crassipupa_interval_dataset_PC1,crassipupa_data[i,6])
}
crassipupa_interval_dataset_PC2= vector()
for (i in interval_list_index){
  crassipupa_interval_dataset_PC2 <- append(crassipupa_interval_dataset_PC2,crassipupa_data[i,7])
}
crassipupa_interval_dataset_PC3= vector()
for (i in interval_list_index){
  crassipupa_interval_dataset_PC3 <- append(crassipupa_interval_dataset_PC3,crassipupa_data[i,8])
}
plot(crassipupa_interval_dataset_ontogeny_axis,crassipupa_interval_dataset_perimeter)
plot(crassipupa_interval_dataset_ontogeny_axis,crassipupa_interval_dataset_curvature)
plot(crassipupa_interval_dataset_ontogeny_axis,crassipupa_interval_dataset_torsion)
plot(crassipupa_interval_dataset_ontogeny_axis,crassipupa_interval_dataset_PC1)
plot(crassipupa_interval_dataset_ontogeny_axis,crassipupa_interval_dataset_PC2)
plot(crassipupa_interval_dataset_ontogeny_axis,crassipupa_interval_dataset_PC3)
##
##
laidlawi_data <- Final_data_output[1337:2096,]
interval <- (max(laidlawi_data[,3])-min(laidlawi_data[,3]))/49
interval_list = min(laidlawi_data[,3])
each_inverval = min(laidlawi_data[,3])
while(each_inverval < (max(laidlawi_data[,3]))){ 
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(laidlawi_data[,3]-i)==min(abs(laidlawi_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
laidlawi_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  laidlawi_interval_dataset_perimeter <- append(laidlawi_interval_dataset_perimeter,laidlawi_data[i,9])
}
laidlawi_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  laidlawi_interval_dataset_ontogeny_axis <- append(laidlawi_interval_dataset_ontogeny_axis,laidlawi_data[i,3])
}
laidlawi_interval_dataset_curvature= vector()
for (i in interval_list_index){
  laidlawi_interval_dataset_curvature <- append(laidlawi_interval_dataset_curvature,laidlawi_data[i,4])
}
laidlawi_interval_dataset_torsion= vector()
for (i in interval_list_index){
  laidlawi_interval_dataset_torsion <- append(laidlawi_interval_dataset_torsion,laidlawi_data[i,5])
}
laidlawi_interval_dataset_PC1= vector()
for (i in interval_list_index){
  laidlawi_interval_dataset_PC1 <- append(laidlawi_interval_dataset_PC1,laidlawi_data[i,6])
}
laidlawi_interval_dataset_PC2= vector()
for (i in interval_list_index){
  laidlawi_interval_dataset_PC2 <- append(laidlawi_interval_dataset_PC2,laidlawi_data[i,7])
}
laidlawi_interval_dataset_PC3= vector()
for (i in interval_list_index){
  laidlawi_interval_dataset_PC3 <- append(laidlawi_interval_dataset_PC3,laidlawi_data[i,8])
}
plot(laidlawi_interval_dataset_ontogeny_axis,laidlawi_interval_dataset_perimeter)
plot(laidlawi_interval_dataset_ontogeny_axis,laidlawi_interval_dataset_curvature)
plot(laidlawi_interval_dataset_ontogeny_axis,laidlawi_interval_dataset_torsion)
plot(laidlawi_interval_dataset_ontogeny_axis,laidlawi_interval_dataset_PC1)
plot(laidlawi_interval_dataset_ontogeny_axis,laidlawi_interval_dataset_PC2)
plot(laidlawi_interval_dataset_ontogeny_axis,laidlawi_interval_dataset_PC3)
##
##
vermiculum_data <- Final_data_output[2097:2768,]
interval <- (max(vermiculum_data[,3])-min(vermiculum_data[,3]))/49
interval_list = min(vermiculum_data[,3])
each_inverval = min(vermiculum_data[,3])
while(each_inverval < (max(vermiculum_data[,3])-interval)){ 
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(vermiculum_data[,3]-i)==min(abs(vermiculum_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
vermiculum_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  vermiculum_interval_dataset_perimeter <- append(vermiculum_interval_dataset_perimeter,vermiculum_data[i,9])
}
vermiculum_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  vermiculum_interval_dataset_ontogeny_axis <- append(vermiculum_interval_dataset_ontogeny_axis,vermiculum_data[i,3])
}
vermiculum_interval_dataset_curvature= vector()
for (i in interval_list_index){
  vermiculum_interval_dataset_curvature <- append(vermiculum_interval_dataset_curvature,vermiculum_data[i,4])
}
vermiculum_interval_dataset_torsion= vector()
for (i in interval_list_index){
  vermiculum_interval_dataset_torsion <- append(vermiculum_interval_dataset_torsion,vermiculum_data[i,5])
}
vermiculum_interval_dataset_PC1= vector()
for (i in interval_list_index){
  vermiculum_interval_dataset_PC1 <- append(vermiculum_interval_dataset_PC1,vermiculum_data[i,6])
}
vermiculum_interval_dataset_PC2= vector()
for (i in interval_list_index){
  vermiculum_interval_dataset_PC2 <- append(vermiculum_interval_dataset_PC2,vermiculum_data[i,7])
}
vermiculum_interval_dataset_PC3= vector()
for (i in interval_list_index){
  vermiculum_interval_dataset_PC3 <- append(vermiculum_interval_dataset_PC3,vermiculum_data[i,8])
}
plot(vermiculum_interval_dataset_ontogeny_axis,vermiculum_interval_dataset_perimeter)
plot(vermiculum_interval_dataset_ontogeny_axis,vermiculum_interval_dataset_curvature)
plot(vermiculum_interval_dataset_ontogeny_axis,vermiculum_interval_dataset_torsion)
plot(vermiculum_interval_dataset_ontogeny_axis,vermiculum_interval_dataset_PC1)
plot(vermiculum_interval_dataset_ontogeny_axis,vermiculum_interval_dataset_PC2)
plot(vermiculum_interval_dataset_ontogeny_axis,vermiculum_interval_dataset_PC3)
##
laidl_rs_data <- Final_data_output[2769:3528,]
interval <- (max(laidl_rs_data[,3])-min(laidl_rs_data[,3]))/49
interval_list = min(laidl_rs_data[,3])
each_inverval = min(laidl_rs_data[,3])
while(each_inverval < (max(laidl_rs_data[,3]))){
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(laidl_rs_data[,3]-i)==min(abs(laidl_rs_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
laidl_rs_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  laidl_rs_interval_dataset_perimeter <- append(laidl_rs_interval_dataset_perimeter,laidl_rs_data[i,9])
}
laidl_rs_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  laidl_rs_interval_dataset_ontogeny_axis <- append(laidl_rs_interval_dataset_ontogeny_axis,laidl_rs_data[i,3])
}
laidl_rs_interval_dataset_curvature= vector()
for (i in interval_list_index){
  laidl_rs_interval_dataset_curvature <- append(laidl_rs_interval_dataset_curvature,laidl_rs_data[i,4])
}
laidl_rs_interval_dataset_torsion= vector()
for (i in interval_list_index){
  laidl_rs_interval_dataset_torsion <- append(laidl_rs_interval_dataset_torsion,laidl_rs_data[i,5])
}
laidl_rs_interval_dataset_PC1= vector()
for (i in interval_list_index){
  laidl_rs_interval_dataset_PC1 <- append(laidl_rs_interval_dataset_PC1,laidl_rs_data[i,6])
}
laidl_rs_interval_dataset_PC2= vector()
for (i in interval_list_index){
  laidl_rs_interval_dataset_PC2 <- append(laidl_rs_interval_dataset_PC2,laidl_rs_data[i,7])
}
laidl_rs_interval_dataset_PC3= vector()
for (i in interval_list_index){
  laidl_rs_interval_dataset_PC3 <- append(laidl_rs_interval_dataset_PC3,laidl_rs_data[i,8])
}
plot(laidl_rs_interval_dataset_ontogeny_axis,laidl_rs_interval_dataset_perimeter)
plot(laidl_rs_interval_dataset_ontogeny_axis,laidl_rs_interval_dataset_curvature)
plot(laidl_rs_interval_dataset_ontogeny_axis,laidl_rs_interval_dataset_torsion)
plot(laidl_rs_interval_dataset_ontogeny_axis,laidl_rs_interval_dataset_PC1)
plot(laidl_rs_interval_dataset_ontogeny_axis,laidl_rs_interval_dataset_PC2)
plot(laidl_rs_interval_dataset_ontogeny_axis,laidl_rs_interval_dataset_PC3)
##
vermic_2X_data <- Final_data_output[3529:4068,]
interval <- (max(vermic_2X_data[,3])-min(vermic_2X_data[,3]))/49
interval_list = min(vermic_2X_data[,3])
each_inverval = min(vermic_2X_data[,3])
while(each_inverval < (max(vermic_2X_data[,3])-interval)){ 
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(vermic_2X_data[,3]-i)==min(abs(vermic_2X_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
vermic_2X_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  vermic_2X_interval_dataset_perimeter <- append(vermic_2X_interval_dataset_perimeter,vermic_2X_data[i,9])
}
vermic_2X_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  vermic_2X_interval_dataset_ontogeny_axis <- append(vermic_2X_interval_dataset_ontogeny_axis,vermic_2X_data[i,3])
}
vermic_2X_interval_dataset_curvature= vector()
for (i in interval_list_index){
  vermic_2X_interval_dataset_curvature <- append(vermic_2X_interval_dataset_curvature,vermic_2X_data[i,4])
}
vermic_2X_interval_dataset_torsion= vector()
for (i in interval_list_index){
  vermic_2X_interval_dataset_torsion <- append(vermic_2X_interval_dataset_torsion,vermic_2X_data[i,5])
}
vermic_2X_interval_dataset_PC1= vector()
for (i in interval_list_index){
  vermic_2X_interval_dataset_PC1 <- append(vermic_2X_interval_dataset_PC1,vermic_2X_data[i,6])
}
vermic_2X_interval_dataset_PC2= vector()
for (i in interval_list_index){
  vermic_2X_interval_dataset_PC2 <- append(vermic_2X_interval_dataset_PC2,vermic_2X_data[i,7])
}
vermic_2X_interval_dataset_PC3= vector()
for (i in interval_list_index){
  vermic_2X_interval_dataset_PC3 <- append(vermic_2X_interval_dataset_PC3,vermic_2X_data[i,8])
}
plot(vermic_2X_interval_dataset_ontogeny_axis,vermic_2X_interval_dataset_perimeter)
plot(vermic_2X_interval_dataset_ontogeny_axis,vermic_2X_interval_dataset_curvature)
plot(vermic_2X_interval_dataset_ontogeny_axis,vermic_2X_interval_dataset_torsion)
plot(vermic_2X_interval_dataset_ontogeny_axis,vermic_2X_interval_dataset_PC1)
plot(vermic_2X_interval_dataset_ontogeny_axis,vermic_2X_interval_dataset_PC2)
plot(vermic_2X_interval_dataset_ontogeny_axis,vermic_2X_interval_dataset_PC3)
##
chris_ob_data <- Final_data_output[4069:4828,]
interval <- (max(chris_ob_data[,3])-min(chris_ob_data[,3]))/49
interval_list = min(chris_ob_data[,3])
each_inverval = min(chris_ob_data[,3])
while(each_inverval < (max(chris_ob_data[,3]))){
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(chris_ob_data[,3]-i)==min(abs(chris_ob_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
chris_ob_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  chris_ob_interval_dataset_perimeter <- append(chris_ob_interval_dataset_perimeter,chris_ob_data[i,9])
}
chris_ob_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  chris_ob_interval_dataset_ontogeny_axis <- append(chris_ob_interval_dataset_ontogeny_axis,chris_ob_data[i,3])
}
chris_ob_interval_dataset_curvature= vector()
for (i in interval_list_index){
  chris_ob_interval_dataset_curvature <- append(chris_ob_interval_dataset_curvature,chris_ob_data[i,4])
}
chris_ob_interval_dataset_torsion= vector()
for (i in interval_list_index){
  chris_ob_interval_dataset_torsion <- append(chris_ob_interval_dataset_torsion,chris_ob_data[i,5])
}
chris_ob_interval_dataset_PC1= vector()
for (i in interval_list_index){
  chris_ob_interval_dataset_PC1 <- append(chris_ob_interval_dataset_PC1,chris_ob_data[i,6])
}
chris_ob_interval_dataset_PC2= vector()
for (i in interval_list_index){
  chris_ob_interval_dataset_PC2 <- append(chris_ob_interval_dataset_PC2,chris_ob_data[i,7])
}
chris_ob_interval_dataset_PC3= vector()
for (i in interval_list_index){
  chris_ob_interval_dataset_PC3 <- append(chris_ob_interval_dataset_PC3,chris_ob_data[i,8])
}
plot(chris_ob_interval_dataset_ontogeny_axis,chris_ob_interval_dataset_perimeter)
plot(chris_ob_interval_dataset_ontogeny_axis,chris_ob_interval_dataset_curvature)
plot(chris_ob_interval_dataset_ontogeny_axis,chris_ob_interval_dataset_torsion)
plot(chris_ob_interval_dataset_ontogeny_axis,chris_ob_interval_dataset_PC1)
plot(chris_ob_interval_dataset_ontogeny_axis,chris_ob_interval_dataset_PC2)
plot(chris_ob_interval_dataset_ontogeny_axis,chris_ob_interval_dataset_PC3)
##
chris_de_data <- Final_data_output[4829:5588,]
interval <- (max(chris_de_data[,3])-min(chris_de_data[,3]))/49
interval_list = min(chris_de_data[,3])
each_inverval = min(chris_de_data[,3])
while(each_inverval < (max(chris_de_data[,3])-interval)){ 
  #print(each_inverval)
  each_inverval <- each_inverval+interval 
  interval_list <- append(interval_list,each_inverval) 
}
interval_list
interval_list_index <- vector()
for (i in interval_list) {
  index = which(abs(chris_de_data[,3]-i)==min(abs(chris_de_data[,3]-i)))
  interval_list_index <- append(interval_list_index,index) 
}
chris_de_interval_dataset_perimeter = vector()
for (i in interval_list_index){
  chris_de_interval_dataset_perimeter <- append(chris_de_interval_dataset_perimeter,chris_de_data[i,9])
}
chris_de_interval_dataset_ontogeny_axis = vector()
for (i in interval_list_index){
  chris_de_interval_dataset_ontogeny_axis <- append(chris_de_interval_dataset_ontogeny_axis,chris_de_data[i,3])
}
chris_de_interval_dataset_curvature= vector()
for (i in interval_list_index){
  chris_de_interval_dataset_curvature <- append(chris_de_interval_dataset_curvature,chris_de_data[i,4])
}
chris_de_interval_dataset_torsion= vector()
for (i in interval_list_index){
  chris_de_interval_dataset_torsion <- append(chris_de_interval_dataset_torsion,chris_de_data[i,5])
}
chris_de_interval_dataset_PC1= vector()
for (i in interval_list_index){
  chris_de_interval_dataset_PC1 <- append(chris_de_interval_dataset_PC1,chris_de_data[i,6])
}
chris_de_interval_dataset_PC2= vector()
for (i in interval_list_index){
  chris_de_interval_dataset_PC2 <- append(chris_de_interval_dataset_PC2,chris_de_data[i,7])
}
chris_de_interval_dataset_PC3= vector()
for (i in interval_list_index){
  chris_de_interval_dataset_PC3 <- append(chris_de_interval_dataset_PC3,chris_de_data[i,8])
}
plot(chris_de_interval_dataset_ontogeny_axis,chris_de_interval_dataset_perimeter)
plot(chris_de_interval_dataset_ontogeny_axis,chris_de_interval_dataset_curvature)
plot(chris_de_interval_dataset_ontogeny_axis,chris_de_interval_dataset_torsion)
plot(chris_de_interval_dataset_ontogeny_axis,chris_de_interval_dataset_PC1)
plot(chris_de_interval_dataset_ontogeny_axis,chris_de_interval_dataset_PC2)
plot(chris_de_interval_dataset_ontogeny_axis,chris_de_interval_dataset_PC3)
##
    ########################################
    # Permutation Distribution Clustering----
    ########################################
library("abind")
## for curvature, torsion and aperture size & aperture shape PC scores
all_species_interval_dataset_curvature<-data.frame(christae_interval_dataset_curvature,crassipupa_interval_dataset_curvature,laidlawi_interval_dataset_curvature,vermiculum_interval_dataset_curvature,laidl_rs_interval_dataset_curvature,vermic_2X_interval_dataset_curvature,chris_ob_interval_dataset_curvature,chris_de_interval_dataset_curvature)
all_species_interval_dataset_torsion<-data.frame(christae_interval_dataset_torsion,crassipupa_interval_dataset_torsion,laidlawi_interval_dataset_torsion,vermiculum_interval_dataset_torsion,laidl_rs_interval_dataset_torsion,vermic_2X_interval_dataset_torsion,chris_ob_interval_dataset_torsion,chris_de_interval_dataset_torsion)
all_species_interval_dataset_perimeter<-data.frame(christae_interval_dataset_perimeter,crassipupa_interval_dataset_perimeter,laidlawi_interval_dataset_perimeter,vermiculum_interval_dataset_perimeter,laidl_rs_interval_dataset_perimeter,vermic_2X_interval_dataset_perimeter,chris_ob_interval_dataset_perimeter,chris_de_interval_dataset_perimeter)
all_species_interval_dataset_PC1<-data.frame(christae_interval_dataset_PC1,crassipupa_interval_dataset_PC1,laidlawi_interval_dataset_PC1,vermiculum_interval_dataset_PC1,laidl_rs_interval_dataset_PC1,vermic_2X_interval_dataset_PC1,chris_ob_interval_dataset_PC1,chris_de_interval_dataset_PC1)
all_species_interval_dataset_PC2<-data.frame(christae_interval_dataset_PC2,crassipupa_interval_dataset_PC2,laidlawi_interval_dataset_PC2,vermiculum_interval_dataset_PC2,laidl_rs_interval_dataset_PC2,vermic_2X_interval_dataset_PC2,chris_ob_interval_dataset_PC2,chris_de_interval_dataset_PC2)
all_species_interval_dataset_PC3<-data.frame(christae_interval_dataset_PC3,crassipupa_interval_dataset_PC3,laidlawi_interval_dataset_PC3,vermiculum_interval_dataset_PC3,laidl_rs_interval_dataset_PC3,vermic_2X_interval_dataset_PC3,chris_ob_interval_dataset_PC3,chris_de_interval_dataset_PC3)
all_species_selected_parameters<-abind(all_species_interval_dataset_curvature,all_species_interval_dataset_torsion,all_species_interval_dataset_perimeter,all_species_interval_dataset_PC1,all_species_interval_dataset_PC2,all_species_interval_dataset_PC3, along=3)
dimnames(all_species_selected_parameters) <- NULL
dimnames(all_species_selected_parameters) <- list(c(seq(1,50)), c("christae", "crassipupa", "laidlawi", "vermiculum","laidl_rs","vermic_2X","chris_ob","chris_de"), c("Curvature","Torsion","Aperture size","PC1","PC2","PC3"))  #  change the dim names

## for curvature, torsion, aperture size and PC1
all_species_selected_parameters <-abind(all_species_interval_dataset_curvature,all_species_interval_dataset_torsion,all_species_interval_dataset_perimeter,all_species_interval_dataset_PC1, along=3)
dimnames(all_species_selected_parameters) <- NULL
dimnames(all_species_selected_parameters) <- list(c(seq(1,50)), c("christae", "crassipupa", "laidlawi", "vermiculum","laidl_rs","vermic_2X","chris_ob","chris_de"), c("Curvature","Torsion","Aperture size","PC1"))  #  change the dim names

library("lattice")
library("pdc")
par(mar=c(4, 4, 4, 4),mfrow=c(2, 2))
heuristic <- entropy.heuristic(all_species_selected_parameters,t.min=1, t.max=6 )
plot(heuristic)
clustering_all_species_selected_parameters <- pdclust(all_species_selected_parameters,m = 5, t = 1, divergence =symmetric.alpha.divergence, clustering.method ="single") #("complete","average","single").
#plot(clustering_all_species_selected_parameters, cols=c(rep("red",1),rep("yellow",1), rep("blue",1), rep("green",1), rep("darkgreen",1), rep("darkorange",1), rep("darkred",1)),timeseries.as.labels = T,type="rectangle")
plot(clustering_all_species_selected_parameters, cols=c(rep("red",1),rep("yellow",1), rep("blue",1), rep("green",1), rep("dodgerblue",1), rep("darkgreen",1), rep("darkorange",1), rep("darkred",1)),timeseries.as.labels = T,type="rectangle")
distance_matrix_all_species_selected_parameters <- pdc.dist(all_species_selected_parameters, m = 5, t = 1, divergence = symmetric.alpha.divergence)

distance_matrix_all_species_selected_parameters <- as.matrix(distance_matrix_all_species_selected_parameters)
#dimnames(distance_matrix_all_species_selected_parameters) <- list(c("christae", "crassipupa", "laidlawi", "vermiculum","vermic_2X","chris_ob","chris_de"), c("christae", "crassipupa", "laidlawi", "vermiculum","vermic_2X","chris_ob","chris_de"))
dimnames(distance_matrix_all_species_selected_parameters) <- list(c("christae", "crassipupa", "laidlawi", "vermiculum","laidl_rs","vermic_2X","chris_ob","chris_de"), c("christae", "crassipupa", "laidlawi", "vermiculum","laidl_rs","vermic_2X","chris_ob","chris_de"))

