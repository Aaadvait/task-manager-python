#Theme settings

theme = "dark"

color_base = "#000000"
color_hbase = "#000000"
color_hhbase = "#000000"

color_mainframe = "#000000"

color_3 = "#000000"
color_4 = "#000000"
color_5 = "#000000"
color_5a = "#000000"
color_5b = "#000000"
color_6 = "#000000"
color_6a = "#000000"
color_button = "#000000"
color_8 = "#000000"

if theme == "dark":
    color_base = "#16181c"  # main background (cool dark, less flat than pure gray)
    color_hbase = "#22262c"  # surface / cards / panels (slight elevation)
    color_hhbase = "#2e333a"  # higher elevation / borders / dividers (clear separation)

    color_mainframe = "#20212C"

    color_3 = "#c0c7d0"  # secondary text / muted labels (cool gray, readable)
    color_4 = "#f0f0fa"  # primary text (soft white, less harsh than pure white)

    color_5 = "#9b8cf0"  # purple accent (slightly refined, less pastel)
    color_5a = "#453d6f"
    color_5b = "#a598ef"
    
    color_6 = "#4a8fd6"  # blue accent (info / links)
    color_6a = "#3e77b0"

    color_button = "#0088bb"  # primary action (balanced, no neon effect)
    color_8 = "#c7374f"  # error / destructive actions
else:
    color_base = "#f4f6f9"  # main background (soft cool white, less sterile than pure white)
    color_hbase = "#e9edf3"  # surface / cards / panels (slight elevation)
    color_hhbase = "#dde3ea"  # higher elevation / borders / dividers (clear separation)

    color_3 = "#5b616b"  # secondary text / muted labels (cool gray, readable)
    color_4 = "#0f141a"  # primary text (near-black, easier on eyes than pure black)

    color_5 = "#5f52c9"  # purple accent (balanced for light bg)
    color_6 = "#2d6bb0"  # blue accent (links / info)
    color_6a = "#427aba"

    color_button = "#0088bb"  # primary action (consistent with dark theme tweak)
    color_8 = "#b4233f"  # error / destructive actions