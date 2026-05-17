local config_dir = os.getenv("XDG_CONFIG_HOME").."/"

local colors = require("hyprtheme")
local binds = require("hyprbinds")
local qs = require("quicksettings")

-- -----------------------
-- ENVIRONMENT VARIABLES
-- -----------------------
hl.env("HYPRCURSOR_THEME", qs.hypr_cursor_theme)
hl.env("HYPRCURSOR_SIZE", "24")
hl.env("XCURSOR_THEME", qs.x_cursor_theme)
hl.env("XCURSOR_SIZE", "24")
hl.env("QT_QPA_PLATFORMTHEME", "qt6ct")
hl.env("SAL_USE_VCLPLUGIN", "qt6")
hl.env("GDK_SCALE", "1.0")
hl.env("ELECTRON_OZONE_PLATFORM_HINT", "auto")
hl.env("DOOMDIR", config_dir.."doom")
hl.env("XDG_CURRENT_DESKTOP", "Hyprland")
hl.env("XDG_SESSION_TYPE", "wayland")
hl.env("XDG_SESSION_DESKTOP", "Hyprland")
hl.env("AQ_DRM_DEVICES", "/dev/dri/card2:/dev/dri/card1")

-- -----------------------
-- Autostart
-- -----------------------
hl.on("hyprland.start", function()
    hl.exec_cmd("waybar -c "..config_dir.."waybar/config -s "..config_dir.."waybar/style.css") --horizontal main bar
    if qs.workspace_orientation == "vertical" then
        hl.exec_cmd("waybar -c "..config_dir.."waybar/config-vert -s "..config_dir.."waybar/style-vert.css") --vertical bar
    end
    hl.exec_cmd("awww-daemon")
    hl.exec_cmd("dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP")
    hl.exec_cmd("/usr/lib/polkit-kde-authentication-agent-1")
    hl.exec_cmd("nm-applet --indicator")
    hl.exec_cmd("sleep 2.0 & /usr/bin/pcloud") --pcloud looks for internet before its connected, sleep removes "no internet" notifs
    hl.exec_cmd("/usr/bin/dunst")
    hl.exec_cmd("fusuma -d -c "..config_dir.."fusuma/config-hyprland.yml")
    hl.exec_cmd("blueman-applet")
    hl.exec_cmd("bluetoothctl connect C0:BC:68:26:93:A9")     --Logi K250 keyboard
    hl.exec_cmd("pactl load-module module-switch-on-connect") --for bluetooth headphones
    hl.exec_cmd("hyprctl setcursor x_cursor_theme 24")
    hl.exec_cmd("gsettings set org.gnome.desktop.interface cursor-theme cursor_theme")
    hl.exec_cmd("wayscriber --daemon --no-tray")
    hl.exec_cmd("copyq --start-server ")
    hl.exec_cmd("hypridle")
    hl.exec_cmd("hyprsunset")
end)


-- -----------------------
-- MONITORS
-- -----------------------
hl.monitor({ output = "eDP-1", mode = "1920x1200", position = "0x0", scale = "1.333333" })
hl.monitor({ output = "eDP-2", mode = "1920x1200@90", position = "0x0", scale = "1.333333" })
hl.monitor({
    output = "desc:Samsung Electric Company C24F390 HFAR300143",
    mode = "1920x1080@60",
    position = "auto-right",
    scale =
    "1"
})
hl.monitor({
    output = "desc:LG Electronics LG FULL HD 403SHFK02755",
    mode = "1920x1080@60",
    position = "auto-right",
    scale =
    "1"
})
hl.monitor({ output = "desc:IWB PC Monitor", mode = "preferred", position = "auto-right", scale = "2" })
hl.monitor({ output = "DP-2", mode = "preferred", position = "auto-right", scale = "1.0" })
hl.monitor({ output = "", mode = "preferred", position = "auto", scale = "auto" })
-- Reserved area
--hl.monitor({ output = "", reserved = "42,0,0,0" }) -- Syntax might vary: check wiki for 'addreserved'

-- -----------------------
-- CONFIGURATION BLOCKS
-- -----------------------
hl.config({
    dwindle = {
        preserve_split = true,
        smart_split = false,
    },
    master = {
        mfact = 0.6,
    },
    scrolling = {
        direction = "right",
        column_width = 0.9,
        focus_fit_method = 0,
        fullscreen_on_one_column = true,
    },
    input = {
        kb_layout = "us",
        kb_options = "caps:swapescape",
        follow_mouse = 1,
        sensitivity = 0,
        numlock_by_default = true,
        touchpad = {
            natural_scroll = true,
        },
    },
    misc = {
        initial_workspace_tracking = 0,
        disable_autoreload = true,
        focus_on_activate = true,
        font_family = "Ubuntu",
        disable_splash_rendering = true,
        force_default_wallpaper = -1,
        disable_hyprland_logo = true,
    },
    general = {
        layout = qs.layout,
        gaps_in = qs.gaps_in,
        gaps_out = qs.gaps_out,
        border_size = qs.border_size,
        gaps_workspaces = 75,
        resize_on_border = true,
        extend_border_grab_area = 15,
        hover_icon_on_border = true,
        col = {
            active_border = { colors = { colors.accent1, colors.accent2 }, angle = 90 },
            inactive_border = colors.gray,
        },
        snap = {
            enabled = true,
            monitor_gap = 20,
            window_gap = 20,
        },
    },
    group = {
        col = {
            border_active = colors.accent2,
            border_locked_active = colors.maroon,
        },
        groupbar = {
            enabled = true,
            height = 15,
            font_size = 15,
            gradients = true,
            col = {
                active = colors.accent2,
                inactive = colors.gray,
            },
            text_color = colors.background,
        },
    },
    decoration = {
        rounding = qs.rounding,
        rounding_power = 2,
        active_opacity = 1.0,
        inactive_opacity = 0.95,
        dim_around = 0.5,
        dim_special = 0.5,
        shadow = {
            enabled = true,
            render_power = 2,
            range = 15,
            offset = { 5, 5 },
            scale = 0.99,
            color = colors.background,
        },
        blur = {
            enabled = true,
            size = 5,
            passes = 1,
            new_optimizations = true,
            xray = true,
        },
    },
    animations = {
        enabled = true,
    },
    gestures = {
        workspace_swipe_forever = true,
        workspace_swipe_create_new = true,
        workspace_swipe_use_r = false,
    },
    binds = {
        allow_workspace_cycles = true,
        workspace_back_and_forth = true,
    },
    debug = {
        vfr = true,
        error_position = 1,
        disable_logs = false,
        enable_stdout_logs = false,
    },
    xwayland = {
        force_zero_scaling = true,
    },
})


-- -----------------------
-- CURVES & ANIMATIONS
-- -----------------------
-- Define custom bezier
hl.curve("myBezier", { type = "bezier", points = { { 0.05, 0.9 }, { 0.1, 1.05 } } })

hl.animation({ leaf = "windows", enabled = true, speed = qs.animation_fast_speed, bezier = "myBezier" })
hl.animation({ leaf = "windowsOut", enabled = true, speed = qs.animation_fast_speed, bezier = "default" })
hl.animation({ leaf = "windowsIn", enabled = true, speed = qs.animation_fast_speed, bezier = "default", style = "popin 70%" })
hl.animation({ leaf = "border", enabled = true, speed = qs.animation_fast_speed, bezier = "default" })
hl.animation({ leaf = "borderangle", enabled = true, speed = qs.animation_fast_speed, bezier = "default" })
hl.animation({ leaf = "fade", enabled = true, speed = qs.animation_fast_speed, bezier = "default" })
hl.animation({
    leaf = "workspaces",
    enabled = true,
    speed = qs.animation_fast_speed,
    bezier = "default",
    style =
    "slidefadevert 10%"
})
hl.animation({
    leaf = "specialWorkspace",
    enabled = true,
    speed = qs.animation_fast_speed,
    bezier = "default",
    style =
    "slidefadevert -50%"
})
hl.animation({ leaf = "layersIn", enabled = true, speed = qs.animation_fast_speed, bezier = "default", style = "slide top" })
hl.animation({ leaf = "layersOut", enabled = true, speed = qs.animation_slow_speed, bezier = "default", style = "slide top" })

-- -----------------------
-- WORKSPACE RULES
-- -----------------------
-- Standard workspaces
hl.workspace_rule({ workspace = "1", persistent = false, default = true })
hl.workspace_rule({ workspace = "2", persistent = false })
hl.workspace_rule({ workspace = "3", persistent = false })
hl.workspace_rule({ workspace = "4", persistent = false })
hl.workspace_rule({ workspace = "5", persistent = false })
hl.workspace_rule({ workspace = "6", persistent = false })
hl.workspace_rule({ workspace = "7", persistent = false })
hl.workspace_rule({ workspace = "8", persistent = false })
hl.workspace_rule({ workspace = "9", persistent = false })
hl.workspace_rule({ workspace = "10", persistent = false })

-- Special workspaces
hl.workspace_rule({ workspace = "special:sysmonitor", on_created_empty = "alacritty -e btop", gaps_out = 60 })
hl.workspace_rule({ workspace = "special:calculator", on_created_empty = "kcalc", gaps_out = 120 })
hl.workspace_rule({ workspace = "special:hidden", gaps_out = 120 })

-- Workspace styling
hl.window_rule({ name = "border_float1", match = { float = true }, border_color = colors.mauve })
hl.workspace_rule({ workspace = "w[vt1]s[false]", border_size = 0, no_rounding = true }) --no borders on workspaces with only one visible (v) tiled (t) window (ignore special workspaces)
hl.workspace_rule({ workspace = "f[1]s[false]", gaps_out = 0, gaps_in = 0, border_size = 0, no_rounding = true }) --no gaps for workspaces with maximised windows

-- Class based workspaces
hl.window_rule({ name = "ws_firefox", match = { class = "firefox" }, workspace = "3" })
hl.window_rule({ name = "ws_code", match = { class = "code" }, workspace = "4" })
hl.window_rule({ name = "ws_zotero", match = { class = "Zotero" }, workspace = "5" })
hl.window_rule({ name = "ws_obsidian", match = { class = "obsidian" }, workspace = "6" })
hl.window_rule({ name = "ws_ferdium", match = { class = "ferdium" }, workspace = "7" })
hl.window_rule({ name = "ws_steam", match = { class = "steam" }, workspace = "8" })
hl.window_rule({ name = "ws_heroic", match = { class = "heroic" }, workspace = "8" })
hl.window_rule({ name = "ws_spotify", match = { class = "Spotify" }, workspace = "9" })
hl.window_rule({ name = "ws_elisa", match = { class = "org.kde.elisa" }, workspace = "9" })
hl.window_rule({ name = "ws_lumo", match = { class = "WebApp-Lumo3764" }, workspace = "10" })

-- Title based rules
hl.window_rule({ name = "progress_float", match = { title = "^Progress" }, float = true })
hl.window_rule({ name = "progress_no_focus", match = { title = "^Progress" }, no_initial_focus = true })
hl.window_rule({ name = "zotero_settings", match = { title = "(.*)(Zotero Settings)" }, float = true })
hl.window_rule({ name = "zotero_rounding", match = { class = "^Zotero" }, rounding = 13 })
hl.window_rule({ name = "copyq_float", match = { title = "(.*)(CopyQ)" }, float = true })
hl.window_rule({ name = "copyq_size", match = { title = "(.*)(CopyQ)" }, size = {"(monitor_w*0.5)", "(monitor_h*0.5)"} })

-- Zoom popup fix
hl.window_rule({ name = "zoom_focus", match = { title = "^menu window", class = "^Zoom Workplace" }, stay_focused = true })

-- VirtualBox rules
hl.window_rule({ name = "vb_opaque", match = { title = "(.*)(Oracle VirtualBox)(.*)" }, opaque = true })
hl.window_rule({ name = "vb_shadow", match = { title = "(.*)(Oracle VirtualBox)(.*)" }, no_shadow = true })
hl.window_rule({ name = "vb_rounding", match = { title = "(.*)(Oracle VirtualBox)(.*)" }, rounding = 0 })

-- SourceGit rules
hl.window_rule({ name = "sg_opaque", match = { class = "(.*)(SourceGit)(.*)" }, opaque = true })
hl.window_rule({ name = "sg_shadow", match = { class = "(.*)(SourceGit)(.*)" }, no_shadow = true })
hl.window_rule({ name = "sg_blur", match = { class = "(.*)(SourceGit)(.*)" }, no_blur = true })

-- File pickers
hl.window_rule({ name = "save_float", match = { title = "^Save(.*)$" }, float = true })
hl.window_rule({ name = "save_size", match = { title = "(Save)(.*)" }, size = {"(monitor_w*0.5)", "(monitor_h*0.7)"} })
hl.window_rule({ name = "open_float", match = { title = "^Open(.*)$" }, float = true })
hl.window_rule({ name = "open_size", match = { title = "(Open)(.*)" }, size = {"(monitor_w*0.5)", "(monitor_h*0.7)"} })

-- -----------------------
-- LAYER RULES
-- -----------------------
hl.layer_rule({ name = "rofi_dim", match = { namespace = "rofi" }, dim_around = true })
hl.layer_rule({ name = "waybar_blur", match = { namespace = "waybar" }, blur = true })
hl.layer_rule({ name = "selection_no_anim", match = { namespace = "selection" }, no_anim = true })

