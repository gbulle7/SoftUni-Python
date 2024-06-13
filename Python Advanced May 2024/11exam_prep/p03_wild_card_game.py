def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    for card_name, card_type in list(args) + list(kwargs.items()):
        if card_type == 'monster':
            monster_cards.append(card_name)
        elif card_type == 'spell':
            spell_cards.append(card_name)

    result = ''
    if monster_cards:
        result += 'Monster cards:\n' + '  ***' + '\n  ***'.join(sorted(monster_cards, reverse=True))
    if spell_cards:
        result += '\nSpell cards:\n' + '  $$$' + '\n  $$$'.join(sorted(spell_cards))

    return result.strip()


# Inputs
print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
