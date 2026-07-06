# Climate rules reference

Deterministic rules for assigning climate zones by hand. Sources: Geoff's Climate Cookbook, Worldbuilding Pasta ("An Apple Pie From Scratch", esp. Part VIb), Artifexian, Köppen–Geiger. These aim for "close enough for worldbuilding," not simulation accuracy.

## 1. The reduced Köppen-14 set

Use these 14 zones (Worldbuilding Pasta's reduction of the full 31). `koppen:` in climate.v1 takes the code.

| Code | Name | Rough conditions | Typical biome |
|------|------|------------------|---------------|
| Af | Tropical rainforest | Hot, wet all year (0–10°) | rainforest |
| Am | Tropical monsoon | Hot, heavy summer rain, short dry | monsoon forest |
| Aw | Tropical savanna | Hot, wet summer / dry winter (5–20°) | savanna |
| BWh | Hot desert | Arid, hot (subtropical highs ~20–30°, leeward, cold-current coasts) | hot desert |
| BWk | Cold desert | Arid, cold winters (continental interiors, rain shadow) | cold desert |
| BSh | Hot steppe | Semi-arid, hot; desert margins | hot grassland/steppe |
| BSk | Cold steppe | Semi-arid, cold winters; interior margins | cold steppe |
| Cs | Mediterranean | Mild wet winter / hot dry summer (30–45° west coasts) | chaparral/scrub |
| Cw | Humid subtropical, dry winter | Warm, summer rain (monsoon margins) | subtropical |
| Cf | Humid subtropical / oceanic | Mild, rain year-round (30–60°, esp. warm-current coasts) | temperate forest/grassland |
| Dw | Cold, dry winter | Cold continental, summer rain | boreal/continental |
| Df | Cold, wet | Cold continental, precip year-round (40–65° interiors/east coasts) | taiga/temperate forest |
| ET | Tundra | Coldest month <10°C, no true summer (>60° or high alt) | tundra |
| EF | Ice cap | All months below freezing (poles, high peaks) | ice |

Temperature bands for the `temp:` enum (summer/winter): frigid, cold, cool, mild, warm, hot. Precip amount: arid, low, moderate, high, very-high. Pattern: year-round, winter-wet, summer-wet(monsoon), erratic.

## 2. Latitude → base temperature and circulation cells

Three-cell model gives both temperature and prevailing wind. For a **prograde** planet (Earth-like); **mirror the wind directions if retrograde**.

| Latitude | Cell / feature | Surface winds | Climate tendency |
|----------|----------------|---------------|------------------|
| 0–5° | ITCZ (rising air) | calm/variable | wet, hot (Af) |
| 5–25° | Hadley | **easterlies** (trade winds) | wet windward, savanna poleward (Aw) |
| ~20–30° | Subtropical high (sinking air) | calm belts | **deserts** (BWh) — the great desert latitudes |
| 30–60° | Ferrel | **westerlies** | temperate; west coasts wet (Cs/Cf) |
| ~60° | Subpolar low | — | wet, cool |
| 60–90° | Polar | **polar easterlies** | cold desert/tundra (ET/EF) |

Axial tilt sets seasonal swing: higher tilt = more extreme seasons and a wider ITCZ migration. Tilt near 0 = almost no seasons.

## 3. Altitude — lapse rate

Temperature falls ~**6.5 °C per km** of elevation (standard environmental lapse rate; Britannica: "about 6.5 °C per kilometre / 18.8 °F per mile in the lower atmosphere"). Practical shifts per ~1 km climbed: warm temperate → cool → cold → tundra → ice. Elevating a biome moves it toward its colder equivalent: grassland→tundra, savanna→steppe, forest→taiga. Highlands in the tropics can be temperate ("eternal spring"); high peaks anywhere reach ET/EF.

## 4. Rain shadow / orographic lift

Air forced up a windward slope cools, drops rain → wet windward side. Descending on the leeward side it warms and dries → **rain-shadow desert**. Decide windward vs leeward from the prevailing wind at that latitude (§2) and the range's orientation.

Earth anchors: Himalaya → Gobi; Sierra Nevada → Great Basin; Cascades → the dry east of Oregon/Washington; Andes → Patagonian desert. A N–S range in the westerlies (30–60°) makes its **east** side dry; the same range in the trade-wind easterlies (5–25°) makes its **west** side dry.

## 5. Ocean currents

Warm currents make coasts warmer and wetter than latitude alone suggests; cold currents make them cooler and drier, and can create **coastal deserts** even beside the sea.

- Warm-current coast (e.g. NW Europe / Gulf Stream): temperate oceanic (Cf) pushed poleward.
- Cold-current coast (e.g. coastal Peru/Atacama, Namib): arid despite the ocean (BWh/BWk) — this is the ONLY clean justification for a desert on open water (SCHEMA rule 1).
- Gyre pattern: currents run clockwise in the N hemisphere, anticlockwise in the S. Warm currents track up western ocean basins / eastern continental coasts; cold currents track down eastern ocean basins / western continental coasts (subtropics). Use this to place currents if `world.v1` didn't specify them.

## 6. Continentality

Distance from the sea increases summer heat, winter cold, and dryness. Maritime moisture rarely penetrates beyond ~3,000 km. Deep interiors trend toward steppe/cold desert (BSk/BWk) and large annual temperature ranges; same-latitude coasts stay milder and wetter.

## 7. ITCZ migration → monsoon

The ITCZ (rain belt) drifts toward the summer hemisphere. Where it swings over land, onshore summer winds bring a wet season and offshore winter winds a dry one — the monsoon (Am/Aw/Cw). Strong over large low-latitude landmasses with a warm sea upwind (South Asia is the archetype).

## 8. Worked examples (Earth validation)

- **Sahara (~20–30°N, interior/leeward, subtropical high)** → sinking air + trade-wind desert → BWh hot desert. ✔
- **UK (50–58°N, west coast, westerlies, warm current)** → Cf temperate oceanic, mild wet winters. ✔
- **Atacama (~20–25°S, west coast, cold Humboldt current, leeward of Andes)** → BWh coastal desert on open water, justified by cold current + rain shadow. ✔ (satisfies SCHEMA rule 1)
- **Amazon (0–5°S, lowland, ITCZ)** → Af rainforest. ✔
- **Gobi (~42–45°N, deep interior, leeward of Himalaya)** → BWk cold desert (continentality + rain shadow). ✔
- **Central India (10–25°N, monsoon)** → Aw/Am, summer-wet. ✔

## 9. Common mistakes to check against

- Desert on a windward coast with a warm current (should be wet).
- Rainforest in a subtropical-high latitude (should be desert unless a special driver).
- Uniform climate across a wide interior (ignore continentality at your peril).
- Same biome on both sides of a mountain range (rain shadow should differentiate them).
- Prevailing winds not mirrored on a retrograde planet.
