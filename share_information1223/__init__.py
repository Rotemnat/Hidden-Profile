from otree.api import *

doc = """
Pay for a random round for guessing the best option
"""


class C(BaseConstants):
    NAME_IN_URL = 'share_information1223'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 8
    ENDOWMENT = cu(50)
    OPTIMAL_OPTION = 'פרויקט E'
    DATA_TEMPLATE = __name__ + '/Infoset.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    randomly_selected_round = models.IntegerField()
    info_item1 = models.StringField(
        choices=[
            "פרויקט A שלילי בקריטריון I",
            "פרויקט B חיובי בקריטריון I",
            "פרויקט C שלילי בקריטריון I",
            "פרויקט D שלילי בקריטריון I",
            "פרויקט D שלילי בקריטריון II",
            "פרויקט E שלילי בקריטריון II",
            "פרויקט A שלילי בקריטריון III",
            "פרויקט E חיובי בקריטריון III",
            "פרויקט A שלילי בקריטריון IV",
            "פרויקט B חיובי בקריטריון IV",
            "פרויקט C שלילי בקריטריון V",
            "פרויקט D חיובי בקריטריון V",
            "פרויקט A חיובי בקריטריון VI",
            "פרויקט C שלילי בקריטריון VI",
            "פרויקט E שלילי בקריטריון VI",
        ],
        label="איזה פריט מידע תבחרו לשתף?",
    )

    info_item2 = models.StringField(
        choices=[
            "פרויקט A שלילי בקריטריון I",
            "פרויקט D שלילי בקריטריון I",
            "פרויקט E חיובי בקריטריון I",
            "פרויקט A חיובי בקריטריון II",
            "פרויקט B שלילי בקריטריון II",
            "פרויקט C חיובי בקריטריון II",
            "פרויקט E שלילי בקריטריון II",
            "פרויקט B שלילי בקריטריון III",
            "פרויקט C חיובי בקריטריון III",
            "פרויקט D חיובי בקריטריון III",
            "פרויקט A שלילי בקריטריון IV",
            "פרויקט B חיובי בקריטריון IV",
            "פרויקט C חיובי בקריטריון IV",
            "פרויקט D שלילי בקריטריון IV",
            "פרויקט D חיובי בקריטריון V",
            "פרויקט E חיובי בקריטריון V",
            "פרויקט B שלילי בקריטריון VI",
            "פרויקט E שלילי בקריטריון VI"
        ],
        label="איזה פריט מידע תבחרו לשתף?",
    )
    info_item3 = models.StringField(
        choices=[
            "פרויקט A שלילי בקריטריון I",
            "פרויקט B חיובי בקריטריון I",
            "פרויקט C שלילי בקריטריון I",
            "פרויקט E חיובי בקריטריון I",
            "פרויקט B שלילי בקריטריון II",
            "פרויקט C חיובי בקריטריון II",
            "פרויקט A שלילי בקריטריון III",
            "פרויקט D חיובי בקריטריון III",
            "פרויקט B חיובי בקריטריון IV",
            "פרויקט C חיובי בקריטריון IV",
            "פרויקט E חיובי בקריטריון IV",
            "פרויקט A חיובי בקריטריון V",
            "פרויקט C שלילי בקריטריון V",
            "פרויקט D חיובי בקריטריון V",
            "פרויקט A חיובי בקריטריון VI",
            "פרויקט B שלילי בקריטריון VI",
            "פרויקט D חיובי בקריטריון VI",
            "פרויקט E שלילי בקריטריון VI"
        ],
        label="איזה פריט מידע תבחרו לשתף?",
    )
    info_item4 = models.StringField(
        choices=[
            "פרויקט B חיובי בקריטריון I",
            "פרויקט D שלילי בקריטריון I",
            "פרויקט A חיובי בקריטריון II",
            "פרויקט D שלילי בקריטריון II",
            "פרויקט E שלילי בקריטריון II",
            "פרויקט B שלילי בקריטריון III",
            "פרויקט C חיובי בקריטריון III",
            "פרויקט B חיובי בקריטריון IV",
            "פרויקט D שלילי בקריטריון IV",
            "פרויקט A חיובי בקריטריון V",
            "פרויקט B שלילי בקריטריון V",
            "פרויקט C שלילי בקריטריון V",
            "פרויקט D חיובי בקריטריון V",
            "פרויקט E חיובי בקריטריון V",
            "פרויקט A חיובי בקריטריון VI"
        ],
        label="איזה פריט מידע תבחרו לשתף?",
    )



class Player(BasePlayer):
    # vars for players opinien and level of confidance
    preferred_option = models.StringField(
        choices=['פרויקט A', 'פרויקט B', 'פרויקט C', 'פרויקט D', 'פרויקט E'],
        label="אם היה עליך להצביע עכשיו לאיזו חלופה היית מעניק.ה את קולך?"
    )

    level_of_confidence = models.FloatField(
        min=20,
        max=100,
        label="מה מידת הביטחון שלך בחלופה?"
    )
    correct_in_round = models.BooleanField()

# vars for information sharing


# FUNCTIONS

def set_outcomes(group):
    for player in group.get_players():
        if player.preferred_option == C.OPTIMAL_OPTION:
            player.correct_in_round = True
        else:
            player.correct_in_round = False


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Input(Page):
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
        pic_address = 'app1223/infoset{}.{}.png'.format(base_number, id_in_group)
        return dict(
            id_in_group=id_in_group,
            pic_address=pic_address,
        )


class MyPage(Page):
    form_model = 'player'
    form_fields = ['preferred_option', 'level_of_consciousness']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant

        # if it's the last round
        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS-1)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            if player_in_selected_round.correct_in_round:
                player_in_selected_round.payoff = C.ENDOWMENT + (C.ENDOWMENT * player_in_selected_round.level_of_confidence / 100)
            else:
                player_in_selected_round.payoff = C.ENDOWMENT - (C.ENDOWMENT * player_in_selected_round.level_of_confidence / 100)

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_outcomes


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        id_in_group = player.id_in_group
        base_number = 1
        pic_address = 'app1223/infoset{}.{}.png'.format(base_number, id_in_group)
        return dict(
            players=group.get_players(),
            id_in_group=id_in_group,
            pic_address=pic_address,
        )


class TempResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Input, MyPage, ResultsWaitPage, Results]
