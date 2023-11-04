import requests
import sqlite3
import contextlib
import os

db_file = "./Astro/S06/GLARE.db"



if os.path.isfile("./Astro/S06/data.txt") == False:
    with open("./Astro/S06/data.txt","w") as f:
        f.write(str(requests.get("http://glade.elte.hu/GLADE_2.4.txt").content)[2:])
        lines = f.readline()
else:
    with open("./Astro/S06/data.txt","r") as f:
        lines = f.readline()
lines = lines.split("\\n")


sql_maketable = f"create table GLARE(gnumber integer primary key, npgc integer, gwgc_name text, leda_name text, mass_name text, wise_name text, sdss_name text, flag text, ra real, dec real, b real, b_err real, b_flag integer, b_abs real, j real, j_err real, h real, h_err real, k real, k_err real, w1 real, w1_err real, w2 real, w2_err real, w1_flag integer, b_j real, b_j_err real, z_helio real, z_cmb real, z_flag integer, v_err real, z_err real, d_l real, d_l_err real, dist_flag integer, mstar real, mstar_err real, mstar_flag integer, merger_rate real, mereger_rate_err real)"
with contextlib.closing(sqlite3.connect(db_file)) as conn :
    cursor = conn.cursor()
    if os.path.isfile("./Astro/S06/GLARE.db") == False:
        cursor.execute(sql_maketable) 
    
    for line in lines:
        line = line.split()
        try:
            gnumber = int(line[0])
        except:
            continue
        try:
            npgc = int(line[1])
        except:
            npgc = 9999999999999999
        try:
            gwgc_name = line[2]
        except:
            gwgc_name = "null"
        try:
            leda_name = line[3]
        except:
            leda_name = "null"
        try:
            mass_name = line[4]
        except:
            mass_name = "null"
        try:
            wise_name = line[5]
        except:
            wise_name = "null"
        try:
            sdss_name = line[6]
        except:
            sdss_name = "null"             
        try:
            flag = line[7]
        except:
            flag = "null"
        try:
            ra = float(line[8])
        except:
            ra = 9999999999999999.99
        try:
            dec = float(line[9])
        except:
            dec = 9999999999999999.99
        try:
            b = float(line[10])
        except:
            b = 9999999999999999.99
        try:
            b_real = float(line[11])
        except:
            b_real = 9999999999999999.99
        try:
            b_err = float(line[12])
        except:
            b_err = 9999999999999999.99
        try:
            b_flag = int(line[13])
        except:
            b_flag = 9999999999999999
        try:
            b_abs = float(line[14])
        except:
            b_abs = 9999999999999999.99
        try:
            j = float(line[15])
        except:
            j = 9999999999999999.99
        try:
            j_err = float(line[16])
        except:
            j_err = 9999999999999999.99
        try:
            h = float(line[17])
        except:
            h = 9999999999999999.99
        try:
            h_err = float(line[18])
        except:
            h_err = 9999999999999999.99
        try:
            k = float(line[19])
        except:
            k = 9999999999999999.99
        try:
            k_err = float(line[20])
        except:
            k_err = 9999999999999999.99
        try:
            w1 = float(line[21])
        except:
            w1 = 9999999999999999.99
        try:
            w1_err = float(line[22])
        except:
            w1_err = 9999999999999999.99
        try:
            w2 = float(line[23])
        except:
            w2 = 9999999999999999.99
        try:
            w2_err = float(line[24])
        except:
            w2_err = 9999999999999999.99
        try:
            w1_flag = int(line[25])
        except:
            w1_flag = 9999999999999
        try:
            b_j = float(line[26])
        except:
            b_j = 9999999999999999.99
        try:
            b_j_err = float(line[27])
        except:
            b_j_err = 9999999999999999.99
        try:
            z_helio = float(line[28])
        except:
            z_helio = 9999999999999999.99
        try:
            z_cmb = float(line[29])
        except:
            z_cmb = 9999999999999999.99
        try:
            z_flag = int(line[30])
        except:
            z_flag = 9999999999999999
        try:
            v_err = float(line[31])
        except:
            v_err = 9999999999999999.99
        try:
            z_err = float(line[32])
        except:
            z_err = 9999999999999999.99
        try:
            d_l = float(line[33])
        except:
            d_l = 9999999999999999.99
        try:
            d_l_err = float(line[34])
        except:
            d_l_err = 9999999999999999.99
        try:
            dist_flag = int(line[35])
        except:
            dist_flag = 9999999999999999
        try:
            mstar = float(line[36])
        except:
            mstar = 9999999999999999.99
        try:
            mstar_err = float(line[37])
        except:
            mstar_err = 9999999999999999.99
        try:
            mstar_flag = int(line[38])
        except:
            mstar_flag = 9999999999999999
        try:
            merger_rate = float(line[39])
        except:
            merger_rate = 9999999999999999.99
        try:
            merger_rate_err = float(line[40])
        except:
            merger_rate_err = 9999999999999999.99
        
        sql_adddata = f"insert into GLARE values({gnumber},{npgc},'{gwgc_name}','{leda_name}','{mass_name}','{wise_name}','{sdss_name}','{flag}',{ra},{dec},{b},{b_err},{b_flag},{b_abs},{j},{j_err},{h},{h_err},{k},{k_err},{w1},{w1_err},{w2},{w2_err},{w1_flag},{b_j},{b_j_err},{z_helio},{z_cmb},{z_flag},{v_err},{z_err},{d_l},{d_l_err},{dist_flag},{mstar},{mstar_err},{mstar_flag},{merger_rate},{merger_rate_err})"

        cursor.execute(sql_adddata)

    conn.commit()
        
        