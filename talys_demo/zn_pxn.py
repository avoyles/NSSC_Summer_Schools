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

rx_zn_pg = ci.Reaction('68ZN(p,x)69GA')
rx_zn_pn = ci.Reaction('68ZN(p,x)68GA')
rx_zn_p2n = ci.Reaction('68ZN(p,x)67GA')
rx_zn_p3n = ci.Reaction('68ZN(p,x)66GA')
rx_zn_p4n = ci.Reaction('68ZN(p,x)65GA')
rx_zn_p5n = ci.Reaction('68ZN(p,x)64GA')
rx_zn_p6n = ci.Reaction('68ZN(p,x)63GA')
rx_zn_p7n = ci.Reaction('68ZN(p,x)62GA')


rx_zn_pd = ci.Reaction('68ZN(p,x)67ZN')
rx_zn_pdn = ci.Reaction('68ZN(p,x)66ZN')
rx_zn_pd2n = ci.Reaction('68ZN(p,x)65ZN')
rx_zn_pd3n = ci.Reaction('68ZN(p,x)64ZN')
rx_zn_pd4n = ci.Reaction('68ZN(p,x)63ZN')
rx_zn_pd5n = ci.Reaction('68ZN(p,x)62ZN')

rx_zn_pa = ci.Reaction('68ZN(p,x)65CU')
rx_zn_pan = ci.Reaction('68ZN(p,x)64CU')
rx_zn_pa2n = ci.Reaction('68ZN(p,x)63CU')
rx_zn_pa3n = ci.Reaction('68ZN(p,x)62CU')
rx_zn_pa4n = ci.Reaction('68ZN(p,x)61CU')



rx_203_201g = ci.Reaction('203TL(p,x)201PBg')
rx_205_201g = ci.Reaction('205TL(p,x)201PBg')
rx_203_203g = ci.Reaction('203TL(p,x)203PBg')
rx_205_203g = ci.Reaction('205TL(p,x)203PBg')


rx_205_198g = ci.Reaction('205TL(p,x)198PBg')
rx_205_200g = ci.Reaction('205TL(p,x)200PBg')
rx_205_202g = ci.Reaction('205TL(p,x)202PBg')
rx_205_204g = ci.Reaction('205TL(p,x)204PBg')

abundance_203Tl = 0.29524
abundance_205Tl = 1 - abundance_203Tl


lb = ci.Library('tendl_p')
print(lb.search(target='203TL', product='200PBo'))


# rx_203_198m = ci.Reaction('203TL(p,x)198PBo')
# rx_203_200m = ci.Reaction('203TL(p,x)200PBo')
rx_203_202m = ci.Reaction('203TL(p,x)202PBm1')
rx_203_204m = ci.Reaction('203TL(p,x)204PBm1')

# rx_205_198m = ci.Reaction('205TL(p,x)198PBm')
# rx_205_200m = ci.Reaction('205TL(p,x)200PBm')
rx_205_202m = ci.Reaction('205TL(p,x)202PBm1')
rx_205_204m = ci.Reaction('205TL(p,x)204PBm1')

# # print(rx.library.name)
# # xs_avg = 10.1        # mb
# xs_avg = rx.average(eng, phi)        # mb
# print('Average cross section (mb): ',xs_avg)
# # print('Reaction integral: ',rx.integrate(eng, phi/max(phi)))

# st = ci.Stack(stack, E0=24.0, particle='d', dE0=0.1, N=1E6,  accuracy=.001)
# # print('Running...')
# st.saveas('arjan_stack.csv')
# st.saveas('arjan_stack.db')
# st.summarize()
# fluxes = st.get_flux('Fe01')

# eng_01 = fluxes[0]
# phi_01 = fluxes[1]

# st = ci.Stack(stack, E0=24.0, particle='d', dE0=0.4, N=1E6,  accuracy=.001)
# # print('Running...')
# st.saveas('arjan_stack.csv')
# st.saveas('arjan_stack.db')
# st.summarize()
# fluxes = st.get_flux('Fe01')

# eng_4 = fluxes[0]
# phi_4 = fluxes[1]

# print(rx_203_202m.xs / rx_203_202g.xs)


# # plt.plot(eng_4,phi_4/max(phi_4), label='Fluxes - dE0=0.4')
# # plt.plot(eng,phi/max(phi),  label='Fluxes - dE0=0.01, N=1E5')
# # plt.plot(eng_01,phi_01/max(phi_01), '--', label='Fluxes - dE0=0.01')
# # plt.plot(rx_203_198g.eng, rx_203_198m.xs/rx_203_198m.xs, label='203TL(p,x)198PB m-to-g')
# # plt.plot(rx_203_200g.eng, rx_203_200m.xs/rx_203_200m.xs, label='203TL(p,x)200PB m-to-g')
# plt.plot(rx_203_202g.eng, rx_203_202m.xs/rx_203_202g.xs, label='203TL(p,x)202PB m-to-g')
# plt.plot(rx_203_204g.eng, rx_203_204m.xs/rx_203_204g.xs, label='203TL(p,x)204PB m-to-g')
# plt.plot(rx_205_202g.eng, rx_205_202m.xs/rx_205_202g.xs, label='205TL(p,x)202PB m-to-g')
# plt.plot(rx_205_204g.eng, rx_205_204m.xs/rx_205_204g.xs, label='205TL(p,x)204PB m-to-g')



# plt.plot(rx_203_198g.eng, rx_203_198g.xs, label='203TL(p,x)198PBg')
# plt.plot(rx_203_200g.eng, rx_203_200g.xs, label='203TL(p,x)200PBg')
# plt.plot(rx_203_202g.eng, rx_203_202g.xs, label='203TL(p,x)202PBg')
# plt.plot(rx_203_204g.eng, rx_203_204g.xs, label='203TL(p,x)204PBg')
# plt.plot(rx_205_202m.eng, rx_205_198g.xs, label='205TL(p,x)198PBg')
# plt.plot(rx_205_202m.eng, rx_205_200g.xs, label='205TL(p,x)200PBg')
# plt.plot(rx_205_202m.eng, rx_205_202g.xs, label='205TL(p,x)202PBg')
# plt.plot(rx_205_204m.eng, rx_205_204g.xs, label='205TL(p,x)204PBg')

plt.plot(rx_zn_pg.eng, rx_zn_pg.xs, label='68Zn(p,g)69Ga')
plt.plot(rx_zn_pn.eng, rx_zn_pn.xs, label='68Zn(p,n)68Ga')
plt.plot(rx_zn_p2n.eng, rx_zn_p2n.xs, label='68Zn(p,2n)67Ga')
plt.plot(rx_zn_p3n.eng, rx_zn_p3n.xs, label='68Zn(p,3n)66Ga')
plt.plot(rx_zn_p4n.eng, rx_zn_p4n.xs, label='68Zn(p,4n)65Ga')
# plt.plot(rx_zn_p5n.eng, rx_zn_p5n.xs, label='68Zn(p,5n)64Ga')
# plt.plot(rx_zn_p6n.eng, rx_zn_p6n.xs, label='68Zn(p,6n)63Ga')

plt.plot(rx_zn_pd.eng, rx_zn_pd.xs, linestyle='dashed', label='68Zn(p,d)67Zn')
plt.plot(rx_zn_pdn.eng, rx_zn_pdn.xs, linestyle='dashed', label='68Zn(p,dn)66Zn')
plt.plot(rx_zn_pd2n.eng, rx_zn_pd2n.xs, linestyle='dashed', label='68Zn(p,d2n)65Zn')
plt.plot(rx_zn_pd3n.eng, rx_zn_pd3n.xs, linestyle='dashed', label='68Zn(p,d3n)64Zn')
plt.plot(rx_zn_pd4n.eng, rx_zn_pd4n.xs, linestyle='dashed', label='68Zn(p,d4n)63Zn')

plt.plot(rx_zn_pa.eng, rx_zn_pa.xs, linestyle='dotted', label='68Zn(p,a)65Cu')
plt.plot(rx_zn_pan.eng, rx_zn_pan.xs, linestyle='dotted', label='68Zn(p,an)64Cu')
plt.plot(rx_zn_pa2n.eng, rx_zn_pa2n.xs, linestyle='dotted', label='68Zn(p,a2n)63Cu')
plt.plot(rx_zn_pa3n.eng, rx_zn_pa3n.xs, linestyle='dotted', label='68Zn(p,a3n)62Cu')
plt.plot(rx_zn_pa4n.eng, rx_zn_pa4n.xs, linestyle='dotted', label='68Zn(p,a4n)61Cu')



# plt.plot(rx_203_201g.eng, abundance_203Tl*rx_203_202g.xs + abundance_205Tl*rx_205_202g.xs, label='Tl(p,x)202gPb')
# plt.plot(rx_203_201g.eng, abundance_203Tl*rx_203_202m.xs + abundance_205Tl*rx_205_202m.xs, label='Tl(p,x)202mPb')
# plt.plot(rx_203_201g.eng, abundance_203Tl*rx_203_203g.xs + abundance_205Tl*rx_205_203g.xs, label='Tl(p,x)203gPb')


plt.legend(loc="upper right")
plt.xlim([0, 75])
plt.xlabel("Proton Energy (MeV)")
plt.ylabel("Cross Section (mb)")
plt.savefig("zn_fig.png", dpi=300)
plt.show()