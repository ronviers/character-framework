#################################################################
#  Python scripts for aperture form analysis in Blender         #
#                                                               #
#  Author: Liew Thor-Seng                                       #
#  Date: 06 Nov 2013; Time: 1510hrs                             #
#                                                               #
#                                                               #
#                                                               #
#################################################################

len(bpy.context.active_object.data.vertices)/64

###################
#                 #
# Import mmodules #
#                 #
###################
import bpy
import math
import os
import array
import mathutils


#################################################################################################
#                                                                                               #
# Defining the number of points of each aperture and total number of point along ontogeny axis  #
#                                                                                               #
# * Parameter: number_of_points_for_each_aperture                                               #
#                                                                                               #
#################################################################################################

number_of_points_for_each_aperture = 64
Total_number_of_points_of_3Dmodel = len(bpy.context.active_object.data.vertices)
Total_number_of_points_of_3Dmodel
number_of_points_for_ontogeny_axis = int(Total_number_of_points_of_3Dmodel/number_of_points_for_each_aperture)
number_of_points_for_ontogeny_axis
list_of_ontogeny_axis_points = []
First_point_of_aperture = 0

while First_point_of_aperture < Total_number_of_points_of_3Dmodel:
    coordinate_for_first_points_of_aperture = bpy.context.active_object.data.vertices[First_point_of_aperture].co
    list_of_ontogeny_axis_points.append(coordinate_for_first_points_of_aperture)
    First_point_of_aperture += number_of_points_for_each_aperture


#########################################################################
#                                                                       #
# Select the retopologised shell and run analysis of apertures size     #
#                                                                       #
#########################################################################
Aperture_outline = bpy.context.active_object.data
total_number_of_points_in_mesh = len(Aperture_outline.vertices)
first_points_for_each_aperture_outlines=0
last_points_for_each_aperture_outlines=number_of_points_for_each_aperture
all_apertures_size = []
all_aperture_EFA =[]
all_aperture_NEFA =[]


#########################################################################
#                                                                       #
# Algorithm for Elliptical Fourier analysis and perimeter of Apertures	#
#                                                                       #
# *Parameter: no_of_harmonics                                           #
#                                                                       #
# **  Looping could not be performed (any suggestion are welcomed)      #
# *** Copy paste this script to the python console until the            #
#     ">>> last_points_for_each_aperture_outlines" is equal to          #
#     ">>> total_number_of_points_in_mesh".                             #
#                                                                       #
#########################################################################
while last_points_for_each_aperture_outlines <= total_number_of_points_in_mesh:
    Aperture_outline_vertices = Aperture_outline.vertices[first_points_for_each_aperture_outlines:last_points_for_each_aperture_outlines]
    points_of_curve = Aperture_outline_vertices
    no_of_points = len(Aperture_outline_vertices)
    name = bpy.context.active_object.name
    Aperture_ID = name + "," + str(first_points_for_each_aperture_outlines)
    print(Aperture_ID)
    x_coord_mesh = []
    y_coord_mesh = []
    z_coord_mesh = []
    for each_point in list(range(first_points_for_each_aperture_outlines,last_points_for_each_aperture_outlines)):
        x_coord_mesh.append(Aperture_outline.vertices[each_point].co[0])
        y_coord_mesh.append(Aperture_outline.vertices[each_point].co[1])
        z_coord_mesh.append(Aperture_outline.vertices[each_point].co[2])
    p=len(x_coord_mesh)
    no_of_harmonics=5
    i=0
    Dx_list=[]
    Dy_list=[]
    Dz_list=[]
    Dt_list=[]
    firstandlast_x=x_coord_mesh[0]-x_coord_mesh[-1]
    Dx_list.append(firstandlast_x)
    firstandlast_y=y_coord_mesh[0]-y_coord_mesh[-1]
    Dy_list.append(firstandlast_y)
    firstandlast_z=z_coord_mesh[0]-z_coord_mesh[-1]
    Dz_list.append(firstandlast_z)
    firstandlast_t=sqrt(firstandlast_x**2 + firstandlast_y**2 +firstandlast_z**2)
    Dt_list.append(firstandlast_t)
    while i <= (p-2):
        Dx=x_coord_mesh[i+1]-x_coord_mesh[i]
        Dx_list.append(Dx)
        Dy=y_coord_mesh[i+1]-y_coord_mesh[i]
        Dy_list.append(Dy)
        Dz=z_coord_mesh[i+1]-z_coord_mesh[i]
        Dz_list.append(Dz)
        Dt= sqrt(Dx**2 + Dy**2 + Dz**2)
        Dt_list.append(Dt)
        i +=1
    cumsum_i = 0
    cumsum_list = []
    for each_Dt in Dt_list:
        if Dt_list.index((Dt_list[-1])) != -1:
            cumsum_i += each_Dt
            cumsum_list.append(cumsum_i)
    t1 = cumsum_list
    t1m1_temp=[float(0)] 
    t1m1_temp1=t1m1_temp + t1
    t1m1=t1m1_temp1[:-1]
    T = sum(Dt_list)
    temp_output0=[]
    list_of_points = list(range(p))
    list_of_harmonic = list(range(1,(no_of_harmonics+1)))
    harmonics_an=[]
    harmonics_bn=[]
    harmonics_cn=[]
    harmonics_dn=[]
    harmonics_en=[]
    harmonics_fn=[]
    for each_harmonic in list_of_harmonic:
        temp_output0=0
        for each_point in list_of_points:
            a=(Dx_list[each_point]/Dt_list[each_point]) * ((cos (2 * each_harmonic * pi * (t1[each_point]) / T)) -(cos (2 * pi * each_harmonic * (t1m1[each_point]) / T)))
            temp_output0 +=a
        an = (T/(2 * pi**2 * each_harmonic**2)) * temp_output0
        harmonics_an.append(an)
    for each_harmonic in list_of_harmonic:
        temp_output0=0
        for each_point in list_of_points:
            b=(Dx_list[each_point]/Dt_list[each_point]) * ((sin (2 * each_harmonic * pi * (t1[each_point]) / T)) -(sin (2 * pi * each_harmonic * (t1m1[each_point]) / T)))
            temp_output0 +=b
        bn = (T/(2 * pi**2 * each_harmonic**2)) * temp_output0
        harmonics_bn.append(bn)
    for each_harmonic in list_of_harmonic:
        temp_output0=0
        for each_point in list_of_points:
            c=(Dy_list[each_point]/Dt_list[each_point]) * ((cos (2 * each_harmonic * pi * (t1[each_point]) / T)) -(cos (2 * pi * each_harmonic * (t1m1[each_point]) / T)))
            temp_output0 +=c
        cn = (T/(2 * pi**2 * each_harmonic**2)) * temp_output0
        harmonics_cn.append(cn)
    for each_harmonic in list_of_harmonic:
        temp_output0=0
        for each_point in list_of_points:
            d=(Dy_list[each_point]/Dt_list[each_point]) * ((sin (2 * each_harmonic * pi * (t1[each_point]) / T)) -(sin (2 * pi * each_harmonic * (t1m1[each_point]) / T)))
            temp_output0 +=d
        dn = (T/(2 * pi**2 * each_harmonic**2)) * temp_output0
        harmonics_dn.append(dn)
    for each_harmonic in list_of_harmonic:
        temp_output0=0
        for each_point in list_of_points:
            e=(Dz_list[each_point]/Dt_list[each_point]) * ((cos (2 * each_harmonic * pi * (t1[each_point]) / T)) -(cos (2 * pi * each_harmonic * (t1m1[each_point]) / T)))
            temp_output0 +=e
        en = (T/(2 * pi**2 * each_harmonic**2)) * temp_output0
        harmonics_en.append(en)
    for each_harmonic in list_of_harmonic:
        temp_output0=0
        for each_point in list_of_points:
            f=(Dz_list[each_point]/Dt_list[each_point]) * ((sin (2 * each_harmonic * pi * (t1[each_point]) / T)) -(sin (2 * pi * each_harmonic * (t1m1[each_point]) / T)))
            temp_output0 +=f
        fn = (T/(2 * pi**2 * each_harmonic**2)) * temp_output0
        harmonics_fn.append(fn)
    temp_ao=0
    for each_point in list_of_points:
        temp_output0=(x_coord_mesh[each_point]) * ((Dt_list[each_point])/T)
        temp_ao +=temp_output0
    ao=2 * temp_ao
    temp_co=0
    for each_point in list_of_points:
        temp_output0=(y_coord_mesh[each_point]) * ((Dt_list[each_point])/T)
        temp_co +=temp_output0
    co=2 * temp_co
    temp_eo=0
    for each_point in list_of_points:
        temp_output0=(z_coord_mesh[each_point]) * ((Dt_list[each_point])/T)
        temp_eo +=temp_output0
    eo=2 * temp_eo
    harmonics_an
    harmonics_bn
    harmonics_cn
    harmonics_dn
    harmonics_en
    harmonics_fn
    ao
    co
    eo
    combine_output=[Aperture_ID,harmonics_an,harmonics_bn,harmonics_cn,harmonics_dn,harmonics_en,harmonics_fn,ao,co,eo]
    combine_output
    all_aperture_EFA.append(combine_output)
    normalised_harmonics_all = []
    all_outline = []
    Output_raw_EFA = '' #silent this after used for the first time
    Output_normal_EFA = '' #silent this after used for the first time
    ##Step 8 - normalisation of harmonics from EFA analysis
    ##(Parameter= k as no_of_harmonics; choose normalization factor: scale, O_inverted, and direction_of_motion)
    ####Script L - Normalization of harmonics from Elliptic fourier Analysis
    k=no_of_harmonics ##see C) EFA analysis
    harmonics_value_index=list(range(k))
    ##Scaling
    psi = (1/2) * atan(2 * ((harmonics_an[0] * harmonics_bn[0]) + (harmonics_cn[0] * harmonics_dn[0]) + (harmonics_en[0] * harmonics_fn[0])) / (harmonics_bn[0]**2 + harmonics_dn[0]**2 + harmonics_fn[0]**2 - harmonics_an[0]**2 - harmonics_cn[0]**2 - harmonics_en[0]**2))
    a = sqrt (((harmonics_an[0]**2 + harmonics_cn[0]**2 + harmonics_en[0]**2) * cos(psi)**2) + ((harmonics_bn[0]**2 + harmonics_dn[0]**2 + harmonics_fn[0]**2) * sin(psi)**2) - (((harmonics_an[0] * harmonics_bn[0]) + (harmonics_cn[0] * harmonics_dn[0]) + (harmonics_en[0] * harmonics_fn[0])) * sin (2 * psi)))
    b = sqrt (((harmonics_an[0]**2 + harmonics_cn[0]**2 + harmonics_en[0]**2) * sin(psi)**2) + ((harmonics_bn[0]**2 + harmonics_dn[0]**2 + harmonics_fn[0]**2) * cos(psi)**2) + (((harmonics_an[0] * harmonics_bn[0]) + (harmonics_cn[0] * harmonics_dn[0]) + (harmonics_en[0] * harmonics_fn[0])) * sin (2 * psi)))
    scale = 1/sqrt(pi * a * b)
    ##Rotation - refered to 1st harmonic
    w = a*b/((harmonics_an[0]*harmonics_fn[0]) - (harmonics_bn[0]*harmonics_en[0]))
    O21 = ((harmonics_cn[0]*cos(psi)) - (harmonics_dn[0]*sin(psi)))/a
    O31 = ((harmonics_en[0]*cos(psi)) - (harmonics_fn[0]*sin(psi)))/a
    O22 = ((harmonics_cn[0]*sin(psi)) + (harmonics_dn[0]*cos(psi)))/b
    O32 = ((harmonics_en[0]*sin(psi)) + (harmonics_fn[0]*cos(psi)))/b
    alpha = ()
    if ((harmonics_an[0]*harmonics_fn[0]) - (harmonics_bn[0]*harmonics_en[0])) > 0:
        alpha = atan(((harmonics_cn[0]*harmonics_fn[0])-(harmonics_dn[0]*harmonics_en[0]))/((harmonics_an[0]*harmonics_fn[0]) - (harmonics_bn[0]*harmonics_en[0])))
    else:
        alpha =(atan(((harmonics_cn[0]*harmonics_fn[0])-(harmonics_dn[0]*harmonics_en[0]))/((harmonics_an[0]*harmonics_fn[0]) - (harmonics_bn[0]*harmonics_en[0])))) + pi
    beta = acos(w*((O21*O31)+(O22*O32)))
    gamma = ()
    if O31 > 0:
        gamma =  acos(O32/sin(beta))
    else:
        gamma = -acos(O32/sin(beta))
    RX_alpha = Matrix (((1,0,0),(0, cos(alpha),-sin(alpha)),(0,sin(alpha),cos(alpha))))
    RX_beta = Matrix (((1,0,0),(0, cos(beta),-sin(beta)),(0,sin(beta),cos(beta))))
    RX_gamma = Matrix (((1,0,0),(0, cos(gamma),-sin(gamma)),(0,sin(gamma),cos(gamma))))
    RY_alpha = Matrix (((cos(alpha),0,sin(alpha)),(0,1,0),(-sin(alpha),0,cos(alpha))))
    RY_beta = Matrix (((cos(beta),0,sin(beta)),(0,1,0),(-sin(beta),0,cos(beta))))
    RY_gamma = Matrix (((cos(gamma),0,sin(gamma)),(0,1,0),(-sin(gamma),0,cos(gamma))))
    RZ_alpha = Matrix (((cos(alpha),-sin(alpha),0),(sin(alpha), cos(alpha),0),(0,0,1)))
    RZ_beta = Matrix (((cos(beta),-sin(beta),0),(sin(beta), cos(beta),0),(0,0,1)))
    RZ_gamma = Matrix (((cos(gamma),-sin(gamma),0),(sin(gamma), cos(gamma),0),(0,0,1)))
    ##O=RX_alpha * RY_beta * RZ_gamma ##x1y2z3
    ##O=RY_alpha * RX_beta * RY_gamma ##y1x2y3
    O=RZ_alpha * RX_beta * RZ_gamma ##z1x2z3
    ##O = Matrix(((((cos(alpha)*cos(gamma)) - (sin(alpha)*cos(beta)*sin(gamma))), ((-cos(alpha)*sin(gamma)) - (sin(alpha)*cos(beta)*cos(gamma))), (sin(alpha)*sin(beta))),(((sin(alpha)*cos(gamma)) + (cos(alpha)*cos(beta)*sin(gamma))), ((-sin(alpha)*sin(gamma)) - (cos(alpha)*cos(beta)*cos(gamma))), (-cos(alpha)*sin(beta))),((sin(beta)*sin(gamma)), (sin(beta)*cos(gamma)),(cos(beta)))))
    O_inverted=O.inverted()
    direction_of_motion = Matrix(((cos(psi),sin(psi)),((-sin(psi),cos(psi)))))
    normalization_factors = scale*O_inverted
    ##convert each haromonic
    normalised_harmonics_an = []
    normalised_harmonics_bn = []
    normalised_harmonics_cn = []
    normalised_harmonics_dn = []
    normalised_harmonics_en = []
    normalised_harmonics_fn = []
    ##normalised_harmonics_all = []
    for each_harmonic in harmonics_value_index:
        the_th_harmonic_matrix = Matrix(((harmonics_an[each_harmonic],harmonics_bn[each_harmonic]),(harmonics_cn[each_harmonic],harmonics_dn[each_harmonic]),(harmonics_en[each_harmonic],harmonics_fn[each_harmonic])))
        the_normalised_th_harmonic=normalization_factors*the_th_harmonic_matrix*direction_of_motion
        normalised_harmonics_an.append((the_normalised_th_harmonic[0])[0])
        normalised_harmonics_bn.append((the_normalised_th_harmonic[0])[1])
        normalised_harmonics_cn.append((the_normalised_th_harmonic[1])[0])
        normalised_harmonics_dn.append((the_normalised_th_harmonic[1])[1])
        normalised_harmonics_en.append((the_normalised_th_harmonic[2])[0])
        normalised_harmonics_fn.append((the_normalised_th_harmonic[2])[1])
        normalised_harmonics_all.append((the_normalised_th_harmonic[0])[0])
        normalised_harmonics_all.append((the_normalised_th_harmonic[0])[1])
        normalised_harmonics_all.append((the_normalised_th_harmonic[1])[0])
        normalised_harmonics_all.append((the_normalised_th_harmonic[1])[1])
        normalised_harmonics_all.append((the_normalised_th_harmonic[2])[0])
        normalised_harmonics_all.append((the_normalised_th_harmonic[2])[1])
    combine_output_N=[Aperture_ID,normalised_harmonics_an, normalised_harmonics_bn, normalised_harmonics_cn, normalised_harmonics_dn, normalised_harmonics_en, normalised_harmonics_fn,ao,co,eo,scale]
    scale    
    combine_output_N
    all_outline.append(name)
    normalised_harmonics_all
    all_outline
    all_aperture_NEFA.append(combine_output_N)
    total_length_between_points=0
    the_distance_between_two_points=0
    length_list=[]
    first_points=0
    while first_points <= (no_of_points-2):
        the_distance_between_two_points=(((points_of_curve[(first_points+1)].co)- (points_of_curve[first_points].co)).length)
        length_list.append(the_distance_between_two_points)
        total_length_between_points +=  the_distance_between_two_points
        first_points +=1
    the_distance_between_1st_lastpoints=(((points_of_curve[0].co)-(points_of_curve[- 1].co)).length)
    total_length_between_points +=  the_distance_between_1st_lastpoints
    total_length_between_points
    each_aperture_data = Aperture_ID,total_length_between_points
    all_apertures_size.append(each_aperture_data)
    Aperture_ID
    first_points_for_each_aperture_outlines
    last_points_for_each_aperture_outlines
    total_number_of_points_in_mesh
    first_points_for_each_aperture_outlines+=number_of_points_for_each_aperture
    last_points_for_each_aperture_outlines+=number_of_points_for_each_aperture


#########################################################################
# 									#
# Reformat the data structure and write and save the data in CSV format	#
#									#
#########################################################################
all_apertures_size.reverse()
all_apertures_size_str = str(all_apertures_size)
all_apertures_size_str_output_temp1 = all_apertures_size_str.replace("), (","\n")
all_apertures_size_str_output_temp2 = all_apertures_size_str_output_temp1.replace("'",'')
all_apertures_size_str_output_temp3 = all_apertures_size_str_output_temp2.replace("[","")
all_apertures_size_str_output_temp4 = all_apertures_size_str_output_temp3.replace("]","")
all_apertures_size_str_output_temp5 = all_apertures_size_str_output_temp4.replace("(","")
all_apertures_size_str_output_final = all_apertures_size_str_output_temp5.replace(")","")

all_aperture_EFA.reverse()
all_aperture_EFA_str = str(all_aperture_EFA)
all_aperture_EFA_str_output_temp1 = all_aperture_EFA_str.replace(", ['","\n")
all_aperture_EFA_str_output_temp2 = all_aperture_EFA_str_output_temp1.replace("'",'')
all_aperture_EFA_str_output_temp3 = all_aperture_EFA_str_output_temp2.replace("[","")
all_aperture_EFA_str_output_temp4 = all_aperture_EFA_str_output_temp3.replace("]","")
all_aperture_EFA_str_output_final = all_aperture_EFA_str_output_temp4.replace(" ","")

all_aperture_NEFA.reverse()
all_aperture_NEFA_str = str(all_aperture_NEFA)
all_aperture_NEFA_str_output_temp1 = all_aperture_NEFA_str.replace(", ['","\n")
all_aperture_NEFA_str_output_temp2 = all_aperture_NEFA_str_output_temp1.replace("'",'')
all_aperture_NEFA_str_output_temp3 = all_aperture_NEFA_str_output_temp2.replace("[","")
all_aperture_NEFA_str_output_temp4 = all_aperture_NEFA_str_output_temp3.replace("]","")
all_aperture_NEFA_str_output_final = all_aperture_NEFA_str_output_temp4.replace(" ","")

##Parameters(newfolderpath)
fp=bpy.data.filepath
filepath=os.path.basename(fp)
Blender_file_name=filepath[:-6]
####newfolderpath="c:/E_19072009/Manuscript/PhD thesis/On growth and form of two heteromorphic terrestrial gastropod snails/3D aperture outline analysis/EFA_blender/"
newfolderpath="c:/E_19072009/abc/"
if not os.path.isdir(newfolderpath):
    os.makedirs(newfolderpath)

outputfile1= newfolderpath+" "+Blender_file_name+ " " + name +" perimeter"+".csv"
outputfile2= newfolderpath+" "+Blender_file_name+ " " + name +" EFA"+".csv"
outputfile3= newfolderpath+" "+Blender_file_name+ " " + name +" NEFA"+".csv"
writefile=open(outputfile1, 'w')
writefile.write("shell,aperture,perimeter\n")
writefile.write(all_apertures_size_str_output_final)
writefile.close()
writefile=open(outputfile2, 'w')
writefile.write("shell,aperture,NEFA_A1,NEFA_A2,NEFA_A3,NEFA_A4,NEFA_A5,NEFA_B1,NEFA_B2,NEFA_B3,NEFA_B4,NEFA_B5,NEFA_C1,NEFA_C2,NEFA_C3,NEFA_C4,NEFA_C5,NEFA_D1,NEFA_D2,NEFA_D3,NEFA_D4,NEFA_D5,NEFA_E1,NEFA_E2,NEFA_E3,NEFA_E4,NEFA_E5,NEFA_F1,NEFA_F2,NEFA_F3,NEFA_F4,NEFA_F5,NEFA_A0,NEFA_C0,NEFA_E0\n")
writefile.write(all_aperture_EFA_str_output_final)
writefile.close()
writefile=open(outputfile3, 'w')
writefile.write("shell,aperture,NEFA_A1,NEFA_A2,NEFA_A3,NEFA_A4,NEFA_A5,NEFA_B1,NEFA_B2,NEFA_B3,NEFA_B4,NEFA_B5,NEFA_C1,NEFA_C2,NEFA_C3,NEFA_C4,NEFA_C5,NEFA_D1,NEFA_D2,NEFA_D3,NEFA_D4,NEFA_D5,NEFA_E1,NEFA_E2,NEFA_E3,NEFA_E4,NEFA_E5,NEFA_F1,NEFA_F2,NEFA_F3,NEFA_F4,NEFA_F5,NEFA_A0,NEFA_C0,NEFA_E0,Scale\n")
writefile.write(all_aperture_NEFA_str_output_final)
writefile.close()



#########################################	
#                                       #
# Algorithm for curvature and torsion   #
#                                       #
# * parameter: q                        #
#                                       #
#########################################
q=70
a1=a2=a3=a4=a5=a6=0
bx1=bx2=bx3=by1=by2=by3=bz1=bz2=bz3=0
l_list=[]
l_list_center =[]
s_list=[]
wi_list=[]
#list_of_curvature = []
#list_of_torsion = []
list_of_curvature_torsion = []
list_of_binormal_B = []
list_of_normal_N = []
list_of_tangent_T = []
windows_frame=[]
li = 0
si = 0
xi = []
yi = []
zi = []
m = 0
ww=1
P=len(list_of_ontogeny_axis_points)
name = bpy.context.active_object.name
Aperture_ID_all = list(range(0,Total_number_of_points_of_3Dmodel,number_of_points_for_each_aperture))
for dummy_h in Aperture_ID_all[:q]:
    Aperture_ID_dummy_head = name + "," + str(dummy_h)
    curvature_and_torsion_dummy_head = Aperture_ID_dummy_head,'NA','NA'
    list_of_curvature_torsion.append(curvature_and_torsion_dummy_head)

for each_P0 in list(range(q,(P-q))):
    windows_frame=[]
    windows_frame = list(range((each_P0-q),(each_P0+q+1)))
    for each_Pi in windows_frame[:-1]:
        si = ((list_of_ontogeny_axis_points[each_Pi+1]) - (list_of_ontogeny_axis_points[each_Pi])).length
        li += si
        l_list.append(li)
        s_list.append(si)
    for each_Pi in windows_frame[1:]:
        xi.append(list_of_ontogeny_axis_points[each_Pi][0])
        yi.append(list_of_ontogeny_axis_points[each_Pi][1])
        zi.append(list_of_ontogeny_axis_points[each_Pi][2])
    m=l_list[q]
    for each_li in l_list:
        l_list_center.append(each_li-m)
    for each_Pi in list(range(q*2)):
        wi_list.append((1/(s_list[each_Pi])))##*((l_list_center[each_Pi])**2))
    for each_i in list(range(2*q)):
        a1 += l_list_center[each_i]**2 * wi_list[each_i]
        a2 += (l_list_center[each_i]**3 * wi_list[each_i])/2
        a3 += (l_list_center[each_i]**4 * wi_list[each_i])/4
        a4 += (l_list_center[each_i]**4 * wi_list[each_i])/6
        a5 += (l_list_center[each_i]**5 * wi_list[each_i])/12
        a6 += (l_list_center[each_i]**6 * wi_list[each_i])/36
        bx1 += wi_list[each_i] * l_list_center[each_i] * (xi[each_i]-list_of_ontogeny_axis_points[each_P0][0])
        bx2 += (wi_list[each_i] * (l_list_center[each_i]**2) * (xi[each_i]-list_of_ontogeny_axis_points[each_P0][0]))/2
        bx3 += (wi_list[each_i] * (l_list_center[each_i]**3) * (xi[each_i]-list_of_ontogeny_axis_points[each_P0][0]))/6
        by1 += wi_list[each_i] * l_list_center[each_i] * (yi[each_i]-list_of_ontogeny_axis_points[each_P0][1])
        by2 += (wi_list[each_i] * (l_list_center[each_i]**2) * (yi[each_i]-list_of_ontogeny_axis_points[each_P0][1]))/2
        by3 += (wi_list[each_i] * (l_list_center[each_i]**3) * (yi[each_i]-list_of_ontogeny_axis_points[each_P0][1]))/6
        bz1 += wi_list[each_i] * l_list_center[each_i] * (zi[each_i]-list_of_ontogeny_axis_points[each_P0][2])
        bz2 += (wi_list[each_i] * (l_list_center[each_i]**2) * (zi[each_i]-list_of_ontogeny_axis_points[each_P0][2]))/2
        bz3 += (wi_list[each_i] * (l_list_center[each_i]**3) * (zi[each_i]-list_of_ontogeny_axis_points[each_P0][2]))/6
    a1_a6_M = Matrix (((a1,a2,a4),(a2,a3,a5),(a4,a5,a6)))
    bx_y_z_M = Matrix (((bx1,by1,bz1),(bx2,by2,bz2),(bx3,by3,bz3)))
    d_dd_xyz_M = (a1_a6_M.inverted())*bx_y_z_M
    Curvature = ((d_dd_xyz_M[0].cross(d_dd_xyz_M[1])).magnitude)/(((d_dd_xyz_M[0]).magnitude)**3)
    Torsion = ((d_dd_xyz_M[0].cross(d_dd_xyz_M[1])).dot(d_dd_xyz_M[2]))/ ((((d_dd_xyz_M[0].cross(d_dd_xyz_M[1])).magnitude))**2)
    tangent_T = d_dd_xyz_M[0] / d_dd_xyz_M[0].magnitude
    normal_N = (d_dd_xyz_M[1] - ((d_dd_xyz_M[1].dot(tangent_T))*tangent_T))/((d_dd_xyz_M[1] - ((d_dd_xyz_M[1].dot(tangent_T))*tangent_T)).magnitude)
    binormal_B = tangent_T.cross(normal_N)
    Curvature
    Torsion
    binormal_B
    normal_N
    tangent_T
    Aperture_ID = name + "," + str(Aperture_ID_all[each_P0])
    curvature_and_torsion = Aperture_ID,Curvature,Torsion
    list_of_curvature_torsion.append(curvature_and_torsion)
    list_of_binormal_B.append(binormal_B)
    list_of_normal_N.append(normal_N)
    list_of_tangent_T.append(tangent_T)
    a1=a2=a3=a4=a5=a6=0
    bx1=bx2=bx3=by1=by2=by3=bz1=bz2=bz3=0
    l_list=[]
    l_list_center =[]
    s_list=[]
    wi_list=[]
    windows_frame=[]
    li = 0
    si = 0
    xi = []
    yi = []
    zi = []
    m = 0

for dummy_e in Aperture_ID_all[-q:]:
    Aperture_ID_dummy_end = name + "," + str(dummy_e)
    curvature_and_torsion_dummy_end = Aperture_ID_dummy_end,'NA','NA'
    list_of_curvature_torsion.append(curvature_and_torsion_dummy_end)

len(list_of_curvature_torsion)
P,q


#################################################
#                                               #
# Algorithm for accumulative length and         # 
# extract x,y,z coordinates for ontogeny axis   #
#                                               #
#################################################
for each_Pi in list(range(P-1)):
    si = (((list_of_ontogeny_axis_points[each_Pi+1])-(list_of_ontogeny_axis_points[each_Pi])).length)
    s_list.append(si)

list_of_accumulative_arclength = [0]
si=0
s_list.reverse()
for each_si in s_list:
    si += each_si
    list_of_accumulative_arclength.append(si)

list_of_ontogeny_axis_points.reverse()
Aperture_ID_all.reverse()
Ontogeny_axis_arclenght_x_y_z = []
for each_Pi in list(range(P)):
    Aperture_ID_ontogenyaxis_x_y_z = (name + "," + str(Aperture_ID_all[each_Pi])),(list_of_accumulative_arclength[each_Pi]),(list_of_ontogeny_axis_points[each_Pi][0]),(list_of_ontogeny_axis_points[each_Pi][1]),(list_of_ontogeny_axis_points[each_Pi][2])
    Ontogeny_axis_arclenght_x_y_z.append(Aperture_ID_ontogenyaxis_x_y_z) 


#########################################################################
#                                                                       #
# Reformat the data structure and write and save the data in CSV format #
#                                                                       #
# *Parameter: newfolderpath                                             #
#                                                                       #
#########################################################################

combined_dataset_ontogenyaxis_curvature_torsion = []
list_of_curvature_torsion.reverse()
for each_dataset in list(range(P)):
    each_combined_dataset = (Ontogeny_axis_arclenght_x_y_z[each_dataset]),(list_of_curvature_torsion[each_dataset])
    combined_dataset_ontogenyaxis_curvature_torsion.append(each_combined_dataset)

combined_dataset_ontogenyaxis_curvature_torsion_str = str(combined_dataset_ontogenyaxis_curvature_torsion)
combined_dataset_ontogenyaxis_curvature_torsion_str_temp1 = combined_dataset_ontogenyaxis_curvature_torsion_str.replace(")), ((","\n")
combined_dataset_ontogenyaxis_curvature_torsion_str_temp2 = combined_dataset_ontogenyaxis_curvature_torsion_str_temp1.replace("'",'')
combined_dataset_ontogenyaxis_curvature_torsion_str_temp3 = combined_dataset_ontogenyaxis_curvature_torsion_str_temp2.replace("[","")
combined_dataset_ontogenyaxis_curvature_torsion_str_temp4 = combined_dataset_ontogenyaxis_curvature_torsion_str_temp3.replace("]","")
combined_dataset_ontogenyaxis_curvature_torsion_str_temp5 = combined_dataset_ontogenyaxis_curvature_torsion_str_temp4.replace("(","")
combined_dataset_ontogenyaxis_curvature_torsion_final = combined_dataset_ontogenyaxis_curvature_torsion_str_temp5.replace(")","")

fp=bpy.data.filepath
filepath=os.path.basename(fp)
Blender_file_name=filepath[:-6]
####newfolderpath="c:/E_19072009/Manuscript/PhD thesis/On growth and form of two heteromorphic terrestrial gastropod snails/3D aperture outline analysis/EFA_blender/"
newfolderpath="c:/E_19072009/abc/"
if not os.path.isdir(newfolderpath):
    os.makedirs(newfolderpath)

outputfile1= newfolderpath+" "+Blender_file_name + " " + name + "_q" + (str(q))+".csv"
writefile=open(outputfile1, 'w')
writefile.write("shell,aperture,ontogeny_axis,x_coordinate,y_coordinate,z_coordinate,shell,aperture,curvature,torsion\n")
writefile.write(combined_dataset_ontogenyaxis_curvature_torsion_final)
writefile.close()
