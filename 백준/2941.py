st=input()
alp=0

for i in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    while i in st:
        alp+=st.count(i)
        st=st.replace(i, ' ')

for i in st:
    if i!=' ':
        alp+=1

print(alp)