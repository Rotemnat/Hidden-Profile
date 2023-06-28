from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'choice1121'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    PAYOFF = cu(150)
    OPTIMAL_OPTION = 'פרויקט D'
    SUBOPTIML_OPTION1 = 'פרויקט A'
    SUBOPTIML_OPTION2 = 'פרויקט B'
    SUBOPTIML_OPTION3 = 'פרויקט E'
    PSSIMAL_OPTION = 'פרויקט C'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    votes_for_option1 = models.FloatField(initial=0)
    votes_for_option2 = models.IntegerField(initial=0)
    votes_for_option3 = models.FloatField(initial=0)
    votes_for_optimal = models.FloatField(initial=0)
    votes_for_option5 = models.FloatField(initial=0)
    group_wins = models.BooleanField()


class Player(BasePlayer):
    vote = models.StringField(
        choices=['פרויקט A', 'פרויקט B', 'פרויקט C', 'פרויקט D', 'פרויקט E'],
        label="עליך להצביע עכשיו לאיזו חלופה תעניק/י את קולך?"
    )
    is_correct = models.BooleanField()
    potential_payoff = models.CurrencyField(initial=0)



# FUNCTIONS

def set_payoffs(group: Group):
    players = group.get_players()
    are_correct_list = [p for p in players if p.vote == C.OPTIMAL_OPTION]
    for p in are_correct_list:
        p.is_correct = True

    not_correct_list = [p for p in players if p.vote != C.OPTIMAL_OPTION]
    for p in not_correct_list:
        p.is_correct = False


    option1_voter_list = [p for p in players if p.vote == C.SUBOPTIML_OPTION1]
    option2_voter_list = [p for p in players if p.vote == C.SUBOPTIML_OPTION2]
    option3_voter_list = [p for p in players if p.vote == C.SUBOPTIML_OPTION3]
    option5_voter_list = [p for p in players if p.vote == C.PSSIMAL_OPTION]
    group.votes_for_optimal = len(are_correct_list)
    group.votes_for_option1 = len(option1_voter_list)
    group.votes_for_option2 = len(option2_voter_list)
    group.votes_for_option3 = len(option3_voter_list)
    group.votes_for_option5 = len(option5_voter_list)
    popular_other_vote = max(group.votes_for_option1,group.votes_for_option2,group.votes_for_option3,group.votes_for_option5)
    if group.votes_for_optimal > 2:
        group.group_wins = True
        for p in players:
            p.payoff = C.PAYOFF
    elif group.votes_for_optimal == 2:
        if group.votes_for_optimal > popular_other_vote:
            group.group_wins = True
            for p in players:
                p.payoff = C.PAYOFF
        else:
            group.group_wins = False
    else:
        group.group_wins = False
        Player.payoff = cu(0)

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['vote']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs



class Results(Page):
    pass



page_sequence = [MyPage, ResultsWaitPage, Results]