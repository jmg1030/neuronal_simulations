import neuron_functions
import nest
import numpy

for b in range(55,105,5):
    for I in range(0,1010,10):
        nest.SetKernelStatus({"local_num_threads":8})
        data = neuron_functions.neuron_population([I], 50, b, 100, 100000)
        numpy.savetxt('Adaptation_' + str(b) + '_External_' + str(I) + '.csv', data, delimiter=',')
        nest.ResetKernel()
