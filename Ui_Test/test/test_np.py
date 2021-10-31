from matplotlib import pyplot as plt

fig = plt.figure()
plot1 = fig.add_subplot(111)
plot1.plot([0,1],[0,1])
figs,ax = fig.subplots(2,1)




plt.show()