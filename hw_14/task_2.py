'''2. Implement the previous method with a magic method
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina' '''


class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

#    def add(self, other_country):
#        if isinstance(other_country, Country):
#            combined_name = f"{self.name} {other_country.name}"
#            combined_population = self.population + other_country.population
#            return Country(combined_name, combined_population)
#        else:
#            raise TypeError("Input must be a Country object")

    def __str__(self):
        return f"{self.name} (Population: {self.population})"

    def __add__(self, other_country):
        if isinstance(other_country, Country):
            combined_name = f"{self.name} {other_country.name}"
            combined_population = self.population + other_country.population
            return Country(combined_name, combined_population)
        else:
            raise TypeError("Input must be a Country object")


def main():
    bosnia = Country('Bosnia', 10_000_000)
    herzegovina = Country('Herzegovina', 5_000_000)

    bosnia_herzegovina = bosnia + herzegovina

    print(bosnia_herzegovina.name)
    print(bosnia_herzegovina.population)


if __name__ == "__main__":
    main()
