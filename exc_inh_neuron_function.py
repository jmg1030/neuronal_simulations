import nest
import pylab
import numpy

def neuron_population(I, J_exc, J_inh, b, N, time):

    dict_params = {"V_peak" : 0.0
    , "V_reset" : -70.0
    , "t_ref" : 2.0
    , "g_L" :  30.0
    , "C_m" : 281.0
    , "E_ex" : 0.0
    , "E_in" : -85.0
    , "E_L" : -70.0
    , "Delta_T" : 2.0
    , "tau_w" : 100.0
    , "a" : 0.0
    , "b" : float(b)
    , "V_th" : -55.0
    , "tau_syn_ex" : 0.2
    , "tau_syn_in" : 2.0
    , "I_e" : 0.0
    , "w": 0.0}

    exc_neurons = nest.Create("aeif_cond_exp", 100)
    inh_neurons = nest.Create("aeif_cond_exp", 20)

    noise = nest.Create("noise_generator")

    nest.SetStatus(exc_neurons, params=dict_params)
    nest.SetStatus(inh_neurons, params=dict_params)

    nest.SetStatus(noise, {"std": float(N)})

    for neuron in exc_neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    for neuron in inh_neurons:
         nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    spike_detector = nest.Create("spike_detector")

    for n in exc_neurons:
        nest.Connect([n], spike_detector)

    for n in inh_neurons:
        nest.Connect([n], spike_detector)

    K_e = 25
    K_i = 10
    d = 1.0

    exc_conn_dict = {"rule": "fixed_indegree", "indegree": K_e}
    inh_conn_dict = {"rule": "fixed_indegree", "indegree": K_i}
    exc_syn_dict = {"delay": d, "weight": float(J_exc)}
    inh_syn_dict = {"delay": d, "weight": -float(J_inh)}

    nest.Connect(exc_neurons, exc_neurons, exc_conn_dict, exc_syn_dict)
    nest.Connect(exc_neurons, inh_neurons, exc_conn_dict, exc_syn_dict)
    nest.Connect(inh_neurons, exc_neurons, inh_conn_dict, inh_syn_dict)
    nest.Connect(inh_neurons, inh_neurons, inh_conn_dict, inh_syn_dict)

    for neuron in exc_neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    for neuron in inh_neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    for i in I:

        nest.SetStatus(exc_neurons, params={"I_e": float(i)})
        nest.SetStatus(inh_neurons, params={"I_e": float(i)})

        nest.Simulate(time)
        nest.ResumeSimulation()

        dSD = nest.GetStatus(spike_detector, keys='events')[0]
        evs = dSD["senders"]
        ts_s = dSD["times"]

    return ts_s, evs
