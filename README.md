# Pokémon Following and Following Renegade Translation

![GitHub release (by tag)](https://img.shields.io/github/downloads/christt105/PokemonFollowingRenegadePlatinumTranslation/Following/total?style=flat-square)
![GitHub release (by tag)](https://img.shields.io/github/downloads/christt105/PokemonFollowingRenegadePlatinumTranslation/FollowingRenegade/total?style=flat-square)
 
Repositorio utilizado para traducir Pokémon Following Platinum y Pokémon Following Renegade Platinum al español.  
La traducción de Following Platinum usa los textos originales de la ROM en español y traduce el contenido nuevo.  
La traducción de Following Renegade Platinum se basa en la traducción de Pokémon Renegade Platinum al español de [Drakyem](https://twitter.com/drakyem) y añade la traducción de Following Platinum.  
La herramienta utilizada es `thenewpoketext`. Soy principiante en el ROM hacking, así que seguro hay mejores maneras de hacerlo, pero espero que esto sea útil para alguien.  

### Más información  
Si quieres saber más o participar en el debate sobre la traducción, puedes visitar el siguiente enlace:  
🗨️ [Foro de Whack a Hack sobre Pokémon Following Platinum en Español](https://whackahack.com/foro/threads/pokemon-following-platinum-espanol.68015/)  

### Agradecimientos  
* [Drayano](https://twitter.com/Drayano60): Creador de Pokémon Renegade Platinum  
* [Drakyem](https://twitter.com/drakyem): Traductor de Pokémon Renegade Platinum al español  
* [Mikelan98](https://twitter.com/Mikelan98) y [AdAstra](https://twitter.com/AdAstra_GL): Creadores de Pokémon Following Platinum  
* [u/chensquared-art](https://www.reddit.com/r/PokemonROMhacks/comments/s4fbhi/complete_renegade_platinum_and_following_platinum/): Integración de Pokémon Following Platinum en Pokémon Renegade Platinum  
* [christt105](https://github.com/christt105): Traductor de Pokémon Following Platinum y creador de los parches de Following y Following Renegade en español.

## Setup

In order to use the repository you need to have [Python 3](https://www.python.org/downloads/) installed. You also need the assets to translate. In my case I have used the following ones:

* PokePlatinumEn.nds [Pokémon Platinum USA 3541]
* PokePlatinumEs.nds [Pokémon Platinum (Spanish)]
* PokeRenegadeEn.nds [Pokémon Renegade Platinum (English)] ([patched](https://pokehacking.com/fangames/renegade-platinum/))
* PokeRenegadeEs.nds [Pokémon Renegade Platinum (Spanish)] ([patched](https://pokehacking.com/fangames/renegade-platinum/))
* PokeFollowingEn.nds [Pokémon Following Platinum (English)] ([patched](https://pokehacking.com/fangames/following-platinum/))
* PokeFollowingEs.nds [Pokémon Following Platinum (Spanish)] (copy of PokeFollowingEn.nds)
* PokeFollowingRenegadeEn.nds [Pokémon Following Renegade Platinum (English)] ([patched](https://www.reddit.com/r/PokemonROMhacks/comments/s4fbhi/complete_renegade_platinum_and_following_platinum/))
* PokeFollowingRenegadeEs.nds [Pokémon Following Renegade Platinum (Spanish)] (copy of PokeFollowingRenegadeEn.nds)

All the roms must be in `./thenewpoketext/` folder.

It is only tested in Windows 10.

## Steps to translate Pokémon Following Platinum to Spanish

* Check that the roms are in the correct folder
* Execute `./thenewpoketext/create_batch.py`. This will create all the scripts to export the text from the roms.
* Execute `./export.py`. This will export the text from the roms to the `./xml/` folder.
* Execute `./comparer.py`. This will compare the text from the roms and create a file with the differences in `./output/comparisons/` folder.
* Execute `./replace.py`. This will replace the english texts from the PokeFollowingEs with the Spanish texts from original Pokémon Platinum Spanish ROM.
* Execute `./translate_following.py`. This will go through all the file 724 and translate the text. The result is a `.csv` file in `./output/translated/Following_724.csv` folder.
* Check manually all the entries.
* Create a manual_translation object in `./import_translation_following.py` for other text that is not in the file 724. ADVISE: If you want to set an empty text, use `"\n"`, instead of `""`. Then execute the script.
* Now, the `./xml/PokeFollowingEs.xml` file should be translated. We need to open `./thenewpoketext/thenewpoketext.exe` and do the following. //TODO: automate with a script
  * Write the Romname. In this case, "`PokeFollowingEs.nds`".
  * "`patch ../xml/PokeFollowingEs.xml`". This will patch the rom with the new text.
  * (Only in platinum) You have to change the msg.narc files. Go to the `./thenewpoketext/tmp_PokeFollowingEs/root/msgdata/` (in case you are using other rom change the name of the `tmp_` folder). Rename `msg.narc` to `pl_msg.narc` and `msg1.narc` to `msg.narc`.
  * Then, in the `thenewpoketext` session write `mkrom PokeFollowingEs.nds`. This will create the patched rom with the texts changed.
  * ADVICE: If you want to continue editing the rom, you have to rename again the `msg.narc` and `pl_msg.narc` files.

## Steps to translate Pokémon Following Renegade Platinum to Spanish

In order to translate Pokémon Following Renegade Platinum to Spanish, we will use the translation of Pokémon Renegade Platinum to Spanish from [Drakyem](https://twitter.com/drakyem) and the translation of Pokémon Following Platinum to Spanish that we made in the previous step. So be sure that yo have execute the scripts `comparer.py` and `replace.py` from the previous step. If everything is ok, we should have the following files:

* `xml/FollowingRenegadeEs.xml` with the translation of the Pokémon Renegade Platinum in Spanish.
* `xml/PokeFollowingEs.xml` with the translation of the Pokémon Following Platinum in Spanish.
* `output/comparisons/split/PokeRenegadeEn-PokeFollowingEn.json` with the differences between the Pokémon Renegade Platinum in English and the Pokémon Following Platinum in English.

Now, we only need to execute `import_following_into_followingrenegade.py`. Once the script is executed, we will have the `xml/PokeFollowingRenegadeEs.xml` file with the translation of the Pokémon Following Renegade Platinum in Spanish. Then we will need to do the last step of the previous section to patch the rom.

* Execute `.thenewpoketext/thenewpoketext.exe`.
* Write the Romname. In this case, "`PokeFollowingRenegadeEs.nds`".
* "`patch ../xml/PokeFollowingRenegadeEs.xml`". This will patch the rom with the new text.
* (Only in platinum) You have to change the msg.narc files. Go to the `./thenewpoketext/tmp_PokeFollowingRenegadeEs/root/msgdata/` (in case you are using other rom change the name of the `tmp_` folder). Rename `msg.narc` to `pl_msg.narc` and `msg1.narc` to `msg.narc`.
* Then, in the `thenewpoketext` session write "`mkrom PokeFollowingRenegadeEs.nds`". This will create the patched rom with the texts changed.
