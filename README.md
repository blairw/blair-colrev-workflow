# blair-colrev-workflow
Blair's personal workflow for CoLRev. Not authoritative on CoLRev. Your mileage may vary.

## What is this?

**CoLRev** (https://github.com/CoLRev-Environment/colrev) is an amazing tool, but still being rapidly developed and thus breaking changes may occur from time to time. There are also some features that I just cannot get working on my environment (could be because of my insistence on using Mac 😅).

This document outlines how I use a ~~hacky~~ **creatively appropriated** workflow around CoLRev on my Mac.

- macOS 14.4.1 23E224 arm64 (Mac14,15 Apple M2)
- Python 3.11.6
- CoLRev 0.11.0

(Unfortunately I could not get CoLRev 0.12.0 working on my setup: nothing was being imported into records.bib...)

## Assumptions

Much of the workflow below will still work if these assumptions are not met, but I'm just documenting what I've been using:

- `.bib` exports from Scopus (e.g., using https://www.litbaskets.io)
- MacOS with Python installed via https://brew.sh

## Part 1 - Getting CoLRev working


1. Go to `~/00blair/gitrepos-colrev` (or equivalent on your machine).

2. In this folder, I like to keep all the various venvs that I could be using with CoLRev. Here's an example of me making a new venv:

	```zsh
	python3.11 -m venv _venv_colrev_0_11_0
	source ./_venv_colrev_0_11_0/bin/activate
	python -m pip install --upgrade pip wheel
	python -m pip install --upgrade colrev==0.11.0
	```

	Immediately after successfully installing CoLRev into a new venv, it could be a good idea to `deactivate` and then ZIP the whole thing: e.g., _"_venv_colrev_0_11_0 (tested on Python 3.11 on macOS 14.4.1 23E224 arm64).zip"_. 📦
	
	**All subsequent steps need to be done with that venv activated.**

## Part 2 - Setting up the repo locally

3. `mkdir` a new folder for the project

4. Run `colrev init`

5. Modify `.gitignore` (e.g., for `.DS_Store`) and make a commit.

6. If the commit gets stuck on _"CoLRev ReviewManager: format............................"_ (or `check` or `report`), comment these out in `.pre-commit-config.yaml`. Then try the commit again.

7. Move the first of the `.bib` files to `data/search`. Then run `colrev retrieve`. WARNING: this step & the next step, collectively, could take quite some time!


8. Hit ENTER for each of these...

	```
	2024-04-11 14:42:17 [INFO] search [colrev.scopus > data/search/Q0070_Foucault.bib]
	DB search (update)
	- Go to https://www.scopus.com/search/form.uri?display=advanced and run the following query:
	
	
	
	- Replace search results in /Users/blair/00blair/gitrepos-colrev/test/data/search/Q0070_Foucault.bib
	Press enter to continue
	```

9. If you get this error — `Invalid language codes: undefined` — go and modify the bib files accordingly (i.e., in this case, search for `language = {undefined},` and replace it somehow). Then run `colrev retrieve` again.

10. If you had recieved messages like this, modify the files manually. Then run `colrev retrieve` again.

	```
	2024-04-11 15:13:05 [ERROR] De Moya2020940 not imported
	2024-04-11 15:13:05 [ERROR] Ochoa Pacheco2023 not imported
	2024-04-11 15:13:05 [ERROR] De Jong20051610 not imported
	2024-04-11 15:13:05 [ERROR] Van Grembergen199963 not imported
	```

	**HINT: for steps 9 and 10, copy-paste the entire contents of the Terminal into CotEditor or equivalent, then search for `[ERROR]` and `Invalid`.**

11. After a few successful "colrev retrieve" runs, run a top-up "colrev retrieve" for good luck (sometimes it consolidates/cleans up some of the records, e.g., around the `md_crossref.bib` and `md_dblp.bib` files). Then ZIP the whole folder just in case. Then close the current terminal window and open a fresh one (for a clean log).

12. Repeat steps 7-11 for each of the bib files, one at a time.
	- Take a ZIP snapshot of the whole repo after this, for good luck.

13. Run `colrev load`
	- Take a ZIP snapshot of the whole repo after this, for good luck.

14. Run `colrev dedupe`
	- Take a ZIP snapshot of the whole repo after this, for good luck.

## Part 3 - Setting up the repo on GitHub

15. Go over to GitHub in your web browser

16. On GitHub, create a new project **but do not initialise it**

17. In terminal:

	```zsh
	git remote add origin https://github.com/<YOUR REMOTE DETAILS HERE>
	git push -u origin main
	```


## Part 4 - Start screening!

_NOTE: For these steps, I like to use the included `blair-data` folder which you can put in your CoLRev repo. Doing so is of course **optional**. I found it was safe to run `python -m pip install -r requirements.txt` using the same venv as in Part 1. So then I could just run `sh ./records_to_csv_wrapper.sh` within the `blair-data` folder without any problems._ 😊

&emsp;

18. Setup exclusion criteria in `settings.json` and test it by setting one entry as `rev_prescreen_excluded`.

	```
	colrev_status                 = {rev_prescreen_excluded},
	screening_criteria            = {notcisr=out},
	```


19. Manually edit `records.bib`, save it, and run `colrev status` from time to time. For screening metadata records, mark as:
	- `rev_prescreen_included`
	- `rev_prescreen_excluded`
	

	Example of `colrev status` output:
	
	```zsh
	~/00blair/gitrepos-colrev/critical-is-research-colrev main* 6s
	_venv_colrev_0_11_0 ❯ colrev status
	Status
		init
		retrieve         20 retrieved     1147 to prepare [only 0 quality-curated]
		prescreen        14 included      [6 prescreen excluded]
		pdfs              0 retrieved     14 to retrieve
		screen            0 included
		data              0 synthesized
	```

20. For screening full-texts, mark as:
	- `rev_synthesized`
	- `rev_included`
	- `rev_excluded`

## Coming soon

- PDFs

## Not working for me yet

- PRISMA chart ☹️

