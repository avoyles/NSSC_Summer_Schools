import curie as ci
import matplotlib.pyplot as plt

# st = ci.Stack("monitor_stack.csv", E0=40, particle='a', dE0=0.4, N=1E4, max_steps=100)

# st.plot('Ni')
# st.summarize()
# st.saveas('monitor_results.csv')


# rx  = ci.Reaction('65CU(p,x)58COg')
# rx2 = ci.Reaction('65CU(p,x)58COm')

# plt.plot(rx.eng, rx.xs, label='58COg')
# plt.plot(rx2.eng, rx2.xs, label='58COm')
# plt.legend()
# plt.show()




# print(ci.COMPOUND_LIST)

# cm = ci.Compound('Brass', weights={'Zn':-33,'Cu':-66}, density=4)
# cm2 = ci.Compound('Brass', weights={'Zn':2,'Cu':5}, density=5)


# print(cm.weights)
# print(cm2.weights)

# print(cm.density)


ip = ci.Isotope('209PO')
print(ip.decay_const())




# sp = ci.Spectrum("eu_calib_7cm.Spe")
# # sp.plot()
# sp.isotopes = ['152EU','40K']

# ### Perform an efficiency calibration
# cb = ci.Calibration()
# cb.calibrate([sp], sources={'isotope':'152EU', 'A0':3.7E4, 'ref_date':'01/01/2009 12:00:00'})
# cb.plot()
# # cb.saveas('eu_calib_7cm.json')



# sp.cb = 'eu_calib_7cm.json'
# sp.plot()
# sp.summarize()
# sp.saveas('summary.csv')
# sp.saveas('summary.db')