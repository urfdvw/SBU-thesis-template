# Stony Brook University Ph.D. Thesis LaTeX Template

## Motivation 

I am shocked by the [lack of proper LaTeX templates](https://grad.stonybrook.edu/_data/documents/forms/2020-forms/Dissertation_template-PHD_EW.pdf) for the Ph.D. thesis at Stony Brook graduate school page. 

This template is modified from [the thesis of Avi Srivastava](https://github.com/k3yavi/thesis). Thank him.

## How to use

### Get started
1. Download this repository from GitHub website as a `.zip` file.
2. Go to [Overleaf website](https://www.overleaf.com/) and log in.
3. When clicking on `New Project` button, choose `Upload Project`.
4. Upload the downloaded `.zip` file
5. (optional but suggested) Connect this Overleaf document to a new Github repository. See [This page](https://www.overleaf.com/learn/how-to/How_do_I_connect_an_Overleaf_project_with_a_repo_on_GitHub,_GitLab_or_BitBucket%3F)

### Start to write
- The `main.tex` file
    - (*The line numbers mentioned here are line numbers in the template. They might change once you fill in your content.*)
    - Head directly to line 80 and fill in `THESIS INFORMATION`
    - In `TITLE PAGE`, you might only want to change line 138, the date.
    - `THESIS CONTENT - CHAPTERS` at line 280 is the main body
        - NEVER write any content here
        - Write your main body in separated `.tex` files and `\input` them here.
    - Appendixes should be `\input`ed in `THESIS CONTENT - APPENDICES` at line 297
    - If you need any extra packages, `\usepackage` them in `Your Packages` at line 55
    - For any other parts of the `main.tex` file, you need to modify them at your own risk.
- The `Chapters` folder
    - All the text parts should be in this folder.
    - You can divide the text by `\chapter` or `\section`
        - The rule of thumb is a file should not exceed 500 lines. If so, break it
    - You can also create subfolders for each Chapter for a better organization.
- The `Figures` folder
    - All the Figure files should be in this folder.
    - If you have figures created by LaTex code (Highly not suggested), put them here as separated `.tex` files.
- The `Tables` folder
    - If you have tables, put them here as separated `.tex` files.
    - If you generated your tables from [tablesgenerator.com](https://www.tablesgenerator.com/) (Highly suggested), put the source file of the table here as well.
- The `Appendices` folder
    - If you have appendices, put them here as separated `.tex` files.


## Warnings and Tricks (From the most important to the least)
- **The ONLY reason that you want to use LaTeX, is that there are off-the-shelf templates available such as a conference paper template from the conference website and this thesis template. NEVER, EVER, EVER, start a LaTeX document from scratch!**
- It is highly recommended that any LaTeX users head to [Overleaf](https://www.overleaf.com/). Avoid using any offline distributions anytime possible.
- Never define your own command if you don't want to confuse your co-author or yourself years later.
- Use `\begin{align}` instead of `\begin{equation}`. They are basically the same, but `align` will allow you to add additional lines of existing equations whenever needed with ease.
- When editing equations, put them into multiple lines, with indention.
    - The rule of thumb is to never let the equation auto wrapped to a new line
    - Indention rules are flexible since indention is for easier reading, not a part of the syntax.
        - It is suggested to follow the indention rule of programming languages, such as the `{}` rules of C++.
- Generate the tables from [tablesgenerator.com](https://www.tablesgenerator.com/)
