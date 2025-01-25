from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes and edges based on the provided flowchart
dot.node('Start', 'Start')
dot.node('Display_Welcome', 'Display Welcome Message')
dot.node('Input_Choice1', 'Input Choice 1 (left or right)')
dot.node('Decision1', 'Decision 1: Choice 1 == "left"?')
# dot.node('Yes1', 'Yes')
# dot.node('No1', 'No')
dot.node('Display_Message', 'Display Message')
dot.node('Game_Over', 'Display "Game Over" Message')
dot.node('End1', 'End')
dot.node('Input_Choice2', 'Input Choice 2')
dot.node('Decision2', 'Decision 2: Choice 2 == "red"?')
# dot.node('Yes2', 'Yes')
# dot.node('No2', 'No')
dot.node('Correct_Door', 'Display "Correct Door"')
dot.node('Wrong_Door', 'Display "Wrong. You\'re out of the game!"')
dot.node('End2', 'End')

# Define the edges
dot.edge('Start', 'Display_Welcome')
dot.edge('Display_Welcome', 'Input_Choice1')
dot.edge('Input_Choice1', 'Decision1')
dot.edge('Decision1', 'Display_Message', label='Yes')
dot.edge('Decision1', 'Game_Over', label='No')
dot.edge('Game_Over', 'End1')
dot.edge('Display_Message', 'Input_Choice2')
dot.edge('Input_Choice2', 'Decision2')
dot.edge('Decision2', 'Correct_Door', label='Yes')
dot.edge('Decision2', 'Wrong_Door', label='No')
dot.edge('Correct_Door', 'End2')
dot.edge('Wrong_Door', 'End2')

# Save the graph to a file
output_file = "flowchart"
dot.render(output_file, format='png')

print(f"The flowchart has been saved as {output_file}.png")