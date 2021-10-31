from control.recv import recv
data = []
for  i in range(5):
    t  = recv()
    data.extend(t)
print(len(data))