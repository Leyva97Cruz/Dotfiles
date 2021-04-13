
# Qtile Workspaces
from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys

"""
Icons:
    Icon    Name        Hex
           Browser     \uf269
    ﬙       mdi-chip    \ufb19
           Terminal    \ue795
           Code        \uf121
           settings    \ue615
           Folder      \uf74a
           Image       \uf7e8
           Camera      \uf03d
           Layers      \uf827
"""

groups = [Group(i) for i in [
    " \uf269 ", " \ufb19 ", " \ue795 "," \uf121 ", " \ue615 ", " \uf74a ", " \uf7e8 ", " \uf03d ", " \uf827 "
] ]

for i, group in enumerate(groups):

    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
