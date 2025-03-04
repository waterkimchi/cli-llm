RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN = "\033[0;36m"
RESET = "\033[0m"


class Utilities:
    def __init__(self):
        pass

    def print_menu(self, name, version):
        print(f"\n{RED}   ________    ____            __    __    __  ___{RESET}")
        print(f"{YELLOW}  / ____/ /   /  _/           / /   / /   /  |/  /{RESET}")
        print(f"{GREEN} / /   / /    / /   ______   / /   / /   / /|_/ /{RESET}")
        print(f"{BLUE}/ /___/ /____/ /   /_____/  / /___/ /___/ /  / /{RESET}")
        print(f"{MAGENTA}\\____/_____/___/           /_____/_____/_/  /_/{RESET}")
        print()
        print(
            f"{BLUE}To keep up with the latest news and updates, visit: github.com/waterkimchi/cli-llm"
        )
        print(f"Version: {name} v{version}")
        print(f"Maintainer: Hyunsu Lim{RESET}\n")
