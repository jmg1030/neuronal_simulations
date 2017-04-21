import neuron_functions
import nest
import numpy

for J in range(0,105,5):
    for I in range(0,1010,10):
        nest.SetKernelStatus({"local_num_threads":8})
        data = neuron_functions.neuron_population([I], 50, b, 100, 100000)
        numpy.savetxt('Recurrent_Weight' + str(J) + '_External_' + str(I) + '.csv', data, delimiter=',')
        nest.ResetKernel()
