local config_dir = os.getenv("XDG_CONFIG_HOME").."/"

qs = require("quicksettings")

-- The following are for keybinds and gestures to get the right directions based on vertical/horizontal workspace orientation
local ws
local ws_alt
local ws_plus
local ws_minus
if qs.workspace_orientation == "vertical" then
    ws = "vertical"
    ws_alt = "horizontal"
    ws_plus = "DOWN"
    ws_minus = "UP"
else
    ws = "orizontal"
    ws_alt = "vertical"
    ws_plus = "UP"
    ws_minus = "DOWN"
end

-- -----------------------
-- GESTURES
-- -----------------------
hl.gesture({ fingers = 3, direction = ws, action = "workspace" })
hl.gesture({ fingers = 3, direction = ws_alt, action = "scroll_move" })
hl.gesture({ fingers = 3, direction = "pinch", action = "fullscreen" })
-- gestures below need fixing, not sure if bug or what 
hl.gesture({ fingers = 4, direction = "up", action = function ()
    hl.dsp.send_shortcut({mods = "CTRL", key = "T", window = "activewindow"})
end
})
hl.gesture({ fingers = 4, direction = "down", action = function ()
    hl.dsp.send_shortcut({mods = "CTRL", key = "W", window = "activewindow"})
end
})
hl.gesture({ fingers = 4, direction = "left", action = function ()
    hl.dsp.send_shortcut({mods = "CTRL", key = "TAB", window = "activewindow"})
end
})
hl.gesture({ fingers = 4, direction = "right", action = function ()
    hl.dsp.send_shortcut({mods = "CTRL + SHIFT", key = "TAB", window = "activewindow"})
end
})

-- -----------------------
-- KEYBINDINGS
-- -----------------------
hl.bind(qs.mainMod .. " + CTRL + R", hl.dsp.exec_cmd("hyprctl reload"))
hl.bind(qs.mainMod .. " + Q", hl.dsp.window.close())
hl.bind(qs.mainMod .. " + T", hl.dsp.window.float({ action = "toggle" }))
--hl.bind(qs.mainMod .. " + CTRL + T", hl.dsp.workspaceopt("allfloat"))
hl.bind(qs.mainMod .. " + CTRL + P", hl.dsp.layout("pseudo"))
hl.bind(qs.mainMod .. " + S", hl.dsp.workspace.toggle_special("sysmonitor"))
hl.bind(qs.mainMod .. " + C", hl.dsp.workspace.toggle_special("calculator"))

-- Launchers
hl.bind(qs.mainMod .. " + Return", hl.dsp.exec_cmd(qs.terminal))
hl.bind(qs.mainMod .. " + B", hl.dsp.exec_cmd("firefox"))
hl.bind(qs.mainMod .. " + D", hl.dsp.exec_cmd(qs.fileManager))
hl.bind(qs.mainMod .. " + E", hl.dsp.exec_cmd("emacsclient -c -a ''"))
hl.bind(qs.mainMod .. " + I", hl.dsp.exec_cmd("copyq toggle"))
hl.bind(qs.mainMod .. " + W", hl.dsp.exec_cmd("pkill -SIGUSR1 wayscriber"))

-- Rofi
hl.bind(qs.mainMod .. " + R", hl.dsp.exec_cmd(config_dir.."rofi/run/run.sh"))
hl.bind(qs.mainMod .. " + A", hl.dsp.exec_cmd("sh "..config_dir.."rofi/apps/apps.sh"))
hl.bind(qs.mainMod .. " + P", hl.dsp.exec_cmd("sh "..config_dir.."rofi/powermenu/powermenu.sh"))
hl.bind(qs.mainMod .. " + O", hl.dsp.exec_cmd("sh "..config_dir.."rofi/filebrowser/filebrowser.sh"))
hl.bind("ALT + TAB", hl.dsp.exec_cmd("sh "..config_dir.."rofi/window/window.sh"))

-- Window actions
hl.bind(qs.mainMod .. " + M", hl.dsp.window.fullscreen({ mode = "maximized", action = "toggle" }))
hl.bind(qs.mainMod .. " + F", hl.dsp.window.fullscreen({ mode = "fullscreen", action = "toggle" }))

-- Special
hl.bind(qs.mainMod .. " + X", hl.dsp.window.move({ workspace = "special:hidden", silent = true }))
hl.bind(qs.mainMod .. " + SHIFT + X", hl.dsp.workspace.toggle_special("hidden"))

-- Move/Resize
hl.bind(qs.mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(qs.mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })
hl.bind(qs.mainMod .. " + CTRL + H", hl.dsp.window.resize({ x = -20, y = 0 }))
hl.bind(qs.mainMod .. " + CTRL + L", hl.dsp.window.resize({ x = 20, y = 0 }))
hl.bind(qs.mainMod .. " + CTRL + J", hl.dsp.window.resize({ x = 0, y = 20 }))
hl.bind(qs.mainMod .. " + CTRL + K", hl.dsp.window.resize({ x = 0, y = -20 }))

-- Inter-workspace Nav
for i = 1, 10 do
    local key = i % 10
    hl.bind(qs.mainMod .. " + " .. key, hl.dsp.focus({ workspace = i }))
    hl.bind(qs.mainMod .. " + SHIFT + " .. key, hl.dsp.window.move({ workspace = i }))
end
hl.bind(qs.mainMod .. " + " .. ws_plus, hl.dsp.focus({ workspace = "r+1" }))
hl.bind(qs.mainMod .. " + " .. ws_minus, hl.dsp.focus({ workspace = "r-1" }))
hl.bind(qs.mainMod .. " + SHIFT + " .. ws_plus, hl.dsp.window.move({ workspace = "r+1" }))
hl.bind(qs.mainMod .. " + SHIFT + " .. ws_minus, hl.dsp.window.move({ workspace = "r-1" }))
hl.bind(qs.mainMod .. " + CTRL + " .. ws_plus, hl.dsp.focus({ workspace = "e+1" }))
hl.bind(qs.mainMod .. " + CTRL + " .. ws_minus, hl.dsp.focus({ workspace = "e-1" }))
hl.bind(qs.mainMod .. " + mouse_up", hl.dsp.focus({ workspace = "m+1" }))
hl.bind(qs.mainMod .. " + mouse_down", hl.dsp.focus({ workspace = "m-1" }))

-- Intra-workspace Nav + Window Focus 
hl.bind(qs.mainMod .. " + TAB", hl.dsp.focus({ workspace = "previous_per_monitor" }))
hl.bind(qs.mainMod .. " + LEFT", hl.dsp.focus({ direction = "l"}))
hl.bind(qs.mainMod .. " + RIGHT", hl.dsp.focus({ direction = "r"}))
hl.bind(qs.mainMod .. " + H", hl.dsp.focus({ direction = "l"}))
hl.bind(qs.mainMod .. " + J", hl.dsp.focus({ direction = "d"}))
hl.bind(qs.mainMod .. " + K", hl.dsp.focus({ direction = "u"}))
hl.bind(qs.mainMod .. " + L", hl.dsp.focus({ direction = "r"}))
hl.bind(qs.mainMod .. " + SHIFT + LEFT", hl.dsp.window.move({ direction = "left" }))
hl.bind(qs.mainMod .. " + SHIFT + RIGHT", hl.dsp.window.move({ direction = "right" }))
hl.bind(qs.mainMod .. " + SHIFT + H", hl.dsp.window.move({ direction = "left" }))
hl.bind(qs.mainMod .. " + SHIFT + L", hl.dsp.window.move({ direction = "right" }))
hl.bind(qs.mainMod .. " + SHIFT + J", hl.dsp.window.move({ direction = "down" }))
hl.bind(qs.mainMod .. " + SHIFT + K", hl.dsp.window.move({ direction = "up" }))
hl.bind(qs.mainMod .. " + SHIFT + mouse_up", hl.dsp.focus({ direction = "r"}))
hl.bind(qs.mainMod .. " + SHIFT + mouse_down", hl.dsp.focus({ direction = "l"}))
hl.bind(qs.mainMod .. " + space", hl.dsp.focus({ direction = "right" }))
hl.bind(qs.mainMod .. " + space", hl.dsp.window.alter_zorder({ mode = "top" }))

-- -- Monitors
hl.bind("CTRL + ALT + LEFT", hl.dsp.workspace.move({ monitor = "l" }))
hl.bind("CTRL + ALT + RIGHT", hl.dsp.workspace.move({ monitor = "r" }))
hl.bind(qs.mainMod .. " + comma", hl.dsp.focus({ monitor = "-1" }))
hl.bind(qs.mainMod .. " + period", hl.dsp.focus({ monitor = "+1" }))
-- hl.bind(qs.mainMod .. " + CTRL + M", hl.dsp.exec_cmd('hyprctl keyword monitor "eDP-2,disable"'))
-- hl.bind(qs.mainMod .. " + CTRL + SHIFT + M", hl.dsp.exec_cmd('hyprctl keyword monitor "eDP-2,enable"'))

-- Groups
hl.bind(qs.mainMod .. " + G", hl.dsp.group.toggle())
hl.bind(qs.mainMod .. " + SHIFT + G", hl.dsp.group.next())

-- Waybar
hl.bind(qs.mainMod .. " + Z", hl.dsp.exec_cmd("killall -SIGUSR1 waybar"))
hl.bind(qs.mainMod .. " + SHIFT + Z", hl.dsp.exec_cmd("killall -SIGUSR2 waybar"))

-- -- Utilities
hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brightnessctl -e1 set +10%"), { locked = true, repeating = true })
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl -e1 set 10%-"), { locked = true, repeating = true })
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("pamixer -i 5"), { locked = true, repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("pamixer -d 5"), { locked = true, repeating = true })
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"), { locked = true })
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"), { locked = true })
hl.bind("Print", hl.dsp.exec_cmd("sh ~/.local/scripts/wayland-screenshot.sh"))

-- -- Power
-- hl.bind(qs.mainMod .. " + F12", hl.dsp.exec_cmd("hyprlock"))
-- hl.bind("switch:Lid Switch", hl.dsp.exec_cmd("hyprlock"))
-- hl.bind(qs.mainMod .. " + SHIFT + F12", hl.dsp.exec_cmd("sleep 1 && hyprctl dispatch dpms toggle"))

-- -- Exit
-- --hl.bind(qs.mainMod .. " + SHIFT + Q", hl.dsp.exec_cmd("sh ~/.local/scripts/logout.sh"))
-- --hl.bind(qs.mainMod .. " + SHIFT + Q", hl.dsp.exit())

hl.bind(qs.mainMod .. " + V", hl.dsp.submap("passthrough"),
    { description = "Submap for virtual machine keyboard passthrough." })
hl.define_submap("passthrough", function()
    hl.bind(qs.mainMod .. "+ V", hl.dsp.submap("passthrough"))
end)

hl.bind(qs.mainMod .. " + CTRL + G", function()
    -- Toggle gaps_in beween 0 and 3 (equivalent to  {3, 3, 3, 3} )

    local gapsInValueTable = hl.get_config("general.gaps_in")

    if gapsInValueTable.top == qs.gaps_in then
        hl.config({
            general = {gaps_in = 0}
        })
    else
        hl.config({
            general = {gaps_in = 3}
        })
    end
end)

-- Gamemode
local is_gamemode_active = false
local function toggle_gamemode()
    is_gamemode_active = not is_gamemode_active

    if is_gamemode_active then
        -- Disable eye candy
        hl.config({
            animations = { enabled = false },
            decoration = {
                rounding = 0,
                blur = { enabled = false },
                shadow = { enabled = false }
            },
            general = {
                gaps_in = 0,
                gaps_out = 0,
                border_size = 0,
            }
        })
        hl.dsp.exec_cmd("notify-send 'Gamemode On'")
    else
        -- Restore default settings
        hl.config({
            animations = { enabled = true },
            decoration = {
                rounding = qs.rounding,
                blur = { enabled = true },
                shadow = { enabled = true }
            },
            general = {
                gaps_in = qs.gaps_in,
                gaps_out = qs.gaps_out,
                border_size = qs.border_size,
            }
        })
        hl.dsp.exec_cmd("notify-send 'Gamemode Off'")
    end
end

-- Bind the function to a key combination (e.g., SUPER + M)
hl.bind(qs.mainMod.." + F1", toggle_gamemode)
