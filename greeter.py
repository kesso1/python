
class Person:
    """A person with a name."""
    def __init__(self, name):
        self._name = name

    def greet_multiple_times(self, times):
        """Person greets n times."""
        for _ in range(times):
            print(f'Hi, I am {self._name}!')

    def set_name(self, name):
        """Change the name of a person."""
        self._name = name


def main():
    """Create a person and have it greet you."""
    bob = Person('Bob')
    bob.greet_multiple_times(3)


if __name__ == '__main__':
    main()
