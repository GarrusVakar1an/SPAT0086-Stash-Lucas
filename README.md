This REPOSITORY contains the material for the project associated to the lecture SPAT0086 

**Practical Guidelines for the project:**

- Commit your work regularly, ideally every time you complete a small step. It is fine to commit non‑working code. If you later remove or rewrite major parts, reference the earlier commit (date or SHA) for traceability.

- Do not commit large catalogues (>50 MB). Store them externally (e.g., OneDrive) and share links. To avoid commiting large files by mistake, you can add those into a ".gitignore" file. 

- Document your methodology briefly in your notebook(s): what you tried, why, and what you changed along the way.

- Use of LLMs is allowed, but you must **fully understand and be able to explain all code and methods**. You must disclose LLM use when:
  * A block of code was drafted with an LLM and you did not already know how to write it.
  * You used methods, modules, or approaches that were unfamiliar to you when you started.


**Evaluation criteria / How you will be Graded:**

* **Methodology (clarity of objectives and approach)**: Explain what you aimed to do and why.

* **Connection with course content**: Refer to lectures/notebooks when justifying method choices.

* **Git history (regularity and clarity)**: Commit regularly. Late, bulk commits will be penalized.

* **Results and discussion**: Discuss your results, including unsuccessful attempts and insights gained.

* **Use of LLMs**: LLMs may support your work but cannot replace your understanding. You must explain your code and disclose LLM contributions.


**Possible structure of you repository for the project**

project-root/
├─ README.md
├─ requirements.txt          # This file should list the versions of the modules that you have been using.
├─ .gitignore
├─ Assignement1		     # Directory containing the first assignement
├─ Assignement2		     # Directory containing the second assignement
├─ data/
│  ├─ README.md              # data filenames (if you rename or create small tables)
│  └─ sample/                # tiny samples for quick tests 
├─ src/
│  └─ utils.py		     # if you write some specific functions used in several Notebook
├─ notebooks/		     # The examples below are only a suggestion of Nb names ! 
│  ├─ 01_exploration.ipynb 
│  └─ 02_modeling.ipynb
├─ results/		     # Optional directory to save specific results or figures 
   └─ figures/ 
