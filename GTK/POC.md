**Apply This to Solitaire Submission:**

---

## **PoC Audit Checklist for Solitaire**

### **1. Boundary Control** ✅
```python
# GOOD: Seed is isolated, reproducible
import random
def play_game(seed_value):
    random.seed(seed_value)
    # No hardcoded seeds, no state leakage
```

### **2. Error Durability** ✅
```python
# Handle edge cases:
- Empty deck refill
- All 4 suits on table while cards remain
- Off-by-one in slot removal
# Test against all 5 examples, not just happy path
```

### **3. Data Density (O(N) not O(N²))** ✅
```python
# BAD: nested loops checking every card against every card
for card in table:
    for other in table:
        if suit_match(card, other)...  # O(N²)

# GOOD: count suits once per round
suits = [card % 8 // 4 for card in table]  # O(N)
```

---

## **Interview Framing (Write in README)**

Instead of: "I built a solitaire game"

**Say:**
> "Built a solitaire simulator focusing on O(N) single-pass operations and reproducible state. Iterated through 3 attempts to handle edge cases (exactly 2 vs 3 matching suits, refill ordering) — demonstrating how I debug algorithmic logic against test cases."

---

## **In Your Attempts Docs: Show Trade-Offs**

**Attempt 1 Analysis:**
```markdown
## Design Decisions

1. Card Representation: 0-31 integers
   - Trade-off: Bitwise arithmetic is O(1), but less readable
   - Why chosen: Speed + memory for "ERP-scale" simulation

2. Suit Matching: Single pass through 4 cards
   - Could use nested loops (clearer, O(N²))
   - Why not: Teaching point—scalability matters

3. Refill Logic: Fill lowest-numbered spot first
   - Why: Maintains consistent state (no ambiguity)
```

---

## **Key Messaging for Odoo/Jeavio Interview**

When they ask about solitaire:

> "I focused on understanding how to handle state mutation correctly—removing cards, refilling in order, checking win/lose conditions. This taught me to think about algorithmic correctness under pressure, which applies directly to ERP workflows where order of operations matters."

---

## **48-Hour Execution Plan**

| Hour | Do This | Why |
|------|---------|-----|
| 0-2 | Break down rules + pseudocode | Avoid vague prompting |
| 2-4 | Attempt 1: Simple prompt to Claude | Document first iteration |
| 4-6 | Test vs seed 6,3,30 | Find edge cases |
| 6-12 | Attempt 2: Fix one thing (refill order) | Show iteration |
| 12-18 | Attempt 3: Fix formatting/output | Polish |
| 18-24 | Document all 5 test cases | Final outputs |
| 24-48 | Write README with trade-offs + learnings | Tell story |

---
