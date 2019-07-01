import discord as d

client = d.Client()



@client.event
async def on_ready():
    print("The bot is ready!")

    print(client.guilds[0].roles[15])
    print(client.guilds[0].text_channels)
    await client.get_channel(590485715196837888).send('bouh')
    
@client.event
async def on_message(message):

    if message.content == 'ok':
        for c in client.guilds:
            for i in c.text_channels:
                await message.channel.send([i.name, i.id])
            
    if message.content == 'ko':
        for c in client.guilds:
            for i in c.members:
                await message.channel.send([i.name," : ",i.top_role, i.roles])

    if message.content == 's':
        for c in client.guilds:
            for i in c.members:
                await i.add_roles(client.guilds[0].roles[1])
                
    if message.content == 'role':
        for c in client.guilds:
            for i in c.roles:
                await message.channel.send([i.id, i.name])
                
    if message.content == 'C1':
        await message.channel.send(':one:')
                
                
    if message.content == 'rol':
        for c in client.guilds:
            await message.channel.send(c.role)
                
    if message.content == 'listm':
        await message.channel.send(client.user)
        
    if message.content.startswith('p'):
        await d.TextChannel(message.id).send('oooo')
        
  
@client.event      
async def on_raw_reaction_add(payload):
    if payload.channel_id==593172777553625109:
        if payload.emoji.name=="😀":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="😀":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[10])

        if payload.emoji.name=="😂":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="😂":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[9])

        if payload.emoji.name=="👌":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="👌":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[8])

        if payload.emoji.name=="😎":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="😎":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[7])

        if payload.emoji.name=="💯":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="💯":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[6])

        if payload.emoji.name=="😋":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="😋":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[5])

        if payload.emoji.name=="😉":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="😉":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[4])

        if payload.emoji.name=="🙄":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="🙄":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[3])

        if payload.emoji.name=="🏃":
            await client.get_user(payload.user_id).send('Ton rôle a été ajouté')
        if payload.emoji.name=="🏃":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[2])

    if payload.channel_id==593183059440959579:
        if payload.emoji.name=="👍":
            await client.get_user(payload.user_id).send('Bienvenue futur data analyst! Je te conseille d ajouter tes roles dans le channel projets')
        if payload.emoji.name=="👍":
            await client.guilds[0].get_member(payload.user_id).add_roles(client.guilds[0].roles[15])       

        
@client.event
async def on_group_join(channel):
    channel.send('bienvenue')


client.run('NTkyNjM0MTE1OTkyMzIyMDQ4.XRE9Cg.Twcr2jRWKPIuCrpfL7nuM7KvoIE')