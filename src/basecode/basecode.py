from src import core
import sys
def main():
    argv = sys.argv
    if len(argv) < 2:
        print("""Usage: basecode <encode><decode> <text> [format]
        Formats:
            utf-8        UTF-8
            ansi         ANSI
            gb           GB2312
            
        
        """)

main()
