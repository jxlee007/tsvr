# Solitaire Game 
```
solitaire-card-game/
│
├── README.md                # Your reflection (replaces writeup.txt)
├── solitaire.py             # code solution
├── .gitignore               # (add __pycache__, .pyc, etc)
│
├── attempts/
│   ├── attempt_1.md         # Prompt + code + output + analysis
│   ├── attempt_2.md
│   ├── attempt_3.md
│   └── ...
│
└── outputs/
    ├── seed_6_lost.txt      # Terminal output from final run
    ├── seed_3_won.txt
    ├── seed_30_won.txt
    ├── seed_20_simulate.txt # simulate(20, 0) output
    └── seed_300_simulate.txt # simulate(300, 7) output

```

## Approach
I built a 32-card solitaire game by:
1. Understanding card encoding (0-31, where suit = card // 8, rank = card % 8)
2. Implementing the game loop: deal → remove matches → refill → check win/lose
3. Iterating to fix bugs by comparing against spec examples

## Key Challenges

**Challenge 1: Card Dealing Order**
- First attempt dealt cards from the end of deck (pop() without index)
- This caused wrong card sequence
- Fixed by using pop(0) to deal from start

**Challenge 2: Removal Logic**
- Initial logic didn't handle all cases (2 cards, 3 cards on table)
- Spec requires: 2 same suit → remove both; 3 same suit → remove lower 2
- Fixed by adding all edge cases

**Challenge 3: Output Formatting**
- Had to match spec exactly: 2x2 card layout, blank lines, spacing

## What I'd Do Differently
- Start with unit tests for remove_matching_suits() before full game loop
- Print deck state at each step when debugging
- Compare output line-by-line against spec examples earlier

## Results
All test cases pass:
- Seed 6: LOSE ✓
- Seed 3: WIN ✓
- Seed 30: WIN ✓
- simulate(20, 0): [distribution]
- simulate(300, 7): [distribution]