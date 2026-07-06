# Map description guide

The `map.description` field in `world.v1` is the single geographic source of truth. `/climate-from-map` derives every region from it, so structured text beats an image every time. Transcribe images into this format and confirm with the user.

## Required elements

1. **Scale** — approximate extent in km (e.g. "continent ~3,500 km N–S, ~2,800 km E–W").
2. **Latitude range** — where the land sits (e.g. "10°N to 55°N"). Without this, no climate zones can be assigned.
3. **Landmasses** — name and rough shape of each continent/large island.
4. **Mountain ranges** — name, orientation (N–S / E–W), position (western seaboard, interior, etc.), and rough height class (hills / high range / alpine). Orientation + prevailing winds = rain shadows.
5. **Coastlines and seas** — which sides face open ocean, enclosed seas, gulfs, straits.
6. **Optional but valuable**: major rivers, large lakes, island chains, known ocean currents (otherwise climate will propose them), and any deliberate anomalies (magical or otherwise) flagged as such.

## Worked example

> The continent of Vessa spans 10°N–55°N, ~3,500 km N–S and ~2,800 km E–W at its widest. The Kharesh Mountains, a high alpine range, run N–S along the western seaboard from 25°N to 45°N, close to the coast. East of them stretch broad interior plains. The west coast faces open ocean; the southeast coast wraps around the warm Gulf of Szel (10°N–20°N), dotted with the Szelic Isles. The north coast (above 50°N) faces a cold polar sea. The River Ammat rises in the central Kharesh and drains east across the plains into the Gulf.

## Anti-patterns

- "A big continent with mountains and forests" — no latitudes, no orientation: climate cannot run.
- Listing biomes ("there's a desert in the middle") — biomes are *outputs* of `/climate-from-map`, not inputs. If the user wants a desert somewhere, record it in `open_questions` as a constraint to verify, not as map fact.
- Coastline left ambiguous — every landmass edge should be attributable to ocean, sea, or another landmass.
