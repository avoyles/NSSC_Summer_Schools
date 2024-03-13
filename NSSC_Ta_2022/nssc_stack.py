import curie as ci

st = ci.Stack('tantalum_stack_new_design.csv', E0=64.0)

st.plot('Ta')
st.saveas('test.csv')