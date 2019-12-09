class IPrinter:
    pass


# Interface Segregation Principle
class IPrinterWithInputInfo(IPrinter):
    def Print(self, textToPrint):
        pass


# Interface Segregation Principle
class IPrinterWithoutInputInfo(IPrinter):
    def Print(self):
        pass


# Single Responsibility Principle, ConsolePrinter only Prints given text, one actor(goal)
# Also it is Open-Closed principle
class ConsolePrinter(IPrinterWithInputInfo):
    def Print(self, textToPrint):
        print(textToPrint)


# Open-Closed Principle
class DbPrinter(IPrinterWithoutInputInfo):
    def Print(self):
        pass


# Open-Closed Principle
class FilePrinter(IPrinterWithoutInputInfo):
    def Print(self):
        pass


class WiredPrinter(IPrinterWithoutInputInfo):
    def Print(self):
        pass


class WirelessPrinter(IPrinterWithoutInputInfo):
    def Print(self):
        pass


if __name__ == '__main__':
    consolePrinter = ConsolePrinter()
    consolePrinter.Print("Hello World")
