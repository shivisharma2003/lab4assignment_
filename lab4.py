class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        result = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return result

    def search_by_location(self, location):
        result = [match for match in self.matches if match.location == location]
        return result

    def search_by_timing(self, timing):
        result = [match for match in self.matches if match.timing == timing]
        return result

def main():
    flight_table = FlightTable()

    # Adding matches to the flight table
    flight_table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    flight_table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    flight_table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    flight_table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    flight_table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    flight_table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("Search options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            team_name = input("Enter the team name: ")
            result = flight_table.search_by_team(team_name)
        elif choice == '2':
            location = input("Enter the location: ")
            result = flight_table.search_by_location(location)
        elif choice == '3':
            timing = input("Enter the timing: ")
            result = flight_table.search_by_timing(timing)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        if result:
            print("Match details:")
            for match in result:
                print(f"Location: {match.location}, Teams: {match.team1} vs {match.team2}, Timing: {match.timing}")
        else:
            print("No matches found for the given criteria.")

if __name__ == "__main__":
    main()
