import os
import discord
from discord import app_commands

TOKEN = os.environ["MTU2MjU0MDM5NDYyODEyODgyMA.GGd30_.L6vT483GlhaABAkES4LuINviBDFDXbEi9o2-J0"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="purge", description="Löscht alle Nachrichten im Channel")
@app_commands.checks.has_permissions(manage_messages=True)
async def purge(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=None)
    await interaction.followup.send(f"{len(deleted)} Nachrichten gelöscht.", ephemeral=True)

@purge.error
async def purge_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("Dir fehlt die Berechtigung dafür.", ephemeral=True)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Eingeloggt als {client.user}")

client.run(TOKEN)
