from src import core
import sys

# Can we just simply use the functions that I wrote in core.py?
# I have no better idea with it.
# So I just use the functions that I wrote in core.py.
# And I'm lazy :)
def main():
    argv = sys.argv
    if len(argv) < 2 or argv[1] == "--help" or argv[1] == "-h":
        print("""Usage: basecode <encode><decode> <options> <text> [format]
        Formats:
            utf-8                     UTF-8
            utf-16                    UTF-16
            ansi                      ANSI
            gb                        GB2312
        
        Options:
            -t TEXT, --text=TEXT      Encode or decode with the text TEXT.
            -f FILE, --file=FILE      Encode or decode with the file FILE.
            -o FILE, --output=FILE    Output the result to the file FILE.
            
        
                                            THIS PROGRAM HAS SUPER COW POWER!
        """)
# I don't want to do the fucking if __name == "__main__" okay?
main()
