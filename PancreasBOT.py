import discord
import json
import random
import string
# from pytz import timezone     
# (this was added because heroku runs on GMT rather than EST but I can't change it because time delta cannot different timezone subtractions)
# (if we run the code from the timezones we are from, than it would be from the timezones that we are from. But if we host the bot through heroku, it will be GMT)

#git add ., git commit -am "ok", git push heroku master

client = discord.Client()
with open('PancreasBOTdata.json') as d:
    data = json.load(d)
data["images"]

@client.event
async def on_message(message):
    id = client.get_guild(1004603688062566430)
    if message.content.lower().find("what are the commands?") != -1:
        await message.channel.send("```hello\namogus\npanc\ns@//owo//\nI would like to have dome among us pictures please\nwhat is this bot```")
   
    if message.author != client.user:
        
        if message.content.lower().find("what is this bot") != -1:
            embed = discord.Embed(title = "**i am a bot**", color=0x2f90e0)
            embed.add_field(
            name = "i am a bot!",
            value = "i am a bot\n:thumbsup:",
            inline = (True)
            )
            embed.set_image(url = "https://i.kym-cdn.com/photos/images/newsfeed/001/881/819/986.png")
            embed.set_footer(text = "have fun")
            await message.channel.send(embed=embed)
        
        if message.content.lower().find("hello") != -1:
            await message.channel.send("https://i.kym-cdn.com/entries/icons/original/000/034/887/daedon.jpg")

        if message.content.lower().find("amogus") != -1:
            await message.channel.send(":face_with_raised_eyebrow:")

        if message.content.lower().find("panc") != -1:
            if message.content.find(" ") == -1:
                await message.channel.send(f"""is very cool (100%) 
            - {message.author}""")

        if client.user.mentioned_in(message):
                await message.channel.send("WHAT")

        if message.content.lower().find("I would like to have some among us pictures please") != -1:
                await message.channel.send(f"""|| {data["images"][random.randint(0, len(data["images"])-1} ||""")])
       
        if message.content.lower().find("christmas") != -1:
            # est = timezone('EST')     (Read above)
            time = datetime.now()
            christmas = datetime(datetime.now().year, 12, 25, 0, 0, 0, 0, )
            diff = christmas-time
                                                   
             if time.month < christmas.month:
                    await message.channel.send(f"There are {diff.days} days, {int(diff.seconds/3600)} hours, {int(diff.seconds%3600/60)} minutes, {(diff.seconds%3600)%60} seconds, {diff.microseconds} microseconds until 9/11 (GMT) :pensive:")
                    await message.channel.send("https://www.citypng.com/public/uploads/preview/-41603940812rethyhget8.png")
                elif time.month == christmas.month:
                    if time.day == christmas.day:
                        await message.channel.send("Today is christmas! (best holiday)")
                        await message.channel.send("https://www.citypng.com/public/uploads/preview/-41603940812rethyhget8.png")
                    elif time.day < christmas.day:
                        await message.channel.send(f"There are {diff.days} days, {int(diff.seconds/3600)} hours, {int(diff.seconds%3600/60)} minutes, {(diff.seconds%3600)%60} seconds, {diff.microseconds} microseconds until 9/11 (GMT) :pensive:")
                        await message.channel.send("https://www.citypng.com/public/uploads/preview/-41603940812rethyhget8.png")
                    else:
                        christmas = datetime(datetime.now().year + 1, 12, 25, 0, 0, 0, 0)
                        diff = christmas-time
                        await message.channel.send(f"There are {diff.days} days, {int(diff.seconds/3600)} hours, {int(diff.seconds%3600/60)} minutes, {(diff.seconds%3600)%60} seconds, {diff.microseconds} microseconds until 9/11 (GMT) :pensive:")
                        await message.channel.send("https://www.citypng.com/public/uploads/preview/-41603940812rethyhget8.png")
                else:
                    christmas = datetime(datetime.now().year + 1, 12, 25, 0, 0, 0, 0)
                    diff = christmas-time
                    await message.channel.send(f"There are {diff.days} days, {int(diff.seconds/3600)} hours, {int(diff.seconds%3600/60)} minutes, {(diff.seconds%3600)%60} seconds, {diff.microseconds} microseconds until 9/11 (GMT) :pensive:")
                    await message.channel.send("https://www.citypng.com/public/uploads/preview/-41603940812rethyhget8.png")

client.run("//redacted bc its my bot token//")
