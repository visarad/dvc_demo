
print('===================================')
print('========START OF STAGE 03==========')
print('===================================')

with open('artifacts_01.txt','r') as f:
    text = f.read()

print(text)

text = "this is very funny to have my dear friend"

with open('artifacts_02.txt','w+') as f:
    f.write(text)


print('===================================')
print('========END OF STAGE 03============')
print('===================================')
