# BMW M Motorsport theme for DeepSeek Harness

A client-only Web UI theme built on the Warsteiner-liveried BMW M3 DTM car:
white body with black screen band, royal blue → azure → cyan → red livery,
checkered finish flag, roundel badging, and the BMW Motorsport lockup on a
black banner in the window's top-left corner. Light mode is the car on race day;
dark mode is the same car at night. The host half is intentionally empty.

## What it changes

- Both Light and Dark palettes, with every alias token supplied for both modes.
- **Banner**: the supplied BMW Motorsport lockup (roundel, M stripes, wordmark)
  on a black plate pinned to the top-left corner, with the four-colour livery
  stripe along its bottom edge. The lockup is embedded in `client.js` as a data
  URI, so the bundle stays one file. Size is exposed as `--bmw-banner-w` /
  `--bmw-banner-h` tokens.
- **Checkered finish flag** in the bottom-right corner, rotated and faded into
  the workspace so it reads as a printed texture.
- **Supplied BMW roundel on the hero**: the blank-session mark is the roundel
  cropped from the logo provided and embedded as a data URI. The hero headline is
  the host's localized "Into the Unknown" and the stylesheet renders it uppercase
  as the team line.
- **Sidebar row greets above New Session**: `Good morning, Sean.` until noon,
  `Good afternoon, Sean.` until 17:00, and `Good evening, Sean.` after that. The
  greeting re-checks the clock every 30 seconds and when the window becomes
  visible, is localized (English and Chinese), and its size is the
  `--bmw-greeting-size` token. The mark cell beside it is collapsed so the
  greeting stands alone.
- **Livery lines** on every composer card (two pixels along the top edge) and
  under the New Session button (three pixels), where the host classes allow it.
- **Composer decal**: slanted bars, a tracked-out `M Motorsport` label, the race
  number, and a small checkered flag, registered in `conversation.composer.dock`.
- The selected Session row carries the **four-colour livery** plus the blue
  selection wash.
- Cyan secondary state marks, yellow (not orange) warnings, red for errors and
  the brand accent, M blue focus rings, tighter radii, crisp flat shadows.

## Install

From the DSH Web GUI: **Plugins → Add plugin → local directory path**, then enter
this directory and choose **Install → Enable now**.

The bundle also works through `plugin_manager` with `action: install_bundle` and
this directory as the `target`.

## Files

| File | Role |
|---|---|
| `index.js` | Host half; empty plugin row that keeps the bundle active. |
| `client.js` | Client half; palette, livery chrome, banner lockup, racing plates, composer decal. |
| `cordis.patch.yml` | Bundle patch that inserts the `bmw-m-theme` row. |
| `icon.svg` | Plugin Manager artwork: the M racing plate. |
| `locale/*.json` | Plugin Manager title and description. |
| `art/` | Scratch: the supplied logo, the compose/embed scripts, and banner mocks. Not part of the runtime. |

## Notes

The theme is an override layer, not a new preference value, so the built-in
Light/Dark/System choice keeps working. Removing or disabling the bundle
restores the host palette, removes the stylesheet, and returns both brand marks
and the composer to the stock content.

The composer and New Session livery lines rely on the host class and data
attributes (`[data-composer-card]`, `button[class*="newSession"]`). If a future
build renames them, only those two lines disappear; everything else is token or
slot based.
