# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess  
import random
from pathlib import Path
home = Path.home()

from libqtile import bar, layout, hook, qtile  # , widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger

# qtile extras for widget decorations
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from colors import Colors


##########################################################
# Wayland or X11
##########################################################
wayland = True if qtile.core.name == "wayland" else False
if wayland:
    screenshot = str(home / '.local/scripts/wayland-screenshot.sh')
    warp = False
else:
    screenshot = 'gnome-screenshot -i'
    warp = True

##########################################################
# General/quick access settings
##########################################################
mod = "mod4"
terminal = "alacritty"
browser = "firefox"
file_manager = "nemo"

default_margin = 6  # window gaps
bar_size = 36
bar_fontsize = 14
bar_margin = int(default_margin / 2)  # smaller gap for bar

volume_mod = 5
brightness_mod = 5

##########################################################
# theme and wallpaper
##########################################################
dark_theme = True

if dark_theme:
    theme = Colors.mocha
    bar_background = Colors.transparent
    # bar_background = theme["Surface1"]
    bar_foreground = theme["Text"]
else:
    theme = Colors.latte
    bar_background = theme["Crust"]
    bar_foreground = theme["Text"]

# @lazy.function
# def toggle_theme(qtile, dark_theme: bool):
#     if dark_theme:
#         theme = Colors.latte
#     else:
#         theme = Colors.mocha
#     lazy.reload_config()
# bar_background = theme["Crust"]


@lazy.function
def random_wallpaper(qtile, wayland: bool):
    """
    Set a new, random wallpaper from a pre-determined list of wallpapers.
    This method can be used in a keybinding or hook.

    This method finds the current wallpaper (from ~/.fehbg or swww query). 
    It then chooses a new random one from wallpaper_list,
    and there is a little check to make sure the same wallpaper as the current one
    isn't chosen.
    wallpaper_list is defined in this function to allow for intermediate changes to the list.
    """
    wallpaper_list = []
    wallpaper_path = home / "Pictures/Wallpapers/favourites/"
    for f in os.listdir(wallpaper_path):
        wallpaper = os.path.join(wallpaper_path, f)
        if os.path.isfile(wallpaper):
            wallpaper_list.append(wallpaper)
    new_wallpaper = random.choice(wallpaper_list)

    if wayland:
        # get current wallpaper (only consider first monitor)
        swww_query = subprocess.check_output(["swww","query"],text=True).splitlines()[0]
        # current_wallpaper = os.path.join(wallpaper_path, swww_query.split('"')[1])
        current_wallpaper = swww_query.partition("image")[-1]
        
        # set new wallpaper if different to current wallpaper
        while new_wallpaper == current_wallpaper:
            new_wallpaper = random.choice(wallpaper_list)        
        subprocess.run(["swww", "img", new_wallpaper, "--transition-fps","60"])
    else:
        with open(home / ".fehbg") as fehbg:
            last_line = fehbg.readlines()[-1]
            current_wallpaper = last_line.split()[-1][1:-1]

        while new_wallpaper == current_wallpaper:
            new_wallpaper = random.choice(wallpaper_list)
        os.system("feh --bg-fill " + new_wallpaper)


##########################################################
# rofi scripts
##########################################################
rofi = {
    "apps": str(home / ".config/rofi/apps/apps.sh"),
    "powermenu": str(home / ".config/rofi/powermenu/powermenu.sh"),
    "window": str(home / ".config/rofi/window/window.sh"),
    "filebrowser": str(home / ".config/rofi/filebrowser/filebrowser.sh"),
}

##########################################################
# Hooks
##########################################################
@hook.subscribe.startup_once
def autostart():
    if wayland:
        autostart_path = home / ".config/qtile/autostart_wayland.sh"
    else:
        autostart_path = home / ".config/qtile/autostart.sh"
    subprocess.Popen([autostart_path])

@hook.subscribe.shutdown
def autostop():
    if wayland:
        autostart_path = home / ".config/qtile/autostop_wayland.sh"
    else:
        autostart_path = home / ".config/qtile/autostop.sh"
    subprocess.Popen([autostop_path])

@hook.subscribe.screen_change
def restart_on_randr(_):
	qtile.cmd_reload_config()

##########################################################
# Keybindings
##########################################################
keys = [
    # Focus windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Focus screens
    Key([mod], "period", lazy.next_screen(), desc="Next monitor"),
    # Move windows in layouts
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "equal", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "minus", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Switch groups/applications
    Key([mod], "Left", lazy.screen.prev_group(), desc="Switch to previous group"),
    Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),
    Key([mod], "Up", lazy.layout.up(), desc="Move up in the layout stack"),
    Key([mod], "Down", lazy.layout.down(), desc="Move down in the layout stack"),
    Key(
        [mod, "control"],
        "Left",
        lazy.screen.prev_group(skip_empty=True, skip_managed=True),
        desc="Switch to previous group, skip empty",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.screen.next_group(skip_empty=True, skip_managed=True),
        desc="Switch to next group, skip empty",
    ),
    Key(
        [mod],
        "Tab",
        lazy.screen.toggle_group(),
        desc="Switch to the last visited group",
    ),
    Key(
        ["mod1"],
        "Tab",
        lazy.spawn(rofi["window"]),
        desc="Spawn rofi with window menu",
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Layout management
    Key([mod], "grave", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle Tiled/Floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "z",
        lazy.hide_show_bar("top"),
        desc="Toggle 'Zen' mode (no bar + fullscreen window)",
    ),
    Key(
        [mod],
        "x",
        lazy.widget["widgetbox"].toggle(),
        desc="Toggle WidgetBox open/closed",
    ),
    # General operations
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Themes
    # Key(
    #     [mod, "control"], "t", toggle_theme(dark_theme), desc="Toggle dark theme on/off"
    # ),
    Key([mod], "w", random_wallpaper(wayland), desc="Randomize wallpaper"),
    Key([mod, "control"], "p", lazy.spawn("pkill picom"), desc="Kill compositing"),
    Key(
        [mod, "control", "shift"], "p", lazy.spawn("picom -b"), desc="Start compositing"
    ),
    # Spawn commands
    Key(
        [mod],
        "p",
        lazy.spawn(rofi["powermenu"]),
        desc="Spawn rofi power menu",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Spawn terminal"),
    Key(
        [mod],
        "b",
        lazy.spawn(browser),
        lazy.group["3"].toscreen(),
        desc="Launch default browser, move to browser group",
    ),
    Key(
        [mod],
        "v",
        lazy.spawn("code"),
        lazy.group["4"].toscreen(),
        desc="Launch VS Code, move to code group",
    ),
    Key([mod], "a", lazy.spawn(rofi["apps"]), desc="Spawn rofi with apps (drun) menu"),
    Key(
        [mod],
        "o",
        lazy.spawn(rofi["filebrowser"]),
        desc="Spawn rofi with filebrowser mode",
    ),
    Key([mod], "e", lazy.spawn(file_manager), desc="Spawn file manager"),
    Key(
        [mod, "control"],
        "o",
        lazy.spawn("alacritty -e lf"),
        desc="Spawn tui file manager",
    ),
    # Audio control
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn(f"pamixer -d {volume_mod}"),
        desc=f"Lower volume by {volume_mod}%",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn(f"pamixer -i {volume_mod}"),
        desc=f"Raise volume by {volume_mod}%",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc=f"Pause/Play audio",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
    # Brightness control
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn(f"xbacklight -dec {brightness_mod}"),
        desc=f"Lower monitor brightness by {brightness_mod}",
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn(f"xbacklight -inc {brightness_mod}"),
        desc=f"Lower monitor brightness by {brightness_mod}",
    ),
    Key(
        [],
        "Print",
        lazy.spawn(screenshot),
        desc="Take screenshot",
    ),
]

##########################################################
# Group definitions
##########################################################
group_list = "1234567890"
groups = [
    Group("1", label="\ue795",layout="columns"),
    Group("2", label="\uf07c",layout="monadtall"),
    Group("3", label="\uf269", matches=[Match(wm_class="firefox")], layout="monadtall"),
    Group("4", label="\ue780", matches=[Match(wm_class="Code")], layout="monadtall"),
    Group(
        "5",
        label="\uf02d",
        matches=[Match(wm_class="qpdfview"), Match(wm_class="Zathura")],
        layout="treetab", 
    ),
    Group("6", label="󰇮", matches=[Match(wm_class="Ferdium")]),
    Group("7", label="\uf11b", matches=[Match(wm_class="Steam")],layout="floating"),
    Group("8", label="\uf001", matches=[Match(wm_class="Cider")]),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


@lazy.window.function
def window_to_next_group(window):
    index = window.qtile.groups.index(window.group)
    new_index = (index + 1) % len(window.qtile.groups)
    window.togroup(window.qtile.groups[new_index].name)


@lazy.window.function
def window_to_prev_group(window):
    index = window.qtile.groups.index(window.group)
    new_index = (index - 1) % len(window.qtile.groups)
    window.togroup(window.qtile.groups[new_index].name)


keys.extend(
    [
        Key(
            [mod, "shift"],
            "Left",
            window_to_prev_group,
            lazy.screen.prev_group(),
            desc="Switch to & move focused window to prev group",
        ),
        Key(
            [mod, "shift"],
            "Right",
            window_to_next_group,
            lazy.screen.next_group(),
            desc="Switch to & move focused window to next group",
        ),
    ]
)

##########################################################
# ScratchPads (invisible groups)
##########################################################
# defaults
sp_width = 0.6  # as a fraction of screen width
sp_height = 0.6  # as a fraction of screen height
sp_x = (1 - sp_width) / 2  # x position of window
sp_y = (1 - sp_height) / 2  # y position of window
sp_defaults = {
    "opacity": 1.0,
    "width": sp_width,
    "height": sp_height,
    "x": sp_x,
    "y": sp_y,
}
groups.extend(
    [
        ScratchPad(
            name="scratchpad",
            dropdowns=[
                DropDown("term", "alacritty", **sp_defaults),
                DropDown("gotop", "alacritty -e gotop", **sp_defaults),
                DropDown(
                    "speedometer",
                    "alacritty -e speedometer -r wlan0 -t wlan0",
                    **sp_defaults,
                ),
                DropDown("calcurse", "alacritty -e calcurse", **sp_defaults),
            ],
        )
    ]
)

keys.extend(
    [
        Key([mod, "control"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod, "control"], "2", lazy.group["scratchpad"].dropdown_toggle("gotop")),
        Key([mod, "control"], "3", lazy.group["scratchpad"].dropdown_toggle("speedometer")),
        Key([mod, "control"], "4", lazy.group["scratchpad"].dropdown_toggle("calcurse")),
    ]
)

##########################################################
# Layouts
##########################################################
layouts = [
    layout.Columns(
        margin=default_margin,
        border_width=3,
        border_focus_stack=[theme["Green"], theme["Lavender"]],
        border_normal=theme["Overlay0"],
        border_focus=theme["Sapphire"],
        border_on_single=True,
    ),
    layout.Max(
        margin=[
            0,
            -default_margin,
            -default_margin,
            -default_margin,
        ],
        border_width=3,
        border_on_single=True,
        border_normal=theme["Overlay0"],
        border_focus=theme["Sapphire"],
    ),
    layout.Floating(
        border_width=3,
        border_focus=theme["Mauve"],
        border_normal=theme["Overlay0"],
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(wm_class="zoom "),  # Zoom meetings
            Match(wm_class="feh"),
        ],
    ),
    # Try more layouts by unleashing below layouts.
    layout.Stack(
        num_stacks=1,
        margin=default_margin,
        border_width=3,
        border_focus=theme["Sapphire"],
        border_focus_stack=theme["Green"],
        border_normal=theme["Overlay0"],
        border_normal_stack=theme["Maroon"],
        border_on_single=True,
    ),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        ratio=0.6,
        margin=default_margin,
        border_width=3,
        border_focus_stack=[theme["Green"], theme["Lavender"]],
        border_normal=theme["Overlay0"],
        border_focus=theme["Sapphire"],
        border_on_single=True,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        margin=default_margin,
        margin_y=0,
        place_right=False,
        border_width=3,
        vspace=3,
        panel_width=150,
        sections=['Main'],
        section_fontsize=bar_fontsize,
        section_fg=theme["Text"],
        bg_color=theme["Crust"],
        active_bg=theme["Sapphire"],
        inactive_bg=theme["Base"],
        inactive_fg=theme["Text"],
        active_fg=theme["Crust"],
        section_left=10,
        section_top=10,
        padding_left=15,
    ),
    # layout.VerticalTile(),
    # layout.Zoomy(
    #     margin=default_margin,
    #     border_width=3,
    # ),
]

##########################################################
# Widgets
##########################################################
# Widget decorations - background boxes from qtile-extras
default_widget_padding = 3
decor_color = theme["Base"] if dark_theme else theme["Surface1"]
decor_group = {
    "decorations": [
        RectDecoration(
            colour=decor_color,
            radius=10,
            filled=True,
			padding_y=3,
            padding=0,
            group=True,
            clip=True,
        )
    ],
    "padding": default_widget_padding,
}
decor_group_statusnotifier = decor_group.copy()
decor_group_statusnotifier["padding"] = default_widget_padding + 4
icon_font = {"font": "Symbols Nerd Font", "fontsize": bar_fontsize + 4}

widget_defaults = dict(
    font="Ubuntu Nerd Font",
    fontsize=bar_fontsize,
)
extension_defaults = widget_defaults.copy()
default_sep_widget = widget.Sep(
    foreground=bar_background, background=bar_background, linewidth=5
)

# The following is a list of all widgets used
def init_widget_list():
    widget_list = [
		default_sep_widget,
        widget.TextBox(
            foreground=theme["Sapphire"],
            fmt=" \uf303 ",
            mouse_callbacks={"Button1": lazy.spawn(rofi["apps"])},
            **icon_font,
            **decor_group,
        ),
        widget.TextBox(
            foreground=theme["Text"],
            fmt="|",
            **decor_group,
        ),
        widget.GroupBox(
            margin_x=10,
            markup=True,
            visible_groups=group_list,
            rounded=True,
            highlight_method="border",
            # highlight_method="line",
            highlight_color=[theme["Base"],theme["Surface2"]],
            borderwidth=1.5,
            padding_y=2,
            active=theme["Sapphire"],
            inactive=theme["Red"],
            this_current_screen_border=theme["Green"],
            this_screen_border=theme["Overlay2"],
            other_current_screen_border=theme["Green"],
            other_screen_border=theme["Overlay2"],
            disable_drag=True,
            **icon_font,
            **decor_group,
        ),
        widget.TextBox(
            foreground=theme["Text"],
            fmt="|  ",
            **decor_group,
        ),
        widget.CurrentLayoutIcon(
            foreground=theme["Text"],
            fmt="{}",
            scale=0.55,
            **icon_font,
            **decor_group,
        ),
        widget.CurrentScreen(
            active_color=theme["Green"],
            active_text="  󱎴  ",
            inactive_color=theme["Red"],
            inactive_text="  󰶐  ",
            **icon_font,
            **decor_group,
        ),
        widget.Prompt(**decor_group),
        # widget.TextBox(
        #     foreground=theme["Text"],
        #     fmt="|",
        #     **decor_group,
        # ),
        # widget.WindowName(
        #     foreground=theme["Text"],
        #     font="Ubuntu Bold",
        #     format="  {name}  ",
        #     width=250,
        #     scroll=True,
        #     **decor_group,
        # ),
        widget.Spacer(width="stretch"),
        widget.WidgetBox(
            text_closed="󰞗",
            text_open="󰞔",
            font="Symbols Nerd Font Bold",
            foreground=theme["Base"],
            widgets=[
                default_sep_widget,
                widget.PulseVolume(
                    fmt=" 󰕾 {} ",
                    limit_max_volume=True,
                    foreground=theme["Lavender"],
                    **decor_group,
                ),
                widget.Backlight(
                    fmt=" 󰃞  {} ",
                    foreground=theme["Sapphire"],
                    backlight_name="intel_backlight",
                    **decor_group,
                ),
                widget.Wlan(
                    format=" \uf1eb {percent:2.0%} ",
                    disconnected_message=" \ufaa9 ",
                    foreground=theme["Teal"],
                    mouse_callbacks={
                        "Button1": lazy.group["scratchpad"].dropdown_toggle(
                            "speedometer"
                        )
                    },
                    **decor_group,
                ),
                widget.CPU(
                    format=" \ue266  {load_percent:.0f}% ",
                    mouse_callbacks={
                        "Button1": lazy.group["scratchpad"].dropdown_toggle("gotop")
                    },
                    foreground=theme["Green"],
                    **decor_group,
                ),
                widget.Memory(
                    format=" \ue240  {MemPercent:.0f}% ({SwapPercent:.0f}%) ",
                    mouse_callbacks={
                        "Button1": lazy.group["scratchpad"].dropdown_toggle("gotop")
                    },
                    foreground=theme["Yellow"],
                    **decor_group,
                ),
                widget.Battery(
                    format="{char} {hour:d}h{min:02d}m ({percent:2.0%})  ",
                    discharge_char="󱟟",
                    charge_char="󰂄",
                    foreground=theme["Peach"],
                    low_foreground=theme["Red"],
                    update_interval=5,
                    notify_below=0.1,
                    notification_timeout=0,
                    **decor_group,
                ),
            ],
        ),
        default_sep_widget,
        # widget.Systray(),
        widget.Sep(
            foreground=decor_color,
            # background=bar_background,
            linewidth=5,
            **decor_group,
        ),
        widget.BatteryIcon(
            theme_path=home / ".config/qtile/battery-icons/",
            update_interval=10,
            scale=1.4,
            **decor_group,
        ),
        widget.StatusNotifier(
            icon_theme="Papirus",
            icon_size=20,
            **decor_group_statusnotifier,
        ),
        widget.Clock(
            font="Ubuntu",
            format="  %H:%M  %a, %-d %b ",  # shows eg. Tue, 7 Jun  11:17
            foreground=bar_foreground,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("calcurse")
            },
            **decor_group,
        ),
        widget.TextBox(
            fmt=" \uf011  ",
            foreground=Colors.mocha["Red"],
            mouse_callbacks={"Button1": lazy.spawn(rofi["powermenu"])},
            **icon_font,
            **decor_group,
        ),
		default_sep_widget,
    ]

    return widget_list


systray_index = -3

# These functions return the widget lists for each screen
# Main screen uses all widgets, secondary uses all but systray
def init_main_widget_list():
    main_widget_list = init_widget_list()
    # if wayland:
    #     del main_widget_list[systray_index]
    return main_widget_list


def init_secondary_widget_list():
    secondary_list = init_widget_list()
    del secondary_list[systray_index]  # remove systray
    return secondary_list


##########################################################
# Screens
##########################################################
screens = [
    # main laptop monitor
    Screen(
        top=bar.Bar(
            widgets=init_main_widget_list(),
            size=bar_size,
            background=bar_background,
            # margin=[bar_margin, bar_margin, default_margin, bar_margin],  # [N E S W]
			margin=0,
        ),
        bottom=bar.Gap(default_margin),
        left=bar.Gap(default_margin),
        right=bar.Gap(default_margin),
        # wallpaper=wallpaper,
        # wallpaper_mode=wallpaper_mode,
    ),
    # secondary monitor
    Screen(
        top=bar.Bar(
            widgets=init_secondary_widget_list(),
            size=bar_size + 4,
            background=bar_background,
            #margin=[bar_margin, bar_margin, default_margin, bar_margin],  # [N E S W]
			margin=0,
        ),
        bottom=bar.Gap(default_margin),
        left=bar.Gap(default_margin),
        right=bar.Gap(default_margin),
        # wallpaper=wallpaper,
        # wallpaper_mode=wallpaper_mode,
    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = warp
floating_layout = layout.Floating(
    border_width=3,
    border_focus=theme["Mauve"],
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="zoom "),  # Zoom meetings
        Match(wm_class="feh"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
from libqtile.backend.wayland import InputConfig

wl_input_rules = {
    # Touchpad settings
    "1267:12299:ELAN0501:00 04F3:300B Touchpad": InputConfig(
        tap=True,
        natural_scroll=True,
        tap_button_map="lrm",  # 1 tap: l. click, 2 tap: r. click, 3 tap: m. click
    ),
}

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
