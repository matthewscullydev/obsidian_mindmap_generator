# Obsidian Mindmap Generator
---

This is a tool for generating mindmaps within obsidian. In order to use this you will want to follow these preliminary steps first.

* Create a new Obsidian vault
	* This is for the safety of your other .md files within the directory you will place this script.
	* It becomes harder to visualize your mindmaps with larger vaults so small vault sizes will be the most optimal

- Place mindmap_generator.py in your obsidian vault directory
```bash
mv mindmap_generator.py /home/User/Documents/yourvault/
```
- Configure your Obsidian Graph View Force Filters so that the mindmap is discernible
	- Set Center Force, Repel Force, and Link Force to 1.0
	- Set Link Distance to 30

![Example Video](https://github.com/matthewscullydev/obsidian_trainer/assets/26017402/ebb4d522-2f88-4a53-8afa-047ab2aa9a63)
# What this program does
---

This program creates markdown files in a tree hierarchy fashion. You first will enter the root node for the tree and the program will prompt you to enter first level dependencies afterwards.

After your first level dependencies have been defined the program will ask whether you would like to continue creating dependencies or not.

If you wish to continue defining dependencies for the tree press Y. It will cycle through the list of dependencies you made and ask which new dependencies you would like to create.

If you dont want to create a dependency for a node simply press enter when prompted for the node.

### Early exit
---

This program adds support for removing markdown files when you misinput nodes. If you mess up at any point in your generation of the tree press CTRL+C, or your defined KeyboardInterrupt key.

Python will handle the thrown exception and remove all markdown files created so far.
