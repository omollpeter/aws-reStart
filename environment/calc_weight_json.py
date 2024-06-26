import jsonFileHandler

data = jsonFileHandler.readJsonFile("insulin.json")
if data:
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print("bInsulin:", bInsulin)
    print("aInsulin:", aInsulin)
    print("molecularWeightInsulinActual:", molecularWeightInsulinActual)

    # Calculating the molecular weight of insulin
    # Getting a list of amino acids (AA) weights
    aaWeights = data["weights"]

    # Count the number of each amino acids
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})

    # multiply the counts by weight
    molecularWeightInsulin = sum({x: aaWeights[x] * aaCountInsulin[x] for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']}.values())
    print("The rough molecular weight of insulin:", molecularWeightInsulin)
    percentageError = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
    print("Error percentage:", percentageError)
else:
    print("Error. Exiting the program")
