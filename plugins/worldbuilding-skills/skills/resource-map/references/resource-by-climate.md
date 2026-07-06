# Resource-by-climate reference

Premodern economy logic (Worldbuilding Workshop / Michael Tedin; Ricardo comparative advantage). Use to assign `produces`/`needs` from a region's climate, biome, elevation, and position.

## Sectors
- **Primary (extraction):** farming, herding, fishing, forestry, mining, quarrying. Placed by geography.
- **Secondary (manufacture):** smithing, weaving, brewing, shipbuilding. Locate near the raw material if it's bulky/costly to move (ore→smelting at the mine), or near population/ports if the input is cheap to move (cloth in cities).
- **Tertiary (services):** trade, banking, transport, administration, scholarship, mercenaries. Concentrates in hubs, capitals, and route crossings.

Combining rule: manufacture often needs imported inputs — tin + imported copper → exported bronze; wool + dye → cloth. These dependencies are trade hooks.

## Goods by climate / terrain

| Region type (koppen / biome) | Typical primary goods | Notes |
|------|------|------|
| Taiga / boreal (Df/Dw) | furs, timber, pitch, amber, honey | classic northern exports; needs grain |
| Tundra / ice (ET/EF) | furs, walrus ivory, whale oil; often nothing | strategic chokepoints > goods |
| Temperate forest/oceanic (Cf) | grain, cattle, timber, wool, flax, ale | breadbasket + shipbuilding timber |
| Mediterranean (Cs) | wine, olives/oil, fruit, wool, marble | dry-summer cash crops |
| Humid subtropical/monsoon (Cw/Am/Aw) | rice, tea, cotton, sugar, dyes | very high yields on the wet coast |
| Tropical rainforest (Af) | spices, hardwoods, fruit, resins, gems | the "spice islands" tier |
| Savanna / hot steppe (BSh/Aw) | grain, cattle, hides, ivory, gold | grazing + placer gold in rivers |
| Cold steppe (BSk) | horses, grain, wool, cattle | horse country — mobility & cavalry |
| Hot/cold desert (BWh/BWk) | salt, gems, minerals, dates (oasis), caravan tolls | scarce; wealth = water + transit |
| Mountains / highland | metals (iron, copper, tin, silver, gold), stone, gems, slate | ores by elevation; smelting on site |
| Coast / sea (any) | fish, salt, pearls, shellfish-dye, shipping | salt pans need sun (warm coasts) |
| Major river valley | irrigated grain surplus, flax, reeds, river trade | a green ribbon through dry land = breadbasket + road |
| Islands | spices, fish, pearls, shipping, piracy | trade-dependent, import staples |

## Strategic / high-value goods (trade & war drivers)
- **Salt** — universal preservative and near-currency; a monopoly saltpan is a power base.
- **Metals** — iron for war, silver/gold for coin; concentrated in mountains.
- **Spices / silk / dyes** — luxury, long-distance, huge markups far from source.
- **Horses** — military and transport; steppe/plains monopoly.
- **Timber (ship-grade)** — naval power; scarce in deserts and treeless plains.

## Needs logic
A region `needs` what it can't make: treeless plains need timber; deserts need grain and water-borne everything; cold north needs grain and wine; islands need staples and metal; pure mining regions need food. These needs become the demand side of `/trade-routes`.
