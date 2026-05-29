from core.banner import show_banner
from cli.menu import show_menu

from social.telegram.tools import (
    username_checker,
    link_analyzer,
    qr_generator
)

from social.instagram.tools import (
    instagram_analyzer
)

from ai.tools import (
    caption_generator,
    password_generator
)

from network.tools import (
    ip_lookup
)

from github_tools.tools import (
    json_formatter,
    github_repo_analyzer
)

show_banner()
show_menu()

choice = input("\nSelect option: ")

if choice == "1":
    username_checker()

elif choice == "2":
    link_analyzer()

elif choice == "3":
    qr_generator()

elif choice == "4":
    instagram_analyzer()

elif choice == "5":
    caption_generator()

elif choice == "6":
    ip_lookup()

elif choice == "7":
    password_generator()

elif choice == "8":
    json_formatter()

elif choice == "9":
    github_repo_analyzer()

elif choice == "0":
    print("\nGoodbye!")

else:
    print("\nInvalid option.")
