def connectBot(fkMaquinas, disco, ram, cpu):
    try:
        listComponente = []
        
        printMaquina = "\nAlertas da Máquina %d:" % (fkMaquinas)
        listComponente.append(printMaquina)

        if disco >= 95:
            printDisco = "\nO disco está em estado crítico, com o uso de %.2f%% de sua capacidade" % (disco)
            listComponente.append(printDisco)
        elif disco >= 40:
            printDisco = "\nO disco está em estado de alerta, com o uso de %.2f%% de sua capacidade" % (disco)
            listComponente.append(printDisco)

        if ram >= 95:
            printRam = "\nA RAM está em estado crítico, com o uso de %.2f%% de sua capacidade" % (ram)
            listComponente.append(printRam)
        elif ram >= 90:
            printRam = "\nO disco está em estado de alerta, com o uso de %.2f%% de sua capacidade" % (ram)
            listComponente.append(printRam)

        if cpu >= 95:
            printCpu = "\nA CPU está em estado crítico, com o uso de %.2f%% de sua capacidade" % (cpu)
            listComponente.append(printCpu)
        elif cpu >= 90:
            printCpu = "\nA CPU está em estado de alerta, com o uso de %.2f%% de sua capacidade" % (cpu)
            listComponente.append(printCpu)

        if len(listComponente) > 1:
            for i in listComponente:
                print(i)

    finally:
        print()