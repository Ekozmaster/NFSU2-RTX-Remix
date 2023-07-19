# Short Documentations, Tutorials and Cheat Sheets

The goal of this file is to be really really short and informative. Place here your tutorials, useful commands or documentations as succinctly as possible, while providing good information.

## Git Commands Explained | [For Command Line Users](https://git-scm.com/download/win)

#### `git init`
Initializes an empty local repository in the directory your terminal is at. An empty repository will start without any remote cloud to store your data, but is already fully operational on the local side. You can create branches, commit, make changes, go back and forth in time, all locally.

<hr>

#### `git fetch`
Updates your local mirror of the remote repository. Whenever someone adds new stuff to the remote repository (GitHub), everyone's local mirrors will be outdated. Sometimes doing `git checkout` (and other commands) might result in an outdated state, because checkout only brings stuff from the mirror.

<hr>

#### `git status`
Tells the current overall status of your local repository. Like this:
```
$ git status
On branch bollards-mesh-replacements
Your branch is up to date with 'origin/bollards-mesh-replacements'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   rtx-remix/mods/gameReadyAssets/myNewFile.dds

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   rtx-remix/mods/gameReadyAssets/mod.usda

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        rtx-remix/mods/gameReadyAssets/AAAAAA.txt
```
It shows:
- Which branch you are, and if it is up to date with your local mirror/copy of origin (remember the mirror can be updated with `git fetch`)
- `Changes to be committed`: AKA Staged changes. New files or modified ones which you added to the commiting "stage" with `git add`.
- `Changes not staged for commit`: AKA Unstaged changes. Changes on already present files which you didn't add yet
- `Untracked files`: Newly created files that didn't exist before.

<hr>

#### `git checkout <something>`
The checkout command is what allows us to jump between one branch or another, or even to specific commits. `git checkout main` will jump into the main branch, while `git checkout 78cbea008a4` will jump into the specific commit whose hash starts with `78cbea008a4`. This is what allows us to travel back and forth in time, and between alternate "timelines" (the branches).
Never use this command if you have unsaved work. Always check if the output of `git status` says you're clean.

<hr>

#### `git add <something>`
Adds your changes (being it additions, modifications or deletions) to the committing stage. You can specify individual files like `git add rtx-remix/mods/gameReadyAssets/mod.usda`, or everything under a specific directory down below with `git add gameReadyAssets/` or, if you prefer, under the current directory your terminal is at: `git add .` (yes, there is a dot for "current directory"). Only the changes added to the stage will be present in the commit when you run the `git commit` command.

<hr>

#### `git commit -m "Some cool message"`
Packs all the changes you've added to the stage into a package called "commit". You can add a message describing what you have done with the -m "Your message" arguments, like:
```
git commit -m "Adding lights to performance shop garages and renaming *_diffuse to *_albedo"
```
Those packages are what we exchange back and forth to the cloud repository and between developers. Branches are made out of sequences of commits, and this is how this "working in alternate timelines" analogy works: Several branches with different sets of commits that branches out and merges back again into the `main` branch, bringing their commits to the pile.

<hr>

#### `git reset --hard <something>`
Undo all the local changes and resets your repository to a given state like a commit or a branch. Ex: `git reset --hard 05db8ef` will nuke all commits made after the `05db8ef` and you're gonna lose all their changes, also, if you had any staged or unstaged changes, they will also be gone.
Likewise, `git reset --hard main` will undo every other commits and go back to the last commit on the `main` branch.
- Note: Untracked files (new files that didn't exist before and were never commited) won't be removed. For that you need to use `git clean -df`.
- Tip: It can be used to make sure your local branch will be exactly the same as the origin mirror's one, like this:
  ```
  git reset --hard origin/main
  ```

<br>


## Git Cheat Sheet | [For Command Line Users](https://git-scm.com/download/win)

### Cloning the repository into your game folder:
```
# Navigate to the game install location
cd "C:\Game-Install-location\"

# Initialize an empty repository in the game folder
git init

# Add this NFSU2-RTX-Remix.git at GitHub repo as the remote origin of this local repo
git remote add origin git@github.com:Ekozmaster/NFSU2-RTX-Remix.git

# Fetch all the most up to date information about the repo
git fetch

# Jump into the main branch with "-f" to ignore game files, so you get the latest stuff from the repo
git checkout main -f
```

<hr>

### Jump into another branch:
```
git checkout branch-name
```
And to make sure your local "branch-name" is up to date with the remote GitHub's, check this next block:

<hr>

### Downloading new updated content in a given branch:
```
# Navigate to the game install location (where you already have the repo installed/cloned)
cd "C:\Game-Install-location\"

# Fetch all the most up to date information about the repo so your local mirror of "origin" is up to date
git fetch

# If necessary, make sure you are in the right branch
git checkout beaconhill-west-lights

# Do a hard reset to set your current local state to the origin branch's:
git reset --hard origin/beaconhill-west-lights

# If your "git status" still shows you have untracked files after the reset:
git clean -df
```
This can be used to download new stuff merged in the `main` branch.

<hr>

### Commit a change
```
# Add your changes to the committing stage
git add file1.dds file2.dds file3.usda  # Or just use "git add ." to add everything

# Pack all the staged changes in a commit with a nice descriptive message
git commit -m "Adding 2 new texture replacements for the hotel plaza building."
```

<hr>

### Send your local branch-name state (new commits and stuff) to the GitHub's branch-name:
```
git push
```
If you're trying to push a state that is behind the GitHub version of your branch (GitHub version has new commits which your local branch doesn't) and you still want to push so the GitHub version goes back in time, remove all new commits and becomes exactly like your local branch:
```
git push -f
```
- OBS: Only use it if you know what you're doing.

<hr>

### Creating a new branch
```
# Got to the source branch you want your new branch to be based on (usually main):
git checkout main

# Checkout with the -b flag to indicate a new branch
git checkout -b new-branch-name

# To send this new branch to GitHub, use push with -u to create a remote branch with the same name and bind your local brach to it:
git push -u origin new-branch-name
```
