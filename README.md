# Scordle
A passion-project discord bot meant to tally up scores for various idle guessing games (idles). The bot is in beta at this stage of development, and only supports results from Narutodle.net and Smashdle.net.

### Description
This program began as a text channel on Discord where friends would post their results from specific idles. I had the idea to surprise them by upping the stakes and making things more interesting by allocating a score based on our performance. Currently, Scordle is a simple Python program using the Discord API and perform the following functions:

- Allow members to register for the service using the '/register' command.
  - Registering will create a new List for the user with a format mentioned later in this document
- Tally Scores for # of guesses per category
- Rank all registered users based a specified idle.
- Prevent players from submitting their results twice in one day to gain drastic points.

### Long-Term Development
Currently, hosting options are being explored to keep the bot active. It only includes two idles at this time, but development plans include expansion to Onepiecedle.net and Pokedle.net results. This is a hobby project that I intend to surprise my non-CS friends with, so the intention is to have a calm, peaceful development process.

Currently, data consistency is my largest concern. As things stand, each time the bot is run, it will completely clear out all registered users, resetting their scores entirely. The prospective implementation will be to use File I/O to write save data to a text file, and then read from that same file upon startup to initialize the player list.

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
