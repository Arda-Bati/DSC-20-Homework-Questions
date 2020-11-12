"""
HW 9, Q4. Tutor Fighter Card Game implementation.
"""

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
    Incorrect type: got: <class 'Tutor_Fighter.Player'>, expected Card object\
, card not added

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
        ## YOUR CODE IS HERE ##

    # Comparators
    def __eq__(self, other):
        """Compares the skill levels of self and another card instance (other).
        All faction related rules are applied during the skill calculations.
        For example Nabi the Noble reduces to 0 skill (forfeits) if the other
        card has a number <= 10.
        Returns True if the final calculated skills are equal. False ow."""
        ## YOUR CODE IS HERE ##

    def __ne__(self, other):
        """ Similar to __eq__ compares the skill levels of self and other.
        Returns True if the final calculated skills are not equal. False ow.
        """
        ## YOUR CODE IS HERE ##

    def __gt__(self, other):
        """Compares skills, returns True if self has higher skill, False ow."""
        ## YOUR CODE IS HERE ##

    def __ge__(self, other):
        """Compares skills, greater than or equal to method."""
        ## YOUR CODE IS HERE ##

    def __lt__(self, other):
        """Compares skills, less than method."""
        ## YOUR CODE IS HERE ##

    def __le__(self, other_card):
        """Compares skills, less than or equal to method."""
        ## YOUR CODE IS HERE ##

    # String and repr representations
    def __str__(self):
        """ String representation for any derived Card instance. Please check
        the doctests for examples. """
        str_form = "Card name: {0}, number: {1}, suit: {2}, card type: {3}"
        ## YOUR CODE IS BELOW IN ... ##
        ## You should uncomment the commented code
        # str_form = str_form.format(...)
        return str_form
    def __repr__(self):
        """ Repr for any derived Card instance. Please check the doctests for
        examples. """
        repr_form = "{0}(\"{1}\")"
        ## YOUR CODE IS BELOW IN ... ##
        ## You should uncomment the commented code
        class_name = self.__class__.__name__
        # repr_form = repr_form.format(...)
        return repr_form

class Warrior_Card(Card):
    """ This class represents all cards belonging to Warriors of Marina.
    Inherits from the Card class """

    # Class Attributes
    suit = "WM"
    chant = "Marina before all!"
    traitor_offset = 5
    suit_comp = [warrior_ordinary, warrior_specials, warrior_leader]

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is a different card from any suit. Note that you should be
        using the traitor_offset, which is the suit bonus of 'WM' """
        ## YOUR CODE IS HERE ##

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
        ## YOUR CODE IS HERE ##

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
        ## YOUR CODE IS HERE ##

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
        suit bonus of Yuxuan's Emissaries (use dragon_fear_offset for it)."""
        ## YOUR CODE IS HERE ##

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
        ## YOUR CODE IS HERE ##

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
        ## YOUR CODE IS HERE ##

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
        ## YOUR CODE IS HERE ##

    # String and repr representations
    def __str__(self):
        """ String representation for a Player instance. Please check the
        doctests for examples. """
        str_form = "name: {0}, score: {1}, cards: {2}"
        ## YOUR CODE IS BELOW IN ...##\
        ## You should uncomment the commented code
        # str_form = str_form.format(...)
        return str_form
    def __repr__(self):
        """ Repr for a Player instance. Please check the doctests for examples.
        """
        repr_form = "{0}(\"{1}\", {2})"
        ## YOUR CODE IS BELOW IN ... ##
        ## You should uncomment the commented code
        class_name = self.__class__.__name__
        # repr_form = repr_form.format(...)
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
        ## WRITE YOUR COMMENTS BELOW ##
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
        with the process_input method. If the result is False, runs
        print("Game not populated") and quits. If result is True, initializes
        the instance attributes as below:.

        Requirements: Should call the process_input method of Game with the
        given parameters.

        Instance attributes to initialize:
        deck(full_deck): initialized as a deep copy of full_deck.
            This deck will be shuffled during tests: random.shuffle(self.deck)
            (not in this function, but in the doctests)
        cards_per_player(int): set according to the given parameter
        players(list): First initialized as empty list. It is then populated
            by two player instances, created according to the player_names.

        Parameters:
        cards_per_player(int): How many cards should be dealt to each player
        player_names(list): List of player names (strings)

        Returns: None
        """
        ## YOUR CODE IS HERE ##

    def deal_cards(self):
        """
        Deals cards_per_player (unique) cards to each player in self.players
        Removes these cards from the deck of Game. Each card in the deck is in
        tuple form. According to the type specified in this tuple, this method
        creates a new card as below, then adds it to the players' cards.
        ie. ("Warrior 9", "WM")   --> Warrior_Card("Warrior 9")
        ie. ("Dragon 6", "DC")    --> Dragon_Card("Dragon 6")
        ie. ("Secret 2", "SS")    --> Secret_Card("Secret 2")
        ie. ("Emissary 4", "YE")  --> Yuxuan_Card("Emissary 4")

        To deal cards, it gives the first cards_per_player cards in self.deck
        to the first player (removing each card from the deck in the process).
        Then, it gives the remaining first cards_per_player cards to the second
        player.

        You should use the __add__method while adding, such as
        self.player += new_card

        Returns: None
        """
        ## YOUR CODE IS HERE ##

    def play(self):
        """ Plays cards_per_player rounds of the game, until both players run
        out of cards. At each round, it removes the first card of player.cards
        for each player instance. It then compares these cards (using the
        comparators of Card class). It breaks ties according to the index of
        suit_tie_breaker (higher index means winner). It uses log_round
        method during each round and adds to the current log. When the final
        round is over, it uses the log_winners method and adds the result to
        log. Finally, it sets cards_per_player to 0 and returns the log.

        Returns log(str): The complete log of the game, as shown in doctests
        """
        log = ""
        ## YOUR CODE IS HERE ##
        return log

    def process_input(cards_per_player, player_names):
        """ Processes the input according to the given Class Attributes.
        Validates the inputs cards_per_player(int) and player_names(list)
        There should be PLAYERS_COUNT players and cards_per_player should be
        <= MAX_DECK_SIZE.

        Requirements: Should have a try catch block validating the input. The
        following should be checked, types of both inputs. player_names' length
        is equal to PLAYERS_COUNT. cards_per_player is <= MAX_DECK_SIZE.
        Finally all elements of player_names should have type str

        Parameters:
        cards_per_player(int)
        player_names(list): All elements are strings

        Returns: boolean (True if parameters valid, False otherwise)
        """
        ## WRITE YOUR COMMENTS BELOW ##
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
        ## YOUR CODE IS BELOW IN … ##
        ## You can use the \ character if your code exceeds the line limit.
        ## You should uncomment all of the commented code
        log = ""
        # winner_player = self.players[...]
        # log += "Round: {0}\n".format(...)
        # log += "Card 1: {0}\n".format(...)
        # log += "Card 2: {0}\n".format(...)
        # log += "Winner: {0}, total score: {1}\n".format(...)
        # log += "Score gained by {0}: {1}\n".format(...)
        # log += "Winner Card: {0}\n".format(...)
        # log += "The card chants: {0}\n".format(...)
        # log += "Player's Total Scores: {0}: {1} points, {2}: {3} points\n\n"\
        # .format(...)
        return log

    def log_winners(self):
        """ Logs the winner(s) of the game according to scores. For example:
        If only Player_1 has higher score, so Player_1 won:
        log = Winning player: Player_1
        If both players have the same score, so both won:
        log = Winning players: Player_1 and Player_2

        Returns: log(str): Log of the winners of this game.
        """
        ## YOUR CODE IS BELOW IN … ##
        ## You should uncomment all of the commented code
        log = ""
        # score0 = self.players[0].score
        # score1 = self.players[1].score
        # if score0 == score1:
        #     log += "Winning players: {0} and {1}".format(...)
        # elif score0 > score1:
        #     log += "Winning player: {0}".format(...)
        # else: # score0 < score1:
        #     log += "Winning player: {0}".format(...)
        return log
