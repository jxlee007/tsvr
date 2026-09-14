## **Concepts Needed for Solitaire (What You'll Use & Where)**

| Concept | What It Does | In Your Solitaire Game |
|---------|-------------|------------------------|
| **Lists** (you know this) | Store items in order | Deck = `[0-31]`, table = 4 card positions |
| **Dictionaries** | Map key→value | Card → (suit, rank): `{0: ('Hearts', 'Seven')}` |
| **String methods** | `.count()`, `.strip()` | Count matching suits in 4 cards |
| **Random module** | `shuffle()`, `seed()` | Seed deck reproducibly |
| **Loops** (you know this) | Repeat logic | Loop until game ends |
| **Conditionals** (you know this) | If/elif/else | Check win/lose conditions |
| **Modulo operator `%`** | Get remainder | Card index % 4 = suit (0-7→Hearts, 8-15→Diamonds, etc) |
| **List slicing** | Extract parts | `cards[index//4]` = rank position |
| **Function** | Reusable logic | `count_suits(table)`, `remove_cards()`, `refill()` |
| **User input** | Get seed | `input()` |
| **String formatting** | Pretty output | Card symbols, spacing, alignment |

---

## **How They Connect (Simple Flow)**

```
Input seed → shuffle deck (random) → deal 4 cards (list slicing)
→ Loop:
   - Count suits in 4 cards (dict lookup + modulo)
   - Remove matching cards (conditional logic)
   - Refill empty spots (list manipulation)
   - Check win/lose (conditional)
   - Print formatted output (string formatting)
→ Repeat until game ends
```

---

## **What You Likely Already Know**
✅ Lists, loops, conditionals, functions (from your test.py)

## **What You Need to Learn/Practice**
- **Modulo `%`** — Card 26 % 8 = 2 (Nine of Spades belongs in suit 3)
- **Dictionary mapping** — Card number → (suit, rank)
- **Random seed reproducibility** — `seed(n)` always produces same shuffle
- **Output formatting** — Exact spacing/symbols match expected

---

## **Start Here (Next 30 min)**

1. **Understand card encoding**: Card 0-7 = Hearts, 8-15 = Diamonds, etc.
   - How do you get suit from card number? (Use modulo)
   - How do you get rank? (Use integer division)

2. **Map cards to symbols**: Create dict: `{0: '♥7', 1: '♥8', ...}`

3. **Test with Claude**: Once you understand #1-2, write ONE simple prompt asking Claude to build the shell.