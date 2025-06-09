from abc import ABC, abstractmethod
from datetime import datetime
import json

class FileSystemComponent(ABC):
    def __init__(self, name, permissions="rw-r--r--", modified_date=None):
        self.name = name
        self.permissions = permissions
        self.modified_date = modified_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def find_all(self, name_part: str):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    def matches_extension(self, ext: str) -> bool:
        return self.name.endswith(ext)


class File(FileSystemComponent):
    def __init__(self, name, size, permissions="rw-r--r--", modified_date=None):
        super().__init__(name, permissions, modified_date)
        self._size = size

    def get_size(self):
        return self._size

    def display(self, indent=0):
        print(" " * indent + f"📄 {self.name} ({self._size} KB) [{self.permissions}, {self.modified_date}]")

    def find_all(self, name_part: str):
        return [self] if name_part in self.name else []

    def to_dict(self):
        return {
            "type": "file",
            "name": self.name,
            "size": self._size,
            "permissions": self.permissions,
            "modified_date": self.modified_date
        }


class Folder(FileSystemComponent):
    def __init__(self, name, permissions="rwxr-xr-x", modified_date=None):
        super().__init__(name, permissions, modified_date)
        self._children = []

    def add(self, component: FileSystemComponent):
        self._children.append(component)

    def get_size(self):
        return sum(child.get_size() for child in self._children)

    def display(self, indent=0, filter_ext=None):
        printed = False
        for child in self._children:
            if isinstance(child, Folder):
                child.display(indent + 2, filter_ext)
            elif not filter_ext or child.matches_extension(filter_ext):
                if not printed:
                    print(" " * indent + f"📁 {self.name}/ [{self.permissions}, {self.modified_date}]")
                    printed = True
                child.display(indent + 2)

    def find_all(self, name_part: str):
        matches = []
        if name_part in self.name:
            matches.append(self)
        for child in self._children:
            matches.extend(child.find_all(name_part))
        return matches

    def to_dict(self):
        return {
            "type": "folder",
            "name": self.name,
            "permissions": self.permissions,
            "modified_date": self.modified_date,
            "children": [child.to_dict() for child in self._children]
        }


def export_to_json(component, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(component.to_dict(), f, indent=2)
    print(f"✅ Exported structure to {filename}")


def export_to_txt(component, filename):
    with open(filename, "w", encoding="utf-8") as f:
        def recurse(comp, indent=0):
            if isinstance(comp, File):
                line = " " * indent + f"📄 {comp.name} ({comp.get_size()} KB) [{comp.permissions}, {comp.modified_date}]\n"
            else:
                line = " " * indent + f"📁 {comp.name}/ [{comp.permissions}, {comp.modified_date}]\n"
            f.write(line)
            if isinstance(comp, Folder):
                for child in comp._children:
                    recurse(child, indent + 2)
        recurse(component)
    print(f"✅ Exported structure to {filename}")


def show_menu():
    print("\n📂 File System CLI")
    print("1. Display structure")
    print("2. Display only files with extension")
    print("3. Search for a file/folder by name")
    print("4. Export to JSON")
    print("5. Export to TXT")
    print("0. Exit")


def main():
    # === Create Example Structure ===
    root = Folder("root")
    root.add(File("README.md", 5))
    root.add(File("setup.py", 2))

    src = Folder("src")
    src.add(File("main.py", 15))
    src.add(File("main.txt", 10))
    src.add(File("utils.py", 7))

    assets = Folder("assets")
    assets.add(File("logo.png", 150))
    assets.add(File("bg.jpg", 300))

    root.add(src)
    root.add(assets)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n📂 Full Structure:")
            root.display()

        elif choice == "2":
            ext = input("Enter file extension (e.g., .py): ").strip()
            print(f"\n📁 Files with extension '{ext}':")
            root.display(filter_ext=ext)

        elif choice == "3":
            target = input("Enter part of filename to search (e.g., 'main'): ").strip()
            matches = root.find_all(target)
            if matches:
                print(f"\n✅ Found {len(matches)} matches:")
                for match in matches:
                    match.display()
            else:
                print(f"\n❌ No matches found for '{target}'.")

        elif choice == "4":
            filename = input("Enter filename to export to (.json): ").strip()
            export_to_json(root, filename)

        elif choice == "5":
            filename = input("Enter filename to export to (.txt): ").strip()
            export_to_txt(root, filename)

        elif choice == "0":
            print("👋 Exiting...")
            break

        else:
            print("❗ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
