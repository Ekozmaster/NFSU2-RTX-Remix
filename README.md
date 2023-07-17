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
- Automated installer coming soon! For now, install the dependencies as mentioned below and instead of using git, download the release file and unzip it into your game folder:<br>
    https://github.com/Ekozmaster/NFSU2-RTX-Remix/releases


## <a name="install-for-contributors"></a>For Contributors:
#### Required Tools
- git for Windows. [Download](https://git-scm.com/download/win)
- git LFS extension to manage large binary files like `.dds` and `.usd`. OBS: `.usda` aren't binary and we want to see and review their content. [Link](https://git-lfs.com/)
  - The repo is already setup, you just need to run `git lfs install`.
- Omniverse Launcher [Download](https://www.nvidia.com/pt-br/omniverse/download/)
  - In the launcher, also install `USD Composer (Formerly named Create)`, the main tool we use to manipulate USD/USDA files and develop the modifications to the game.

#### Installing Dependencies
- Download **Underground 2 Widescreenfix** and paste the contents in the game directory. [NFSUnderground2.WidescreenFix.zip](https://github.com/ThirteenAG/WidescreenFixesPack/releases/tag/nfsu2).
  - Modify the `scripts/NFSUnderground2.WidescreenFix.ini` with a text editor so `WindowedMode = 4` and `Skip Intro = 1`.
  - Rename the `dinput8.dll` file to `dsound.dll`.
- Download **RTX-Remix 0.2.0** and paste the contents in the game directory so the `.trex` folder will be next to `SPEED2.exe`. [Link](https://github.com/NVIDIAGameWorks/rtx-remix/releases/tag/remix-0.2.0) (GitHub Login required to see the links).
- Do the same with **Bridge Remix** (Release version) [Link](https://github.com/NVIDIAGameWorks/bridge-remix/actions/runs/5095209923) (GitHub Login required to see the links).
- And with **DXVK Remix** (Also release version), but paste the files inside the `.trex` folder. [Link](https://github.com/NVIDIAGameWorks/dxvk-remix/actions/runs/5150202285) (GitHub Login required to see the links).

#### Installing the mod itself:
- Using a terminal (Ex: Git bash):
    ```
    cd "C:\Game-Install-location\"

    # Initialize an empty repository in the game folder
    git init

    # Add NFSU2-RTX-Remix.git repo as the remote origin of this local repo
    git remote add origin git@github.com:Ekozmaster/NFSU2-RTX-Remix.git

    # Fetch all the most up to date information about the repo
    git fetch

    # Jump into the main branch with "-f" to ignore game files, so you get the latest stuff from the repo
    git checkout main -f
    ```
- Copy the `rtx-remix-defaults/rtx.conf` in the same folder as your `SPEED2.exe`.
- Have fun!
