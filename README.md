# edutain.fun

Free browser games in the spirit of 90s edutainment, teaching history, geography and civics to kids in about 3rd–5th grade. No logins, no ads, no tracking.

## Layout

```
index.html        Launcher (At Ease–style desktop)
fonts/            Fonts shared by the launcher, the Gallery and Gone Fishing (self-hosted, no Google Fonts calls)
map/              Mixed-Up Map
gallery/          A Puzzling Presidential Gallery  (portraits/NN.jpg, 00 = Washington)
first/            Which Came First?  (the original flat-card version, still on the launcher)
packs/            Which Came First? card-pack version, in testing  (art/ = frames, card pictures, packs, logo, back and joke items; data.js = the 67 cards and 9 chains; lib/ = three.js)
chase/            The Big Map Chase
bill/             Bill's Big Trip  (art/ = pixel art, fonts/ = Pixelify Sans + Atkinson Hyperlegible)
fish/             Gone Fishing: Chesapeake Bay  (fish/<id>.webp = Duane Raver USFWS paintings, art/ = painted scenes, map, boat and props)
```

Each game is a single self-contained `index.html`, plus its own fonts and images. Every game has the shared "edutain.fun" menu bar. Its config line `EB={id:"…",home:"/"}` sends Quit back to the launcher at `/#<id>`, which plays the zoom-shut into that game's tile.

The launcher's game list is the `GAMES` array near the top of its script. To add a game, add a folder and a line there.

## Run it locally

Any static server from the repo root works:

```
python3 -m http.server 8000
```

Then open http://localhost:8000. Opening the files directly (`file://`) mostly works too, but Quit links back to the launcher may not.

## Notes

- Saved progress lives in each player's browser (localStorage) and never leaves it.
- `bill/art/palette.png` is the shared 48-color sprite palette. It isn't loaded by the game; new Bill's Big Trip sprites get snapped to it.
- Not in this repo on purpose: the MIDI files (rights unclear) and the retired first-sheet Bill sprites (`bill-front`, `bill-3q`, `bill-side`).

## Credits and licenses

- **ChicagoFLF** by Robin Casady: public domain.
- **Atkinson Hyperlegible** (Braille Institute), **Pixelify Sans**, **Cormorant Garamond**, **Source Sans 3**, **Zilla Slab** and **Patrick Hand** (Patrick Wagesreiter): SIL Open Font License 1.1. License texts are next to the font files.
- **Presidential portraits**: public-domain works.
- **Fish paintings** (Gone Fishing): Duane Raver, U.S. Fish and Wildlife Service, public domain.
- **Scenes, map, boat and props** (Gone Fishing): made for this project with Adobe Firefly.
- **Barlow Condensed** (Which Came First? card packs): SIL Open Font License 1.1, license next to the font files.
- **three.js** r160 (Which Came First? card packs): MIT License, `packs/lib/LICENSE-three.txt`.
- **Card frames, foil packs, logo, card back and joke items** (Which Came First? card packs): made for this project with Adobe Firefly and Nano Banana Pro.
- **Card pictures** (Which Came First? card packs): public-domain and openly licensed photos and paintings, mostly from Wikimedia Commons. The credits in `packs/data.js` are provisional until each one is checked against its source page.
- **Map data** (The Big Map Chase): Natural Earth via world-atlas and us-atlas, public domain.
- Pixel art for Bill's Big Trip was made for this project.

No license has been chosen yet for the code and writing. Until one is added, all rights are reserved.
