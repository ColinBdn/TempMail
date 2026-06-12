class Colors:
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright text colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Bright background colors
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    
    # Additional colors
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;200m'
    VIOLET = '\033[38;5;129m'
    LIGHT_GREEN = '\033[38;5;120m'
    LIGHT_BLUE = '\033[38;5;123m'
    LIGHT_CYAN = '\033[38;5;152m'
    LIGHT_MAGENTA = '\033[38;5;207m'
    GOLD = '\033[38;5;220m'
    SILVER = '\033[38;5;7m'
    TEAL = '\033[38;5;86m'
    GREY = '\033[38;5;242m'
    
    # Text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'
    RESET = '\033[0m'

def cPrint(*args, color=None, **kwargs):
    if color:
        print(color, end="")
    print(*args, **kwargs)
    if color:
        print(Colors.RESET, end="")



def test_print_all():
    cPrint("BLACK           test ==== //// ---- AAAAA", color=Colors.BLACK          )
    cPrint("RED             test ==== //// ---- AAAAA", color=Colors.RED            )
    cPrint("GREEN           test ==== //// ---- AAAAA", color=Colors.GREEN          )
    cPrint("YELLOW          test ==== //// ---- AAAAA", color=Colors.YELLOW         )
    cPrint("BLUE            test ==== //// ---- AAAAA", color=Colors.BLUE           )
    cPrint("MAGENTA         test ==== //// ---- AAAAA", color=Colors.MAGENTA        )
    cPrint("CYAN            test ==== //// ---- AAAAA", color=Colors.CYAN           )
    cPrint("WHITE           test ==== //// ---- AAAAA", color=Colors.WHITE          )
    cPrint("BRIGHT_BLACK    test ==== //// ---- AAAAA", color=Colors.BRIGHT_BLACK   )
    cPrint("BRIGHT_RED      test ==== //// ---- AAAAA", color=Colors.BRIGHT_RED     )
    cPrint("BRIGHT_GREEN    test ==== //// ---- AAAAA", color=Colors.BRIGHT_GREEN   )
    cPrint("BRIGHT_YELLOW   test ==== //// ---- AAAAA", color=Colors.BRIGHT_YELLOW  )
    cPrint("BRIGHT_BLUE     test ==== //// ---- AAAAA", color=Colors.BRIGHT_BLUE    )
    cPrint("BRIGHT_MAGENTA  test ==== //// ---- AAAAA", color=Colors.BRIGHT_MAGENTA )
    cPrint("BRIGHT_CYAN     test ==== //// ---- AAAAA", color=Colors.BRIGHT_CYAN    )
    cPrint("BRIGHT_WHITE    test ==== //// ---- AAAAA", color=Colors.BRIGHT_WHITE   )
    cPrint("ORANGE          test ==== //// ---- AAAAA", color=Colors.ORANGE         )
    cPrint("PINK            test ==== //// ---- AAAAA", color=Colors.PINK           )
    cPrint("VIOLET          test ==== //// ---- AAAAA", color=Colors.VIOLET         )
    cPrint("LIGHT_GREEN     test ==== //// ---- AAAAA", color=Colors.LIGHT_GREEN    )
    cPrint("LIGHT_BLUE      test ==== //// ---- AAAAA", color=Colors.LIGHT_BLUE     )
    cPrint("LIGHT_CYAN      test ==== //// ---- AAAAA", color=Colors.LIGHT_CYAN     )
    cPrint("LIGHT_MAGENTA   test ==== //// ---- AAAAA", color=Colors.LIGHT_MAGENTA  )
    cPrint("GOLD            test ==== //// ---- AAAAA", color=Colors.GOLD           )
    cPrint("SILVER          test ==== //// ---- AAAAA", color=Colors.SILVER         )
    cPrint("SILVER          test ==== //// ---- AAAAA", color=Colors.SILVER         )
    cPrint("GREY            test ==== //// ---- AAAAA", color=Colors.GREY           )