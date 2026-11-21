"""Calcola tutti i risultati degli esercizi di gravitazione (fonte unica dei numeri)."""
from math import pi, sqrt
G=6.67e-11; MT=5.97e24; RT=6.37e6; g0=9.81; MS=1.99e30; UA=1.50e11
ML=7.35e22; RL=1.74e6; dTL=3.84e8; c=3.00e8; MM=6.42e23; RM=3.39e6
GMT=3.98e14  # valore arrotondato mostrato nelle pagine
def p(k,v): print(f"{k:28s} {v:.4g}")
print("== L1 ==")
p("1 a(T=27y) UA",27**(2/3))
p("2 T Cerere a=2.77",2.77**1.5)
p("3 Europa a km",4.22e5*(3.55/1.77)**(2/3))
a=(0.59+35.1)/2; e=(35.1-0.59)/(35.1+0.59)
p("4 a UA",a); p("4 e",e); p("4 T anni",a**1.5); p("4 c",a-0.59)
p("5 v_af m/s",54.5e3*8.8e10/5.25e12)
p("6 F auto",G*1500*1200/3.0**2)
p("7 fattore",2/9)
p("8 F Sole-Terra",G*MS*MT/UA**2)
p("9 g Marte rapporti",0.107/0.532**2*g0); p("9 rapporto",0.107/0.532**2)
p("10 h=(sqrt2-1)R km",(sqrt(2)-1)*RT/1e3)
p("11 M Venere",8.87*6.05e6**2/G)
V=4/3*pi*RT**3; p("12 V Terra",V); p("12 densita",MT/V)
p("13 F tra Luna e 70kg su Luna g",G*ML*70/RL**2); p("13 gLuna",G*ML/RL**2)
p("14 F satellite h=500km m=850",G*MT*850/(RT+5e5)**2)
print("== L2 ==")
r=RT+8.0e5; v=sqrt(GMT/r); T=2*pi*r/v
p("1 r",r); p("1 v",v); p("1 T s",T); p("1 T min",T/60)
T=7.65*3600; r=9.38e6; p("2 T s",T); p("2 M Marte",4*pi**2*r**3/(G*T**2))
T=88620; r=(G*MM*T**2/(4*pi**2))**(1/3); p("3 r areost",r); p("3 h km",(r-RM)/1e3)
p("3 r^3",G*MM*T**2/(4*pi**2))
h=4.2e5; gh=GMT/(RT+h)**2; p("5 g(420km)",gh); p("5 F 75kg",75*gh); p("5 frazione",gh/g0)
p("6 g a h=2R",g0/9)
x=UA*sqrt(MT/MS)/(1+sqrt(MT/MS)); p("7 x da Terra",x); p("7 sqrt",sqrt(MT/MS)); p("7 frazione d",x/UA)
d=2.0; m1=200; m2=800; p("8 g1",G*m1/1**2); p("8 g2",G*m2/1**2); p("8 tot",G*(m2-m1)/1**2)
p("8 x nullo da m1", d/(1+sqrt(m2/m1)))
p("9 T Luna",1.50*sqrt(g0/1.62))
T=43080; r=(GMT*T**2/(4*pi**2))**(1/3); p("10 r GPS",r); p("10 h km",(r-RT)/1e3); p("10 v",2*pi*r/T)
p("11 M Sole da Terra",4*pi**2*UA**3/(G*(3.156e7)**2))
print("== L3 ==")
r=RT+1.0e6; p("1 U",-GMT*1200/r); p("1 r",r)
p("2 L contro grav",GMT*500/(2*RT))
p("2 mgh (sbagliato)",500*g0*RT)
r=RT+6.0e5; m=900; p("3 r",r); p("3 K",GMT*m/(2*r)); p("3 U",-GMT*m/r); p("3 E",-GMT*m/(2*r))
r1=RT+4.0e5; r2=4.22e7; m=2000; p("4 E1",-GMT*m/(2*r1)); p("4 E2",-GMT*m/(2*r2)); p("4 dE",GMT*m/2*(1/r1-1/r2))
p("5 vf Giove",sqrt(2*G*1.90e27/7.15e7))
rp=7.00e6; ra=2.10e7; vp=sqrt(2*GMT*ra/(rp*(rp+ra))); p("6 vp",vp); vp=9.24e3; p("6 va",vp*rp/ra)
p("6 check E_p/m",0.5*vp**2-GMT/rp); p("6 check E_a/m",0.5*(vp*rp/ra)**2-GMT/ra)
v0=5.0e3; rmax=1/(1/RT-v0**2/(2*GMT)); p("7 rmax",rmax); p("7 hmax km",(rmax-RT)/1e3); p("7 naive km",v0**2/(2*g0)/1e3)
p("8 RS 10 Msole",2*G*10*MS/c**2); p("8 RS Giove",2*G*1.90e27/c**2)
p("9 vf Sole da 1UA",sqrt(2*G*MS/UA)); p("9 v orbitale Terra",sqrt(G*MS/UA))
p("10 vf Terra",sqrt(2*GMT/RT)); p("10 v radente",sqrt(GMT/RT))
p("11 v impatto da h=RT",sqrt(GMT/RT)); 
print("== teoria ==")
p("g(h) 400km",GMT/(RT+4e5)**2); p("ac Luna",4*pi**2*dTL/(27.3*86400)**2)
for nome,a_,T_ in [("Mercurio",0.387,0.241),("Venere",0.723,0.615),("Terra",1,1),("Marte",1.524,1.881),("Giove",5.203,11.86),("Saturno",9.537,29.45)]:
    print(nome,a_**3,T_**2)
print("== verifica ==")
p("9 g Saturno",95.2/9.45**2*g0)
r=RT+2.0e6; v=sqrt(GMT/r); p("10 v",v); p("10 T",2*pi*r/v); p("10 T min",2*pi*r/v/60)
p("11 vf Luna",sqrt(2*G*ML/RL))
r1=RT+3e5; r2=RT+1.3e6; p("12 dE",GMT*1000/2*(1/r1-1/r2)); p("12 1/r1",1/r1); p("12 1/r2",1/r2)
p("12 dE con 3.98e14",3.98e14*1000/2*(1/r1-1/r2))
print("== verifica lunga ==")
from math import atan, degrees, isclose
# B1 biglia su pianeta ignoto
R=3.40e6; h=1.80; t=0.98
g=2*h/t**2; p("B1 g",g); g_r=round(g,2); p("B1 v=g t (g arrot.)",g_r*t); p("B1 M (g arrot.)",g_r*R**2/G)
# B2 sasso lanciato in alto
R=1.56e6; v0=4.0; t=6.2
g=2*v0/t; p("B2 g",g); g_r=round(g,3); p("B2 M",g_r*R**2/G); p("B2 vf",sqrt(2*g_r*R))
# B3 ellisse da perigeo: r_P, v_P -> r_A, v_A, e
rp=6.90e6; vp=8.80e3
eps=0.5*vp**2-GMT/rp; hh=rp*vp
vc=sqrt(GMT/rp); vesc=sqrt(2*GMT/rp); assert vc<vp<vesc
# 1/r_A: radici di (h^2/2)x^2 - GM x - eps = 0
a2=hh**2/2; disc=GMT**2+4*a2*eps; x1=(GMT+sqrt(disc))/(2*a2); x2=(GMT-sqrt(disc))/(2*a2)
ra=1/x2; va=hh/ra
assert isclose(1/x1,rp,rel_tol=1e-9); assert isclose(0.5*va**2-GMT/ra,eps,rel_tol=1e-9)
p("B3 eps",eps); p("B3 h",hh); p("B3 vc",vc); p("B3 vesc",vesc); p("B3 rA",ra); p("B3 vA",va); p("B3 e",(ra-rp)/(ra+rp))
p("B3 h^2/2",a2); p("B3 disc",disc); p("B3 sqrt disc",sqrt(disc))
# B4 asteroide: r_P, r_A -> v_P, v_A, e, T
GMS=G*MS; rp=2.0e11; ra=6.0e11
vp=sqrt(2*GMS*ra/(rp*(rp+ra))); va=vp*rp/ra
assert isclose(0.5*vp**2-GMS/rp,0.5*va**2-GMS/ra,rel_tol=1e-9)
p("B4 GMS",GMS); p("B4 vp",vp); p("B4 va",va); p("B4 e",(ra-rp)/(ra+rp)); a=(rp+ra)/2; p("B4 a UA",a/UA); p("B4 T anni",(a/UA)**1.5)
# B5 geostazionario con T=24 h
m=800; T=86400; r=(GMT*T**2/(4*pi**2))**(1/3)
p("B5 r",r); r_r=4.22e7; p("B5 U",-GMT*m/r_r); p("B5 K",GMT*m/(2*r_r)); p("B5 E",-GMT*m/(2*r_r)); p("B5 Usup",-GMT*m/RT); p("B5 L min",-GMT*m/(2*r_r)+GMT*m/RT)
# B6 tre stelle
M=1.5e30; L=2.0e11
F=G*M**2/L**2; Fr=sqrt(3)*F; Rc=L/sqrt(3); assert isclose(Rc,(2/3)*L*sqrt(3)/2)
v=sqrt(G*M/L); assert isclose(M*v**2/Rc,Fr,rel_tol=1e-9)
p("B6 F",F); p("B6 Fris",Fr); p("B6 R",Rc); p("B6 v",v); p("B6 T s",2*pi*Rc/v); p("B6 T anni",2*pi*Rc/v/3.156e7)
# B7 quadrato con M, M, 300, 100
l=0.80; mc=5.0; d2=l**2/2; assert isclose(sqrt(d2),l*sqrt(2)/2)
p("B7 d",sqrt(d2)); p("B7 F300",G*300*mc/d2); p("B7 F100",G*100*mc/d2); p("B7 Fris",G*200*mc/d2)
# B8 quadrato 100,200,300,400
l=1.0; mc=2.0; d2=l**2/2
Fd=G*200*mc/d2; p("B8 componente",Fd); p("B8 Fris",sqrt(2)*Fd)
# B9 stelle doppie uguali
M=2.0e30; d=1.0e11
v=sqrt(G*M/(2*d)); assert isclose(M*v**2/(d/2),G*M**2/d**2,rel_tol=1e-9)
p("B9 F",G*M**2/d**2); p("B9 v",v); p("B9 T s",pi*d/v); p("B9 T giorni",pi*d/v/86400)
# B10 asteroidi in linea
mA=6.0e15; mB=3.0e15; mC=1.5e16; AB=2.0e5; BC=5.0e5
FA=G*mA*mB/AB**2; FC=G*mC*mB/BC**2; p("B10 FA",FA); p("B10 FC",FC); p("B10 net",FA-FC)
# B11 angolo retto
m=10; M1=50; x1=0.40; M2=80; y2=0.60
F1=G*M1*m/x1**2; F2=G*M2*m/y2**2; p("B11 F1",F1); p("B11 F2",F2); p("B11 F",sqrt(F1**2+F2**2)); p("B11 ang",degrees(atan(F2/F1)))
# B12 campo al terzo vertice
M=500; L=2.0; gi=G*M/L**2; p("B12 g singolo",gi); p("B12 gtot",sqrt(3)*gi)
# B13 rapporto fuga/orbita su Marte
p("B13 vorb Marte",sqrt(G*MM/RM)); p("B13 vf Marte",sqrt(2*G*MM/RM))
# B14 Callisto
T=16.7*86400; r=1.88e9; p("B14 T",T); p("B14 MJ",4*pi**2*r**3/(G*T**2))
# B15 cambio orbita
m=1500; r1=RT+5.0e5; r2=RT+2.0e6
for k,r in (("1",r1),("2",r2)):
    v=sqrt(GMT/r); p(f"B15 r{k}",r); p(f"B15 v{k}",v); p(f"B15 T{k} min",2*pi*r/v/60); p(f"B15 E{k}",-GMT*m/(2*r))
p("B15 dE",GMT*m/2*(1/r1-1/r2))
# B16 lancio dalla Luna
GML=G*ML; p("B16 GML",GML); v0=2.0e3
x=1/RL-v0**2/(2*GML); p("B16 1/RL",1/RL); p("B16 v0^2/2GM",v0**2/(2*GML)); p("B16 rmax",1/x); p("B16 hmax km",(1/x-RL)/1e3)
vfL=sqrt(2*GML/RL); p("B16 vf",vfL); v0=3.0e3; p("B16 vinf",sqrt(v0**2-vfL**2))
# B17 esopianeta con luna
r=4.0e8; T=5.0*86400; Rp=2.0e7
Mp=4*pi**2*r**3/(G*T**2); p("B17 T",T); p("B17 M",Mp); Mp_r=float(f"{Mp:.3g}")
p("B17 g",G*Mp_r/Rp**2); p("B17 vf",sqrt(2*G*Mp_r/Rp)); p("B17 vrad",sqrt(G*Mp_r/Rp))
