
## Counting Stack
"""
    A simple implementation of a stack (LIFO: Last In, First Out).
    This class provides basic push and pop operations.
    """
class Stack:

    def __init__(self):
        self.__stk = []  # private list to hold stack elements

    def push(self, val):
        """
        Push a value onto the stack.
        """
        self.__stk.append(val)  # add element to the end of the list

    def pop(self):
        """
        Pop (remove and return) the last element from the stack.
        """
        val = self.__stk[-1]    # get the last element
        del self.__stk[-1]      # remove the last element
        return val


class CountingStack(Stack):
    """
    Extended version of Stack that counts the number of push and pop operations.
    Useful for monitoring stack usage.
    """
    def __init__(self):
        Stack.__init__(self)
        self.__push_counter = 0  # counter for push operations
        self.__pop_counter = 0   # counter for pop operations

    def get_push_counter(self):
        """
        Return the number of push operations performed.
        """
        return self.__push_counter

    def get_pop_counter(self):
        """
        Return the number of pop operations performed.
        """
        return self.__pop_counter

    def total_operations(self):
        """
        Return the total number of push + pop operations performed.
        """
        return self.__push_counter + self.__pop_counter

    def push(self, val):
        """
        Push a value onto the stack and increment the push counter.
        """
        self.__push_counter += 1
        return Stack.push(self, val)

    def pop(self):
        """
        Pop a value from the stack and increment the pop counter.
        """
        self.__pop_counter += 1
        return Stack.pop(self)


# Example usage
if __name__ == "__main__":
    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()

    print("Push count:", stk.get_push_counter())     # 100
    print("Pop count:", stk.get_pop_counter())       # 100
    print("Total operations:", stk.total_operations())  # 200
