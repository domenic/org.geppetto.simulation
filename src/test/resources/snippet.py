from py4j.java_gateway import JavaGateway

class Addition(object):
    def doOperation(self, i, j, k = None):
        if k == None:
            return i + j
        else:
            return i + j + k

    class Java:
        implements = ['org.geppetto.simulation.test.Operator']

if __name__ == '__main__':
    gateway = JavaGateway(start_callback_server=True)
    operator = Addition()
    numbers = gateway.entry_point.randomBinaryOperator(operator)
    print(numbers)
    numbers = gateway.entry_point.randomTernaryOperator(operator)
    print(numbers)
    gateway.shutdown()