## Guidance for Texture artists
### Naming and paths
-   Texture names should match material hash with prefix added: 
Prefix list: *..._albedo; ..._roughness; ..._normal; ..._emissive; ..._metallic; ..._opacity*.

> Example:  *1290B1ECE63951FA_albedo.dds, 30AB9D52A75E6601_metallic.dds,
 53B3E936B785E132_emissive.dds*.

-   Make sure to put your textures in the separate folder under *[game folder]\rtx-remix\mods\gameReadyAssets\02_materials]* path. More detailed paths can be found down the notes, in the [**Shared File Hierarchy**](https://github.com/Ekozmaster/NFSU2-RTX-Remix/blob/readmeChanges/rtx-remix/mods/gameReadyAssets/README.md#shared-file-hierarchy) section.

> Example: *[game folder]\rtx-remix\mods\gameReadyAssets\02_materials\01_environment\13_airport*.

-   When replacing textures, make sure path references in *mod.usda* are not hard coded, like if they start with your drive letter.

> Example: good looking texture path: @./textures/env/garageLobby/952E501EB3175B1C_albedo.dds@;
> bad looking path: *@C:/Games/NFSU2/rtx-remix/mods/gameReadyAssets/textures/env/garageLobby/952E501EB3175B1C_albedo.dds@*

-   For better project merging capabilities, use custom *.usda* naming and place it as a sublayer for *mod.usda*. Your naming should briefly describe the content of the *.usda* file. More detailed naming can be found down the notes, in the [**Shared File Hierarchy**](https://github.com/Ekozmaster/NFSU2-RTX-Remix/blob/readmeChanges/rtx-remix/mods/gameReadyAssets/README.md#shared-file-hierarchy) section.
    
> Example: good naming: *burritoLightPlazaV01.usda*; bad naming: *burritoV01.usda*.

-   You can add your credentials in your *.usda* file if you feel like so. To make sure nothing break, just start the line with '#' sign which will mark it as a comment. Text can be anything you'd like. Text will get deleted if saved over Omniverse Create.
    
-   When sharing your assets, make sure you include your custom *.usda* and *.../texture* from *[your game]\rtx-remix\mods\gameReadyAssets* folder into an archive. Acceptable archive formats: *.7z,  .zip, .rar*. Name archive the same as included *.usda* file. In other words, don't include files that aren't referenced directly by your *.usda*.
    
-   Make sure that none of your files depend on the *captures* folder. All assets should be stored in the *gameReadyAssets* folder.
    
-   If you want to add an emissive, roughness, or metallic map you MUST include a new albedo map as well. Remix will not pass the original diffuse texture through if there are any changes to the texture so the object will have a blank gray albedo map.

### File formats
-   All the texture maps have to be in *.dds* format.
-   Common setting for different maps:  
    *Albedo/Emissive* map: sRGB 8-bit, BC7 RGBA compression, Mip Gamma Correct setting enabled;
*Normal map*: Octahedral 8-bit, BC5 RGBA\Grayscale compression, Mip Gamma Correct setting disabled;
*Roughness/Metallic* map: Grayscale 8-bit, BC4 RGBA\Grayscale compression, Mip Gamma Correct setting disabled.
-   Combined maps are not supported yet. Every material channel requires a separate file connected.
-   Texture size should be a factor of 4.

> Example: *4px, 512px, 800px*.

-   Be mindful of texture size as it impacts performance. Texture size should not go over 4096px on any side(for general scenarios).
-   Try to use smaller textures where it is possible. An overall project size should not go over 10Gb storage space.

## Guidance for Light artists
### Naming and paths
-   Light names can be anything you'd like, but it is more appreciated to name them according to their placement in the scene.

> Example: *350zHeadlight_part05_01*, *SphereLight8953*, *RectLight_0A48A0D79FB6594C_01*, etc.

-   For better project merging capabilities, use custom *.usda* naming and place it as a sublayer for mod.usda. Your naming should briefly describe the content of the *.usda file*. More detailed naming can be found down the notes, in the [**Shared File Hierarchy**](https://github.com/Ekozmaster/NFSU2-RTX-Remix/blob/readmeChanges/rtx-remix/mods/gameReadyAssets/README.md#shared-file-hierarchy) section.
   

> Example: good naming: *burritoLightPlazaV01.usda*; bad naming: *burritoV01.usda*.

-   You can add your credentials in your *.usda* file if you feel like so. To make sure nothing break, just start the line with '#' sign which will mark it as a comment. Text can be anything you'd like. Text will get deleted if saved over Omniverse Create.
- When sharing your assets, make sure you include your custom *.usda* from *[your game]\rtx-remix\mods\gameReadyAssets* folder into an archive. Acceptable archive formats: *.7z, .zip, .rar*. Name archive the same as included *.usda* file. In other words, don't include files that aren't referenced directly by your *.usda*.

### Remix settings
-   For better merging capabilities, stick to the following key settings in the Remix Developer Menu, while setting up your lights.

Rendering/Lighting: **Effect Light Intensity: *0.000***, **Emissive Intensity: *1.000***;
Rendering/Post-Processing/Auto Exposure: **Eye Adaptation: *OFF***;
Rendering/Post-Processing/Tonemapping: **Exposure Level: *0.750***, **Shadow Level: *2.000***, **Highlight Level: *4.000***;
Rendering/Experimental Features: **Anti-Culling: *ON***, **Anti-Culling Lights: *ON***, **Max Number Of Lights: *5000***, **Max Number Of Frames to...: *>60***;
Game Setup/Step 2: Parameter Tuning: **Scene Unit Scale: *0.010***(should be set back to 1.0 when making captures), **Scene Z-Up: *ON***;
Game Setup/Step 2: Parameter Tuning/Sky Tuning: **Sky Brightness: *1.000***;
Game Setup/Step 2: Parameter Tuning/Light Translation/Ignore Game Lights: **Directional: *ON***, **Point: *ON***, **Spot: *ON***;
Dev Settings/Developer Options: **Enable: *OFF***.

### Light settings
-   ~~Always enable Normalize Power~~.
-   IES shaping is not supported at the moment.
-   Prioritize changing only one brightness value over the other. Ideally you should get either default Intensity and adjusted Exposure, or adjusted Intensity and default Exposure.

> Example: for SphereLight: *30k Intensity and -8 Exposure* or *80 Intensity
and 0 Exposure*.

- Don’t forget to add *custom int preserveOriginalDrawCall = 1* line to every mesh you apply light source to.

## Shared File Hierarchy
-   Following structure is used in the shared github project [link](https://github.com/Ekozmaster/NFSU2-RTX-Remix).
-   Just as by default, the *mod.usda* file stays in the *gameReadyAssets* folder. The following structure is used to link any purpose *.usda* to the location in the hierarchy. Every folder/file should be already added to the list of *mod.usda* sublayers.
-   When naming your *.usda* file, first include all the numerals of the path, then add *‘_’(underscore)*, after that add the path signs starting from level 2 of the structure and divide signs with *‘-’(dash)*.

> Example: for *01_lights/01_buildings/16_garages/01_garageLobby* use *01011601_garages-garageLobby.usda*; for *01_lights/03_cars/23_RX7* use *010323_RX7.usda*.

-   Place your *.usda* files directly into the corresponding folder. Be aware, when creating a material *.usda*, you have to store it in the same folder where your referenced textures are. So all the references in *.usda* go to the same folder.
    

> Example: for Mazda RX7 materials, both *020223_RX7.usda* and your textures will be in the same *02_materials/02_cars/23_RX7* folder;
> for Stadium lights, you place your *010109_stadium.usda* in *01_lights/01_buildings/09_stadium* folder.

-   When using a map, please follow the rule of borders: if some assets are on the border line between regions, they will be part of the same region as the ROAD they are connected to.
- Map to orient on (for better experience, please download it): [Vector map in PDF format](https://drive.google.com/file/d/19Vm7AYMqBA9o0kP-r8bYHkXg0utPkTGW/view?usp=sharing)

<details>
<summary>FILE STRUCTURE</summary>
  
- gameReadyAssets
  - 01_lights
    - 01_buildings
      - 01_jacksonHeights01
      - 02_jacksonHeights02
      - 03_jacksonHeights03
      - 04_beaconHillWest
      - 05_beaconHillEast
      - 06_pigeonPark
      - 07_hotelPlaza
      - 08_cityCenter
      - 09_stadium
      - 10_southMarket
      - 11_fortUnion
      - 12_elNorte
      - 13_airport
      - 14_coalHarborWest
      - 15_coalHarborEast
      - 16_garages
        - 01_garageLobby
        - 02_garageCareer
        - 03_garageCar
        - 04_garagePerf
        - 05_garageSpec
        - 06_garageBody
        - 07_garageGraph
        - 08_garageDyno
    - 02_roadways
      - 01_jacksonHeights01
      - 02_jacksonHeights02
      - 03_jacksonHeights03
      - 04_beaconHillWest
      - 05_beaconHillEast
      - 06_pigeonPark
      - 07_hotelPlaza
      - 08_cityCenter
      - 09_stadium
      - 10_southMarket
      - 11_fortUnion
      - 12_elNorte
      - 13_airport
      - 14_coalHarborWest
      - 15_coalHarborEast
      - 16_airportCircuit
      - 17_bayviewSpeedway
      - 18_stadiumDrift
      - 19_parkadeDrift
      - 20_parkadeTrack
      - 21_industrialPark
    - 03_cars
      - 01_240SX
      - 02_350Z
      - 03_3000GT
      - 04_A3
      - 05_CELICA
      - 06_CIVIC
      - 07_COROLLA
      - 08_ECLIPSE
      - 09_ESCALADE
      - 10_FOCUS
      - 11_G35
      - 12_GOLF
      - 13_GTO
      - 14_HUMMER
      - 15_IMPREZAWRX
      - 16_IS3000
      - 17_LANCEREV08
      - 18_MIATA
      - 19_MUSTANGGT
      - 20_NAVIGATOR
      - 21_PEUGOT
      - 22_RSX
      - 23_RX7
      - 24_RX8
      - 25_SENTRA
      - 26_SKYLINE
      - 27_SUPRA
      - 28_TIBURON
      - 29_TT
      - 30_traffic
    - 04_unique
      - 01_stage01
        - ...
      - 02_stage02
        - ...
      - 03_stage03
        - ...
      - 04_stage04
        - ...
      - 05_stage05
        - ...
    - 05_global
      - 01_stage01
        - ...
      - 02_stage02
        - ...
      - 03_stage03
        - ...
      - 04_stage04
        - ...
      - 05_stage05
        - ...
  - 02_materials
    - 01_environment
      - 01_jacksonHeights01
      - 02_jacksonHeights02
      - 03_jacksonHeights03
      - 04_beaconHillWest
      - 05_beaconHillEast
      - 06_pigeonPark
      - 07_hotelPlaza
      - 08_cityCenter
      - 09_stadium
      - 10_southMarket
      - 11_fortUnion
      - 12_elNorte
      - 13_airport
      - 14_coalHarborWest
      - 15_coalHarborEast
      - 16_garages
        - 01_garageLobby
        - 02_garageCareer
        - 03_garageCar
        - 04_garagePerf
        - 05_garageSpec
        - 06_garageBody
        - 07_garageGraph
        - 08_garageDyno
      - 17_airportCircuit
      - 18_bayviewSpeedway
      - 19_stadiumDrift
      - 20_parkadeDrift
      - 21_parkadeTrack
      - 22_industrialPark
    - 02_cars
      - 01_240SX
      - 02_350Z
      - 03_3000GT
      - 04_A3
      - 05_CELICA
      - 06_CIVIC
      - 07_COROLLA
      - 08_ECLIPSE
      - 09_ESCALADE
      - 10_FOCUS
      - 11_G35
      - 12_GOLF
      - 13_GTO
      - 14_HUMMER
      - 15_IMPREZAWRX
      - 16_IS3000
      - 17_LANCEREV08
      - 18_MIATA
      - 19_MUSTANGGT
      - 20_NAVIGATOR
      - 21_PEUGOT
      - 22_RSX
      - 23_RX7
      - 24_RX8
      - 25_SENTRA
      - 26_SKYLINE
      - 27_SUPRA
      - 28_TIBURON
      - 29_TT
      - 30_traffic
    - 03_global
      - 01_roads
      - 02_worldSprites
  - 03_meshes
    - ...
</details>
