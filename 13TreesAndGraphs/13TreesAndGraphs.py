# class GameStateNode:
#     def __init__(self, board_config, player_turn):
#         self.board = board_config  # e.g., a 2D list for a Tic-Tac-Toe board
#         self.turn = player_turn    # 'MAX' or 'MIN'
#         self.children = []         # Possible next states after one move
#         self.score = None          # Will be determined by Minimax

#     def add_child_state(self, child_node):
#         self.children.append(child_node)

# # --- Conceptual Example ---
# # This is not a full implementation, but a demonstration of the structure.
# initial_state = GameStateNode(board_config=[[None]*3 for _ in range(3)], player_turn='MAX')

# # After MAX places an 'X' in the center:
# move1_state = GameStateNode(board_config=[[None, None, None], [None, 'X', None], [None, None, None]], player_turn='MIN')
# initial_state.add_child_state(move1_state)

# print("\n--- Game Tree Structure ---")
# print(f"Initial state created. Player to move: {initial_state.turn}")
# print(f"Number of possible first moves (children): {len(initial_state.children)}")
# print("In Chunk 15, we will learn how to recursively explore this entire tree.")

class BudgetGameState:
    def __init__(self, dus_remaining, turn, move_made="Start"):
        self.dus = dus_remaining
        self.turn = turn
        self.move = move_made
        self.children = []
    
    def generate_next_states(self):
        next_turn = 'MIN' if self.turn == 'MAX' else 'MAX'
        if self.dus >= 2:
            self.children.append(BudgetGameState(self.dus - 2, next_turn, "Allocated 2"))
        if self.dus >= 3:
            self.children.append(BudgetGameState(self.dus - 3, next_turn, "Allocated 3"))

def print_game_tree(node, depth=0):
    indent = "    " * depth
    outcome = ""
    if not node.children: # It's a leaf node
        if node.dus % 2 != 0:
            outcome = "-> MAX wins"
        else:
            outcome = "-> MIN wins"
            
    print(f"{indent}Move by {node.turn}: {node.move}, DUs left: {node.dus} {outcome}")
    
    for child in node.children:
        print_game_tree(child, depth + 1)

# --- The Budget War Simulation ---
start_node = BudgetGameState(10, 'MAX')

# Level 1: MAX's moves
start_node.generate_next_states() 

# Level 2: MIN's moves
for child_of_start in start_node.children:
    child_of_start.generate_next_states()

print("\n--- The Ministry Budget War Game Tree ---")
print_game_tree(start_node)

print("\nAnalysis: By inspection, MAX can choose to allocate 3 DUs, leaving 7.")
print("From there, MIN can leave either 5 or 4. If MIN leaves 5, MAX wins. MAX has a winning path!")