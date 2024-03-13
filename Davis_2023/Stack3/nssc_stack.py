import curie as ci

print('Running...')
# st = ci.Stack(stack, E0=15.11, particle='d', dE0=0.22, N=1E4, max_steps=100)
st = ci.Stack('monitor_stack_35MeV.csv', E0=35.0, particle='a', dE0=0.35, N=1E4, max_steps=100)
st.saveas('results_monitor_stack.csv')
st.saveas('results_mo_stack.db')

# st.plot('Pd')
