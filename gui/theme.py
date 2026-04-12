# Theme selectectionnnn
# "samsung dark mode (dark)" | "apna wala basic(void)" | "dune"

ACTIVE_THEME = "dune"

F_HEAD    = ("DM Sans",  18, "bold")
F_SUB     = ("DM Sans",  11)
F_LABEL   = ("DM Sans",  12, "bold")
F_BODY    = ("DM Sans",  12)
F_MONO    = ("DM Mono",  12, "bold")
F_MONO_S  = ("DM Mono",  11)
F_TAG     = ("DM Mono",  10)
F_BTN     = ("DM Sans",  11, "bold")
F_ATLF    = ("Bungee"  , 14)

if ACTIVE_THEME == "dark":
    C_PAGE       = "#000000"
    C_CARD       = "#0D0D0D"
    C_CARD2      = "#141414"
    C_BORDER     = "#1F1F1F"
    C_BORDER2    = "#2A2A2A"
    C_TEXT       = "#F0F0F0"
    C_TEXT2      = "#C0C0C0"
    C_MUTED      = "#3A3A3A"
    C_VIOLET     = "#4F8EF7"
    C_VIOLET_DIM = "#0D1A3A"
    C_VIOLET_BRD = "#0F2040"
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
    C_PAGE       = "#080808"
    C_CARD       = "#101010"
    C_CARD2      = "#181818"
    C_BORDER     = "#222222"
    C_BORDER2    = "#2E2E2E"
    C_TEXT       = "#EFEFEF"
    C_TEXT2      = "#BBBBBB"
    C_MUTED      = "#383838"
    C_VIOLET     = "#7B68EE"
    C_VIOLET_DIM = "#1A1640"
    C_VIOLET_BRD = "#201C50"
    C_RED        = "#FF4444"
    C_ROSE       = "#FF6B8A"
    C_ROSE_HOV   = "#3A1020"
    C_ROSE_DIM   = "#220A14"
    C_ROSE_BRD   = "#4A1525"
    C_TEAL       = "#00CFA1"
    C_TEAL_HOV   = "#003D30"
    C_TEAL_DIM   = "#00261E"
    C_TEAL_BRD   = "#004D3C"

elif ACTIVE_THEME == "dune":
    C_PAGE       = "#0A0A0A"
    C_CARD       = "#111111"
    C_CARD2      = "#1A1A1A"
    C_BORDER     = "#242424"
    C_BORDER2    = "#2E2E2E"
    C_TEXT       = "#F5F0E8"
    C_TEXT2      = "#C8BFA8"
    C_MUTED      = "#3D3D3D"
    C_VIOLET     = "#E8A020"
    C_VIOLET_DIM = "#2E1E05"
    C_VIOLET_BRD = "#3A2808"
    C_RED        = "#CC2222"
    C_ROSE       = "#E05555"
    C_ROSE_HOV   = "#380E0E"
    C_ROSE_DIM   = "#200808"
    C_ROSE_BRD   = "#481212"
    C_TEAL       = "#50C8A0"
    C_TEAL_HOV   = "#0D3828"
    C_TEAL_DIM   = "#082218"
    C_TEAL_BRD   = "#104030"

else:
    # raise valueerror idk the syntax
    print("just pylance error hataya ")
