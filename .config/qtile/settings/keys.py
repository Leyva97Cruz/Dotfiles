# Configuracion de los atajos del teclado en Qtile

from libqtile.config import Key
from libqtile.lazy import lazy
from settings.rofi import runApps, runNav

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in[

    # -------- windows configs ------------------

    # Betwenn windows in current stack pane
    ([mod], "j",lazy.layout.down()),
    ([mod], "k",lazy.layout.up()),
    ([mod], "h",lazy.layout.left()),
    ([mod], "l",lazy.layout.right()),

    # Change size window
    ([mod,"shift"], "l",lazy.layout.grow()),
    ([mod,"shift"], "h",lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f",lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),    
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab",lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),

    # ----------- Apps -------------

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Doom Emacs
    ([mod], "d", lazy.spawn("emacs")),

    # Rofi
    ([mod], "r", lazy.spawn(runApps)),  # run apps
    ([mod, "shift"], "r", lazy.spawn(runNav)),  # navigation window

    # Browser
    ([mod],"b", lazy.spawn("brave")),
    
    # Filed explorer
    ([mod],"e", lazy.spawn("thunar")),

    # Screeshot
    ([mod],"s", lazy.spawn("scrot -e 'mv $f ~/Imagenes/'")),
    ([mod, "shift"],"s", lazy.spawn("scrot -s -e 'mv $f ~/Imagenes/'")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),


    # Audio Control Next, Preview, Pause, Play
    ([],"XF86AudioPlay", lazy.spawn("playerctl play-pause")),    
    ([],"XF86AudioPause", lazy.spawn("playerctl play-pause")),
    ([],"XF86AudioNext", lazy.spawn("playerctl next")),
    ([],"XF86AudioPrev", lazy.spawn("playerctl prev")),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),    

]]
