# Diagrams XBlock
XBlock for generating diagrams from text. The text is simple markdown-like script language. 
This is a simple wrapper around mermaid (https://github.com/knsv/mermaid)



# Installation
Install the requirements into the python virtual environment of your `edx-platform` installation.

```bash
$ pip install -r requirements.txt
```

Enabling in Studio
------------------

You can enable the Diagrams XBlock in studio through the
advanced settings.

1. From the main page of a specific course, navigate to `Settings ->
   Advanced Settings` from the top menu.
2. Check for the `advanced_modules` policy key, and add
   `"diagrams-xblock"` to the policy value list.
3. Click the "Save changes" button.

Usage
-----

When you add the `Diagrams XBlock` component to a course in the studio,
the block is field with default content, shown in the screenshot below.
