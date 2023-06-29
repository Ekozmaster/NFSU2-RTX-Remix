# NFSU2-RTX-Remix
RTX Remix mod for Need for Speed Underground 2
![](/rtx-remix/ModThumb.png)

<br>

#### Dependencies:
- **[Underground 2 Widescreenfix](https://github.com/ThirteenAG/WidescreenFixesPack/releases/tag/nfsu2)**: For nowadays FHD to excessively giga wide screens.
- **[RTX-Remix](https://github.com/NVIDIAGameWorks/rtx-remix)**: Nvidia modding tool to intercept the game and load the mod files.
- **[Bridge Remix](https://github.com/NVIDIAGameWorks/bridge-remix)**
- **[DXVK-Remix](https://github.com/NVIDIAGameWorks/dxvk-remix)**

# Installation
[Video Version](https://www.youtube.com/watch?v=U32QaB23Mws)
or reader's version:

## For Playing:
- Automated installer coming soon! For now, you can use the same steps as the [Installation for contributors](#install-for-contributors). Skip the requirements and take the `.zip` path.


## <a name="install-for-contributors"></a>For Contributors:
#### Required Tools
- git for Windows. [Download](https://git-scm.com/download/win)
- git LFS extension to manage large binary files like `.dds` and `.usd`. OBS: `.usda` aren't binary and we want to see and review their content. [Link](https://git-lfs.com/)
  - The repo is already setup, you just need to run `git lfs install`.
- Omniverse Launcher [Download](https://www.nvidia.com/pt-br/omniverse/download/)
  - In the launcher, also install `Create`, the main tool we use to manipulate USD/USDA files and develop the modifications to the game.

#### Installing Dependencies
- Download **Underground 2 Widescreenfix** and paste the contents in the game directory. [NFSUnderground2.WidescreenFix.zip](https://github.com/ThirteenAG/WidescreenFixesPack/releases/tag/nfsu2).
  - Modify the `scripts/NFSUnderground2.WidescreenFix.ini` with a text editor so `WindowedMode = 4` and `Skip Intro = 1`.
  - Rename the `dinput8.dll` file to `dsound.dll`.
- Download **RTX-Remix 0.2.0** and paste the contents in the game directory so the `.trex` folder will be next to `speed.exe`. [Link](https://github.com/NVIDIAGameWorks/rtx-remix/releases/tag/remix-0.2.0) (GitHub Login required to see the links).
- Do the same with **Bridge Remix** [Link](https://github.com/NVIDIAGameWorks/bridge-remix/actions/runs/5095209923) (GitHub Login required to see the links).
- And with **DXVK Remix**, but paste the files inside the `.trex` folder. [Link](https://github.com/NVIDIAGameWorks/dxvk-remix/actions/runs/5150202285) (GitHub Login required to see the links).

#### Installing the mod itself:
- Either [download the repo as zip](https://github.com/Ekozmaster/NFSU2-RTX-Remix/archive/refs/heads/main.zip) and unzip it inside the game directory (replace everything it asks for) or
- Initialize a git repo in the game installation directory, add this repository as it's remote origin, `fetch` the mod files from the origin and switch to the `main` branch, all using `git bash`:
    ```
    cd C:\Games\Need for Speed Underground 2\
    git init
    git remote add origin https://github.com/Ekozmaster/NFSU2-RTX-Remix.git
    git fetch
    git checkout main
    ```
- At the end, just make sure this README.md file is right next to `speed.exe`.
- Have fun!
