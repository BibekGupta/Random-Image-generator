import discord                                  # Discord Lib 
import time                                     # Time Lib for delay X fuction's
import random                                   # To generates random X value's 
import string                                   # String Lib
from setting import data                        # Import data from another file's
from PIL import Image, ImageDraw, ImageFont     # pip install pillow (for Images)

Debug_Mode, Error_Alert, Owner_Id, Bot_Id, Bot_Token, Warn_E , Ver = data()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

client_id = Bot_Id  
task_counter=0 #Starting Value Will be always zero

print('🟢 Running...')

def generate_random_string(length):
    character_pool = string.ascii_letters + string.digits
    return ''.join(random.choice(character_pool) for _ in range(length))

def generate_random_color():
    red = random.randint(0, 200)
    green = random.randint(0, 200)
    blue = random.randint(0, 200)

    return red, green, blue    

def generate_image_with_cuts(draw, width, height):
    random_color = generate_random_color() 
    num_cuts = int(70)
    for _ in range(num_cuts):
        x1 = random.randint(0, width - 80)
        y1 = random.randint(0, height - 0)
        x2 = random.randint(0, width - 0)
        y2 = random.randint(0, height - 0)
        
        draw.line([(x1, y1), (x2, y2)], fill=(random_color), width=2)

def generate_random_position():
    X=random.randint(0,100)
    Y=random.randint(0,100)

    return X,Y        

@client.event
async def on_ready(): #Console that I logged in
    await client.change_presence(activity=discord.Game(name=f"Version {Ver}"))
    print(f'I logged successfully [{client.user}] \n') if Debug_Mode else None

async def generate_image(message):
    global task_counter  # Use the global counter variable
    try:
            task_counter += 1
            random_string_length = 7
            random_word = generate_random_string(random_string_length)
            random_color = generate_random_color() 
            random_position= generate_random_position()

            print(f'Generate Image Fuction [{task_counter}]')
            print(f' | Random word was: [{random_word}]') if Debug_Mode else None
            print(f' | RGB was: [{random_color}]') if Debug_Mode else None
            print(f' | Position was: [{random_position}]') if Debug_Mode else None
            print(f' | Given Channel Id: [{message.id}]') if Debug_Mode else None

            base_image = Image.open("blank.png")
            draw = ImageDraw.Draw(base_image)

            font_size = 30
            # font = ImageFont.load_default().font_variant(size=font_size)
            font = ImageFont.truetype("Roboto-Black.ttf", size=30) # Used Google Font buz default was getting error on diff device's
        
            # text_position = (165, 80) # X , Y Center Point Better to Use Random
            text_position=(random_position)
            text_color = (random_color)

            draw.text(text_position, random_word, font=font, fill=text_color)

            generate_image_with_cuts(draw, base_image.width, base_image.height)

            generated_image_filename = "temp.png"

            base_image.save(generated_image_filename)

            await message.channel.send(file=discord.File(generated_image_filename))
            
            print(f' | File Was Send : [{generated_image_filename}] \n') if Debug_Mode else None

            return random_word

    except Exception as e:
            print(f'Got an error at Generate Function: {str(e)}')
            await message.channel.send(f'{Warn_E} Hey <@{Owner_Id}>,I Encountered an error in the Generate_Image! Check Logs') if Error_Alert else None

@client.event
async def on_message(message):  # Main Block Here Calling all fuctions
    if message.author == client.user:
        return
    
    if message.content=="test":
        await generate_image(message)

client.run(Bot_Token)    
