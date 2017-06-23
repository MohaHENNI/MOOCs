def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    results = []
    resistants = []
    counter = 0
    for t in xrange(300):
        results.append(0)
        resistants.append(0)

    for trial in xrange(numTrials):
        viruses = []
        for i in xrange(numViruses):
            viruses.append(ResistantVirus(maxBirthProb,clearProb, resistances, mutProb))

        patient = TreatedPatient(viruses, maxPop)

        for t in xrange(150):
            results[t] += patient.update()
            resistants[t] += patient.getResistPop(["guttagonol"])
        patient.addPrescription("guttagonol")
        for t in xrange(150, 300):
            results[t] += patient.update()
            resistants[t] += patient.getResistPop(["guttagonol"])

    for t in xrange(300):
        results[t] = float (results[t])/numTrials
        resistants[t] = float (resistants[t])/numTrials

    pylab.plot(range(300), results, label= "Population")
    pylab.plot(range(300), resistants, label = "Guttagonol resistants")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.show()
