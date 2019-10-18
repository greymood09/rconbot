# What is this?
This repo currently contains a collection of tools and scripts to be used to remotely control (RCON) a Squad server.

# What is Squad (from wikipedia.org)?
Squad is a tactical first-person shooter video game "set in the current modern day environment" being developed by Canadian studio Offworld Industries. It is set to be self-published through Steam and is a spiritual successor to the multi-award-winning Project Reality modification for Battlefield 2. The game features several playable factions, including various insurgent forces and national armies. Squad became available on Steam Early Access on December 15, 2015.

See [the official website](https://joinsquad.com/) for more information.

# Planned feature list (not in any particular order)
- [ ] Add map voting to a server. Shortly after a match starts, the bot (this tool) sends text chat to all users and offers options on maps to vote on. The map with the highest vote is set as the next map. In the event of the tool failing or not running, the original map rotation takes over (defined in a config file).
- [ ] Having multiple map rotations based on some event (e.g. when player count is low, switch to seeding rotation). This feature will require this bot to handle the map rotations entirely and set next map every time (ignoring the default map rotation config file).
- [ ] A team shuffle command (optionally add the ability to vote for this).
- [ ] A team swap command that swaps both teams completely (useful for competitive servers).
- [ ] The ability to set which team joining players will be assigned to based on clan tags (also useful for competitive servers).
- [ ] (Very ambitious) some kind of team balance feature that perhaps triggers a team shuffle when the previous game was lopsided (using tickets, probably depends on mode). There's a lot of potential for these ideas, but it depends on what data is available through RCON.
- [ ] Automatically give whitelist to seeders/regulars who put in enough hours.
- [ ] The ability for players to ping an admin on Discord if no admin is available on the server.
- [ ] A trivia questions bot to keep seeding servers more interesting for players, possibly with rewards (whitelist for best players).

# Resources needed to develop this.
- The RCON protocol used by Squad servers is based off of [Valve's RCON protocol](https://developer.valvesoftware.com/wiki/Source_RCON_Protocol), with minor modifications (for handling Unicode and multi-packet messages). See [SQUAD RCON](https://discord.gg/8tpbYZK) Discord group for more support.
- The list of RCON allowed commands are found [in the wiki](https://squad.gamepedia.com/Server_Administration).

# Python version and testing.
I used Python 3.6.8 to write this, and used nose2 (the python3 version) to run the tests. Just use `nose2-3` in the root
directory to run the unit tests.

# License
The license is GPLv3. Please see the LICENSE file.