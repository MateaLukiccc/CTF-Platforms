from hashlib import md5
from hashlib import md5

mainalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.'
alphalen = len(mainalphabet)


def affine(a, b, outlen):
    tmpout = ''
    for i in range(outlen):
        tmpout += mainalphabet[((a*i+b)%outlen)]
    return tmpout

encryptedstr = 'BOHHIKBI,OZ,REI,WZRIKZIR,EX.,BOHI,RO,KISU,XSHO.R,ICBSG.WYISU,OZ, WZXZBWXS,WZ.RWRGRWOZ.,.IKYWZP,X.RKG.RIT,REWKT,DXKRWI.,RO,DKOBI..,ISIBRKOZWB,DXUHIZR.F,NEWSI,REI,.U.RIH,NOKA.,NISS,IZOGPE, OKHO.R,RKXZ.XBRWOZ.Q,WR,.RWSS,.G  IK., KOH,REI,WZEIKIZR,NIXAZI..I.,O ,REI,RKG.R,MX.IT,HOTISF,BOHDSIRISU,ZOZKIYIK.WMSI,RKXZ.XBRWOZ.,XKI,ZOR,KIXSSU,DO..WMSIQ,.WZBI, WZXZBWXS,WZ.RWRGRWOZ.,BXZZORXYOWT,HITWXRWZP,TW.DGRI.F,REI,BO.R,O ,HITWXRWOZ,WZBKIX.I.,RKXZ.XBRWOZ,BO.R.Q,SWHWRWZP,REIHWZWHGH,DKXBRWBXS,RKXZ.XBRWOZ,.WJI,XZT,BGRRWZP,O  ,REI,DO..WMWSWRU, OK,.HXSS,BX.GXS,RKXZ.XBRWOZ.QXZT,REIKI,W.,X,MKOXTIK,BO.R,WZ,REI,SO..,O ,XMWSWRU,RO,HXAI,ZOZKIYIK.WMSI,DXUHIZR., OK,ZOZKIYIK.WMSI.IKYWBI.F,NWRE,REI,DO..WMWSWRU,O ,KIYIK.XSQ,REI,ZIIT, OK,RKG.R,.DKIXT.F,HIKBEXZR.,HG.RMI,NXKU,O ,REIWK,BG.ROHIK.Q,EX..SWZP,REIH, OK,HOKI,WZ OKHXRWOZ,REXZ,REIU,NOGST,OREIKNW.I,ZIITF,X,BIKRXWZ,DIKBIZRXPI,O , KXGT,W.,XBBIDRIT,X.,GZXYOWTXMSIF,REI.I,BO.R.,XZT,DXUHIZR,GZBIKRXWZRWI.BXZ,MI,XYOWTIT,WZ,DIK.OZ,MU,G.WZP,DEU.WBXS,BGKKIZBUQ,MGR,ZO,HIBEXZW.H,ICW.R.,RO,HXAI,DXUHIZR.OYIK,X,BOHHGZWBXRWOZ.,BEXZZIS,NWREOGR,X,RKG.RIT,DXKRUF'

for a in range(1, alphalen):
    for b in range(1, alphalen):
        encalphabet = affine(a, b, alphalen)
        tmpout = ''
        for c in encryptedstr:
            tmpout += mainalphabet[encalphabet.index(c)]
        theval = tmpout.find("THE")
        andval = tmpout.find("AND")
        if (theval >= 0) and (andval >= 0):
            print ("Possible outcome: A, B", a, b, md5(tmpout.encode()).hexdigest())
