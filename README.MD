# Obsidian Mindmap Generator
---

This is a tool for generating mindmaps within obsidian. In order to use this you will want to follow these preliminary steps first.

* Create a new Obsidian vault
	* This is for the safety of your other .md files within the directory you will place this script.
	* It becomes harder to visualize your mindmaps with larger vaults so small vault sizes will be the most optimal
	* In the future support will be added for automating the creation of vaults with preconfigured plugins

- Place mindmap_generator.py in your obsidian vault directory
```bash
mv mindmap_generator.py /home/User/Documents/yourvault/
```
- Configure your Obsidian Graph View Force Filters so that the mindmap is discernible
	- Set Center Force, Repel Force, and Link Force to 1.0
	- Set Link Distance between 70-80

#![Obsidian Force Filters](https://imgur.com/yHDrUqM.png) | ![Example Video](<blockquote class="imgur-embed-pub" lang="en" data-id="a/Tae4rbo" data-context="false" ><a href="//imgur.com/a/Tae4rbo"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>)

<p align="center">
  <img src="https://imgur.com/yHDrUqM.png" width="400" alt="Obsidian Force Filters">
  <img src="https://imgur.com/a/Tae4rbo" width="400" alt="Example Video">
</p>
## What this program does
---

This program creates markdown files in a tree hierarchy fashion. You first will enter the root node for the tree and the program will prompt you to enter first level dependencies afterwards.

After your first level dependencies have been defined the program will ask whether you would like to continue creating dependencies or not.

If you wish to continue defining dependencies for the tree press Y. It will cycle through the list of dependencies you made and ask which new dependencies you would like to create.

If you dont want to create a dependency for a node simply press enter when prompted for the node.

### Early exit
---

This program adds support for removing markdown files when you misinput nodes. If you mess up at any point in your generation of the tree press CTRL+C, or your defined KeyboardInterrupt key.

Python will handle the thrown exception and remove all markdown files created so far.
