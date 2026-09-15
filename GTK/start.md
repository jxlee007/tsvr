**STEP 1: Card Encoding (15 min)**

Cards are 0-31. Understand this:

```
0-7   = Hearts (7, 8, 9, 10, J, Q, K, A)
8-15  = Diamonds (7, 8, 9, 10, J, Q, K, A)
16-23 = Clubs (7, 8, 9, 10, J, Q, K, A)
24-31 = Spades (7, 8, 9, 10, J, Q, K, A)
```

**How to extract suit from card number?**
```
card = 26
suit = card // 8  # 26 // 8 = 3 (Spades)
```

**How to extract rank?**
```
card = 26
rank = card % 8   # 26 % 8 = 2 (9 is the 2nd rank after 7)
```

**Map to symbols:**
```python
suits = ['♥', '♦', '♣', '♠']
ranks = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

card = 6
print(f"{suits[card//8]} {ranks[card%8]}")  # ♥ K
```

---

**STEP 2: Game Flow (Explain back to me)**

After shuffling and dealing 4 cards on table:

1. **Count suits** in the 4 cards
2. **Remove rule:**
   - Exactly 2 same suit? Remove those 2
   - Exactly 3 same suit? Remove the 2 in **lower-numbered positions**
   - 2 pairs or all 4 same suit? Remove all 4
   - Otherwise? Remove nothing
3. **Refill empty spots** with deck cards (fill position 0, then 1, then 2, then 3)
4. **Check:**
   - If deck empty → WIN
   - If all 4 suits on table while deck has cards → LOSE
   - Otherwise → repeat

**Explain:** If table has [♥7, ♦8, ♥9, ♣10] and we remove 2 hearts, which positions are now empty?