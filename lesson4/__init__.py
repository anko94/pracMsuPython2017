# import matplotlib as mp
# from matplotlib import pyplot
#
# x = [10, 50, 100, 200, 500, 1000]
# y1 = [0.5619350000000001, 9.352698, 40.259785750000006, 152.63097975, 398.76540976, 811.1567845556]
# y2 = [0.026289000000000007, 0.687094250000003, 2.7596809999999934, 11.463490249999978, 51.1876545556, 107.476453778]
# y3 = [0.10703675000000001, 1.9350535000000004, 7.567243749999996, 31.68105374999999, 134.7657889, 266.65252]
# y4 = [0.01799699999999982, 0.10255574999999872, 0.24237425000001167, 0.672813199994561, 2.567556, 5.4473324]
# y5 = [0.02036299999999991, 0.5237615000000009, 2.2088652500000023, 9.3154722199991789, 47.6785679998, 71.4645272]
# y6 = [0.047436000000000034, 0.3099149999999984, 0.7524735000000078, 1.827005367, 3.6789665 , 7.846443]
# y7 = [0.003762250000000078, 0.03528825000000069, 0.1431429999999949, 0.5806442219990999, 2.9756447, 4.7885543]
# y8 = [0.04664024999999983, 0.3080772500000002, 0.7358145000000036, 1.757426038876529, 3.165538767, 8.9363739]
# y9 = [0.00704425573348999, 0.0349307656288147, 0.07016241550445557, 0.1685706377029419, 0.42683160305023193, 1.2038469910621643]
# pyplot.ylabel('время')
#
# # x = [10, 50, 100, 200, 500, 1000]
# # y1 = [1, 1, 1, 1, 1, 1]
# # y2 = [21.375290045, 13.611957894, 14.588565037, 13.314529556, 7.790265313, 7.547297627]
# # y3 = [5.249925843, 4.83330202, 5.320270772, 4.817736839, 2.958951326, 3.04199932]
# # y4 = [31.22381508, 91.196232293, 166.105870364, 226.854912703, 155.309332984, 148.908993429]
# # y5 = [27.595884693, 17.85678787, 18.226456209, 16.384674458, 8.363619683, 11.350481369]
# # y6 = [11.846171684, 30.178268235, 53.50326058, 83.541615425, 108.390606373, 103.378917626]
# # y7 = [149.361419363, 265.03717243, 281.255707579, 262.864890353, 134.009752495, 169.394922504]
# # y8 = [12.048284475, 30.358288384, 54.714586013, 86.849162567, 125.970787001, 90.770237865]
# # y9 = [79.772089666, 267.749584976, 573.808433768, 905.442263432, 934.245278256, 673.80388918]
# # pyplot.ylabel('ускорение')
#
# pyplot.plot(x, y1,'r', label = "scipy")
# pyplot.plot(x, y2,'b', label = "verlet")
# pyplot.plot(x, y3, 'g', label = "verletThreading")
# pyplot.plot(x, y4, 'y', label = "verletMultiprocessing")
# pyplot.plot(x, y5, 'purple', label = "verletCython1")
# pyplot.plot(x, y6, 'c', label = "verletCythonWithOpenmp")
# pyplot.plot(x, y7, 'm', label = "verletCythonWithMemoryView")
# pyplot.plot(x, y8, 'k', label ="verletCython4")
# pyplot.plot(x, y9, 'orange', label = "opencl")
# pyplot.xlabel('число точек')
# leg = pyplot.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
# leg.get_frame().set_alpha(0.5)
# pyplot.show()