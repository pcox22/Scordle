import discord
from discord import app_commands
from discord.ext import commands
from datetime import date
import copy
from cryptography.fernet import Fernet


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

score = []


@client.event
async def on_ready():
    print("bot is ready")

    synced = await client.tree.sync()
    print(f"Synced {len(synced)} command(s)")

@client.tree.command(name='test', description='This is a test slash-command.')
async def test_command(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f'This is a test command. You entered: {message}')

@client.tree.command(name='reset_all_scores', description='Reset every user\'s score to zero.')
async def reset_All_Scores(interaction: discord.Interaction):
    for user in score:
        user[1] = 0
        user[2] = 0
        user[3] = 0
        user[4] = 0
    await interaction.response.send_message(f'All scores have been reset to zero.')


@client.tree.command(name='print_all_scores', description='Display every score.')
async def print_All_Scores(interaction: discord.Interaction):
    output = ""
    for user in score:
        output += user[0] + ": " + " Narutodle: " + user[1] + " Smashdle: " + user[2] + " Pokedle: " + user[3] + " OnePieceDle: " + user[4] + "\n"

    await interaction.response.send_message(f'Scores: \n{output}')


@client.tree.command(name='register', description='Register for Scoredle.')
async def register(interaction: discord.Interaction):
    userExists = False
    username = interaction.user.display_name
    for user in score:
        if user[0] == username:
            await interaction.response.send_message(f'{username}, you silly goose! You\'re already registered!')
            userExists = True

    if not userExists:
        newUser = []
        newUser.append(username)    # Username
        newUser.append(0)           # Narutodle
        newUser.append(0)           # Smashdle
        newUser.append(0)           # Pokedle
        newUser.append(0)           # OnePieceDle
        newUser.append("-- --")         # Narutodle Date
        newUser.append("-- --")         # Smashdle Date
        newUser.append("-- --")         # Pokedle Date
        newUser.append("-- --")         # OP Date
        score.append(newUser)
        await interaction.response.send_message(f'{username}, congratulations! You are ready to play!')

@commands.has_permissions(administrator=True)
@client.tree.command(name='delete_all_scores', description='ONLY SELECT TO DELETE ALL SCORES')
async def clear_All(interaction: discord.Interaction):
    score = []
    await interaction.response.send_message(f'EVERY Score has been deleted. Mwah ha ha.')


# Begin The Idle Programming
@client.tree.command(name="narutodle", description="Tally your score for the daily Narutodle.")
async def Narutodle(interaction: discord.Interaction, content: str):
    for user in score:
        for value in user:
            print(value, end=" ")
        print()

    print(content)
    username = interaction.user.display_name
    today = date.today()

    i = -1

    classicScore = 0.1
    jutsuScore = 0.1
    quoteScore = 0.1
    eyeScore = 0.1

    isRegistered = False

    try:
        for index in range(len(score)):
            print(index, username)
            if score[index][0] == username:
                i = index
                isRegistered = True

        if not isRegistered:
            await interaction.response.send_message(f"Please call /register to play Scoredle.")
            return

        if score[i][5] == today:
            await interaction.response.send_message(f"{username}, you cheater! You've already done the Narutodle today!")
            return

        # Classic Calculation
        index = content.find("Classic: ")
        curScore = ""
        if index != -1:
            index += 9
            while content[index].isdigit():
                curScore += content[index]
                index += 1

            if int(curScore) > 10:
                curScore = "10"

            classicScore = (21 - (int(curScore)))

        # Jutsu Calculation
        index = content.find("Jutsu: ")
        curScore = ""
        if index != -1:
            index += 7

        while content[index].isdigit():
            curScore += content[index]
            index += 1

            if int(curScore) > 10:
                curScore = "10"

            jutsuScore = (11 - int(curScore))

        # Quote Calculation
        index = content.find("Quote: ")
        curScore = ""
        if index != -1:
            index += 7

        while content[index].isdigit():
            curScore += content[index]
            index += 1

            if int(curScore) > 10:
                curScore = "10"

            quoteScore = (16 - int(curScore))

        # Eye Calculation
        index = content.find("Eye: ")
        curScore = ""
        if index != -1:
            index += 5

        while content[index].isdigit():
            curScore += content[index]
            index = 1
            if index > len(content):
                break

            if int(curScore) > 10:
                curScore = "10"

            eyeScore = (11 - int(curScore))

        if classicScore % 1 != 0 or jutsuScore % 1 != 0 or quoteScore % 1 != 0 or eyeScore % 1 != 0:
            await interaction.response.send_message(f"Something went wrong calculating you score.\nPlease verify you are copying the string correctly.")

        else:
            totalScore = classicScore + jutsuScore + quoteScore + eyeScore
            score[i][1] += totalScore
            score[i][5] = today
            await interaction.response.send_message(f"You gained {totalScore} points for the Narutodle on {today}. \nYou now have {score[i][1]} total Naurtodle points.")


    except Exception as e:
        await interaction.response.send_message(f"Something is off... Have the Dev check the debug log.")
        print(e)



@client.tree.command(name="smasdhle", description="Tally your score for today's smashdle.")
async def Smashdle(interaction: discord.Interaction, content: str):
    print(content)
    username = interaction.user.display_name
    today = date.today()

    i = -1

    classicScore = 0.1
    finalSmashScore = 0.1
    kirbyScore = 0.1
    emojiScore = 0.1
    silhScore = 0.1

    isRegistered = False

    try:
        for index in range(len(score)):
            if score[index][0] == username:
                i = index
                isRegistered = True

        if not isRegistered:
            await interaction.response.send_message(f"Please call /register to play Scoredle.")
            return

        if score[i][6] == today:
            await interaction.response.send_message(
                f"{username}, you cheater! You've already done the Smashdle today!")
            return

        # Classic Calculation
        index = content.find("Classic: ")
        curScore = ""
        if index != -1:
            index += 9
            while content[index].isdigit():
                curScore += content[index]
                index += 1

            if int(curScore) > 10:
                curScore = "10"

            classicScore = (21 - (int(curScore)))

        # Final Smash Calculation
        index = content.find("Final Smash: ")
        curScore = ""
        if index != -1:
            index += 13

        while content[index].isdigit():
            curScore += content[index]
            index += 1

            if int(curScore) > 10:
                curScore = "10"

            finalSmashScore = (11 - int(curScore))

        # Kirby Calculation
        index = content.find("Kirby: ")
        curScore = ""
        if index != -1:
            index += 7

        while content[index].isdigit():
            curScore += content[index]
            index += 1

            if int(curScore) > 10:
                curScore = "10"

            kirbyScore = (6 - int(curScore))

        # Emoji Calculation
        index = content.find("Emoji: ")
        curScore = ""
        if index != -1:
            index += 7

        while content[index].isdigit():
            curScore += content[index]
            index = 1

            if int(curScore) > 10:
                curScore = "10"

            emojiScore = (11 - int(curScore))

        # Silhouette Calculation
        index = content.find("Silhouette: ")
        curScore = ""
        if index != -1:
            index += 12

        while content[index].isdigit():
            curScore += content[index]
            index = 1
            if index > len(content):
                break

            if int(curScore) > 10:
                curScore = "10"

            silhScore = (11 - int(curScore))

        if classicScore % 1 != 0 or finalSmashScore % 1 != 0 or kirbyScore % 1 != 0 or emojiScore % 1 != 0 or silhScore % 1 != 0:
            await interaction.response.send_message(
                f"Something went wrong calculating you score.\nPlease verify you are copying the string correctly.")

        else:
            totalScore = classicScore + finalSmashScore + kirbyScore + emojiScore + silhScore
            score[i][2] += totalScore
            score[i][6] = today
            await interaction.response.send_message(
                f"You gained {totalScore} points for the Smashdle on {today}. \nYou now have {score[i][2]} total Smashdle points.")


    except Exception as e:
        await interaction.response.send_message(f"Something is off... Have the Dev check the debug log.")
        print(e)


@client.tree.command(name="rank_naruto", description="View a ranking of Narutodle Player's scores in Descending order.")
async def NarutodleRanking(interaction: discord.Interaction):
    players = copy.deepcopy(score)

    players = sort_narutodle(players)
    results = ""
    for i in range(len(players)):
        results += (f"{i + 1}: {players[i][0]} - {players[i][1]} Points [Last Played: {players[i][5]}]\n")

    await interaction.response.send_message(f"{results}")

@client.tree.command(name="rank_smash", description="View a ranking of Smashdle Player's scores in Descending order.")
async def SmashdleRanking(interaction: discord.Interaction):
    players = copy.deepcopy(score)

    players = sort_smashdle(players)
    results = ""
    for i in range(len(players)):
        results += (f"{i + 1}: {players[i][0]} - {players[i][2]} Points [Last Played: {players[i][6]}]\n")

    await interaction.response.send_message(f"{results}")


# Used for the ranking methods
def sort_narutodle(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

    return arr

def sort_smashdle(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

cipher_suite = Fernet(b'v-dCv0J2E4R2acNwt_atbuGftyIED_25SovOCMiSuB8=')
superSecret = cipher_suite.decrypt(b'gAAAAABpFkRrOzgnLV7xhRPjkJpBFzGR1FhbrXFVG3bsJbmpslnYow1k5ghcaTkY7MfKwjqzLOEZRF0CfkFzHqwjhTy_C1gTZ7QXMc4zJUqkvKTixL5m42y2B8KDxaole18VJ1FzFxvNZZzDWqEcLxuCRfAOOgH5QLBjl16nxzQmNuKYA9Zjgrk=')
superSecret = str(superSecret).replace('\'', '\"', -1)
constructed = ""
for i in range(len(superSecret)):
    if i != 0 and i != 1 and i != len(superSecret) - 1:
        constructed += superSecret[i]

#print(constructed)
client.run(constructed)