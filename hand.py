class Hand:
    def __init__(self, cards):
        self.cards = cards

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            val = card.value
            if val == 1:
                aces += 1
            else:
                value += min(val, 10)

        if not aces:
            return value
        if value + 11 > 21:
            return value + 1
        elif aces == 1:
            return value + 11  # line 19-22 not inderstood
        elif value + 11 + (aces - 1) <= 21:
            return value + 11 + (aces - 1)
        else:
            return value + aces

    def add_to_hand(self, card):
        self.cards.append(card)

    def __str__(self):
        string_card = [str(card) for card in self.cards]
        return ",".join(string_card)
