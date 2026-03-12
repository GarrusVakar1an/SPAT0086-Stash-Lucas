[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8jmRRK3S)
This REPOSITORY contains the material for the project associated to the lecture SPAT0086 

**Practical Guidelines for Your Project:**

- Make sure to commit your work often, ideally every time you complete a small step. It is fine to commit non‑working code. If you later remove or rewrite major parts, reference the earlier commit (date or SHA) for traceability. And do not forget to push it regularly so that it gets registered on the Github server where we can fetch it.

- Please do not commit large catalogues (>50 MB). Store them externally (e.g., OneDrive) and share links. To avoid committing large files by mistake, you can list their names in a `.gitignore` file (yes, that file name must start with a dot, and make sure to add and commit that file as well). 

- Document your methodology briefly in your notebook(s): What did you try? Why? What did you change along the way?

- Use of _Large Language Models_ (LLMs, aka AI) is allowed. However you must **fully understand and be able to explain all code and methods** that you submit. You must disclose LLM use whenever:
  * A block of code was drafted with an LLM and you did not know how to write it from the beginning;
  * You used methods, modules, or approaches that you were unfamiliar with when you started.


**Evaluation criteria / How will your Work be Graded:**

* **Methodology (clarity of objectives and approach)**: Explain what you aimed to do and why.

* **Connection with course content**: Refer to lectures/notebooks when justifying method choices.

* **Git history (regularity and clarity)**: commit often. Late, bulk commits will be penalized.

* **Results and discussion**: Discuss your results, including unsuccessful attempts and insights gained.

* **Use of LLMs**: you are allowed to call upon LLMs to support your work but they cannot replace your understanding. LLM contributions have to be disclosed and you must be able explain your code.


**Possible structure of your repository for the project**

```
project-root/
├─ README.md
├─ requirements.txt          # This file should list the versions of the modules that you have been using.
├─ .gitignore
├─ data/
│  ├─ README.md              # data filenames (if you rename or create small tables)
│  └─ sample/                # tiny samples for quick tests
├─ src/
│  └─ utils.py               # if you write some specific functions used in several Notebooks
├─ notebooks/                # The examples below are only suggestions of Nb names! 
│  ├─ 01_exploration.ipynb
│  └─ 02_modeling.ipynb
├─ results/                  # Optional directory to save specific results or figures 
   └─ figures/ 
```

If you use a virtual environment for your project (strongly recommended), and you use the conda package manager, the `requirements.txt` file can be created by issuing `conda list --export > requirements.txt` on the command line while in `project-root` (or however you named it). Please ask for help if you are using pip instead of conda.

In case of doubt or trouble with git, please do not hesitate to reach out to any of us for help.
