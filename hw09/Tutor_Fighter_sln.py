from Tutor_Fighter_data import *
import random

def doctests_go_here():
    """
    Contains all the doctests for the question.

    >>> card = full_deck[12]
    >>> print(card)
    ('Marina the Marvel 50', 'WM')

    # Card Class tests

    >>> card_name1 = full_deck[5][0]
    >>> card_name2 = full_deck[24][0]
    >>> card_name3 = full_deck[37][0]
    >>> card_name4 = full_deck[48][0]
    >>> warrior_card = Warrior_Card(card_name1)
    >>> dragon_card  = Dragon_Card(card_name2)
    >>> secret_card  = Secret_Card(card_name3)
    >>> yuxuan_card  = Yuxuan_Card(card_name4)

    >>> print(warrior_card)
    Card name: Warrior 7, number: 7, suit: WM, card type: ordinary
    >>> print(dragon_card)
    Card name: Nabi the Noble 40, number: 40, suit: DC, card type: special
    >>> print(secret_card)
    Card name: Wesley the Wrecker -20, number: -20, suit: SS, card type: \
special
    >>> print(yuxuan_card)
    Card name: Emissary 11, number: 11, suit: YE, card type: special

    >>> warrior_card.get_skill(dragon_card)
    12
    >>> dragon_card.get_skill(warrior_card)
    0
    >>> secret_card.get_skill(yuxuan_card)
    32
    >>> yuxuan_card.get_skill(dragon_card)
    34

    # Player Class Tests

    >>> Player_1 = Player("Player_1")
    >>> Player_1 + 1
    Incorrect type: got: <class 'int'>, expected Card object, card not added
    Player("Player_1", 0)
    >>> Player_1 + warrior_card + dragon_card
    Player("Player_1", 0)
    >>> for card in Player_1.cards: print(card)
    Card name: Warrior 7, number: 7, suit: WM, card type: ordinary
    Card name: Nabi the Noble 40, number: 40, suit: DC, card type: special
    >>> print(Player_1)
    name: Player_1, score: 0, cards: [Warrior_Card("Warrior 7"), \
Dragon_Card("Nabi the Noble 40")]
    >>> Player_1 = Player_1 - warrior_card - dragon_card
    >>> print(Player_1)
    name: Player_1, score: 0, cards: []
    >>> Player_1 = Player_1 + 3
    Incorrect type: got: <class 'int'>, expected Card object, card not added
    >>> Player_1 = Player_1 + Player_1
    Incorrect type: got: <class 'Tutor_Fighter_sln.Player'>, expected Card \
object, card not added

    # Game Class Tests

    # No shuffling for game 0, game gives the first two cards (Warrior 2 and 3)
    # to Player 1, the next two cards (Warrior 4 and 5) to Player 2
    >>> game0 = Game(2, ["Player 1", "Player 2"])
    >>> print(game0.deck[:4])
    [('Warrior 2', 'WM'), ('Warrior 3', 'WM'), ('Warrior 4', 'WM'), \
('Warrior 5', 'WM')]
    >>> game0.deal_cards()
    >>> result = game0.play()
    >>> print(result)
    Round: 1
    Card 1: Card name: Warrior 2, number: 2, suit: WM, card type: ordinary
    Card 2: Card name: Warrior 4, number: 4, suit: WM, card type: ordinary
    Winner: Player 2, total score: 1
    Score gained by Player 2: 1
    Winner Card: Warrior 4
    The card chants: Marina before all!
    Player's Total Scores: Player 1: 0 points, Player 2: 1 points
    <BLANKLINE>
    Round: 2
    Card 1: Card name: Warrior 3, number: 3, suit: WM, card type: ordinary
    Card 2: Card name: Warrior 5, number: 5, suit: WM, card type: ordinary
    Winner: Player 2, total score: 2
    Score gained by Player 2: 1
    Winner Card: Warrior 5
    The card chants: Marina before all!
    Player's Total Scores: Player 1: 0 points, Player 2: 2 points
    <BLANKLINE>
    Winning player: Player 2

    >>> game1 = Game(28, ["Player 1", "Player 2"])
    Something is wrong with the parameters
    Game not populated
    >>> game1 = Game(28, [32, "Player 2"])
    Something is wrong with the parameters
    Game not populated
    >>> game1 = Game(1, ["Player_1", "Player_2"])
    >>> random.seed(1)
    >>> random.shuffle(game1.deck)
    >>> print(game1.deck[:2])
    [('Emissary 12', 'YE'), ('Sudi the Sincere 11', 'WM')]
    >>> game1.deal_cards()
    >>> result = game1.play()
    >>> print(result)
    Round: 1
    Card 1: Card name: Emissary 12, number: 12, suit: YE, card type: special
    Card 2: Card name: Sudi the Sincere 11, number: 11, suit: WM, card type: \
special
    Winner: Player_1, total score: 2
    Score gained by Player_1: 2
    Winner Card: Emissary 12
    The card chants: I am the Piazza!
    Player's Total Scores: Player_1: 2 points, Player_2: 0 points
    <BLANKLINE>
    Winning player: Player_1

    >>> game2 = Game(2, ["Player_1", "Player_2"])
    >>> random.seed(2)
    >>> random.shuffle(game2.deck)
    >>> print(game2.deck[:4])
    [('Dragon 4', 'DC'), ('Secret 5', 'SS'), ('Sudi the Sincere 11', 'WM'), \
('Dragon 10', 'DC')]
    >>> game2.deal_cards()
    >>> result = game2.play()
    >>> print(result)
    Round: 1
    Card 1: Card name: Dragon 4, number: 4, suit: DC, card type: ordinary
    Card 2: Card name: Sudi the Sincere 11, number: 11, suit: WM, card type: \
special
    Winner: Player_2, total score: 2
    Score gained by Player_2: 2
    Winner Card: Sudi the Sincere 11
    The card chants: Marina before all!
    Player's Total Scores: Player_1: 0 points, Player_2: 2 points
    <BLANKLINE>
    Round: 2
    Card 1: Card name: Secret 5, number: 5, suit: SS, card type: ordinary
    Card 2: Card name: Dragon 10, number: 10, suit: DC, card type: ordinary
    Winner: Player_2, total score: 3
    Score gained by Player_2: 1
    Winner Card: Dragon 10
    The card chants: All hail the Recursive Dragon!
    Player's Total Scores: Player_1: 0 points, Player_2: 3 points
    <BLANKLINE>
    Winning player: Player_2


    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    pass

class Card():
    """
    This class is the parent for all other card types. It is not used directly,
    meaning no direct instances of Card will be created. This class includes
    methods which are common among all the derived (child) classes such as
    Dragon_Card. Keep in mind that for an instance of a child class, such as
    dc1 = Dragon_Card("Dragon 2"), isinstance(dc1, Card) == True.
    """
    # Class Attributes
    card_types = ["ordinary", "special", "leader"]

    # Constructor
    def __init__(self, name):
        """ Constructor for Card Class, will be used by all child instances.

        Instance attributes to initialize:
        name(str): Card's name (ie "Warrior 9")
        number(int): Card's number (ie. 9)
        card_type(str): Card's type (ie. "ordinary"). To determine the Card's
        type, you can use the suit & suit_comp variable of the child Classes.

        Parameters:
        name (str): The name of the card. Assume it will be a string.

        Returns: None
        """
        self.name = name
        self.number = int(name.split()[-1])
        card_types = Card.card_types
        card_type = card_types[0]
        for i in range(len(card_types)):
            if (self.name, self.suit) in self.suit_comp[i]:
                card_type = card_types[i]
        self.card_type = card_type

    # Comparators
    def __eq__(self, other):
        """Compares the skill levels of self and another card instance (other).
        All faction related rules are applied during the skill calculations.
        For example Nabi the Noble reduces to 0 skill (forfeits) if the other
        card has a number <= 10.
        Returns True if the final calculated skills are equal. False ow."""
        my_skill = self.get_skill(other)
        other_skill = other.get_skill(self)
        return my_skill == other_skill
    def __ne__(self, other):
        """ Similar to __eq__ compares the skill levels of self and other.
        Returns True if the final calculated skills are not equal. False ow.
        """
        return not self.__eq__(other)
    def __gt__(self, other):
        """Compares skills, returns True if self has higher skill, False ow."""
        my_skill = self.get_skill(other)
        other_skill = other.get_skill(self)
        return my_skill > other_skill
    def __ge__(self, other):
        """Compares skills, greater than or equal to method."""
        return self.__eq__(other) or self.__gt__(other)
    def __lt__(self, other):
        """Compares skills, less than method."""
        return not (self.__eq__(other) or self.__gt__(other))
    def __le__(self, other):
        """Compares skills, less than or equal to method."""
        return self.__eq__(other) or (not self.__gt__(other))

    # String and repr representations
    def __str__(self):
        """ String representation for any derived Card instance. """
        str_form = "Card name: {0}, number: {1}, suit: {2}, card type: {3}"
        str_form = str_form.format(self.name, self.number, self.suit,\
                   self.card_type)
        return str_form
    def __repr__(self):
        """ Repr for any derived Card instance. """
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form

class Warrior_Card(Card):
    """ This class represents all cards belonging to Warriors of Marina.
    Inherits from the Card class """

    # Class Attributes
    suit = "WM"
    chant = "Marina before all!"
    traitor_offset = 5
    special_card_bonus = 10
    suit_comp = [warrior_ordinary, warrior_specials, warrior_leader]

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is a different card from any suit. Note that you should be
        using the traitor_offset, which is the suit bonus of 'WM' """
        skill_lvl = self.number
        if self.card_type == "special":
            skill_lvl += Warrior_Card.special_card_bonus
        if other_card.suit in ["DC", "SS"] :
            return skill_lvl + Warrior_Card.traitor_offset
        else:
            return skill_lvl

class Dragon_Card(Card):
    """ This class represents all cards belonging to Dragon's Children.
    Inherits from the Card class """

    # Class Attributes
    suit = "DC"
    chant = "All hail the Recursive Dragon!"
    suit_comp = [dragon_ordinary, dragon_specials, dragon_leader]

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is another card instance of any suit. Notice the skill
        calculations will be different for different card types (special,
        ordinary, leader)"""
        if self.card_type == "special":
            if other_card.number <= 10:
                return 0
            else:
                return self.number
        elif self.card_type == "ordinary":
            skill = ((self.number) ** 2) / 4
            return skill
        else: # self.card_type == "Leader"
            return self.number

class Secret_Card(Card):
    """ This class represents all cards belonging to Secret Strikers.
    Inherits from the Card class """

    # Class Attributes
    suit = "SS"
    chant = "We shall strike again!"
    suit_comp = [secret_ordinary, secret_specials, secret_leader]
    secret_offset = 12

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is another card instance of any suit. Notice you should
        be using the secret_offset variable in the calculations. Also keep in
        mind the suit bonus of the Secret Strikers. """
        if other_card.suit != "SS":
            if self.card_type in ["ordinary", "special"]:
                return Secret_Card.secret_offset - self.number
            else: # self.card_type == "Leader"
                return self.number
        else:
            return self.number

class Yuxuan_Card(Card):
    """ This class represents all cards belonging to Yuxuan's Emissaries.
    Inherits from the Card class """

    # Class Attributes
    suit = "YE"
    chant = "I am the Piazza!"
    suit_comp = [yuxuan_ordinary, yuxuan_specials, yuxuan_leader]
    ord_mult = 0.8
    spe_mult = 4
    dragon_fear_offset = -10

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is another card instance of any suit. Keen in mind that
        different rules apply for different card types. Also keep in mind the
        suit bonus of Yuxuan's Emissaries."""
        if self.card_type == "ordinary":
            return self.number * Yuxuan_Card.ord_mult
        elif self.card_type == "special":
            skill = self.number * Yuxuan_Card.spe_mult
            if other_card.suit == "DC":
                return skill + Yuxuan_Card.dragon_fear_offset
            else:
                return skill
        else: # self.card_type == "Leader"
            return self.number

class Player():
    """ This class represents one of the two players of the game."""

    # Constructor
    def __init__(self, player_name):
        """ Consturctor for the Player class. Initiazlies a player instance

        Instance attributes to initialize:
        name(str): Player's name (ie. "Player_1")
        cards(list): Should be initialized as an empty list.
        score(int): Should be initialized to 0.

        Parameters:
        player_name (str): The name of the player. Assume it will be a string.

        Returns: None
        """
        self.name = player_name
        self.cards = []
        self.score = 0

    # Add card special method
    def __add__(self, new_card):
        """ Special __add__ method used to add new_card to the player's hand.
        Requirements: call the method process_card to make sure the supplied
        parameter is of correct type. If True add card to the players cards.
        If False, do not operate on the users cards.

        Parameters: new_card(child of Card) a card belonging to one of the 4
        suits. This card should be added to this player's cards.

        Returns self (regardless of input correctness). This way we can write
        operations like:
        player1 + card1 + card2 + card3   # Which proceeds as follows:
        (player1 + card1) + card2 + card3 # the expression in () is executed
                                          # and returns the player1 instance
        (player1 + card2) + card3         # same as above
        (player1 + card3)                 # same as above
        player1                           # the line above returns the instance
        player1.cards --> [card1, card2, card3] # all cards added

        This idea will also be mentioned in the mini discussion.
        """
        card_ok = Player.process_card(new_card)
        if card_ok:
            self.cards.append(new_card)
            return self
        else:
            return self

    # Remove Card special method
    def __sub__(self, old_card):
        """ Special __sub__ method used to remove old_card from the player's
        hand.
        Requirements: call the method process_card to make sure the supplied
        parameter is of correct type. If True remove card from cards list.
        If False, do not operate on cards list.

        Parameters: old_card(child of Card) a card belonging to one of the 4
        suits. This card should be removed from this players cards.

        Returns self (regardless of input correctness): The same idea as add:

        player1.cards --> [card1, card2, card3]
        player1 - card1 - card2 - card3   # Will proceed as follows:
        (player1 - card1) - card2 - card3 # the expression in () is executed
                                          # and returns the player1 instance
        (player1 - card2) - card3         # same as above
        (player1 - card3)                 # same as above
        player1                           # the line above returns the instance
        player1.cards --> []              # all cards removed
        """
        card_ok = Player.process_card(old_card)
        if card_ok:
            self.cards.remove(old_card)
            return self
        else:
            return self

    # String and repr representations
    def __str__(self):
        """ String representation for a Player instance. """
        str_form = "name: {0}, score: {1}, cards: {2}"
        str_form = str_form.format(self.name, self.score, self.cards)
        return str_form
    def __repr__(self):
        """ Repr for a Player instance. """
        repr_form = "{0}(\"{1}\", {2})"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name, self.score)
        return repr_form

    # Helper method
    def process_card(a_card):
        """ Helper method which checks if the supplied card parameter is
        an instance of the Card class. Uses a try - except block.

        Requirements: You should use a try - except block. In the try block
        you should check if isinstance(a_card, Card) (subclasses count as
        instances of the parent class). If false, print the output as shown in
        the doctest. For example:
        Incorrect type: got: <class 'int'>, expected Card object, card not
        added

        Parameters: a_card(unknown type) input parameter to validate.

        Returns boolean (True if instance of card, False otherwise)
        """
        try:
            if isinstance(a_card, Card) == False:
                raise TypeError()
        except:
            excp = "Incorrect type: got: {0}, expected Card object".\
                    format(type(a_card))
            excp += ", card not added"
            print(excp)
            return False
        return True

class Game():
    """ This represents a single game between two players. It creates two
    Player instances, deals them a certain number of cards. Then it implements
    each round of the game, calculating an logging the output. Finally, it
    logs the winner(s) of the game."""
    # Class Attributes
    MAX_DECK_SIZE = int(len(full_deck) / 2)
    PLAYERS_COUNT = 2
    suit_tie_breaker = ["SS", "WM", "YE", "DC"]

    # Constructor
    def __init__(self, cards_per_player, player_names):
        """ Consturctor for the Game class. First processes the parameters
        with the process input method. If the result is False, calls
        print("Game not populated") and quits. If result is True initializes
        the instance attributes.

        Requirements: Should call the process_input method of Game with the
        given parameters.

        Instance attributes to initialize:
        deck(full_deck): initialized as a deep copy of full_deck.
            This deck will be shuffled during tests: random.shuffle(self.deck)
        cards_per_player(int): set according to the given parameter
        players(list): First initialized as empty list. It is then populated
            by two player instances, created according to the player_names.

        Parameters:
        cards_per_player(int): How many cards should be dealt to each player
        player_names(list): List of player names (strings)

        Returns: None
        """
        param_ok = Game.process_input(cards_per_player, player_names)
        if param_ok:
            self.deck = list(full_deck)
            self.cards_per_player = cards_per_player
            self.players = []
            for player_name in player_names:
                self.players.append(Player(player_name))
        else:
            print("Game not populated")

    def deal_cards(self):
        """
        Deals cards_per_player (unique) cards to each player in self.players
        Removes these cards from the deck of Game. Each card in the deck is in
        tuple form. According to the type specified in this tuple, this method
        creates a new card.
        ie. ("Warrior 9", "WM")   --> Warrior_Card("Warrior 9")
        ie. ("Dragon 6", "DC")    --> Dragon_Card("Dragon 6")
        ie. ("Secret 2", "SS")    --> Secret_Card("Secret 2")
        ie. ("Emissary 4", "YE")  --> Yuxuan_Card("Emissary 4")

        You should use the __add__method while adding, such as
        self.player += new_card
        """
        for self.player in self.players:
            for i in range(self.cards_per_player):
                card_name, card_type = self.deck.pop(0) #card removed from deck
                if card_type == "WM":
                    new_card = Warrior_Card(card_name)
                elif card_type == "DC":
                    new_card = Dragon_Card(card_name)
                elif card_type == "SS":
                    new_card = Secret_Card(card_name)
                else: # card_type == "YE":
                    new_card = Yuxuan_Card(card_name)
                self.player += new_card

    def play(self):
        """ Plays cards_per_player rounds of the game, until both players run
        of of cards. At each round, it removes the first card of player.cards
        for each player instance. It then compares these cards (using the
        comparators of Card class). It breaks ties according to the index of
        suit_tie_breaker (higher index means winner). It calls log_round
        method during each round and adds to the current log. When the final
        round is over, it calls the log_winners method and adds the result to
        log. Finally, it sets cards_per_player to 0 and returns the log.
        """
        log = ""
        for cur_round in range(self.cards_per_player):
                pla0_card = self.players[0].cards.pop(0)
                pla1_card = self.players[1].cards.pop(0)
                cur_cards = [pla0_card, pla1_card]
                if pla0_card  > pla1_card:
                    winner = 0
                elif pla0_card == pla1_card:
                    pla0_suit = Game.suit_tie_breaker.index(pla0_card.suit)
                    pla1_suit = Game.suit_tie_breaker.index(pla1_card.suit)
                    winner = (pla0_suit < pla1_suit) * 1
                else: # pla1_card < pla2_card:
                    winner = 1
                score_gained = 1 + Card.card_types.index(cur_cards[winner].\
                                                         card_type)
                self.players[winner].score += score_gained
                log += self.log_round(cur_round, winner, \
                            [pla0_card, pla1_card], score_gained)
        log += self.log_winners()
        self.cards_per_player = 0
        return log

    def process_input(cards_per_player, player_names):
        """ Processes the input according to the given Class Attributes.
        Validates the inputs cards_per_player(int) and player_names(list)
        There should be PLAYERS_COUNT players and cards_per_player should be
        <= MAX_DECK_SIZE.

        Requirements: Should have a try catch block validating the input. The
        following should be checked, types of both inputs. player_names' lenght
        is equal to PLAYERS_COUNT. cards_per_player is <= MAX_DECK_SIZE.
        Finally all elements of player_names should have type str

        Parameters:
        cards_per_player(int)
        player_names(list): All elements are strings

        Returns: boolean (True if parameters valid, False otherwise)
        """
        try:
            bool_val = isinstance(player_names, list) and (len(player_names)\
                       == Game.PLAYERS_COUNT) and all(isinstance(elem, str) \
                   for elem in player_names) and isinstance(cards_per_player,\
                       int) and cards_per_player <= Game.MAX_DECK_SIZE
            if bool_val == False:
                raise ValueError()
        except:
            print("Something is wrong with the parameters")
            return False
        return True

    def log_round(self, round_num, winner, cards, score_gained):
        """ Logs round info according to the given parameters, and as shown on
        the write-up and doctests. Appends an empty line at the end.

        Parameters:
        round_num(int): Indicates the current round number - 1
        winner(int): 0 or 1, indicates the index of the winning player
        cards(list): Contains the two cards of the current round. cards[0] is
            the card of players[0]. cards[1] is the card of players[1].
        score_gained(int): indicates the score gained by the winner player.

        Returns: log(str): Log of the current round.
        """
        winner_player = self.players[winner]
        log = ""
        log += "Round: {0}\n".format(round_num + 1)
        log += "Card 1: {0}\n".format(cards[0])
        log += "Card 2: {0}\n".format(cards[1])
        log += "Winner: {0}, total score: {1}\n".format(winner_player.name, \
                                              winner_player.score)
        log += "Score gained by {0}: {1}\n".format(winner_player.name,\
                                          score_gained)
        log += "Winner Card: {0}\n".format(cards[winner].name)
        log += "The card chants: {0}\n".format(cards[winner].chant)
        log += "Player's Total Scores: {0}: {1} points, {2}: {3} points\n\n"\
        .format(self.players[0].name, self.players[0].score,\
                self.players[1].name, self.players[1].score)
        return log

    def log_winners(self):
        """ Logs the winner(s) of the game according to scores. For example:
        If only Player_1 has higher score, so Player_1 won:
        log = Winning player: Player_1
        If both players have the same score, so both won:
        log = Winning players: Player_1 and Player_2

        Returns: log(str): Log of the winners of this game.
        """
        log = ""
        score0 = self.players[0].score
        score1 = self.players[1].score
        if score0 == score1:
            log += "Winning players: {0} and {1}".format(self.players[0].name,\
                  self.players[1].name)
        elif score0 > score1:
            log += "Winning player: {0}".format(self.players[0].name)
        else: # score0 < score1:
            log += "Winning player: {0}".format(self.players[1].name)
        return log
