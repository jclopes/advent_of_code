import pathlib

class Hand:
    def __init__(self, hand, bid):
        self.cards = list(map(Hand.card2value, hand))
        self.bid = int(bid)
        self.score = Hand.score_hand(self.cards)

    @staticmethod
    def card2value(card):
        res = None
        match card:
            case 'A': res = 14
            case 'K': res = 13
            case 'Q': res = 12
            case 'J': res = 11
            case 'T': res = 10
            case _: res = int(card)
        return res

    @staticmethod
    def score_hand(cards):
        h = sorted(cards)
        res = 0
        # five
        if h[0] == h[1] and h[0] == h[2] and h[0] == h[3]  and h[0] == h[4]:
            res = 6
        # four
        elif h[1] == h[2] and h[1] == h[3] and (h[1] == h[0] or h[1] == h[4]):
            res = 5
        # three_two
        elif h[0] == h[1] and h[3] == h[4] and (h[1] == h[2] or h[2] == h[3]):
            res = 4
        # three
        elif (h[0] == h[1] and h[1] == h[2]) or (h[1] == h[2] and h[2] == h[3]) or (h[2] == h[3] and h[3] == h[4]):
            res = 3
        # two_two
        elif (h[1] == h[2] and h[3] == h[4]) or (h[0] == h[1] and h[2] == h[3]) or (h[0] == h[1] and h[3] == h[4]):
            res = 2
        # two
        elif h[0] == h[1] or h[1] == h[2] or h[2] == h[3] or h[3] == h[4]:
            res = 1
        # high
        else:
            res = 0
        return res

    def comp_cards_lt_(self, other):
        hand1 = self.cards
        hand2 = other.cards
        res = False
        for i in range(len(hand1)):
            if hand1[i] < hand2[i]:
                res = True
                break
            elif hand1[i] > hand2[i]:
                res = False
                break
        return res

    def __lt__(self, other):
        """
        True if hand1 has lower value than hand2
        """
        hand1 = self.cards
        hand2 = other.cards
        s1 = self.score
        s2 = other.score
        res = s1 < s2
        if s1 == s2:
            res = self.comp_cards_lt_(other)

        return res

    def __repr__(self):
        return "{" + str(self.score) + " <= " + "(" + str(self.cards) + ", " + str(self.bid) + ")}"

class Hand2:
    def __init__(self, hand, bid):
        self.cards = list(map(Hand2.card2value, hand))
        self.bid = int(bid)
        self.score = Hand2.score_hand(self.cards)

    @staticmethod
    def card2value(card):
        res = None
        match card:
            case 'A': res = 14
            case 'K': res = 13
            case 'Q': res = 12
            case 'J': res = 1
            case 'T': res = 10
            case _: res = int(card)
        return res

    @staticmethod
    def score_hand(cards):
        count = {0: 0}
        count[1] = cards.count(1)
        best2 = 0
        best = 0
        for c in range(2, 15):
            count[c] = cards.count(c)
            if count[best] < count[c]:
                best2 = best
                best = c
            elif count[best2] < count[c]:
                best2 = c

        count[best] += count[1]
        res = 0
        if count[best] == 5:
            res = 6
        elif count[best] == 4:
            res = 5
        elif count[best] == 3 and count[best2] == 2:
            res = 4
        elif count[best] == 3:
            res = 3
        elif count[best] == 2 and count[best2] == 2:
            res = 2
        elif count[best] == 2:
            res = 1
        else:
            res = 0

        return res

    def comp_cards_lt_(self, other):
        hand1 = self.cards
        hand2 = other.cards
        res = False
        for i in range(len(hand1)):
            if hand1[i] < hand2[i]:
                res = True
                break
            elif hand1[i] > hand2[i]:
                res = False
                break
        return res

    def __lt__(self, other):
        """
        True if hand1 has lower value than hand2
        """
        hand1 = self.cards
        hand2 = other.cards
        s1 = self.score
        s2 = other.score
        res = s1 < s2
        if s1 == s2:
            res = self.comp_cards_lt_(other)

        return res

    def __repr__(self):
        return "{" + str(self.score) + " <= " + "(" + str(self.cards) + ", " + str(self.bid) + ")}"

def parse(data):
    hands = []
    for line in data.split('\n'):
        line = line.strip()
        hand, bid = line.split(' ')
        hands.append(Hand(hand, bid))
    return hands

def parse2(data):
    hands = []
    for line in data.split('\n'):
        line = line.strip()
        hand, bid = line.split(' ')
        hands.append(Hand2(hand, bid))
    return hands


def p1(data):
    games = parse(data)

    rank = 1
    sum = 0
    for g in sorted(games):
        sum += g.bid * rank
        rank += 1

    return sum

def p2(data):
    games = parse2(data)

    rank = 1
    sum = 0
    for g in sorted(games):
        sum += g.bid * rank
        rank += 1

    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    # data = """
    #     32T3K 765
    #     T55J5 684
    #     KK677 28
    #     KTJJT 220
    #     QQQJA 483
    #     """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
