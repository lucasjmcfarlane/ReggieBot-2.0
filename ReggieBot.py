###POGCHAMP###
#Selects a random gif of a character doing the fortite default dance and sends it to the channel.
@client.command(pass_context = True , aliases=['pog'])
async def pogchamp(ctx):
	i=[
        "https://media.tenor.com/images/5d733c78788ce501949fe737709e5049/tenor.gif",
        "https://i.pinimg.com/originals/13/28/17/1328177857dfa41ab6bb71bf3166f42e.gif",
        "https://thumbs.gfycat.com/AgonizingUltimateAbalone-max-1mb.gif",
        "https://i.kym-cdn.com/photos/images/newsfeed/001/477/954/a55.gif",
        "https://thumbs.gfycat.com/FaithfulSneakyGoshawk-size_restricted.gif"
	]
	
	embed = discord.Embed(
		title="POGGERS!!",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = choice(i))
	await ctx.send(embed=embed)

###OWO###
#literally just prints "OwO"
@client.command()
async def owo(ctx):
	await ctx.send("**OwO**")

###UWU###
#literally just prints "UwU"
@client.command()
async def uwu(ctx):
	await ctx.send("**UwU**")


###PPSIZE#NSFW###
#returns the user's pp size
@client.command(pass_context = True , aliases=['pp'])
@commands.is_nsfw()
async def ppsize(ctx, *, user=''):
	original = user

	if user.startswith("<@"):
		user = user[3:-1]
		user = int(user)
		print(user)
		user = get(client.get_all_members(), id=user)
	else:
		try:
			user = await getmembers(ctx, user)
			user = int(user[1])
			user = get(client.get_all_members(), id=user)
		except:
			if original == '':
				user = ctx.message.author
			else:
				user = original

	i="8"
	j=random.randint(1,15)
	for k in range(j):
		i+="="
	i+="D"

	if (j > 10):
		i+=" **NICE!**"
	elif (j>5 and j<=10):
		i+=" **Not too bad!**"
	else:
		i+=" **That's pretty rough...**"

	embed = discord.Embed(
		title = f"{user}'s pp size: ",
		description=i
	)
	embed.set_image(url = "https://i.ytimg.com/vi/_zBaBlKgjWI/maxresdefault.jpg")
	await ctx.send(embed=embed)

@ppsize.error
async def ppsize_error(ctx, error):
	await ctx.send("You must be in a NSFW channel!")


###RATE###
#rates whatever is sent to the bot randomly
@client.command()
async def rate(ctx):
    j = [
        "1/10, ew.",
        "2/10, icky.",
        "3/10, meh.",
        "4/10, eh, alright i guess..",
        "5/10, Not horrible...",
        "6/10, It's alright",
        "7/10, Pretty good",
        "8/10, Very good",
        "9/10, Amazing",
        "10/10, POGGERS!",
    ]
    i=random.randint(0,len(j) -1)
    await ctx.send(j[i])

###REGGEPIC#NSFW###
#randomly returns one of sixteen images of reggie.
##NSFW##
@client.command(pass_context = True , aliases=['rpic'])
@commands.is_nsfw()
async def reggiepic(ctx):
	j=[
		"https://cdn.discordapp.com/attachments/505177959686995978/770072831182241802/ElHl5HTU0AEPAme.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770072904682831874/Ek8OMOXVgAIXl39.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770073506385362944/EiDm2fhU8AEccTY.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/805494433318436864/861b550f0ac0d8b800dd3d58cd9ed67c.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/805494782984978462/ce5269d0b908c50662aeb3f7818f3559.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770073830184976384/EdLZa3HWAAElkq0.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770073907616808970/EgMLgjCUcAAhRtj.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770073958979993660/EdIrkfgUMAAnXtF.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/805495107947069460/welcome-intrusion-005.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/805495475176210462/EsHlZdAVQAEUAYA.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/805495548340863016/Er8yS7LU0AAo6Im.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/805495574366781440/EsBtZJWW8AARDWq.png",
		"https://twitter.com/i/status/1314658830765047809",
		"https://twitter.com/i/status/1308214223080570880",
		"https://twitter.com/i/status/1281640986297290753",
		"https://twitter.com/i/status/1274037700698374144",
		"https://twitter.com/i/status/1247290642956341248",
		"https://twitter.com/i/status/1247293619536461826",
		"https://twitter.com/i/status/1243711781794504704",
		"https://twitter.com/i/status/1243711092846559232",
		"https://cdn.discordapp.com/attachments/505177959686995978/770074185208299630/unknown.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770074410689364048/unknown.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770074684582002748/unknown.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770074933518270485/EZHsOBdVAAExOkY.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770074992833462323/EYTvZOfXgAMqUwX.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770075316965998622/EX54hU7X0AcAIXV.png",
		"https://cdn.discordapp.com/attachments/505177959686995978/770075393687814174/EW8mhbkVcAAbeS5.png",
	]
	i=random.randint(0,len(j) -1)
	embed = discord.Embed(
		title="Here's Your Reggie pic!",
	)
	if (j[i].startswith("https://twitter.com")):
		embed.add_field(name="UwU", value=j[i])
	else:
		embed.set_image(url=j[i])
	await ctx.send(embed=embed)

@reggiepic.error
async def reggiepic_error(ctx, error):
	await ctx.send("You must be in a NSFW channel!")


###POLL###
#Creates a poll for the requested topic
@client.command()
async def poll(ctx,*,poll):
   message = await ctx.send(f"**{poll}?** *30 seconds to vote*")
   await message.add_reaction("👍")
   await message.add_reaction("👎")
   user = client.get_user(766730222665728061)


###WARCRIME###
#Reggie commits a warcrime
@client.command()
async def warcrime (ctx):
	i=[
		"**I just bombed an innocent Syrian village!!**",
		"**I just conducted a biological experiment on prisoners of war!!**",
		"**I just took a civilian hostage!!**",
		"**I led a direct attack against innocents!!**"
	]
	embed = discord.Embed(
		title=choice(i)
	)
	embed.set_image(url="https://img.ifunny.co/images/54e619252b0af7c944109eafdcdb1ee2fdeec8bae58d051654ad1612097cd5f1_1.gif")
	await ctx.send(embed=embed)

#########################
###MODERATION COMMANDS###
#########################
#server moderation type commands, as well as the reddit and r34 commsands

###GETMEMBERS###
#function to get a member by a string that their name contains. used throughout the entire bot
async def getmembers(ctx, user):
    
    if user == 'ME':
        return [ctx.message.author.name, ctx.message.author.id]

    user = user.lower()
    memberNameList = []
    memberIdList = []
    memberNickList = []
    matchingNameList = []
    matchingIdList = []
    matchingNicknameList = []

    #add the name and ID of every member to coresponding lists
    for member in ctx.message.guild.members:
        memberNameList.append(member.name)
        memberIdList.append(member.id)
        memberNickList.append(member.display_name)

    #find all members with matching strings in their names
    for i in range(len(memberNameList)):
        if user in memberNameList[i].lower():
            matchingNameList.append(memberNameList[i]) 
            matchingIdList.append(memberIdList[i])
        elif user in memberNickList[i].lower():
            matchingNameList.append(memberNameList[i]) 
            matchingIdList.append(memberIdList[i])

    #find if a user exactly matches the string
    for i in range(len(matchingNameList)):
        if matchingNameList[i].lower() == user:
            return [matchingNameList[i], matchingIdList[i]]

    if len(matchingNameList) == 1:
        return [matchingNameList[0], matchingIdList[0]]

    else:
        return ['','']

###MUTE###
#requires perms
#mute the selected member if you have the permissions to do so
@client.command(pass_context = True , aliases=['mt'])
@has_guild_permissions(mute_members=True)
async def mute(ctx, user):

	if user.startswith("<@"):
		user = user[3:-1]
		user = int(user)
		print(user)
		user = get(client.get_all_members(), id=user)
	else:
		user = await getmembers(ctx, user)
		user = int(user[1])
		user = get(client.get_all_members(), id=user)

	await user.edit(mute = True)
	await ctx.message.add_reaction("👍")

@mute.error
async def mute_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###DEAFEN###
#requires perms
#deafens the selected member if you have the permissions to do so
@client.command(pass_context = True , aliases=['df'])
@has_guild_permissions(deafen_members=True)
async def deafen(ctx, user):

	if user.startswith("<@"):
		user = user[3:-1]
		user = int(user)
		print(user)
		user = get(client.get_all_members(), id=user)
	else:
		user = await getmembers(ctx, user)
		user = int(user[1])
		user = get(client.get_all_members(), id=user)

	await user.edit(deafen = True)
	await ctx.message.add_reaction("👍")

@deafen.error
async def deafen_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###DISCONNECT###
#requires perms
#disconnects the chosen user if you have the permissions to do so
@client.command(pass_context = True , aliases=['dc'])
@has_guild_permissions(move_members=True)
async def disconnect(ctx, user):

	if user.startswith("<@"):
		user = user[3:-1]
		user = int(user)
		print(user)
		user = get(client.get_all_members(), id=user)
	else:
		user = await getmembers(ctx, user)
		user = int(user[1])
		user = get(client.get_all_members(), id=user)

	await user.edit(voice_channel = None)
	await ctx.message.add_reaction("👍")

@disconnect.error
async def disconnect_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###BAN###
#requires perms
#bans the chosen user
@client.command()
@has_guild_permissions(ban_members=True)
async def ban(ctx, user, *, reason):

	if user.startswith("<@"):
		user = user[3:-1]
		user = int(user)
		print(user)
		user = get(client.get_all_members(), id=user)
	else:
		user = await getmembers(ctx, user)
		user = int(user[1])
		user = get(client.get_all_members(), id=user)

	await ctx.guild.ban(user, reason=reason)
	await ctx.message.add_reaction("👍")

@ban.error
async def ban_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###KICK###
#requires perms
#kicks the chosen user
@client.command()
@has_guild_permissions(kick_members=True)
async def kick(ctx, user, *, reason):

	if user.startswith("<@"):
		user = user[3:-1]
		user = int(user)
		print(user)
		user = get(client.get_all_members(), id=user)
	else:
		user = await getmembers(ctx, user)
		user = int(user[1])
		user = get(client.get_all_members(), id=user)

	await ctx.guild.kick(user, reason=reason)
	await ctx.message.add_reaction("👍")

@kick.error
async def kick_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###CLEAR###
#requires perms
#clears the set amount of messages with the limit being 300
@client.command(pass_context = True , aliases=['clr'])
@has_guild_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    if (amount > 300): amount = 300
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###SENDMSG###
#Send a message to any channel reggie can access by channel ID
#This is meant for dev purposes, so it's left out of help
@client.command()
async def sendmsg(ctx, arg, *, message):
	channel = client.get_channel(int(arg))
	await channel.send(message)
	await ctx.message.add_reaction("👍")


###PINGSPAM###
#Spams the chosen user with 5 pings.
@client.command(pass_context = True , aliases=['spam'])
async def pingspam(ctx, *, userInput):
    user = userInput
    try: 
        user = await getmembers(ctx, user)
        user = int(user[1])
        user = get(client.get_all_members(), id=user)
        user = user.mention
    except:
        user = userInput

    for i in range(5):
        await ctx.send(user)


###PING###
#Reports the bot's ping to the user.
@client.command()
async def ping(ctx): ##Does "round()" round a number to the nearest integer value? because if so, that's pretty damn useful.
	await ctx.send(f'my ping is {round(client.latency * 1000)} ms')


###REDDIT#NSFW###
#gets a random post from the hot top 100 from the chosen subreddit.
@client.command(pass_context = True , aliases=['reddit'])
async def r(ctx, sub):
    await ctx.send("**Searching...**")
    try:
        postlist = []
        subreddit = reddit.subreddit(f'{sub}')

        if subreddit.over18:
            if ctx.message.channel.is_nsfw() == False:
                await ctx.send("This subreddit is NSFW, Please use an NSFW channel!")
                return

        hot = subreddit.hot(limit=50)
        for submission in hot:
            if not submission.stickied:
                postlist.append(submission.title)
                postlist.append(submission.author)
                postlist.append(submission.url)

        i=len(postlist)
        j = random.randint(0, (i/3)-1)
        await ctx.send(f'**{postlist[j*3]}\nPost by: u/{postlist[(j*3)+1]}**')
        await ctx.send(f'{postlist[(j*3)+2]}')
    except:
        await ctx.send("**Something went wrong, maybe check your spelling?**")


###NEWEVENT###
#allow users to create new events and have reggie notify them when they occur (only down to the hour right now)
@client.command()
async def newevent(ctx, setTime, *,eventName):

	#get the current date and time and format it
	currentTime = str(datetime.now())
	currentTime = currentTime.replace(" ", "").replace("-", "")
	currentTime = currentTime[:10]

	#format the date given by the user
	setTime = setTime.replace("-", "")

	#check that the inputted date length is the same as the current to ensure valid input
	if ( len(setTime) != len(currentTime) ):
		await ctx.send("Invalid date, try again")
		return

	#get clannel id so notification can be sent there
	channel = str(ctx.channel.id)
	#get server id for check events command
	server = str(ctx.guild.id)

	#assign information from currentTime to seperate variables to compare against user input
	currentYear = currentTime[:4]
	currentMonth = currentTime[4:6]
	currentDate = currentTime[6:8]
	currentHour = currentTime[8:]
	#assign information given by user to seperate variables to compare against current date
	setYear = setTime[:4]
	setMonth = setTime[4:6]
	setDate = setTime[6:8]
	setHour = setTime[8:]

	#a sketchy attempt at keeping invalid dates out of the database (a txt file)
	if (setYear < currentYear):
		await ctx.send("**Invalid Year, Try Again**")
		return
	if (setYear == currentYear and setMonth < currentMonth):
		await ctx.send("**invalid Month, Try Again**")
		return
	if (setYear == currentYear and setMonth == currentMonth and setDate < currentDate):
		await ctx.send("**invalid Date, Try Again**")
		return
	if (setYear == currentYear and setMonth == currentMonth and setDate == currentDate and setHour < currentHour):
		await ctx.send("**invalid Hour, Try Again**")
		return
    
	#after data has been verified, write the information to the events.txt document.
	f = open("events.txt", "a")
	f.write(f"{setTime}-{eventName}--{server}-{channel}\n")
	f.close()
	await ctx.send(f"**Event '{eventName}' added successfully!!**")

###VIEW EVENTS###
#see all currently set events for your server
@client.command()
async def viewevents(ctx):

	#open the file
	f = open("events.txt", "r")

	#clean up the items in the file
	eventList = []
	newEvents = []

	for line in f:
		eventList.append(line)
	for item in eventList:
		newEvents.append(item.replace("\n",""))

	eventList = newEvents

	#get the events that apply to the server of where the command was called
	currentServer = str(ctx.guild.id)
	
	#get a new list of events that belong to the correct server
	validEvents = []
	for item in eventList:
		if item.find(currentServer) > 1:
			validEvents.append(item)

	printEvents = []

	for item in validEvents:
		output = ""
		cutoff = item.find("--")
		output += f"{item[:4]}-{item[4:6]}-{item[6:8]}-{item[8:10]}: {item [11:cutoff] }"
		printEvents.append(output)
	
	output = ""
	counter = 1
	for item in printEvents:
		output += f"{counter}: {item}\n"
		counter+=1
	
	f.close()

	if len(printEvents) == 0:
		await ctx.send("**NO EVENTS!!**")
		return

	await ctx.send(output)

###DELEVENT###
#delete an event based on its numerical position in in the txt document
@client.command()
async def delevent(ctx, number):

	number = int(number)
	f = open("events.txt", "r+")

	#clean up the items in the file
	eventList = []

	for line in f:
		eventList.append(line)
	
	currentServer = str(ctx.guild.id)
	validEvents = []

	for item in eventList:
		if item.find(currentServer) > 1:
			validEvents.append(item)
	
	print(len(validEvents))
	
	if number > len(validEvents):
		await ctx.send("**Invalid Input, Try Again**")
		return

	itemToRemove = validEvents[number-1]
	f.seek(0)

	lines = f.readlines()
	f.seek(0)

	for line in lines:
		if line != itemToRemove:
			f.write(line)
	f.truncate()

	await ctx.send(f"**Event #{number} has been removed!**")
	f.close()

###################
###LOOPING TASKS###
###################

##STATUS##
#Changes the bot's status once an hour.
status = ["Doki Doki Literature Club","Huniepop","Minecraft", "Roblox", "Amorous"]
@tasks.loop(seconds=1200)
async def change_status():

	serverCount = 0
	userCount = 0
	for guild in client.guilds:
		serverCount += 1
		userCount += guild.member_count

	message = choice(status)
	message = message + f" (used by {userCount} people in {serverCount} servers!)"
	await client.change_presence(activity=discord.Game(message))


@tasks.loop(seconds=30)
async def check_events():
  #get the current date and time and format it
	currentTime = str(datetime.now())
	currentTime = currentTime.replace(" ", "").replace("-", "")
	currentTime = currentTime[:10]

	f = open("events.txt", "r+")

	eventList = []
	for line in f:
		eventList.append(line)

	for item in eventList:
		eventTime = item[:10]

		if eventTime == currentTime:
			
			#get the event name from the item
			cutoff = item.find("-")
			secondCutoff = item.find("--")
			eventName = item[(cutoff + 1):secondCutoff]
			print(eventName)

			#trim down item to server and chat
			cutoff = item.find("--")
			eventInfo = item[cutoff + 2:]

			#get event server from the event info
			cutoff = eventInfo.find("-")
			eventServer = eventInfo[:cutoff]

			#get the event chat from the event info
			eventChat = eventInfo[(cutoff + 1):]

			channel = client.get_channel(int(eventChat))
			await channel.send(f"@here **EVENT '{eventName}' IS HAPPENING RIGHT NOW!!**")

			f.seek(0)
			lines = f.readlines()
			f.seek(0)

			for line in lines:
				if line != item:
					f.write(line)
			f.truncate()
	f.close()

client.run(envTOKEN)
