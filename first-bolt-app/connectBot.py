
def verificacao(fkMaquinas, disco, ram, cpu):
    try:
        listComponente = []

        printMaquina = "Alertas da Máquina %d: " % (fkMaquinas)
        listComponente.append(printMaquina)

        if disco >= 95:
            printDisco = "O disco está em estado crítico, com o uso de %.2f%% de sua capacidade" % (
                disco)
            listComponente.append(printDisco)
        elif disco >= 40:
            printDisco = "O disco está em estado de alerta, com o uso de %.2f%% de sua capacidade" % (
                disco)
            listComponente.append(printDisco)

        if ram >= 95:
            printRam = "A RAM está em estado crítico, com o uso de %.2f%% de sua capacidade" % (
                ram)
            listComponente.append(printRam)
        elif ram >= 90:
            printRam = "O disco está em estado de alerta, com o uso de %.2f%% de sua capacidade" % (
                ram)
            listComponente.append(printRam)

        if cpu >= 95:
            printCpu = "A CPU está em estado crítico, com o uso de %.2f%% de sua capacidade" % (
                cpu)
            listComponente.append(printCpu)
        elif cpu >= 90:
            printCpu = "A CPU está em estado de alerta, com o uso de %.2f%% de sua capacidade" % (
                cpu)
            listComponente.append(printCpu)

   
        # for i in listComponente:
        #      return i

        return listComponente

    finally:
        print()

    
