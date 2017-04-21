import exc_inh_neuron_function
import nest
import numpy

for I in range(0,1005,5):
    for b in range(0,105,5):

        nest.SetKernelStatus({"local_num_threads":28})
        data = exc_inh_neuron_function.neuron_population([I], 5, 35, b, 100, 100000)
        numpy.savetxt('J_exc_' + str(J_exc) + '_J_inh_' + str(J_inh) + '.csv', data, delimiter=',')
        nest.ResetKernel()
