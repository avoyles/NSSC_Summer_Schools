import curie as ci
import numpy as np
import matplotlib.pyplot as plt


# ## Compound must be specified, and enough info to determine areal density
# ## Units:
# ## thickness: mm
# ## mass: g
# ## area: cm^2
# ## ad (areal density): mg/cm^2
# ## density: g/cm^3

# x_kapton = 0.013
# x_silicone = 0.013

# ad_degrader_a = 599.   #2.24 mm
# ad_degrader_b = 415.0   #1.55 mm
# ad_degrader_c = 261.5   #0.97 mm
# # ad_degrader_d = 599.0
# ad_degrader_e = 68.3   #0.256 mm
# ad_degrader_h = 33.8

# ad_be_backing = 4.425     #23.9130435 microns

# rho_r = 500.0   # mg/cm2


# # stack = [{'compound':'U', 'name':'U01', 'ad':rho_r},
# stack = [{'compound':'Al',  'name':'Al01',   'thickness':0.0001},
# 	     {'compound':'Fe', 'name':'Fe01', 'ad':rho_r},
# 	     {'compound':'Al',  'name':'Al02',   'thickness':0.0001}]
# 		 # {'compound':'Th', 'name':'Th01', 'thickness':0.030},
# 		 # {'compound':'Cu',  'name':'Cu01',   'thickness':0.025},
# 		 # #
# 		 #
# 		 #
# 		 #
# 		 #
# 		 # {'compound':'SS_316', 'name':'SS2', 'ad':100.0}]




# print('Running...')
# st = ci.Stack(stack, E0=24.0, particle='d', dE0=0.01, N=1E4,  accuracy=.001)
# # print('Running...')
# st.saveas('arjan_stack.csv')
# st.saveas('arjan_stack.db')
# st.summarize()
# fluxes = st.get_flux('Fe01')

# eng = fluxes[0]
# phi = fluxes[1]

rx_zn_pg = ci.Reaction('203TL(p,x)204PB')
rx_zn_pn = ci.Reaction('203TL(p,x)203PB')
rx_zn_p2n = ci.Reaction('203TL(p,x)202PB')
rx_zn_p3n = ci.Reaction('203TL(p,x)201PB')
rx_zn_p4n = ci.Reaction('203TL(p,x)200PB')
rx_zn_p5n = ci.Reaction('203TL(p,x)199PB')
rx_zn_p6n = ci.Reaction('203TL(p,x)198PB')
# rx_zn_p7n = ci.Reaction('203TL(p,x)62GA')


rx_zn_pd = ci.Reaction('203TL(p,x)202TL')
rx_zn_pdn = ci.Reaction('203TL(p,x)201TL')
rx_zn_pd2n = ci.Reaction('203TL(p,x)200TL')
rx_zn_pd3n = ci.Reaction('203TL(p,x)199TL')
rx_zn_pd4n = ci.Reaction('203TL(p,x)198TL')
rx_zn_pd5n = ci.Reaction('203TL(p,x)197TL')

rx_zn_pa = ci.Reaction('203TL(p,x)200HG')
rx_zn_pan = ci.Reaction('203TL(p,x)199HG')
rx_zn_pa2n = ci.Reaction('203TL(p,x)198HG')
rx_zn_pa3n = ci.Reaction('203TL(p,x)197HG')
rx_zn_pa4n = ci.Reaction('203TL(p,x)196HG')



# rx_203_201g = ci.Reaction('203TL(p,x)201PBg')
# rx_205_201g = ci.Reaction('205TL(p,x)201PBg')
# rx_203_203g = ci.Reaction('203TL(p,x)203PBg')
# rx_205_203g = ci.Reaction('205TL(p,x)203PBg')


# rx_205_198g = ci.Reaction('205TL(p,x)198PBg')
# rx_205_200g = ci.Reaction('205TL(p,x)200PBg')
# rx_205_202g = ci.Reaction('205TL(p,x)202PBg')
# rx_205_204g = ci.Reaction('205TL(p,x)204PBg')

abundance_203Tl = 0.29524
abundance_205Tl = 1 - abundance_203Tl


lb = ci.Library('tendl_p')
# print(lb.search(target='27AL'))

print(rx_zn_pn.xs)

plt.plot(rx_zn_pg.eng, rx_zn_pg.xs, label='203Tl(p,g)204Pb')
plt.plot(rx_zn_pn.eng, rx_zn_pn.xs, label='203Tl(p,n)203Pb')
plt.plot(rx_zn_p2n.eng, rx_zn_p2n.xs, label='203Tl(p,2n)202Pb')
plt.plot(rx_zn_p3n.eng, rx_zn_p3n.xs, label='203Tl(p,3n)201Pb')
plt.plot(rx_zn_p4n.eng, rx_zn_p4n.xs, label='203Tl(p,4n)200Pb')
plt.plot(rx_zn_p5n.eng, rx_zn_p5n.xs, label='203Tl(p,5n)199Pb')
plt.plot(rx_zn_p6n.eng, rx_zn_p6n.xs, label='203Tl(p,6n)198Pb')

plt.plot(rx_zn_pd.eng, rx_zn_pd.xs, linestyle='dashed', label='203Tl(p,d)202Tl')
plt.plot(rx_zn_pdn.eng, rx_zn_pdn.xs, linestyle='dashed', label='203Tl(p,dn)201Tl')
plt.plot(rx_zn_pd2n.eng, rx_zn_pd2n.xs, linestyle='dashed', label='203Tl(p,d2n)200Tl')
plt.plot(rx_zn_pd3n.eng, rx_zn_pd3n.xs, linestyle='dashed', label='203Tl(p,d3n)199Tl')
plt.plot(rx_zn_pd4n.eng, rx_zn_pd4n.xs, linestyle='dashed', label='203Tl(p,d4n)198Tl')

plt.plot(rx_zn_pa.eng, rx_zn_pa.xs, linestyle='dotted', label='203Tl(p,a)200Hg')
plt.plot(rx_zn_pan.eng, rx_zn_pan.xs, linestyle='dotted', label='203Tl(p,an)199Hg')
plt.plot(rx_zn_pa2n.eng, rx_zn_pa2n.xs, linestyle='dotted', label='203Tl(p,a2n)198Hg')
plt.plot(rx_zn_pa3n.eng, rx_zn_pa3n.xs, linestyle='dotted', label='203Tl(p,a3n)197Hg')
plt.plot(rx_zn_pa4n.eng, rx_zn_pa4n.xs, linestyle='dotted', label='203Tl(p,a4n)196Hg')



# plt.plot(rx_203_201g.eng, abundance_203Tl*rx_203_202g.xs + abundance_205Tl*rx_205_202g.xs, label='Tl(p,x)202gPb')
# plt.plot(rx_203_201g.eng, abundance_203Tl*rx_203_202m.xs + abundance_205Tl*rx_205_202m.xs, label='Tl(p,x)202mPb')
# plt.plot(rx_203_201g.eng, abundance_203Tl*rx_203_203g.xs + abundance_205Tl*rx_205_203g.xs, label='Tl(p,x)203gPb')


plt.legend(loc="upper right")
plt.xlim([0, 75])
plt.xlabel("Proton Energy (MeV)")
plt.ylabel("Cross Section (mb)")
plt.savefig("tl_fig.png", dpi=300)
plt.show()