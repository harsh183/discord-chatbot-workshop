from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command(name="idea", help="Help you brainstorm an idea")
async def idea(ctx):
    await ctx.send("Aaah I see you're stuck with the paralysis of having so many different things to choose from")
    await ctx.send("Worry not, I think you should...")

    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extention', 'api', 'web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']

    idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)}! :slight_smile:'
    await ctx.send(idea)

@bot.command(name="calc", help="Perform 4 function calculator where fn is +, -, *, /")
async def calc(ctx, x: float, fn: str, y: float):
    answer = None
    if fn == '+':
        answer = x + y
    elif fn == '-':
        answer = x - y
    elif fn == '*':
        answer = x * y
    elif fn == '/':
        answer = x / y
    else:
        await ctx.send("You didn't format it right!")
        return

    response = f"{x} {fn} {y} is {answer}"
    await ctx.send(response)


# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read and bot started!")
    bot.run(TOKEN)
    