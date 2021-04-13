""" l1=["H201","KH40","KH40","KH40","CKH60","SJ35","TS10","MG35","TS25","TS25","S601","J601","C601","MA60","M601",
                    "WTK500","BI40","MSS1","LSS1","KSS1","KVS1","RSS1","VSS1","SCS1","KES1","SSS1"
                    ,"BSS1","MT30","M451","K1A1","G1A1","S901","CHCH","MCH250","CH250","MCH500","CH500","FK250","KDC250","M250","CC250","SC250","CH50C","00NP40","00BS40","00PC40"
                    ,"KEW1","SO20","CR10","CR15","00SB40","00MD40"]
l2=["hing","JEERA KHARI","Masala khari","WHEAT KHARI","CHEESE KHARI","SURTI JEERA BUTTER","FRUIT TOAST","MULTI GRAIN TOAST","FRUIT TOAST200G","JEERA TOAST",
                    "SADA KHAKRA","JEERA KHAKRA","CHAT MASALA KHAKRA","MASALA KHAKRA","METHI KHAKHRA","WT KACHARYU","COOKIES"
                    ,"MASALA SODA","LEMON SHARBAT","KALA KHATTA","KALI DRAKSH","ROYAL ROSE","REAL VARIYALI","SAHI COOL",
    "KESAR ELAICHI","STRAWBERRY","BUTTER SCOTCH","TEA MASALA","BUTTER MILK MASALA","RAW MANGO PICKLE","GOR KERI PICKLE","SUTH PWD","CHAMACPRASH","MSL CHK PAPAD","CHK PAPAD","MSL CHK PAPAD500G","CHK PAPAD500G",
    "KHAJUR PAK","DRY FRUIT CHIKKI","MAVA CHIKKI","CHOCO CHIKKI","SINGH CHIKKI","CHAKKRI","NYLON PHOA CHIVDA","BHEL SEV","POHA CHEVDO","KELA WAFER","SOYA STICK","CREAM ROLL","CREAM ROLL 15","SING BHAJIYA","MUNG DAL"]
l3=[20,40,40,40,60,35,10,40,30,30,70,70,70,70,70,100,40,110,120,110,175,120,120,150,110,110,110,65,45,55,55,130,150,30,30,50,50,135,160,55,55,50,50,40,40,40,20,20,10,15,40,40]
print(len(l1),len(l2),len(l3))
#('ssd', 'sfs', '1'), ('sdf', 'sds', '3')
for i in range(len(l1)):
    print("(","'",l1[i],"','",l2[i],"',",l3[i],"),") """
import mysql.connector
d=mysql.connector.connect(
    host="sql109.epizy.com",
    user="epiz_28050905",
    password="krupal@amba"
)
mycursor=d.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)