import curie as ci

print('Running...')
# st = ci.Stack(stack, E0=15.11, particle='d', dE0=0.22, N=1E4, max_steps=100)
st = ci.Stack('pd_stack.csv', E0=50.2, particle='a', dE0=0.5, N=1E4, max_steps=100)
st.saveas('nssc_pd_stack.csv')
st.saveas('nssc_pd_stack.db')

# st.plot('Pd')
