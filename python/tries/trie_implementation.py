from rich.console import Console
from rich.table import Table
from rich.text import Text
from keyboard import read_event


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _collect(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)
        for ch, next_node in node.children.items():
            self._collect(next_node, prefix + ch, results)

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._collect(node, prefix, results)
        return results


console = Console()


def display_suggestions(prefix, suggestions):
    console.clear()

    console.print(f"Type letters (Press ESC to exit)\n", style="italic dim")

    console.print(f"You typed: [bold yellow]{prefix}[/bold yellow]\n")

    if suggestions:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Suggestions", justify="left", style="cyan")
        for s in suggestions[:5]:
            highlighted = Text()
            highlighted.append(prefix, style="bold green")
            highlighted.append(s[len(prefix):], style="white")
            table.add_row(highlighted)
        console.print(table)
    else:
        console.print("[red]No suggestions found[/red]")


def run_autocomplete(trie):
    prefix = ""
    display_suggestions(prefix, [])
    title = Text("Command-line Autocomplete System", style="bold cyan")
    console.print(title)

    while True:
        event = read_event(suppress=True)
        if event.event_type == "down":
            key = event.name

            if key == "esc":
                console.print("\n [bold cyan]Goodbye![/bold cyan]")
                break
            elif key == "backspace":
                prefix = prefix[:-1]
            elif len(key) == 1 and key.isprintable():
                prefix += key

            suggestions = trie.autocomplete(prefix)
            display_suggestions(prefix, suggestions)


if __name__ == "__main__":
    trie = Trie()
    words = [
        "bat", "bad", "ball", "bark",
        "cat", "can", "cap", "call",
        "dog", "doll", "door", "doom",
        "elephant", "ear", "earth", "eat"
    ]
    for w in words:
        trie.insert(w)

    run_autocomplete(trie)
