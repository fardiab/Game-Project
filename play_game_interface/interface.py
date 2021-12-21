from abc import ABCMeta, abstractmethod

class IPlayGameTypes(metaclass=ABCMeta):
    @abstractmethod
    def team_death_match(self):
        pass

    @abstractmethod
    def death_match(self):
        pass

    @abstractmethod
    def team_catch_flag(self):
        pass

            
class Score:
    @staticmethod
    def kill_death_score(kill, death):
        kill_count = []
        death_count = []
        kill_num = 1
        death_num = 1
        for i in range(kill):
            print(f"Kill {kill_num} soldier")
            kill_count.append(kill_num)
            kill_num += 1

        for i in range(death):
            print("Die")
            death_count.append(death_num)
            death_num += 1

        score = {"kill": f"{kill_num-1}", "death": f"{death_num-1}"}
        return score

class FateOfTheGame:
    @staticmethod
    def win():
        return "You won"

    @staticmethod
    def lose():
        return "You lost"

class Match(IPlayGameTypes):
    def show_menu(self):
        return """TDM(Team Death Match) - 1
DM(Death Match) - 2
TCF(Team Catch Flag) - 3
KOTH(Kill Of The Macth) - 4"""

    def team_death_match(self):
        return """Connecting TDM
------- Wait -------
Connected matchmaking"""

    def death_match(self):
        return """Connecting DM
------- Wait -------
Connected matchmaking
Choose team"""

    def team_catch_flag(self):
        return """Connecting TCF
------- Wait -------
Connected matchmaking"""

    def kill_of_the_match(self):
        return """Connecting TCF
------- Wait -------
Connected matchmaking"""

    def choose_team(self):
        return """Choose team
Blue Team - 1
Red team - 2"""

    def join_team(self, team):
        return f"""Joining {team}"""

class Coin:
    def collect_coins(self, kill_num, death_num):
        collect_coin = []
        for i in range(kill_num):
            coin = i*10 - death_num*2
            collect_coin.append(coin)
        return f"You collected {collect_coin[-1]} Zen"

class Menu:
    def show_menu(self):
        return """Play Game - 1 
Custimization - 2
Missions - 3
Settings - 4
Exit - 5"""

class Customization:
    def __str__(self):
        return """Armor - 1
Weapon - 2"""