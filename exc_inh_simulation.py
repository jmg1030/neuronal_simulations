import exc_inh_neuron_function
import nest
import numpy

for J_exc in range(0,105,5):
    for J_inh in range(0,105,5):

        nest.SetKernelStatus({"local_num_threads":2})
        data = exc_inh_neuron_function.neuron_population([350], J_exc, J_inh, 0, 100, 5000)
        numpy.savetxt('J_exc_' + str(J_exc) + '_J_inh_' + str(J_inh) + '.csv', data, delimiter=',')
        nest.ResetKernel()
