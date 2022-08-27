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

from pathlib import Path

from libqtile import bar, layout, hook  # , widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

# qtile extras for widget decorations
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from colors import Colors
import subprocess  # for hooks

# General/quick access settings
mod = "mod4"
terminal = "alacritty"
browser = "firefox"
home = Path.home()
wallpaper = home / "Pictures/Wallpapers/catpuccin/waves/Waves Dark 6016x6016.jpg"
default_margin = 10  # window gaps
bar_size = 30
bar_fontsize = 14
bar_margin = int(default_margin / 2)  # smaller gap for bar
volume_mod = 5
brightness_mod = 5

# rofi scripts
rofi = {
    "apps": str(home / ".config/rofi/apps/apps.sh"),
    "powermenu": str(home / ".config/rofi/powermenu/powermenu.sh"),
    "window": str(home / ".config/rofi/window/window.sh"),
}

# Hooks
@hook.subscribe.startup_once
def autostart():
    autostart_path = home / ".config/qtile/autostart.sh"
    subprocess.Popen([autostart_path])


# Keybindings
keys = [
    # Focus windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows in layouts
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Switch groups/applications
    Key([mod], "Left", lazy.screen.prev_group(), desc="Switch to previous group"),
    Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),
    Key(
        [mod],
        "grave",
        lazy.screen.toggle_group(),
        desc="Switch to the last visited group",
    ),
    Key(
        ["mod1"], "Tab", lazy.spawn(rofi["window"]), desc="Spawn rofi with window menu",
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
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle Tiled/Floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "z",
        lazy.hide_show_bar("top"),
        desc="Toggle 'Zen' mode (no bar + fullscreen window)",
    ),
    # General operations
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Spawn commands
    Key([mod], "p", lazy.spawn(rofi["powermenu"]), desc="Spawn rofi power menu",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod],
        "b",
        lazy.spawn(browser),
        lazy.group["2"].toscreen(),
        desc="Launch default browser, move to browser group",
    ),
    Key([mod], "a", lazy.spawn(rofi["apps"]), desc="Spawn rofi with apps (drun) menu"),
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
]

# Group definitions
group_list = "1234567"
groups = [
    Group("1", label=""),
    Group("2", label="\ufa9e", matches=[Match(wm_class="firefox")]),
    Group("3", label="", matches=[Match(wm_class="code")]),
    Group("4", label=""),
    Group("5", label="", matches=[Match(wm_class="Thunderbird")]),
    Group("6", label="\uf11b", matches=[Match(wm_class="Steam")]),
    Group("7", label="\ue006", matches=[Match(wm_class="Spotify")]),
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
    index = (index + 1) % len(window.qtile.groups)
    window.cmd_togroup(window.qtile.groups[index].name)


@lazy.window.function
def window_to_prev_group(window):
    index = window.qtile.groups.index(window.group)
    index = (index - 1) % len(window.qtile.groups)
    window.cmd_togroup(window.qtile.groups[index].name)


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

# ScratchPads (invisible groups)
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
        Key(["control"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key(["control"], "2", lazy.group["scratchpad"].dropdown_toggle("gotop")),
        Key(["control"], "3", lazy.group["scratchpad"].dropdown_toggle("speedometer")),
        Key(["control"], "4", lazy.group["scratchpad"].dropdown_toggle("calcurse")),
    ]
)

# Layout configs
layouts = [
    layout.Columns(
        margin=default_margin,
        border_width=3,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_normal=Colors.frappe["Overlay0"],
        border_focus=Colors.frappe["Sapphire"],
        border_on_single=True,
    ),
    layout.Max(margin=0,),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Widget decorations - background boxes
# left, right, middle (none) decor determines rounded edges
default_padding = 3
decor = {
    "decorations": [
        RectDecoration(colour=Colors.mocha["Crust"], radius=10, filled=True, padding=0,)
    ],
    "padding": default_padding,
}
leftdecor = {
    "decorations": [
        RectDecoration(
            colour=Colors.mocha["Crust"], radius=[10, 0, 0, 10], filled=True, padding=0,
        )
    ],
    "padding": default_padding,
}
rightdecor = {
    "decorations": [
        RectDecoration(
            colour=Colors.mocha["Crust"], radius=[0, 10, 10, 0], filled=True, padding=0,
        )
    ],
    "padding": default_padding,
}
middledecor = {
    "decorations": [
        RectDecoration(colour=Colors.mocha["Crust"], radius=0, filled=True, padding=0,)
    ],
    "padding": default_padding,
}

widget_defaults = dict(
    font="Ubuntu",
    fontsize=bar_fontsize,
    # foreground=Colors.mocha["Text"],
    # background=Colors.transparent,
    padding=0,
)
extension_defaults = widget_defaults.copy()
default_sep_widget = widget.Sep(
    foreground=Colors.transparent, background=Colors.transparent, linewidth=5
)

# Widgets
widget_list = [
    widget.TextBox(
        font="Nerd",
        fontsize=bar_fontsize + 4,
        foreground=Colors.mocha["Sapphire"],
        fmt=" \uf303 ",
        mouse_callbacks={"Button1": lazy.spawn(rofi["apps"])},
        **decor,
    ),
    default_sep_widget,
    widget.GroupBox(
        font="Nerd",
        fontsize=bar_fontsize + 4,
        margin_x=10,
        markup=True,
        visible_groups=group_list,
        rounded=True,
        highlight_method="border",
        borderwidth=1,
        padding_y=1,
        this_current_screen_border=Colors.mocha["Sapphire"],
        active=Colors.mocha["Sapphire"],
        this_screen_border=Colors.mocha["Red"],
        inactive=Colors.mocha["Red"],
        disable_drag=True,
        **decor,
    ),
    default_sep_widget,
    widget.Prompt(**decor),
    widget.WindowName(
        foreground=Colors.mocha["Crust"],
        font="Ubuntu",
        fontsize=bar_fontsize + 2,
        format=" \uf2d0 {name}",
        width=310,
        scroll=True,
    ),
    widget.Spacer(width="stretch"),
    widget.Clock(
        format="  %H:%M  %a, %-d %b  ",  # shows eg. Tue, 7 Jun  11:17
        foreground=Colors.mocha["Text"],
        mouse_callbacks={
            "Button1": lazy.group["scratchpad"].dropdown_toggle("calcurse")
        },
        **decor,
    ),
    widget.Spacer(),
    default_sep_widget,
    widget.WidgetBox(
        text_closed="\ufc95",
        text_open="\ufc96",
        font="Bold",
        foreground=Colors.mocha["Crust"],
        widgets=[
            default_sep_widget,
            widget.Systray(),
            default_sep_widget,
            widget.PulseVolume(
                fmt=" \ufa7d {}",
                limit_max_volume=True,
                foreground=Colors.mocha["Lavender"],
                # emoji=True,
                **leftdecor,
            ),
            widget.Backlight(
                foreground=Colors.mocha["Teal"],
                backlight_name="intel_backlight",
                fmt=" \uf5dd {}",
                **middledecor,
            ),
            widget.Wlan(
                format=" \uf1eb {percent:2.0%}",
                disconnected_message=" \ufaa9",
                foreground=Colors.mocha["Green"],
                mouse_callbacks={
                    "Button1": lazy.group["scratchpad"].dropdown_toggle("speedometer")
                },
                **middledecor,
            ),
            # widget.CPU(
            #     format="  \ue266  {load_percent}%  ",
            #     mouse_callbacks={
            #         "Button1": lazy.group["scratchpad"].dropdown_toggle("gotop")
            #     },
            #     foreground=Colors.mocha["Yellow"],
            #     **middledecor,
            # ),
            widget.Memory(
                format=" \ue240 {MemPercent} ({SwapPercent})%",
                mouse_callbacks={
                    "Button1": lazy.group["scratchpad"].dropdown_toggle("gotop")
                },
                foreground=Colors.mocha["Yellow"],
                **middledecor,
            ),
            widget.Battery(
                format=" \uf57d {char} {hour:d}h{min:02d}m ({percent:2.0%})  ",
                discharge_char="\uf175",
                charge_char="\uf176",
                foreground=Colors.mocha["Peach"],
                **rightdecor,
            ),
        ],
    ),
    default_sep_widget,
    widget.Sep(**leftdecor, linewidth=8, foreground=Colors.transparent),
    widget.BatteryIcon(
        theme_path=home / ".config/qtile/battery-icons/", scale=1.00, **middledecor,
    ),
    widget.TextBox(
        font="Nerd Bold",
        fmt=" \uf924 ",
        fontsize=bar_fontsize + 4,
        foreground=Colors.latte["Flamingo"],
        mouse_callbacks={"Button1": lazy.spawn(rofi["powermenu"])},
        **rightdecor,
    ),
    # widget.QuickExit(
    #     fontsize="16",
    #     foreground=Colors.latte["Maroon"],
    #     background=Colors.transparent,
    #     default_text="    ",
    #     countdown_format="  [{}]  ",
    #     **rightdecor,
    # ),
]

keys.extend(
    [
        Key(
            [mod],
            "x",
            lazy.widget["widgetbox"].toggle(),
            desc="Toggle WidgetBox open/closed",
        ),
    ]
)

screens = [
    Screen(
        top=bar.Bar(
            widget_list,
            size=bar_size,
            background=Colors.transparent,
            # background=Colors.latte["Crust"],
            margin=[bar_margin, bar_margin, bar_margin, bar_margin],  # [N E S W]
            # margin=0,
        ),
        bottom=bar.Gap(default_margin),
        left=bar.Gap(default_margin),
        right=bar.Gap(default_margin),
        wallpaper=wallpaper,
        wallpaper_mode="stretch",
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
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=2,
    border_focus=Colors.frappe["Mauve"],
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="zoom "),  # Zoom meetings
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
