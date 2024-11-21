from mindmap_leaf import MindMapLeaf

# Step 5: Create a MindMapLeaf object and test the __str__ and display methods.
leaf = MindMapLeaf("Jean-Luc Picard", "circle")
print(str(leaf))  # Should display "((Jean-Luc Picard))"
leaf.display(2)   # Should display "  ((Jean-Luc Picard))" with two spaces

print("MindMapLeaf tests completed!")