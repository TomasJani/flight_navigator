import csv


class AirportCode:
    pass


class FlightInfo:
    pass


FlightsGraph = dict[AirportCode, dict[AirportCode, list[FlightInfo]]]


class FightNavigator:
    filtering_pipelines = []

    def solve(self, graph: FlightsGraph, start: AirportCode, end: AirportCode):
        shortest_flights = {}
        visited_airports: set[AirportCode] = set()
        shortest_flights = self._solve(graph, start, end, visited_airports, shortest_flights)




def parse_row():
    pass


def main(path, ):
    with open(path, encoding="utf-8") as csv_file:
        flights_file_reader = csv.reader(csv_file, dialect="unix")
        for row in flights_file_reader:
            parse_row(row)
