#!/usr/bin/env python3
"""uwp_world.py - deterministic Traveller mainworld facts generator.

Usage:  python3 uwp_world.py "<world line>"

Accepts anything from a bare UWP ("A788899-C") to a full sector-file line
("0310 Regina A788899-C N Ri Cp A 703 Im"). The seed is derived ONLY from
hex + name + UWP, so supplying extensions later never re-rolls the world.
Extensions (bases, zone, PBG, allegiance, {Ix} (Ex) [Cx], stellar) are
parsed best-effort and passed through as provided canon.

Output: JSON facts block on stdout. Mainworld only - never invents stars,
moons, gas giants, or other system bodies.
"""

import hashlib
import json
import os
import re
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tables  # per-digit flavour tables, one per UWP element value

# ---------------------------------------------------------------- parsing

UWP_RE = re.compile(r"^([A-EX])([0-9A-F])([0-9A-F])([0-9A-F])([0-9A-F])([0-9A-F])([0-9A-F])-([0-9A-Z])$")
HEX_RE = re.compile(r"^\d{4}$")
PBG_RE = re.compile(r"^\d{3}$")
STELLAR_RE = re.compile(r"^([OBAFGKM]\d|D|BD)$|^(Ia|Ib|II|III|IV|V|VI|VII)$")
TRADE_RE = re.compile(r"^[A-Z][a-z]{1,2}$")
BASE_LETTERS = set("NSDWKMBCGVTE")

KNOWN_TRADE = {
    "Ag", "As", "Ba", "De", "Fl", "Ga", "Hi", "Ht", "Ic", "In", "Lo", "Lt",
    "Na", "Ni", "Po", "Ri", "Va", "Wa", "Cp", "Cs", "Cx", "Da", "Di", "Dw",
    "Fo", "Pz", "An", "Ab", "Pi", "Pe", "Pr", "Re", "Rs", "Sa", "Tz", "Mr",
    "Fa", "Mi", "Px", "He", "Oc", "Bo", "Co", "Tr", "Tu", "Lk", "St",
    "Ph", "Pa", "Cy", "Fr", "Ho",
}


def hv(c):
    """Extended-hex value (0-9, A-Z minus I/O in some editions - base36 is fine)."""
    return int(c, 36)


def parse_line(text):
    notes = []
    raw = text.strip()
    # pull T5 extensions out first (strict patterns - a remark like
    # "(Tethmari)" is NOT an economic extension and stays a remark)
    ix = re.search(r"\{\s*[+-]?\d+\s*\}", raw)
    ex = re.search(r"\([0-9A-Z]{3}[+-]\d\)", raw)
    cx = re.search(r"\[[0-9A-Z]{4}\]", raw)
    for m in (ix, ex, cx):
        if m:
            raw = raw.replace(m.group(0), " ")
    tokens = [t for t in raw.split() if t != "-"]  # "-" = empty column

    uwp_i = next((i for i, t in enumerate(tokens) if UWP_RE.match(t.upper())), None)
    if uwp_i is None:
        sys.exit("ERROR: no UWP found in input (expected e.g. A788899-C)")
    uwp = tokens[uwp_i].upper()

    pre = tokens[:uwp_i]
    hex_ = next((t for t in pre if HEX_RE.match(t)), None)
    name = " ".join(t for t in pre if t != hex_) or None

    provided = {"bases": [], "trade_codes": [], "zone": None, "pbg": None,
                "worlds_in_system": None, "allegiance": None,
                "importance": ix.group(0) if ix else None,
                "economic": ex.group(0) if ex else None,
                "cultural": cx.group(0) if cx else None,
                "stellar": [], "unparsed": []}

    post = tokens[uwp_i + 1:]
    for j, t in enumerate(post):
        tu = t.upper()
        if PBG_RE.match(t) and provided["pbg"] is None:
            provided["pbg"] = t
        elif t.isdigit() and len(t) <= 2 and provided["pbg"] and provided["worlds_in_system"] is None:
            provided["worlds_in_system"] = int(t)  # recorded verbatim; out of mainworld scope
        elif STELLAR_RE.match(t):
            provided["stellar"].append(t)
        elif t in KNOWN_TRADE:
            provided["trade_codes"].append(t)
        elif len(t) == 1 and tu in ("A", "R") and j > 0:
            provided["zone"] = tu  # amber/red travel zone
        elif len(tu) <= 2 and all(c in BASE_LETTERS for c in tu) and tu.isalpha() and t.isupper():
            provided["bases"].extend(list(tu))
        elif TRADE_RE.match(t) and provided["allegiance"] is None:
            provided["allegiance"] = t
        elif t.isalpha() and 2 <= len(t) <= 4 and provided["allegiance"] is None:
            provided["allegiance"] = t
        else:
            provided["unparsed"].append(t)
    if provided["unparsed"]:
        notes.append("Unrecognised tokens kept verbatim: " + " ".join(provided["unparsed"]))
    if post:
        notes.append("Extension parsing is best-effort; treat 'provided' fields as canon and correct manually if misread.")
    return hex_, name, uwp, provided, notes


# ---------------------------------------------------------------- seeding

def canonical_id(hex_, name, uwp):
    return "{}|{}|{}".format(hex_ or "----", (name or "UNNAMED").upper(), uwp)


def rng_for(canon, category):
    h = hashlib.sha256((canon + "|" + category).encode("utf-8")).hexdigest()
    return random.Random(int(h, 16))


# ---------------------------------------------------------------- static tables

STARPORT = {
    "A": "Excellent - refined fuel, full shipyard, highport",
    "B": "Good - refined fuel, spacecraft yards, annual maintenance",
    "C": "Routine - unrefined fuel, major repairs, modest highport at pop 6+",
    "D": "Poor - unrefined fuel, limited repair facilities",
    "E": "Frontier - a marked landing area and little else",
    "X": "None - no port; landing at your own risk",
}

ATMO = {
    0: ("None (vacuum)", "vacc suit required"),
    1: ("Trace", "vacc suit required"),
    2: ("Very thin, tainted", "respirator + filter"),
    3: ("Very thin", "respirator"),
    4: ("Thin, tainted", "filter mask"),
    5: ("Thin", "breathable"),
    6: ("Standard", "breathable"),
    7: ("Standard, tainted", "filter mask"),
    8: ("Dense", "breathable"),
    9: ("Dense, tainted", "filter mask"),
    10: ("Exotic", "air supply required"),
    11: ("Corrosive", "protective suit, hostile environment"),
    12: ("Insidious", "sealed hostile-environment suit; defeats protection over time"),
    13: ("Dense, high", "breathable at altitude"),
    14: ("Thin, low", "breathable in lowlands/canyons"),
    15: ("Unusual", "varies - see dossier"),
}

GOV = {
    0: "None / family-clan bonds", 1: "Company or corporation",
    2: "Participating democracy", 3: "Self-perpetuating oligarchy",
    4: "Representative democracy", 5: "Feudal technocracy",
    6: "Captive government / colony", 7: "Balkanization",
    8: "Civil service bureaucracy", 9: "Impersonal bureaucracy",
    10: "Charismatic dictator", 11: "Non-charismatic leader",
    12: "Charismatic oligarchy", 13: "Religious dictatorship",
    14: "Religious autocracy", 15: "Totalitarian oligarchy",
}

LAW = {
    0: "No restrictions - anything goes, including nukes in principle",
    1: "Only WMD and battle dress prohibited",
    2: "Portable energy weapons prohibited",
    3: "Military weapons (automatics, heavy) prohibited",
    4: "Light assault weapons and submachine guns prohibited",
    5: "Personal concealable firearms prohibited",
    6: "All firearms except shotguns prohibited; carrying discouraged",
    7: "Shotguns prohibited",
    8: "All bladed weapons and stunners prohibited",
    9: "Any weapon outside the home prohibited",
}

TL_BAND = [
    (0, 0, "Stone age"), (1, 3, "Pre-industrial (bronze to steam)"),
    (4, 6, "Industrial (radio, atomics, rocketry)"),
    (7, 9, "Pre-stellar (early space, fusion, first jump drives)"),
    (10, 11, "Early stellar (established interstellar tech)"),
    (12, 14, "Average stellar (grav vehicles, weather control)"),
    (15, 17, "High stellar (cutting edge of Charted Space)"),
    (18, 99, "Beyond the imperial maximum - anomalous"),
]

SIZE_G = {0: "microgravity (0.00-0.01g)", 1: "0.05g", 2: "0.15g", 3: "0.25g",
          4: "0.35g", 5: "0.45g", 6: "0.70g", 7: "0.90g", 8: "1.00g",
          9: "1.25g", 10: "1.40g", 11: "1.60g", 12: "2.00g",
          13: "2.3g", 14: "2.6g", 15: "3.0g"}

CULTURE_QUIRKS = [
    "gifts must be refused twice before acceptance",
    "eye contact with strangers is a challenge; smoked visors are polite wear",
    "meals are eaten in silence; conversation happens before and after",
    "personal names are private - everyone goes by profession or nickname",
    "debts are heritable and meticulously tracked across generations",
    "the dead are recycled into the ecosystem; graves are considered obscene",
    "tattoos record career history; a bare arm marks a nobody or a liar",
    "hospitality law is sacred - a guest, once fed, cannot be harmed or robbed",
    "timekeeping is tidal/seasonal, not clock-based; appointments are approximate",
    "haggling is theatre and skipping it is deeply rude",
    "offworlders are called by the name of their ship, not their own",
    "public argument is a spectator sport with formal rules and betting",
    "music is the marker of status; the wealthy commission personal anthems",
    "veils/masks are worn in public; faces are for family",
    "sworn friendship is a legal contract stronger than marriage",
    "children are raised communally; asking who a child's parents are is crass",
    "weapons are worn openly as jewellery, elaborately peace-bonded",
    "silence is the highest compliment; applause is for mediocrity",
    "every home keeps a shrine to the first settlers; guests bow to it on entry",
    "food is never sold - it is gifted, and the gift is repaid in kind or in favour",
    "age is counted in local great-years, so everyone quotes alarmingly low numbers",
    "the left hand is for dirty work; offering it is an insult",
    "bureaucratic stamps are collected and displayed like trophies",
    "lying to an outsider is a sport; lying to kin is unforgivable",
    "hair length/colour signals caste, mood or allegiance - visitors misread it constantly",
    "all contracts are oral, memorised by professional witnesses",
    "sport rivalries structure politics; ask someone's team before their party",
    "clothing must show at least one repaired patch - visible mending is virtue",
    "names are traded, borrowed and sold; identity is more fluid than the law likes",
    "sunset (or shift-change) is marked by a planet-wide moment of stillness",
]

WEIRD = [
    "a perfectly circular sea/crater that predates known settlement",
    "radio ghosts: old transmissions replay on calm nights, source unknown",
    "the ruins of a failed prior colony nobody's records mention",
    "a native organism that mimics human voices with unsettling accuracy",
    "gravity anomalies in one region strong enough to matter to pilots",
    "an ancient orbital debris ring - someone fought here once",
    "seasonal auroras bright enough to read by, tied to local folklore",
    "a mineral found nowhere else, prized offworld, cursed locally",
    "clocks drift here - tiny, measurable, unexplained",
    "megafauna migration routes that all commerce respectfully detours around",
    "a sealed vault/door from the first landing that no one has opened",
    "the water tastes wrong to newcomers for exactly nine days",
    "a hermit settlement that trades fairly but refuses all conversation",
    "star patterns locals swear differ from what charts say should be visible",
    "abandoned terraforming machinery, still humming, no maintainer on record",
    "a low-grade psionic hum reported by sensitive visitors; locals deny everything",
    "lightning storms that strike the same three places every time",
    "an annual 'quiet plague' - a week when everyone sleeps ten hours extra",
    "cave systems mapped to 40km depth without finding a bottom",
    "a language isolate spoken in one valley, related to nothing",
    "salvage keeps washing up/surfacing that matches no registered hull",
    "the founder's ship, enshrined, is of a make no database identifies",
    "birds (or the local equivalent) here sing in what sounds like Morse",
    "one moonless night per year the tides come anyway",
]

PATRONS = ["a minor noble with appearances to keep up", "a scout service contact (semi-official)",
           "a free trader captain in over their head", "a mid-level port official with a side interest",
           "a criminal broker who pays well and asks no questions", "a corporate factor from offworld",
           "an academic with a grant and no field experience", "a dissident who claims to speak for many",
           "a retired mercenary turned fixer", "a religious functionary with discreet needs",
           "a naval intelligence officer (unacknowledged)", "a wealthy local with an inheritance dispute"]

NEEDS = ["retrieve something from a place people avoid", "escort a person who is less innocent than claimed",
         "survey a region the government says is empty", "carry cargo that must not be scanned",
         "investigate a disappearance the authorities closed quickly", "deliver a message that cannot be transmitted",
         "quietly ruin a rival's shipment or reputation", "guard a meeting both sides expect to go wrong",
         "recover a debt from someone under another faction's protection", "smuggle a person off-planet ahead of an arrest",
         "authenticate (or fake) a claim about the world's past", "break a blockade of red tape - or of ships"]

COMPLICATIONS = ["a rival crew has the same brief and a head start", "local law takes an interest at the worst moment",
                 "the job crosses a faction boundary nobody mentioned", "weather/environment turns the timetable into fiction",
                 "it's a test - the real job is offered only if this goes well", "the objective is not what the patron said it was",
                 "payment is contingent on silence that gets harder to keep", "an informer inside the patron's circle is selling the details",
                 "the opposition would rather negotiate - which is somehow worse", "success will make the news, and the crew infamous"]

LOCATIONS = [
    # (requirement lambda name, text). req takes facts dict f.
    ("any", "the Founders' Landing - preserved first-settlement site, part shrine, part tourist trap"),
    ("any", "a black-market bazaar operating at a polite distance from the port gate"),
    ("any", "the Registry - where every claim, deed and grudge on the planet is filed"),
    ("hydro5", "a drowned city/structure visible from orbit at low tide"),
    ("hydro5", "storm-harvester platforms riding the open ocean, crewed by hard people"),
    ("hydroA", "the only dry land: volcanic islets crowded with everything that matters"),
    ("hydro0", "a canyon deep enough to hold its own weather and its own settlements"),
    ("hydro0", "the ice mines / aquifer heads - whoever holds them holds the world"),
    ("sealed", "the Old Dome - breached decades ago, sealed off, never demolished, allegedly empty"),
    ("sealed", "an airlock graveyard where retired hab modules go to be stripped"),
    ("open", "highland monasteries/retreats above the weather, jealous of their solitude"),
    ("open", "a rewilded zone where the terraform baseline is kept pure - entry licensed"),
    ("cold", "geothermal vent towns strung along the one warm fault line"),
    ("hot", "night-markets that only open when the temperature drops to survivable"),
    ("hipop", "arcology stacks so dense they have their own weather and their own laws"),
    ("hipop", "the Underlevels - officially service infrastructure, unofficially a second city"),
    ("lopop", "a single settlement where everyone genuinely does know everyone"),
    ("lopop", "an automated installation that outnumbers its keepers a thousand to one"),
    ("hiport", "the Highport Strip - extraterritorial, glittering, and full of bad ideas"),
    ("loport", "the crash line - a century of hulks that landed badly, picked half-clean"),
    ("hitech", "a fabrication commons where TL wonders are printed while you wait"),
    ("lotech", "the Relic Yard - imported machines kept running by rote and reverence"),
    ("hilaw", "Processing - the arrival compound every visitor remembers unfondly"),
    ("lolaw", "a duelling ground with posted etiquette and a long memorial wall"),
    ("balk", "the Neutral Strip between rival states - free, feral and profitable"),
    ("any", "a wayhouse where crews of every flag drink under a strict truce"),
    ("any", "the beacon hill/antenna farm - the planet's one thread to the sky lanes"),
    ("asteroid", "spin-section habitats threaded through the rock like wormholes"),
    ("asteroid", "the Docks - more tonnage in salvage than the belt ever shipped in ore"),
    ("any", "a quarantine annex, currently empty, maintained with suspicious diligence"),
]

ANOMALY_RULES = [
    ("crowded_rock", lambda f: f["pop"] >= 9 and f["size"] <= 3,
     "A billion-plus people on a body this small demands an explanation.",
     ["deep warren-cities bored down toward the core over centuries",
      "it is the habitable anchor of a polity whose wealth lies elsewhere - people followed the money",
      "refugee waves from a nearby disaster settled and never left",
      "a corporate hiring boom snowballed into permanence"]),
    ("sealed_masses", lambda f: f["pop"] >= 8 and f["atmo"] in (0, 1, 10, 11, 12),
     "Huge population under seal - why settle here at all?",
     ["mineral or exotic wealth that pays for every litre of air",
      "strategic position on a trade or military lane",
      "a religious or ideological founding that outgrew its founders",
      "it was habitable once; the atmosphere failed after settlement"]),
    ("anarchy_scale", lambda f: f["gov"] == 0 and f["pop"] >= 7,
     "Tens of millions with no government on paper.",
     ["clan-web mediation handles what states elsewhere do, mostly",
      "corporate arbitration courts fill the vacuum for anyone who pays",
      "a dozen informal authorities exist; none admits to being a government",
      "the census is honest and the chaos is real - visitors should be too"]),
    ("locked_port", lambda f: f["law"] >= 9 and f["port"] in ("A", "B"),
     "A first-rate port inside a police state - friction guaranteed.",
     ["the port is an extraterritorial bubble; the gate is the true border",
      "trade is the regime's lifeline, so spacers get one carefully policed district",
      "an offworld authority runs the port over local objections"]),
    ("preind_masses", lambda f: f["tl"] <= 4 and f["pop"] >= 8,
     "Hundreds of millions at pre-industrial tech.",
     ["a collapsed higher culture - the ruins are better than the workshops",
      "deliberate tech limitation by law, faith or treaty",
      "imported goods sustain an elite; the masses farm as they always have"]),
    ("dry_millions", lambda f: f["hydro"] == 0 and f["pop"] >= 6,
     "Millions with no surface water.",
     ["polar/subsurface ice mining on an industrial scale",
      "deep aquifers, jealously guarded and slowly falling",
      "closed-loop recycling so total that water is currency"]),
    ("silent_world", lambda f: f["port"] == "X",
     "No port at all - the silence is the story.",
     ["interdiction: someone with ships wants this world left alone",
      "the locals refuse contact and have made that stick",
      "collapse: there is no one left to run a port - probably"]),
    ("big_port_nobody", lambda f: f["port"] == "A" and f["pop"] <= 3,
     "An excellent port serving almost no one.",
     ["a pure transit/refuelling hub - the world is the port's afterthought",
      "corporate or naval investment ahead of a planned expansion",
      "it served a population that has since gone, and momentum keeps it lit"]),
    ("abandoned", lambda f: f["pop"] == 0,
     "The world is empty - but worlds rarely start that way.",
     ["never settled: surveyed, claimed, and left on a shelf",
      "evacuated in living memory; the reason is on file and disputed",
      "failed colony - the hardware is still there",
      "the population left no records and no forwarding address"]),
]

GEOGRAPHY = {
    "asteroid": ["tumbling rubble-pile geography of spurs, voids and tethered rock",
                 "a cratered iron-nickel surface scarred by mining benches",
                 "slow-spin plains of regolith broken by insertion shafts"],
    "desert": ["rust-red erg seas and wind-carved yardangs", "salt flats that mirage into false oceans",
               "basalt plains cut by ancient, bone-dry river channels", "dune oceans banked against black mesas"],
    "dry": ["steppe and scrubland bleeding into true desert at the equator",
            "great salt lakes that double in size each brief wet season",
            "canyon-lands where all the water and all the people hide"],
    "mixed": ["broad continents with mountain spines and generous river plains",
              "two major landmasses locked in a slow tectonic embrace",
              "a single supercontinent with a brutal dry interior and green coasts"],
    "archipelago": ["island chains strung along volcanic arcs", "drowned continents showing only their highlands",
                    "a world of straits, ferries and ten thousand harbours"],
    "ocean": ["a world-sea unbroken except for reefs and platforms",
              "storm belts that circle the globe unimpeded by land"],
    "ice": ["ice sheets kilometres thick over three-quarters of the surface",
            "a frozen ocean whose pressure ridges make mountains"],
}

SETTLE_SEALED = ["pressure domes clustered like soap bubbles around the port",
                 "warrens dug deep, with the surface reserved for industry and antennas",
                 "sealed arcology towers linked by tube-trains, backs to the wind"]
SETTLE_OPEN_LO = ["a single main settlement and a scatter of homesteads within a day's drive",
                  "one port town; everything else is wilderness with opinions"]
SETTLE_OPEN_MID = ["a handful of proper cities along the best coast/valley, thinning fast inland",
                   "market towns strung along the rail/river corridors between two modest cities"]
SETTLE_OPEN_HI = ["dense conurbations sprawling into each other along every temperate coast",
                  "a planet of cities - agriculture happens in towers and vats"]

LANG_STYLES = [
    ("clipped", ["k", "t", "s", "d", "n", "r", "v", "z", "br", "kr", "st", "dr"], ["a", "e", "i", "o", "u", "ai"], ["n", "r", "k", "s", "th", ""]),
    ("flowing", ["m", "l", "n", "s", "y", "w", "h", "sh", "th", ""], ["a", "e", "ia", "o", "ei", "ua"], ["l", "n", "m", "", "", ""]),
    ("guttural", ["g", "kh", "b", "d", "gr", "zh", "k", "v"], ["a", "o", "u", "au", "e"], ["g", "kh", "rn", "d", "z", ""]),
    ("sibilant", ["s", "sh", "z", "ts", "x", "f", "th", "sk"], ["i", "e", "a", "ii", "ae"], ["ss", "x", "sh", "n", "", ""]),
]


# ---------------------------------------------------------------- generation

def make_name(rng, style, syllables=None):
    onsets, vowels, codas = style[1], style[2], style[3]
    n = syllables or rng.randint(2, 3)
    parts = []
    for i in range(n):
        parts.append(rng.choice(onsets) + rng.choice(vowels))
    word = "".join(parts) + rng.choice(codas)
    return word.capitalize()


def human_pop(mult, exp):
    if exp == 0:
        return "0"
    val = mult * (10 ** exp)
    for cut, label in ((10 ** 9, "billion"), (10 ** 6, "million"), (10 ** 3, "thousand")):
        if val >= cut:
            q = val / cut
            return ("{:.0f} {}" if q >= 10 else "{:.1f} {}").format(q, label)
    return str(val)


def generate(hex_, name, uwp, provided, notes):
    m = UWP_RE.match(uwp)
    port = m.group(1)
    size, atmo, hydro, pop, gov, law = (hv(m.group(i)) for i in range(2, 8))
    tl = hv(m.group(8))
    canon = canonical_id(hex_, name, uwp)
    f = {"port": port, "size": size, "atmo": atmo, "hydro": hydro,
         "pop": pop, "gov": gov, "law": law, "tl": tl}

    # ---- derived (pure lookup, no dice)
    computed_codes = []
    def add(code, cond):
        if cond:
            computed_codes.append(code)
    add("Ag", 4 <= atmo <= 9 and 4 <= hydro <= 8 and 5 <= pop <= 7)
    add("As", size == 0 and atmo == 0 and hydro == 0)
    add("Ba", pop == 0 and gov == 0 and law == 0)
    add("De", atmo >= 2 and hydro == 0)
    add("Fl", atmo >= 10 and hydro >= 1)
    add("Ga", 6 <= size <= 8 and atmo in (5, 6, 8) and 5 <= hydro <= 7)
    add("Hi", pop >= 9)
    add("Ht", tl >= 12)
    add("Ic", atmo <= 1 and hydro >= 1)
    add("In", atmo in (0, 1, 2, 4, 7, 9, 10, 11, 12) and pop >= 9)
    add("Lo", 1 <= pop <= 3)
    add("Lt", pop >= 1 and tl <= 5)
    add("Na", atmo <= 3 and hydro <= 3 and pop >= 6)
    add("Ni", 4 <= pop <= 6)
    add("Po", 2 <= atmo <= 5 and hydro <= 3)
    add("Ri", atmo in (6, 8) and 6 <= pop <= 8)
    add("Va", atmo == 0)
    add("Wa", hydro >= 10)

    tl_desc = next(d for lo, hi, d in TL_BAND if lo <= tl <= hi)
    law_desc = LAW.get(law, "Rigid control of civilian movement and all technology; a police state by any measure")

    # ---- population multiplier: PBG digit if provided, else seeded
    if provided.get("pbg"):
        mult = max(1, int(provided["pbg"][0])) if pop > 0 else 0
        mult_src = "PBG"
    else:
        mult = rng_for(canon, "popmult").randint(1, 9) if pop > 0 else 0
        mult_src = "seeded"

    # ---- physical (seeded)
    r = rng_for(canon, "temperature")
    if atmo <= 1:
        temp = "extreme swings between day and night (no insulating atmosphere)"
    else:
        mod = {2: -2, 3: -2, 4: -1, 5: -1, 14: -1, 8: 1, 9: 1, 10: 2, 13: 2, 15: 2, 11: 6, 12: 6}.get(atmo, 0)
        roll = r.randint(1, 6) + r.randint(1, 6) + mod
        temp = ("frozen" if roll <= 2 else "cold" if roll <= 4 else
                "temperate" if roll <= 9 else "hot" if roll <= 11 else "boiling")
    r = rng_for(canon, "rotation")
    day_h = round(10 + r.randint(2, 20) + r.randint(2, 20) * 0.5, 1)
    year_y = round(0.2 + r.randint(1, 100) / 33.0, 2)
    tilt = r.randint(0, 45)

    r = rng_for(canon, "geography")
    if size == 0:
        geo_key = "asteroid"
    elif hydro == 0:
        geo_key = "desert" if atmo >= 2 else "asteroid" if size <= 1 else "desert"
    elif hydro <= 3:
        geo_key = "dry"
    elif hydro <= 7:
        geo_key = "mixed"
    elif hydro <= 9:
        geo_key = "archipelago"
    else:
        geo_key = "ocean"
    if temp == "frozen" and hydro >= 2:
        geo_key = "ice"
    motifs = r.sample(GEOGRAPHY[geo_key], min(2, len(GEOGRAPHY[geo_key])))

    # ---- society (seeded)
    sealed = atmo in (0, 1, 10, 11, 12) or size == 0
    r = rng_for(canon, "settlement")
    if pop == 0:
        settlement = "none - see anomalies"
    elif sealed:
        settlement = r.choice(SETTLE_SEALED)
    elif pop <= 3:
        settlement = r.choice(SETTLE_OPEN_LO)
    elif pop <= 6:
        settlement = r.choice(SETTLE_OPEN_MID)
    elif pop <= 8:
        settlement = r.choice(SETTLE_OPEN_MID) + "; the largest is a true city"
    else:
        settlement = r.choice(SETTLE_OPEN_HI)

    gov_char = rng_for(canon, "flavour:gov").choice(tables.clamp_pick(tables.GOV_FLAVOUR, gov)) if pop > 0 else None
    law_char = rng_for(canon, "flavour:law").choice(tables.clamp_pick(tables.LAW_FLAVOUR, law)) if pop > 0 else None
    port_scene = rng_for(canon, "flavour:port").choice(tables.PORT_FLAVOUR[port])
    size_fl = rng_for(canon, "flavour:size").choice(tables.clamp_pick(tables.SIZE_FLAVOUR, size))
    atmo_fl = rng_for(canon, "flavour:atmo").choice(tables.clamp_pick(tables.ATMO_FLAVOUR, atmo))
    hydro_fl = rng_for(canon, "flavour:hydro").choice(tables.clamp_pick(tables.HYDRO_FLAVOUR, hydro))
    pop_fl = rng_for(canon, "flavour:pop").choice(tables.clamp_pick(tables.POP_FLAVOUR, pop))
    tl_fl = rng_for(canon, "flavour:tl").choice(tables.clamp_pick(tables.TL_FLAVOUR, tl))

    # ---- names (seeded; generate a stable pool, then slice)
    style = rng_for(canon, "language").choice(LANG_STYLES)
    r = rng_for(canon, "names")
    pool = [make_name(r, style) for _ in range(16)]
    settlements = pool[0:4] if pop > 0 else []
    people = ["{} {}".format(pool[i], pool[i + 1]) for i in (4, 6, 8)] if pop > 0 else []

    # ---- factions (seeded)
    factions = []
    if pop >= 3:
        r = rng_for(canon, "factions")
        count = r.randint(1, 3) + (2 if gov == 7 else 0)
        ftypes = ["ruling-elite splinter", "commercial cartel", "popular movement",
                  "offworld-backed interest", "criminal network", "religious current",
                  "military/veteran bloc", "separatist region", "labour combine", "tech guild"]
        fgoals = ["capture the next succession/election", "control the port and its revenue",
                  "force (or block) offworld investment", "win autonomy for its region or class",
                  "suppress a rival before it grows", "change the law that keeps it illegal",
                  "protect a monopoly nobody admits exists", "avenge or reverse a historic defeat"]
        chosen_t = r.sample(ftypes, min(count, len(ftypes)))
        for i in range(count):
            factions.append({
                "name": "the {}".format(pool[10 + (i % 5)]),
                "type": chosen_t[i % len(chosen_t)],
                "agenda": r.choice(fgoals),
                "strength": r.choice(["marginal", "rising", "established", "dominant in its sphere"]),
            })

    # ---- culture, locations, hooks, weirdness (seeded)
    quirks = rng_for(canon, "culture").sample(CULTURE_QUIRKS, 2) if pop > 0 else []

    def loc_ok(tag):
        return {"any": True, "hydro5": hydro >= 5, "hydroA": hydro >= 10, "hydro0": hydro == 0,
                "sealed": sealed, "open": not sealed and pop > 0, "cold": temp in ("cold", "frozen"),
                "hot": temp in ("hot", "boiling"), "hipop": pop >= 8, "lopop": 1 <= pop <= 4,
                "hiport": port in ("A", "B"), "loport": port in ("D", "E", "X"),
                "hitech": tl >= 12, "lotech": tl <= 5, "hilaw": law >= 7, "lolaw": law <= 1,
                "balk": gov == 7, "asteroid": size == 0}.get(tag, False)
    eligible = [txt for tag, txt in LOCATIONS if loc_ok(tag)]
    locations = rng_for(canon, "locations").sample(eligible, min(3, len(eligible)))

    r = rng_for(canon, "hooks")
    pats = r.sample(PATRONS, 3)
    hooks = [{"patron": pats[i], "job": r.choice(NEEDS), "complication": r.choice(COMPLICATIONS)}
             for i in range(3)]
    weird = rng_for(canon, "weird").choice(WEIRD)

    # ---- anomalies / tensions (seeded per rule)
    anomalies = []
    for key, cond, question, answers in ANOMALY_RULES:
        if cond(f):
            pick = rng_for(canon, "anomaly:" + key).choice(answers)
            anomalies.append({"tension": question, "explanation": pick})

    mismatches = []
    if provided["trade_codes"]:
        core = {"Ag", "As", "Ba", "De", "Fl", "Ga", "Hi", "Ht", "Ic", "In", "Lo",
                "Lt", "Na", "Ni", "Po", "Ri", "Va", "Wa"}
        given_core = set(provided["trade_codes"]) & core
        mismatches = sorted(given_core.symmetric_difference(set(computed_codes)))

    return {
        "identity": {
            "hex": hex_, "name": name, "uwp": uwp,
            "canonical": canon,
            "seed": hashlib.sha256(canon.encode()).hexdigest()[:16],
        },
        "parse_notes": notes,
        "provided_extensions": provided,
        "derived": {
            "starport": {"class": port, "meaning": STARPORT[port], "flavour": port_scene},
            "size": {"code": size, "diameter_km": size * 1600 if size else "under 800",
                     "gravity": SIZE_G.get(size, "high"), "flavour": size_fl},
            "atmosphere": {"code": atmo, "type": ATMO[atmo][0], "survival": ATMO[atmo][1], "flavour": atmo_fl},
            "hydrographics": {"code": hydro, "surface_water_pct": "{}-{}%".format(max(hydro * 10 - 5, 0), min(hydro * 10 + 5, 100)), "flavour": hydro_fl},
            "population": {"code": pop, "multiplier": mult, "multiplier_source": mult_src,
                           "approx": human_pop(mult, pop), "flavour": pop_fl},
            "government": {"code": gov, "type": GOV[gov], "flavour": gov_char},
            "law": {"code": law, "restrictions": law_desc, "flavour": law_char},
            "tech": {"code": tl, "band": tl_desc, "flavour": tl_fl},
            "trade_codes_computed": computed_codes,
            "trade_code_mismatches_vs_provided": mismatches,
        },
        "physical": {
            "climate": temp, "day_length_hours": day_h, "year_length_std_years": year_y,
            "axial_tilt_deg": tilt, "geography": motifs,
        },
        "society": {
            "settlement_pattern": settlement, "government_character": gov_char,
            "law_character": law_char, "starport_scene": port_scene,
            "factions": factions, "culture_quirks": quirks,
        },
        "colour": {
            "notable_locations": locations, "patron_hooks": hooks,
            "one_weird_thing": weird,
        },
        "anomalies": anomalies,
        "names": {
            "language_flavour": style[0],
            "settlements": settlements, "people": people,
        },
        "scope_note": "Mainworld only. No stars, moons, belts or other system bodies are implied.",
    }


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    text = " ".join(sys.argv[1:])
    hex_, name, uwp, provided, notes = parse_line(text)
    print(json.dumps(generate(hex_, name, uwp, provided, notes), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
