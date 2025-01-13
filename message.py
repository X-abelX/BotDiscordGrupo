import discord
from openai import OpenAI

api_key = 'TOKEN'

client = OpenAI(api_key=api_key)

async def get_chatgpt_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000
        )
        response = completion.choices[0].message.content
        formatted_content = format_response(response)
        return formatted_content
    except Exception as e:
        return f"Lo siento por no poder ayudarte esta vez... **Reportalo a un administrador** {e}"

def format_response(content):
    content = content.replace("```", "```\n")
    return content

hilos = [1328271421213900924] #sustituyelo por el id del canal que desees

async def message_on(message, bot):
    if isinstance(message.channel, discord.DMChannel):
        return
    
    if message.channel.id in hilos:
        thread = await message.create_thread(name=f"Duda de {message.author.name}", auto_archive_duration=60)
        async with message.channel.typing():
            response = await get_chatgpt_response(message.content)  # Pasar el contenido del mensaje
        response_message = f"**Hola {message.author.mention}**\n" + response + "\n\n**Espero te haya servido mi respuesta🤖. Sino es así, puedes esperar la respuesta de otro usuario.**"
        if len(response_message) > 2000:
            response_message = response_message[:1997] + "..."
        await thread.send(response_message)
    await bot.process_commands(message)