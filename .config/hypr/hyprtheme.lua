--theme  = os.getenv("HYPR_THEME")
--source = $XDG_CONFIG_HOME/hypr/$theme
local qs = require("quicksettings")

local theme_file = require("colors")
local c = theme_file[qs.theme]

local colors = {
    text       = c.text,
    background = c.mantle,
    accent1    = c.pink,
    accent2    = c.pink,
    grey       = c.surface2,
    gray       = c.surface2,
}
return colors
