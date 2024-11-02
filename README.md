# Number Guessing Game with Stats

## Table of Contents

	1.	Description
	2.	Functionality
	3.	Instructions for Use
	4.	Additional Notes

### Description

This Python program is an enhanced version of the classic number guessing game, where the player has to guess a randomly chosen number within a specific range. The improvements are detailed below.

### Functionality

	1.	Game Modes: Choose between:
	•	Single Player Mode
	•	Two Player Mode
	•	Statistics Mode (where you can see the game’s history)
	•	Exit
	2.	Difficulty Levels: Different levels are available:
	•	Easy (20 attempts)
	•	Medium (12 attempts)
	•	Hard (5 attempts)
	3.	Customizable Guessing Range: The default range is from 1 to 1000, but players can customize this to a different upper limit.
	4.	Tracking and Saving Results: The game saves each player’s name and result (win or loss) in an Excel file (records.xlsx). These statistics can be visualized using bar charts in the Statistics section.
	5.	Statistics: The program offers two ways to view game statistics:
	•	Total wins and losses.
	•	Filtering by specific players to see how many times a particular player has played.

### Instructions for Use

	1.	Running the Program:
	•	Make sure all the required files, including min_max.py and records.xlsx, are in the same directory as the main script.
	•	Run the program with a Python 3 interpreter.
	2.	Playing the Game:
	•	Choose a game mode.
	•	Select the difficulty level.
	•	If in two-player mode, Player 1 chooses a secret number, and Player 2 attempts to guess it.
	•	Players have a limited number of attempts based on the difficulty level.
	•	After guessing correctly or using all attempts, the game will ask for the player’s name and save the result in the Excel file.
	3.	Viewing Statistics:
	•	Select the Statistics option in the main menu.
	•	Choose the type of statistic to view and follow the instructions.
	•	Charts will display based on your selections.

### Additional Notes

	•	Excel File: records.xlsx should be pre-configured with at least a worksheet named “Stats” to save game results correctly.
	•	Graph Library: The program uses Matplotlib to display statistics. Make sure this library is installed.
	•	Security for Multiplayer Mode: When Player 1 enters the secret number, it is hidden using getpass to prevent Player 2 from seeing it.
