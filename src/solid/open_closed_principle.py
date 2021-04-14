"""
Open-Closed Principle

Software entities should be open for extension, but closed for modification
"""
from enum import Enum as _Enum
from typing import List, Iterator


class Continent(_Enum):
    EUROPE = 1
    ASIA = 2
    AFRICA = 3


class Language(_Enum):
    ENGLISH = 1
    GERMAN = 2
    ARABIC = 3


class Country:
    def __init__(self, name: str, continent: Continent, language: Language):
        self.name = name
        self.continent = continent
        self.language = language


class BadFilter:
    def filter_by_language(
        self, countries: List[Country], language: Language
    ) -> Iterator[Country]:
        for country in countries:
            if country.language == language:
                yield country

    def filter_by_continent(
        self, countries: List[Country], continent: Continent
    ) -> Iterator[Country]:
        for country in countries:
            if country.continent == continent:
                yield country

    def filter_by_continent_and_language(self):
        pass

    def filter_by_continent_or_language(self):
        pass


class Specification:
    """
    Base Class to be inherited (extended)
    """

    def __or__(self, other):
        return OrSpecification(self, other)

    def __and__(self, other):
        return AndSpecification(self, other)

    def is_satisfied(self, country: Country) -> bool:
        pass


class Filter:
    """
    Base Class to be inherited (extended)
    """

    def filter(
        self, countries: List[Country], specification: Specification
    ) -> Iterator[Country]:
        pass


class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, country):
        return any(map(lambda spec: spec.is_satisfied(country), self.args))


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, country):
        return all(map(lambda spec: spec.is_satisfied(country), self.args))


class ContinentSpecification(Specification):
    def __init__(self, continent: Continent):
        self.continent = continent

    def is_satisfied(self, country: Country) -> bool:
        return country.continent == self.continent


class LanguageSpecification(Specification):
    def __init__(self, language: Language):
        self.language = language

    def is_satisfied(self, country: Country) -> bool:
        return country.language == self.language


class BetterFilter(Filter):
    def filter(
        self, countries: List[Country], specification: Specification
    ) -> Iterator[Country]:
        for country in countries:
            if specification.is_satisfied(country):
                yield country


if __name__ == "__main__":
    england = Country("England", Continent.EUROPE, Language.ENGLISH)
    germany = Country("Germany", Continent.EUROPE, Language.GERMAN)
    austria = Country("Austria", Continent.EUROPE, Language.GERMAN)
    egypt = Country("Egypt", Continent.AFRICA, Language.ARABIC)

    countries = [england, germany, egypt, austria]

    lang_spec = LanguageSpecification(Language.ENGLISH)
    continent_spec = ContinentSpecification(Continent.AFRICA)

    german_europe_spec = lang_spec & continent_specs
    english_africa_spec = lang_spec | continent_spec

    bf = BetterFilter()

    for country in bf.filter(countries, english_africa_spec):
        print(country.name)