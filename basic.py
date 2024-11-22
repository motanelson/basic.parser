class TreeNode:
    def __init__(self, content=""):
        self.content = content.strip()
        self.children = []

    def __repr__(self, level=0):
        indent = " " * (level * 4)
        result = f"{indent}{self.content}\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        return result


def parse_basic_tree(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Palavras-chave importantes para construir a hierarquia
    keywords = {"sub", "function", "class", "for", "then", "while", "loop", "select"}
    end_keywords = {"end","next"}  # Marca o fim de uma seção
    stack = []
    root = TreeNode("root")
    current_node = root

    for line in lines:
        stripped_line = line.strip()
        tokens = stripped_line.split()

        if not tokens:
            continue  # Ignorar linhas vazias

        keyword = tokens[0].lower()

        if keyword in keywords:
            # Inicia um novo nível na hierarquia
            new_node = TreeNode(stripped_line)
            current_node.children.append(new_node)
            stack.append(current_node)
            current_node = new_node
        elif keyword in end_keywords:
            # Finaliza o nível atual e retorna ao nível superior
            if stack:
                current_node = stack.pop()
        else:
            # Adiciona uma linha como nó filho no nível atual
            current_node.children.append(TreeNode(stripped_line))

    return root


def main():
    file_name = input("Enter the name of the BASIC file to load: ")

    try:
        tree = parse_basic_tree(file_name)
        print("\nParsed BASIC Tree:")
        print(tree)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

