
```
solitaire-card-game/
│
├── README.md                 # Your reflection (replaces writeup.txt)
├── finalsolitaire.py         # Final solution
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

Shuffle → Deal 4 → Loop (remove matches, refill) → Until deck empty or stuck with all 4 suits
draw  → remove  → refill

if initial 4 are all different suits → stuck immediately → LOSE