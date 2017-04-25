import exc_inh_neuron_function
import nest
import numpy

def server_run(n_value):

    I_array = range(0,1010,10)

    for b in range(0,105,5):

        nest.SetKernelStatus({"local_num_threads":20})
        data = exc_inh_neuron_function.neuron_population([I_array[n_value]], 5, 35, b, 100, 100000)
        numpy.savetxt('W_noise_External_' + str(I_array[n_value]) + '_Adaptation_' + str(b) + '.csv', data, delimiter=',')
        nest.ResetKernel()
