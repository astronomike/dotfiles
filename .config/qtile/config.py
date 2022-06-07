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

from libqtile import bar, layout#, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#qtile extras for widget decorations
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

# General/default settings
mod = "mod1"  #mod1 -> Alt key
terminal = "alacritty"
browser = "firefox"
default_margin = 20
bar_margin = int(default_margin/2)

# Color definitions
colors_latte = {"sky":      "#04a5e5",
                "teal":     "#179299"
                }

colors_frappe = {"crust":       "#232634",
                 "base":        "#303446",
                 "overlay":     "#6e778d",
                 "alttext":     "#b5bfe2",
                 "text":        "#c6d0f5",
                 "yellow":      "#e5c890",
	             "rosewater":   "#f2d5cf",
	             "flamingo":    "#eebebe",
                 "pink":        "#f4b8e4",
                 "peach":       "#ef9f76",
                 "maroon":      "#ea999c",
                 "red":         "#e78284",
                 "mauve":       "#ca9ee6",
                 "blue":        "#8caaee",
	             "sapphire":    "#85c1dc",
	             "teal":        "#81c8be",
                 "sky":         "#91dbd1",
                 "green":       "#a6d189",
                 }

# Keybindings
keys = [
    # Focus windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Switch groups/applications
    Key([mod], "Left", lazy.screen.prev_group(), desc="Switch to previous group"),
    Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),
    Key([mod], "Tab", lazy.spawn("rofi -show window"), desc="Spawn rofi with window menu"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Layout management
    Key(["mod4"],"Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle Tiled/Floating"),
    Key([mod], "z", lazy.hide_show_bar(), lazy.window.toggle_fullscreen(), desc="Toggle Zen mode (no bar + fullscreen window)"),
    # General operations
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Spawn commands
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), lazy.group["2"].toscreen(), desc="Launch default browser, move to browser group"),
    Key([mod], "a", lazy.spawn("rofi -show run"), desc="Spawn rofi with run menu"),

]

# Group definitions
group_list = "123456"
groups = [Group("1",label=""),#,matches=[Match(title="")]),
          Group("2",label="",matches=[Match(wm_class="firefox")]),
          Group("3",label="",matches=[Match(wm_class="code-oss")]),
          Group("4",label=""),  #""),#,matches=[Match(title="")])
          Group("5",label=""),#,matches=[Match(title="")])
          Group("6",label=""),#,matches=[Match(title="")])
]

for i in groups:
    keys.extend([Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name),),
                 Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name),),
                ])

# Layout configs
layouts = [
    layout.Columns(margin=default_margin,
		           border_width=0,	#border doesn't work too nicely with rounded corners at the moment
		           border_focus_stack=["#d75f5f", "#8f3d3d"],
		           border_normal=colors_latte["teal"],
		           border_focus=colors_latte["sky"],
		           border_on_single=True),
    layout.Max(),
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

widget_defaults = dict(
    font="Ubuntu",
    #font="sans",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

decor = {
    "decorations": [
        RectDecoration(colour=colors_frappe["crust"], radius=10, filled=True, padding_y=0)
    ],
    "padding": 3,
}

widget_list = [widget.GroupBox(font="Nerd",
				               fontsize=18,
                               margin_x=8,
				               markup=True,
				               visible_groups=group_list,
				               rounded=True,
                               highlight_method="border",
                               borderwidth=1,
				               background="#00000000",
                               this_current_screen_border=colors_frappe["sapphire"],
                               active=colors_frappe["sapphire"],
                               this_screen_border=colors_frappe["red"],
                               inactive=colors_frappe["maroon"],
                               # highlight_color=[colors_frappe["crust"],colors_frappe["overlay"]],
                               # padding_x=6,
                               **decor,
                               ),
                widget.Prompt(background=colors_frappe["crust"],),
                widget.WindowName(foreground=colors_frappe["text"],),
                widget.Spacer(),
                # widget.TextBox("mike's config",foreground=colors_frappe["text"],),
                widget.Systray(),
                widget.Clock(format="  %a, %-d %b  %H:%M  ",    #shows eg. Tue, 7 Jun  11:17
                             foreground=colors_frappe["text"],
                             #background=colors_frappe["crust"],
                            #  padding=10,
                             **decor,),
                # widget.CurrentLayoutIcon(scale=0.6,
                                        #  foreground=colors_frappe["text"],
                                        #  background="#00000000",
                                        #  **decor,),
                # widget.MemoryGraph(type="linefill",
				# 				   samples=50,
                #                    width=50,
				# 				   border_width=2,
                #                    graph_color=colors_frappe["sky"],
                #                    fill_color=colors_frappe["sky"],
                #                    border_color=colors_frappe["sky"],
                #                    background=colors_frappe["crust"],
                #                    ),
                # widget.CPUGraph(type="box",
                #                 samples=20,
				# 				width=50,
                #                 graph_color=colors_frappe["green"],
                #                 border_color=colors_frappe["green"],
                #                 background=colors_frappe["crust"],
                #                 ),
				widget.Sep(),
                widget.QuickExit(fontsize="15",
				                 foreground=colors_frappe["red"],
				                 # background=colors_frappe["crust"],
				                 default_text="    ",
				                 countdown_format="[{}]",
                                 # padding=10,
								 
								 **decor,
				                 ),
            	# widget.Sep(foreground=colors_frappe["crust"]),

]


screens = [
    Screen(top=bar.Bar(widget_list,
                       size=32,
                       background="#00000000",
                    #    background=colors_frappe["crust"],
                       margin=[bar_margin,bar_margin,0,bar_margin], #[N E S W]
                    #    opacity=0.9,
                       # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                       # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                       ),
           wallpaper="/home/michael/Pictures/Wallpapers/dt/0197.jpg",  
           wallpaper_mode="stretch",
          ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
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
