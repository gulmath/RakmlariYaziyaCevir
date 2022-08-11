import re
Text =[["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"],
       ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]]
def parcaal(s,bas,bit):
	i=0
	k=""
	for a in s:
		i=i+1
		if i>=bas:
			if i<=bit:
				k=k+a
			else:
				break
	return k
def parca(s,bas,adt):
	i=0
	k=""
	j=0
	for a in s:
		i=i+1
		if i>=bas:
			k=k+a
			j=j+1
			if j==adt:
			    break
	return k
	
def Oku(Deg):
    B1=""
    B2=""
    P=""
    if len(Deg)==3:
        B1 = Text[0][int(parca(Deg, 3, 1))]
        B2 = Text[1][int(parca(Deg, 2, 1))]
        P = Text[0][int(parca(Deg, 1, 1))]
        if P!="":
            if int(parca(Deg, 1, 1))>1:
                ok=P+"Yüz"+B2+B1
            elif int(parca(Deg, 1, 1))==1:
                ok="Yüz"+B2+B1
        else:
            ok=B2+B1
    elif len(Deg)==2:
        B2 = Text[0][int(parca(Deg, 2, 1))]
        P = Text[1][int(parca(Deg, 1, 1))]
        ok=P+B2
    else:
        P = Text[1][int(parca(Deg, 1, 1))]
        ok=P
    return ok

def degistir(s,neyi,neyle):
    k=""
    for i in s:
        if i==neyi:
            k=k+neyle
        else:
            k=k+i
    return k

def Yaziyla(Number):
    Sy=""
    Syt=""
    S=""
    t=""

    #if int(Number)<=0:
    #    return ""
    # S= FormatFloat('0',int(Number))
    # a="1.600,42"
    S=degistir(degistir(Number,".",""),",",".")
    S='000000000000000' + S
    krs=S.split(".")[1]
    Sy=S.split(".")[0]
    syt=""
    bol0=parca(Sy,len(Sy)-2,3)
    bol1=parca(Sy,len(Sy)-5,3)
    bol2=parca(Sy,len(Sy)-8,3)
    bol3=parca(Sy,len(Sy)-11,3)
    bol4=parca(Sy,len(Sy)-14,3)
    if Oku(krs)!="":
        syt=Oku(krs)+"Kuruş"
    if Oku(bol0)!="":
        syt=Oku(bol0)+"TL "+syt
    if Oku(bol1)!="":
        if int(bol1)==1:
            syt="Bin"+syt
        else:
            syt=Oku(bol1)+"Bin"+syt
    if Oku(bol2)!="":
        syt=Oku(bol2)+"Milyon"+syt
    if Oku(bol3)!="":
        syt=Oku(bol3)+"Milyar"+syt
    if Oku(bol4)!="":
        syt=Oku(bol4)+"Trilyon"+syt
    
    return syt

sayi = input("Sayı Girin: ")
print(Yaziyla(sayi))
