text = 'this is the only outcome of this file '
print('===================================')
print('=========START OF STAGE 01=========')
print('===================================')

with open('artifacts_01.txt','w') as f:
    f.write(text)

print('===================================')
print('==========END OF STAGE 01==========')
print('===================================')
text = 'visarad kumar and deepthi comes pararthi'

with open('artifacts01.txt','w+') as f:
    f.write(text)

print("end of file 01")

