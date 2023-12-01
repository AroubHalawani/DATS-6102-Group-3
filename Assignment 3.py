#%%
# Needed packages
import numpy as np
import random

# %%
# Create an array with 1 row and 3 columns
graphdata = np.zeros(shape=(1, 3), dtype = int)

# Create the first row which will be the root to the first node
graphdata[0] = [0, 1, 1]

# How many rows we want
num_rows = 20
#%%
# Add new rows up to the number we want
for i in range(num_rows-1):
    new_row = [0,0,0]

    # Choose an existing non-root node to be the new parent
    new_parent = random.choice(graphdata[:,1])
    new_row[0] = new_parent

    # Determine relationships to existing children, if any
    parent_existing_relationships = []
    for j in graphdata:
        if j[0] == new_parent:
            parent_existing_relationships.append(graphdata[i,2])
    # print(parent_existing_relationships)

    # Create a new node as the child
    new_row[1] = graphdata[:,1].max()+1
    
    # Randomly assign a relationship
    new_row[2] = random.choice([1,2,3,4,5])

    # Add the new row to the existing data
    graphdata = np.append(graphdata, np.array(new_row).reshape(1,3), axis = 0)

# %%
print(graphdata)

# %%
