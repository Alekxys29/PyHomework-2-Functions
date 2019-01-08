"""
Homework Assignment #2: Functions

This program is composed of functions for generating specific values based on music choice.
"""

def title():
    title = "The Scientist"
    return title

def artist():
    artist = "Coldplay"
    return artist

def genre():
    genre = "Rock"
    return genre

def isRock(genre):
    if genre == 'Rock':
        return True
    return False

Title = title()
Artist = artist()
Genre = genre()


print('Title: %s' % Title)
print('Artist: %s' % Artist)
print('Genre: %s' % Genre)

rock = isRock(Genre)
print('==================================')
print('Question: Is this a rock song? ')
print('Answer: %s') % rock

folk = isRock("Folk")
print('==================================')
print('Question: Is this a folk song? ')
print('Answer: %s') % folk