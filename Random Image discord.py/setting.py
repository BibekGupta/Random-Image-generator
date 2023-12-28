import discord

def data():
    Debug_Mode=True
    Error_Alert=True
    Owner_Id= 00000000000000                # Replacw with your own id
    Bot_Id= 000000000000000                 # Replace with Bot Id 
    Bot_Token=""                            # Replace with Your bot token
    Warn_E=discord.PartialEmoji(name='MI_info_warn', id='1090643537663639562', animated=True) #warn emoji
    Ver="0.1"

    # If you change alignment the Data here , It will get affected !!!
    return Debug_Mode, Error_Alert, Owner_Id, Bot_Id, Bot_Token, Warn_E , Ver 
