import argparse
import os
import xxhash

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='Path to directory', required=True)
parser.add_argument('-o', '--output', help='Output file name', default='mod')
parser.add_argument('-g', '--generate-hashes', help='Generate hashes for file names', action='store_true')
parser.add_argument('-m', '--multiple-files', help='Save multiple .usda files, one for each suffix type (except for diffuse)', action='store_true')
parser.add_argument('-a', '--add-sublayers', action='store_true', help='Add sublayers made with -m to the mod.usda file. This argument only modifies the mod.usda file and does not affect any custom USDA file specified by the -o argument.')
args = parser.parse_args()

directory_path = args.directory
game_ready_assets_path = os.path.join(directory_path)

suffixes = ['_normal', '_emissive', '_metallic', '_rough']

def generate_hashes(file_path):
    # Read the file and extract the raw data. Thanks @BlueAmulet!
    with open(file_path, 'rb') as file:
        data = file.read()
        
    dwHeight = int.from_bytes(data[12:16], "little")
    dwWidth  = int.from_bytes(data[16:20], "little")
    pfFlags  = int.from_bytes(data[80:84], "little")
    pfFourCC = data[84:88]
    bitCount = int.from_bytes(data[88:92], "little")
        
    mipsize = dwWidth*dwHeight
    if pfFlags & 0x4: # DDPF_FOURCC
        if pfFourCC == b'DXT1': # DXT1 is 4bpp
            mipsize //= 2
    elif pfFlags & 0x20242: # DDPF_ALPHA | DDPF_RGB | DDPF_YUV | DDPF_LUMINANCE
        mipsize = mipsize*bitCount//8
        
    hash_value = xxhash.xxh3_64(data[128:128+mipsize]).hexdigest()

    return hash_value.upper()

created_files = []
modified_files = []

def write_usda_file(suffix=None):
    # Check if there are any texture files with the specified suffix
    if suffix:
        has_suffix_files = False
        for file_name in os.listdir(game_ready_assets_path):
            if file_name.endswith(f'{suffix}.dds'):
                has_suffix_files = True
                break
        if not has_suffix_files:
            return

    usda_file_name = f'{args.output}{suffix if suffix else ""}.usda'
    usda_file_path = os.path.join(game_ready_assets_path, usda_file_name)

    if os.path.exists(usda_file_path):
        modified_files.append(usda_file_path)
    else:
        created_files.append(usda_file_path)

    hashes = set()
    
    for file_name in os.listdir(game_ready_assets_path):
        if file_name.endswith('.dds'):
            name, ext = os.path.splitext(file_name)
            if '_' not in name:
                hashes.add(name)
            else:
                name, file_suffix = name.rsplit('_', 1)
                if (suffix and file_suffix == suffix) or (not suffix and (file_suffix in suffixes or file_suffix == 'diffuse')):
                    hashes.add(name)

    with open(usda_file_path, 'w') as usda_file:
        usda_file.write(f'''#usda 1.0
(
    upAxis = "Y"
)

def Scope "Looks"
{{
}}

over "RootNode"
{{
    over "Looks"
    {{''')
        
        added_hashes = set()
        for hash in hashes:
            # Check if there is a corresponding texture file for the specified suffix
            if suffix and not any(file_name.endswith(f'{hash}{suffix}.dds') for file_name in os.listdir(game_ready_assets_path)):
                continue

            if args.generate_hashes:
                if f'{hash}.dds' in os.listdir(game_ready_assets_path):
                    hash_value = generate_hashes(os.path.join(game_ready_assets_path, f'{hash}.dds'))
                elif f'{hash}_diffuse.dds' in os.listdir(game_ready_assets_path):
                    hash_value = generate_hashes(os.path.join(game_ready_assets_path, f'{hash}_diffuse.dds'))
                else:
                    hash_value = hash
            else:
                hash_value = hash

            if hash_value in added_hashes:
                continue
            added_hashes.add(hash_value)

            usda_file.write(f'''
        over "mat_{hash_value.upper()}"
        {{
            over "Shader"
            {{''')


            if not suffix or suffix == '_diffuse':
                if f'{hash}.dds' in os.listdir(game_ready_assets_path):
                    usda_file.write(f'''
                asset inputs:diffuse_texture = @./{hash}.dds@ (
                    customData = {{
                        asset default = @@
                    }}
                    displayGroup = "Diffuse"
                    displayName = "Albedo Map"
                    doc = "The texture specifying the albedo value and the optional opacity value to use in the alpha channel"
                    hidden = false
                )''')

                elif f'{hash}_diffuse.dds' in os.listdir(game_ready_assets_path):
                    usda_file.write(f'''
                asset inputs:diffuse_texture = @./{hash}_diffuse.dds@ (
                    customData = {{
                        asset default = @@
                    }}
                    displayGroup = "Diffuse"
                    displayName = "Albedo Map"
                    doc = "The texture specifying the albedo value and the optional opacity value to use in the alpha channel"
                    hidden = false
                )''')

            if not suffix or suffix == '_emissive':
                if f'{hash}_emissive.dds' in os.listdir(game_ready_assets_path):
                    usda_file.write(f'''
                asset inputs:emissive_mask_texture = @./{hash}_emissive.dds@ (
                    colorSpace = "auto"
                    customData = {{
                        asset default = @@
                    }}
                    displayGroup = "Emissive"
                    displayName = "Emissive Mask Map"
                    doc = "The texture masking the emissive color"
                    hidden = false
                )
                bool inputs:enable_emission = 1 (
                    customData = {{
                        bool default = 0
                    }}
                    displayGroup = "Emissive"
                    displayName = "Enable Emission"
                    doc = "Enables the emission of light from the material"
                    hidden = false
                )
                float inputs:emissive_intensity = 5 (
                    customData = {{
                        float default = 40
                        dictionary range = {{
                            float max = 65504
                            float min = 0
                        }}
                    }}
                    displayGroup = "Emissive"
                    displayName = "Emissive Intensity"
                    doc = "Intensity of the emission"
                    hidden = false
                )''')

            if not suffix or suffix == '_metallic':
                if f'{hash}_metallic.dds' in os.listdir(game_ready_assets_path):
                    usda_file.write(f'''
                asset inputs:metallic_texture = @./{hash}_metallic.dds@ (
                    colorSpace = "auto"
                    customData = {{
                        asset default = @@
                    }}
                    displayGroup = "Specular"
                    displayName = "Metallic Map"
                    hidden = false
                )''')

            if not suffix or suffix == '_normal':
                if f'{hash}_normal.dds' in os.listdir(game_ready_assets_path):
                    usda_file.write(f'''
                asset inputs:normalmap_texture = @./{hash}_normal.dds@''')

            if not suffix or suffix == '_rough':
                if f'{hash}_rough.dds' in os.listdir(game_ready_assets_path):
                    usda_file.write(f'''
                asset inputs:reflectionroughness_texture = @./{hash}_rough.dds@ (
                    colorSpace = "auto"
                    customData = {{
                        asset default = @@
                    }}
                    displayGroup = "Specular"
                    displayName = "Roughness Map"
                    hidden = false
                )''')
            
            usda_file.write('''
            }
        }''')
        
        usda_file.write('''
    }
}
''')


def add_sublayers():
    mod_file_name = 'mod.usda'
    mod_file_path = os.path.join(game_ready_assets_path, mod_file_name)
    if os.path.exists(mod_file_path):
        modified_files.append(mod_file_path)
        with open(mod_file_path, 'r') as mod_file:
            mod_file_content = mod_file.read()
            sublayer_start = mod_file_content.find('subLayers = [')
            if sublayer_start != -1:
                sublayer_end = mod_file_content.find(']', sublayer_start)
                existing_sublayers = mod_file_content[sublayer_start+len('subLayers = ['):sublayer_end].split('\n')
                existing_sublayers = [sublayer.strip().rstrip(',') for sublayer in existing_sublayers if sublayer.strip()]
                new_sublayers = [f'@./{args.output}{suffix}.usda@' for suffix in suffixes if f'@./{args.output}{suffix}.usda@' not in existing_sublayers and os.path.exists(os.path.join(game_ready_assets_path, f'{args.output}{suffix}.usda'))]
                if new_sublayers:
                    sublayers = ',\n        '.join(existing_sublayers + new_sublayers)
                    mod_file_content = mod_file_content[:sublayer_start+len('subLayers = [')] + f'\n        {sublayers}\n    ' + mod_file_content[sublayer_end:]
                    with open(mod_file_path, 'w') as mod_file:
                        mod_file.write(mod_file_content)
            else:
                sublayers = ',\n        '.join([f'@./{args.output}{suffix}.usda@' for suffix in suffixes if os.path.exists(os.path.join(game_ready_assets_path, f'{args.output}{suffix}.usda'))])
                with open(mod_file_path, 'w') as mod_file:
                    mod_file.write(f'''#usda 1.0
(
    subLayers = [
        {sublayers}
    ]
)

{mod_file_content}''')

if args.add_sublayers:
    add_sublayers()

if args.multiple_files:
    for suffix in suffixes:
        write_usda_file(suffix)
else:
    write_usda_file()

print("Finished!")
print("Created files:")
for file in created_files:
    print(f"  - {file}")
print("Modified files:")
for file in modified_files:
    print(f"  - {file}")
