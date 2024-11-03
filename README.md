# Flames
The FLAMES Game in Python is a fun and interactive program that helps users determine the type of relationship between two names using a classic childhood game. FLAMES, which stands for Friends, Lovers, Affectionate, Marriage, Enemies, and Siblings, is a game often used to predict relationships or compatibility.

This project takes two names as input from the user and applies the following steps:

Remove Common Letters: The program compares the two names and removes common letters, reducing each name to its unique letters.

Calculate Remaining Characters: It counts the remaining letters after common letters are removed. This count is then used to determine the position in the FLAMES sequence.

Determine Relationship Type: By iterating through the FLAMES acronym, the program eliminates letters based on the remaining count until only one letter is left. The final letter corresponds to a specific relationship type, such as "Friends," "Lovers," or "Marriage."

Key Features:

Uses Python's collections.Counter to manage letter counts efficiently.
Employs a looping algorithm to simulate the FLAMES elimination process.
Provides a simple and entertaining way to find compatibility between two names.
