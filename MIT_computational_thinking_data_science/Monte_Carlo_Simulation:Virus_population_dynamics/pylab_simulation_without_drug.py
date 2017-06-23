def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    results = []
    counter = 0
    for t in xrange(300):
        results.append(0)

    for trial in xrange(numTrials):
        viruses = []
        for i in xrange(numViruses):
            viruses.append(SimpleVirus(maxBirthProb,clearProb))

        patient = Patient(viruses, maxPop)

        for t in xrange(300):
            results[t] += patient.update()
    for t in xrange(300):
        results[t] = float (results[t])/numTrials

    pylab.plot(range(300), results)
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.show()