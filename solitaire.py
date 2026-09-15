import random


def main():
    seed = int(input("Enter an integer to pass to the seed() function: "))
    
    cards = list(range(32))
    random.seed(seed)
    random.shuffle(cards)
    
    # Deal 4 cards from the TOP (index 0)
    table = [cards.pop(0) for _ in range(4)]
    
    round_num = 0
    while True:
        round_num += 1
        print_round(table)
        
        # Remove matching suits
        remove_matching_suits(table)
        
        # Refill empty spots from deck (in order: 0, 1, 2, 3)
        for spot in range(4):
            if table[spot] is None and cards:
                table[spot] = cards.pop(0)
        
        # Check win: deck empty
        if not cards:
            print("So glad that you won! 🎉")
            break
        
        # Check lose: all 4 suits on table with cards remaining
        suits_on_table = {card // 8 for card in table if card is not None}
        if len(suits_on_table) == 4 and cards:
            print("So sorry that you lost! 😞")
            break


def remove_matching_suits(table):
    """Remove matching suits according to spec rules"""
    suit_positions = {}
    
    # Group positions by suit
    for position, card in enumerate(table):
        if card is not None:
            suit = card // 8
            if suit not in suit_positions:
                suit_positions[suit] = []
            suit_positions[suit].append(position)
    
    # Get suit groups, sorted by count (largest first)
    suit_groups = sorted(suit_positions.values(), key=len, reverse=True)
    suit_counts = [len(group) for group in suit_groups]
    
    positions_to_remove = []
    
    # Apply spec rules
    if suit_counts == [4]:
        # All 4 same suit → remove all
        positions_to_remove = suit_groups[0]
    elif suit_counts == [3, 1]:
        # 3 of one suit, 1 other → remove lower 2 of the 3
        positions_to_remove = sorted(suit_groups[0])[:2]
    elif suit_counts == [2, 2]:
        # 2 pairs → remove all 4
        positions_to_remove = suit_groups[0] + suit_groups[1]
    elif suit_counts == [2, 1, 1]:
        # 2 of one suit, 1 each of others → remove the pair
        positions_to_remove = suit_groups[0]
    elif suit_counts == [2]:
        # Only 2 cards on table, same suit → remove both
        positions_to_remove = suit_groups[0]
    elif suit_counts == [3]:
        # Only 3 cards on table, all same suit → remove lower 2
        positions_to_remove = sorted(suit_groups[0])[:2]
    
    # Remove the cards
    for pos in positions_to_remove:
        table[pos] = None


def print_round(table):
    """Print the current table state"""
    print()  # Blank line before round
    
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    # Convert cards to symbols
    card_symbols = []
    for card in table:
        if card is not None:
            suit_idx = card // 8
            rank_idx = card % 8
            card_symbols.append(f"{suits[suit_idx]} {ranks[rank_idx]}")
        else:
            card_symbols.append(None)
    
    # Print the 2x2 layout
    print(f"    {card_symbols[0]:>3}     {card_symbols[1]:>3}")
    print(f"    {card_symbols[2]:>3}     {card_symbols[3]:>3}")


def simulate(n, i):
    """Run n games starting with seed i, report distribution of cards left"""
    results = {}  # cards_left -> count
    
    for game_num in range(n):
        seed = i + game_num
        cards = list(range(32))
        random.seed(seed)
        random.shuffle(cards)
        
        table = [cards.pop(0) for _ in range(4)]
        
        while True:
            # Remove matching suits
            remove_matching_suits(table)
            
            # Refill empty spots
            for spot in range(4):
                if table[spot] is None and cards:
                    table[spot] = cards.pop(0)
            
            # Check win: deck empty
            if not cards:
                cards_left = 0
                break
            
            # Check lose: all 4 suits on table with cards remaining
            suits_on_table = {card // 8 for card in table if card is not None}
            if len(suits_on_table) == 4 and cards:
                cards_left = len(cards)
                break
        
        # Record result
        if cards_left not in results:
            results[cards_left] = 0
        results[cards_left] += 1
    
    # Print table
    print("Number of cards left | Number of rounds | Frequency")
    print("-" * 55)
    
    for cards_left in sorted(results.keys()):
        count = results[cards_left]
        percentage = (count / n) * 100
        rounds = count
        print(f"{cards_left:>20} | {rounds:>16} | {percentage:>6.2f}%")


if __name__ == "__main__":
    main()