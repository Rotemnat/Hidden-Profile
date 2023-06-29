from otree.api import *

doc = """
Pay for a random round for guessing the best option
"""


class C(BaseConstants):
    NAME_IN_URL = 'share_information1111'
    PLAYERS_PER_GROUP = 1
    NUM_ROUNDS = 1
    ENDOWMENT = cu(50)
    OPTIMAL_OPTION = 'פרויקט A'
    DATA_TEMPLATE = __name__ + '/Infoset.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    info_item1 = models.StringField(
        choices=[
            'פרויקט A חיוביי בקריטריון II',
            'פרויקט B חיובי בקריטריון II',
            'פרויקט D חיובי בקריטריון II',
            'פרויקט E חיובי בקריטריון II',
            'פרויקט D חיובי בקריטריון III',
            'פרויקט E חיובי בקריטריון III',
            'פרויקט A חיוביי בקריטריון IV',
            'פרויקט B שלילי בקריטריון IV',
            'פרויקט C שלילי בקריטריון IV',
            'פרויקט D שלילי בקריטריון IV',
            'פרויקט E שלילי בקריטריון IV',
            'פרויקט A חיובי בקריטריון V',
            'פרויקט B חיובי בקריטריון V',
            'פרויקט C שלילי בקריטריון V',
            'פרויקט D שלילי בקריטריון V',
            'פרויקט B שלילי בקריטריון VI',
            'פרויקט D חיובי בקריטריון VI',
            'פרויקט E חיובי בקריטריון VI',
        ],
        label="איזה פריט מידע תבחרו לשתף?"
    )

    info_item2 = models.StringField(
        choices=[
            'פרויקט B חיובי בקריטריון II',
            'פרויקט D חיובי בקריטריון II',
            'פרויקט E חיובי בקריטריון II',
            'פרויקט A שלילי בקריטריון III',
            'פרויקט C שלילי בקריטריון III',
            'פרויקט D חיובי בקריטריון III',
            'פרויקט E חיובי בקריטריון III',
            'פרויקט A חיוביי בקריטריון IV',
            'פרויקט B שלילי בקריטריון IV',
            'פרויקט C שלילי בקריטריון IV',
            'פרויקט A חיובי בקריטריון V',
            'פרויקט C שלילי בקריטריון V',
            'פרויקט A חיובי בקריטריון VI',
            'פרויקט B שלילי בקריטריון VI',
            'פרויקט C חיובי בקריטריון VI',
        ],
        label="איזה פריט מידע תבחרו לשתף?"
    )
    info_item3 = models.StringField(
        choices=[
            'פרויקט A חיוביי בקריטריון II',
            'פרויקט B חיובי בקריטריון II',
            'פרויקט D חיובי בקריטריון II',
            'פרויקט E חיובי בקריטריון II',
            'פרויקט A שלילי בקריטריון III',
            'פרויקט B חיובי בקריטריון III',
            'פרויקט C שלילי בקריטריון III',
            'פרויקט A חיוביי בקריטריון IV',
            'פרויקט B שלילי בקריטריון IV',
            'פרויקט C שלילי בקריטריון IV',
            'פרויקט D שלילי בקריטריון IV',
            'פרויקט E שלילי בקריטריון IV',
            'פרויקט B חיובי בקריטריון V',
            'פרויקט C שלילי בקריטריון V',
            'פרויקט D שלילי בקריטריון V',
            'פרויקט B שלילי בקריטריון VI',
            'פרויקט D חיובי בקריטריון VI',
            'פרויקט E חיובי בקריטריון VI',
        ],
        label="איזה פריט מידע תבחרו לשתף?"
    )
    info_item4 = models.StringField(
        choices=[
            'פרויקט B חיובי בקריטריון II',
            'פרויקט D חיובי בקריטריון II',
            'פרויקט E חיובי בקריטריון II',
            'פרויקט D חיובי בקריטריון III',
            'פרויקט E חיובי בקריטריון III',
            'פרויקט A חיוביי בקריטריון IV',
            'פרויקט B שלילי בקריטריון IV',
            'פרויקט C שלילי בקריטריון IV',
            'פרויקט D שלילי בקריטריון IV',
            'פרויקט A חיובי בקריטריון V',
            'פרויקט C שלילי בקריטריון V',
            'פרויקט E שלילי בקריטריון V',
            'פרויקט A חיובי בקריטריון VI',
            'פרויקט B שלילי בקריטריון VI',
            'פרויקט C חיובי בקריטריון VI',
        ],
        label="איזה פריט מידע תבחרו לשתף?"
    )


class Player(BasePlayer):
    # vars for players opinien and level of confidance
    preferred_option = models.StringField(
        choices=['פרויקט A', 'פרויקט B', 'פרויקט C', 'פרויקט D', 'פרויקט E'],
        label="אם היה עליך להצביע עכשיו לאיזו חלופה היית מעניק.ה את קולך?"
    )

    level_of_consciousness = models.FloatField(
        initial= None,
        min=20,
        max=100,
        label="מה מידת הביטחון שלך בחלופה?"
    )
    correct_in_round = models.BooleanField()
    potential_payoff = models.CurrencyField(initial=None)


# vars for information sharing


# FUNCTIONS

'''
def set_outcomes(group):
    for player in group.get_players():
        if player.preferred_option == C.OPTIMAL_OPTION:
            player.correct_in_round = True
        else:
            player.correct_in_round = False
'''

# PAGES
class Introduction1(Page):
    pass

class Introduction2(Page):
    pass

class Introduction3(Page):
    pass

class Introduction4(Page):
    pass

class Introduction5(Page):
    pass

class Introduction6(Page):
    pass

class Introduction7(Page):
    pass

class Introduction8(Page):
    pass

class Introduction10(Page):
    pass

class Introduction11(Page):
    pass

class Input9(Page):
    form_model = 'group'

    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 1:
            return ['info_item1']
        elif player.id_in_group == 2:
            return ['info_item2']
        elif player.id_in_group == 3:
            return ['info_item3']
        else:
            return ['info_item4']

    def vars_for_template(player: Player):
        id_in_group = player.id_in_group
        base_number = 1
        pic_address = 'app11111/infoset{}.{}.png'.format(base_number, id_in_group)
        return dict(
            id_in_group=id_in_group,
            pic_address=pic_address,
        )


class MyPage11(Page):
    form_model = 'player'
    form_fields = ['preferred_option', 'level_of_consciousness']

'''    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant
        #participant.potential_payoff = player.potential_payoff

        # if it's the last round
        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS-1)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            if player_in_selected_round.correct_in_round:
                player.payoff = C.ENDOWMENT + (C.ENDOWMENT * player_in_selected_round.level_of_consciousness / 100)
            else:
                player.payoff = C.ENDOWMENT - (C.ENDOWMENT * player_in_selected_round.level_of_consciousness / 100)

'''
class ResultsWaitPage(WaitPage):
    pass
    #after_all_players_arrive = set_outcomes


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        id_in_group = player.id_in_group
        base_number = 1
        pic_address = 'app1111/infoset{}.{}.png'.format(base_number, id_in_group)
        return dict(
            players=group.get_players(),
            id_in_group=id_in_group,
            pic_address=pic_address,
        )


'''
class TempResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
'''

page_sequence = [Introduction1,Introduction2,Introduction3,Introduction4, Introduction5, Introduction6, Introduction7, Introduction8, Input9, Introduction10, MyPage11, Introduction11,  ResultsWaitPage, Results]
