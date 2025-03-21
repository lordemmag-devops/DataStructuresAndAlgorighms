my_favourite = {"red", "green", "black", "blue", "purple"}
her_favourite = {"blue", "orange", "purple", "green"}

# union
all_favourites = my_favourite | her_favourite
print(all_favourites)
# You may see + to combine lists, in which there are repeats.
# But we are not working with lists...so i'll try to focus here.

# Intersection (elements shared between both)
wedding_colours = my_favourite & her_favourite
print(wedding_colours)
# This is like the inside section of a venn diagram

#There are also method versions:
all_favourites = my_favourite.union(her_favourite)
print(all_favourites)

wedding_colours = my_favourite.intersection(her_favourite)
print(wedding_colours)


###### DIFFERENT AND SYMMETRIC DIFFERENCE ######


my_favourite = {"red", "green", "black", "blue", "purple"}
her_favourite = {"blue", "orange", "purple", "green"}

# Difference
only_my_colours = my_favourite - her_favourite
print(only_my_colours) # elements in left getting rid of all in right.
# Could go other way too:
only_her_colours = her_favourite - my_favourite
print(only_her_colours)

# Symmetric difference is like of you took colours only I liked union with colours only she liked

symmetric = my_favourite ^ her_favourite
print(symmetric)

#This is like:
symmetric = only_my_colours | only_her_colours
print(symmetric)