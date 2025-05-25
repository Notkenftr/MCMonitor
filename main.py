import discord
import pytz
from datetime import datetime
from discord.ext import commands, tasks
from mcstatus import JavaServer

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


asiaTime = pytz.timezone('Asia/Bangkok')
message = None

serverName = ''
serverIp = '' #ip + port / localhost:25565
botToken = ''

#Hướng dẫn sử dụng
#1. vào kênh cần thông báo status sử dụng /start
#2. để stop sử dụng /stop




@tasks.loop(seconds=5)
async def server_lookup(ctx):
    global message
    try:
        server = JavaServer.lookup(serverIp)
        status = server.status()
        latency = round(status.latency)
        players = status.players
        now = datetime.now(asiaTime).replace(microsecond=0)
        footer = f"Cập nhập vào: {now}"
        embed = discord.Embed(
            title=serverName,
            description=(
                "**Thông tin**\n"
                "> **IP:** `103.161.113.54:25049`\n"
                "> **Version:** `1.9.x -> 1.21.4`\n"
                "**Trạng thái**\n"
                f"> **Status:** ``🟢 Online``\n"
                f"> **Ping:** `{latency}ms`\n"
                f"> **Players:** `{players.online}/{players.max}`"
            ),
            color=discord.Color.green()
        )
        embed.set_footer(text=footer)

    except Exception as e:
        embed = discord.Embed(
            title=serverName,
            description="Không thể kết nối tới server.",
            color=discord.Color.red()
        )
        print(f"Lỗi: {e}")

    if not message:
        message = await ctx.send(embed=embed)
    else:
        await message.edit(embed=embed)

@bot.tree.command(name='start', description='start')
async def starttrack(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    if not interaction.user.guild_permissions.add_reactions:
        await interaction.followup.send('``❌ Không có quyền sử dụng lệnh này``', ephemeral=True)
        return
    global message
    message = None
    if not server_lookup.is_running():
        await interaction.followup.send("✅ Đã chạy", ephemeral=True)
        server_lookup.start(interaction.channel)
    else:
        await interaction.followup.send("⚠️ Đang chạy rồi!", ephemeral=True)

@bot.tree.command(name='stop', description='stop')
async def stoptrack(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    if not interaction.user.guild_permissions.add_reactions:
        await interaction.followup.send('``❌ Không có quyền sử dụng lệnh này``', ephemeral=True)
        return
    if server_lookup.is_running():
        server_lookup.cancel()
        await interaction.followup.send("🛑 Đã dừng.", ephemeral=True)
    else:
        await interaction.followup.send("❌ Chưa chạy.", ephemeral=True)
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Đã chạy với {bot.user}")

bot.run(botToken)
#by kenftr
