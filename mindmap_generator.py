
import os

def create_markdown_file(filename):
    with open(filename, 'w') as file:
        file.write('---\n')

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(f'[[{content}]]\n')

def remove_markdown_files(filenames):
    for filename in filenames:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

def main():
    try:
        root_node = input("Enter Root Node: ")
        root_filename = f'{root_node}.md'
        create_markdown_file(root_filename)

        first_level_dependencies = input("Enter First Level Dependencies (separate with commas): ").split(',')
        for dependency in first_level_dependencies:
            append_to_file(root_filename, dependency.strip())

        # Prompt to continue with first level dependencies
        continue_first_level = input("Do you want to continue with first level dependencies? (Y/N): ").lower()
        if continue_first_level != 'y':
            print("Exiting.")
            return

        try:
            second_level_dependencies = []
            for node in first_level_dependencies:
                node_filename = f'{node.strip()}.md'
                create_markdown_file(node_filename)

                second_level_nodes = input(f"Enter Dependencies for {node.strip()} (separate with commas): ").split(',')
                for second_node in second_level_nodes:
                    append_to_file(node_filename, second_node.strip())
                    second_level_dependencies.append(second_node.strip())

            continue_second_level = input("Do you want to continue with second level dependencies? (Y/N): ").lower()
            while continue_second_level == 'y':
                new_second_level_dependencies = []
                for node in second_level_dependencies:
                    add_node = input(f"Do you want to add nodes for {node.strip()}? (Y/N): ").lower()
                    if add_node == 'y':
                        node_filename = f'{node.strip()}.md'
                        new_second_nodes = input(f"Enter Dependencies for {node.strip()} (separate with commas): ").split(',')
                        for new_second_node in new_second_nodes:
                            append_to_file(node_filename, new_second_node.strip())
                            new_second_level_dependencies.append(new_second_node.strip())

                second_level_dependencies = new_second_level_dependencies
                continue_second_level = input("Do you want to continue with second level dependencies? (Y/N): ").lower()

        except KeyboardInterrupt:
            print("\nTerminated by user. Cleaning up and exiting.")
            return

    except KeyboardInterrupt:
        print("\nTerminated by user. Cleaning up and exiting.")
        return

    print("Exiting.")

if __name__ == "__main__":
    main()
