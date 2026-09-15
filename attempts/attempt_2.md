ATTEMPT 2
=========

PROBLEM IDENTIFIED:
First version had 3 critical bugs that caused incorrect game logic and wrong outputs

BUGS IN ATTEMPT 1:
1. Card dealing from wrong end: used pop() (from end) instead of pop(0) (from start)
   → This reversed deck order, making game unwinnable
2. Removal logic incomplete: didn't handle all cases (2 cards, 3 cards on table)
   → Spec requires: 2 same suit→remove both; 3 same suit→remove lower 2
3. Output format: wasn't matching spec (2x2 layout, spacing, blank lines)

HOW I NOTICED:
- Tested seed 6 against PDF spec example
- Spec said LOSE, but code output WON
- This indicated card order was backwards
- Printed raw shuffled deck and saw pop() taking from end

FIXES APPLIED:
1. Changed dealing: `table = [cards.pop(0) for _ in range(4)]` (from start, not end)
2. Fixed removal logic: Added all missing cases in remove_matching_suits()
   - Added case for [2]: only 2 cards, same suit → remove both
   - Added case for [3]: only 3 cards, all same suit → remove lower 2
   - Kept existing cases: [4], [3,1], [2,2], [2,1,1]
3. Fixed output: Changed print_round() to show 2x2 card layout with proper spacing

TESTING RESULTS:
- Seed 6 (should LOSE): ✓ LOSE
- Seed 3 (should WIN): ✓ WIN  
- Seed 30 (should WIN): ✓ WIN
- simulate(20, 0): ✓ Correct distribution
- simulate(300, 7): ✓ Correct distribution

KEY LEARNINGS:
- One-line bug (pop vs pop(0)) can break entire game logic
- Testing against spec examples is essential for debugging
- Removal logic needs to handle edge cases (fewer than 4 cards)
- Output formatting must match spec exactly (spacing matters)

WHAT CHANGED FROM ATTEMPT 1:
- Completely rewrote remove_matching_suits() to handle all cases
- Fixed deck dealing to pop from start instead of end
- Improved output formatting to match 2x2 spec layout
- All 5 test cases now pass