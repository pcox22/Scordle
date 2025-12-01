# Scordle
A passion-project discord bot meant to tally up scores for various idle guessing games (idles). The bot is in beta at this stage of development; while I have recently updated it to include all intended idle games, I cannot confidently affirm the lack of bugs or glitches.

### Description
This program began as a text channel on Discord where friends would post their results from specific idles. I had the idea to surprise them by upping the stakes and making things more interesting by allocating a score based on our performance. Currently, Scordle is a simple Python program using the Discord API and performs the following functions:

- Allow members to register for the service using the '/register' command.
  - Registering will create a new List for the user with a format mentioned later in this document
- Tally Scores for # of guesses per category
- Rank all registered users based a specified idle.
- Prevent players from submitting their results twice in one day to gain drastic points.

### Long-Term Development
Currently, hosting options are being explored to keep the bot active. It currently employs all 4 idles that I wished to include. More may be added at my discretion. This is a hobby project that I surprised my non-CS friends with, so the intention is to have a calm, peaceful development process.

Currently, data consistency is my largest concern. As things stand, each time the bot is run, it will completely clear out all registered users, resetting their scores entirely. ~~The prospective implementation will be to use File I/O to write save data to a text file, and then read from that same file upon startup to initialize the player list.~~ The current consideration is to create a database that the bot will read and write from consistently. 

The current data format is as follows: a master list called score; it is paramount to a 2D array in that it will contain only lists.
Each sublist contains player data formatted by the following indices:

0. Username
1. Narutodle Score
2. Smashdle Score
3. Pokedle Score
4. Onepiecedle Score
5. Date of Last Narutodle
6. Date of Last Smashdle
7. Date of Last Pokedle
8. Date of Last Onepiecedle

It's worth noting that instead of using a 2D array, I could have created a player class containing all of the above parameters. My reason for not doing so was unfamiliarity with Discord bot development. I was concerned with how it would handle data, and so I chose to oversimplify. Pending availability, I expect to create a class instead once I've confirmed I can do so and maintain the current logic.

### Sharing
Scoredle is my first ever interation with the Discord API. It is also the second time I've ever addeed any bot to the server, so it is redundant to say that I'm new to the scene. I am open to other people using this bot, or at least creating their own bot using my Source Code. So long as you don't call '/steal_social_security_number' I won't have any gripes.

Some messages are currently hard-coded to channels in my private server, so adjustments would be required if implementing your own version.

### Commands
Commands are as follows:
- end_game
  - Terminates the current round. All score categories are reset, but dates are retained (you must wait until the next day to begin a new game).
- reset_all_scores
  - Navigates through every player in the master list and resets all their scores to 0. It *should* require admin privileges.
- print_all_scores
  - Self-Explanatory: In order of registration, prints each user and their scores for each idle.
- register
  - As aforementioned, creates a list for the player calling the command, enabling them to use the play commands.
- clear_all
  - COMPLETELY resets the score list. Requires admin privileges (probably).
- narutodle
  - Takes 1 input; it should be the result string provided by Narutodle.net after completing all categories. Will tally up points based on number of guesses in each category.
- smashdle
  - Takes 1 input; it should be the result string provided by Smashdle.net after completing all categories. Will tally up points based on number of guesses in each category.
- pokedle
  - Takes 1 input; it should be the result string provided by Pokedle.net after completing all categories. Will tally up points based on number of guesses in each category.
- onepiecedle
  - Takes 1 input; it should be the result string provided by Onepiecedle.net after completing all categories. Will tally up points based on number of guesses in each category.
- rank_naruto
  - Implements bubble sorting (we all get lazy) to sort a deep copy of the score list by descending order of the Narutodle Score.
- rank_smash
  - See previous command, replace naruto with smash.
- rank_pokemon
  - See previous command, replace naruto with pokemon.
- rank_onepiece
  - See previous command, replace naruto with one piece.
 
### Hosting 
Scordle is currently hosted in a production environment using Railway.com - I'm currently using their 1-month free plan. My understanding (which will be updated out in about 23 days) is that the bot will be freely hosted until the trial ends, or it exceeds the free-use memory. While I'm not familiar with actual resource prices, Railway has indicated that only ¢10 worth of memory has been expended after running the bot continously for over a week.

Since Railway has been such an amicable service, I intend to purchase their Hobby tier, pending personal needs and desires.

