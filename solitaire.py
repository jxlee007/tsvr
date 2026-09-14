import random


def main():
    seed = int(input("Enter an integer to pass to the seed() function: "))
    
    cards = list(range(32))
    random.seed(seed)
    random.shuffle(cards)
    
    table = [cards.pop() for _ in range(4)]  # Deal 4
    deck_index = 0
    
    while True:
        # Print current round
        print_table(table)  # Shows 4 cards with symbols
        
        # Check/remove matching suits
        removed = remove_matching_suits(table)
        
        # Refill empty spots
        for spot in range(4):
            if table[spot] is None:
                if deck_index < len(cards):
                    table[spot] = cards[deck_index]
                    deck_index += 1
        
        # Check win/lose
        if deck_index >= len(cards):
            print("So glad that you won! 🎉")
            break
        
        if len(set(card // 8 for card in table if card is not None)) == 4 and deck_index < len(cards):
            print("So sorry that you lost! 😞")
            break


def remove_matching_suits(table):
    suit_positions = {}
    for position, card in enumerate(table):
        if card is not None:
            suit_positions.setdefault(card // 8, []).append(position)

    suit_groups = sorted(suit_positions.values(), key=len, reverse=True)
    suit_counts = [len(positions) for positions in suit_groups]

    if suit_counts in ([4], [2, 2]):
        positions_to_remove = [position for group in suit_groups for position in group]
    elif suit_counts == [3, 1]:
        positions_to_remove = suit_groups[0][:2]
    elif suit_counts == [2, 1, 1]:
        positions_to_remove = suit_groups[0]
    else:
        positions_to_remove = []

    for position in positions_to_remove:
        table[position] = None

    return positions_to_remove


def print_table(table):
    print()  # Blank line before round
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    for card in table:
        suit_idx = card // 8
        rank_idx = card % 8
        print(f" {suits[suit_idx]} {ranks[rank_idx]}", end="  ")
    print()


if __name__ == "__main__":
    main()