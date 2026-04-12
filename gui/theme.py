# Theme selectectionnnn
# "samsung dark mode (dark)" | "apna wala basic(void)" | "dune"

ACTIVE_THEME = "void"

F_HEAD    = ("DM Sans",  18, "bold")
F_TITLE   = ("DM Sans",  18, "bold")
F_SUB     = ("DM Sans",  13)
F_LABEL   = ("DM Sans",  12, "bold")
F_BODY    = ("DM Sans",  12)
F_MONO    = ("DM Mono",  12, "bold")
F_MONO_S  = ("DM Mono",  11)
F_TAG     = ("DM Mono",  10)
F_BTN     = ("DM Sans",  11, "bold")
F_ATLF    = ("Bungee", 14)

if ACTIVE_THEME == "dark":
    C_PAGE       = "#000000"
    C_CARD       = "#0D0D0D"
    C_CARD2      = "#141414"
    C_BORDER     = "#1F1F1F"
    C_BORDER2    = "#2C2C2C"   # slightly more separation
    C_TEXT       = "#F0F0F0"
    C_TEXT2      = "#C0C0C0"
    C_MUTED      = "#2F3448"   # subtle blue tint (was flat gray)

    C_VIOLET     = "#4F8EF7"
    C_VIOLET_DIM = "#0A1430"   # deeper
    C_VIOLET_BRD = "#1A3A70"   # clearly visible border

    C_RED        = "#FF3333"
    C_ROSE       = "#F75F7A"
    C_ROSE_HOV   = "#3A0D14"
    C_ROSE_DIM   = "#220A0F"
    C_ROSE_BRD   = "#4A1020"

    C_TEAL       = "#3DD68C"
    C_TEAL_HOV   = "#0D3A22"
    C_TEAL_DIM   = "#082214"
    C_TEAL_BRD   = "#10402A"


elif ACTIVE_THEME == "void":
    C_PAGE       = "#0B0D17"
    C_CARD       = "#12152A"
    C_CARD2      = "#181B33"
    C_BORDER     = "#1E2240"
    C_BORDER2    = "#2D2660"
    C_TEXT       = "#E8EAFF"
    C_TEXT2      = "#C8CBF0"
    C_MUTED      = "#555A8A"

    C_VIOLET     = "#7C6FCD"
    C_VIOLET_DIM = "#1E1A3A"
    C_VIOLET_BRD = "#272248"

    C_RED        = "#E43434"
    C_ROSE       = "#E05C7B"
    C_ROSE_HOV   = "#3A1521"
    C_ROSE_DIM   = "#2A0F18"
    C_ROSE_BRD   = "#3D1525"

    C_TEAL       = "#2DD4A7"
    C_TEAL_HOV   = "#164A34"
    C_TEAL_DIM   = "#0D2A1E"
    C_TEAL_BRD   = "#183D2C"


elif ACTIVE_THEME == "dune":
    C_PAGE       = "#0A0A0A"
    C_CARD       = "#111111"
    C_CARD2      = "#1A1A1A"
    C_BORDER     = "#242424"
    C_BORDER2    = "#323232"   # more visible step
    C_TEXT       = "#F5F0E8"
    C_TEXT2      = "#C8BFA8"
    C_MUTED      = "#3D372F"   # warm tint instead of neutral gray

    C_VIOLET     = "#E8A020"
    C_VIOLET_DIM = "#241804"
    C_VIOLET_BRD = "#5A3A0C"   # stronger contrast

    C_RED        = "#AA1A1A"   # deeper, distinct from rose
    C_ROSE       = "#E05555"
    C_ROSE_HOV   = "#380E0E"
    C_ROSE_DIM   = "#200808"
    C_ROSE_BRD   = "#481212"

    C_TEAL       = "#50C8A0"
    C_TEAL_HOV   = "#0D3828"
    C_TEAL_DIM   = "#082218"
    C_TEAL_BRD   = "#104030"


else:
    raise ValueError(f"Unknown theme: {ACTIVE_THEME}")