"""Fitment transcribed from owner's manuals opened on 16 Nov 2026.

Each value is what that edition prints. Where a chart lists more than one
lamp package, both are included. Inch lengths are included only when the
manual prints them. Motorcraft part numbers are included only as printed.
"""
from config import PUBLISHED

NHTSA = "https://www.nhtsa.gov/recalls"

def V(make, model, year, nhtsa, fitment, sources, note=""):
    return {
        "make": make,
        "model": model,
        "year": str(year),
        "nhtsa": nhtsa,  # list of (make, model) strings as NHTSA spells them
        "fitment": fitment,  # list of (part_key, label, value)
        "sources": sources,  # list of (title, url, publisher, date, note)
        "note": note,
        "published": PUBLISHED,
        "modified": PUBLISHED,
    }

# part keys: key, wiper, rear, head, brake, turn
F150_2018 = V(
    "Ford", "F-150", 2018, [("ford", "F-150")],
    [
        ("key", "Key fob battery", "Integrated keyhead transmitter: one CR2032, or equivalent. Intelligent Access key: one CR2450, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft parts tables print windshield wiper blade WW-2242 and, in another table, WW-2247. The manual does not print an inch length or say which table is which cab."),
        ("rear", "Rear wiper", "No rear wiper part is printed in the Motorcraft parts tables we read."),
        ("head", "Headlight", "Low beam H11, 55 W. High beam 9005, 65 W. Daytime running lamps are LED."),
        ("brake", "Brake light", "Rear lamps, brake lamps, rear direction indicator and rear side marker lamps: 3157, 27/8 W. The chart says these may have optional LED lamps, which are not serviceable. Central high mounted brake lamp: 921, 16 W, or LED on vehicles with a cargo box lamp."),
        ("turn", "Turn signal", "Front direction indicator and parking lamps: 7444NA, 21/5 W. Side direction indicator: LED. Rear direction indicator is included in the 3157 rear lamp above."),
    ],
    [("2018 Ford F-150 Owner's Manual, third printing, February 2018",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2018-Ford-F-150-Owners-Manual_version-3_om_EN-US_EN-CA_01_2018_V3.pdf",
      "Ford Motor Company", "2018-02",
      "Remote battery in Keys and Remote Controls. Bulb Specification Chart. Motorcraft parts tables for the windshield wiper blade.")],
)
F150_2020 = V(
    "Ford", "F-150", 2020, [("ford", "F-150")],
    [
        ("key", "Key fob battery", "Integrated keyhead transmitter: one CR2032, or equivalent. Intelligent Access key: one CR2450, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft part WW-2248 for the windshield wiper blade, printed in the parts tables. The manual does not print an inch length."),
        ("rear", "Rear wiper", "No rear wiper part is printed in those parts tables."),
        ("head", "Headlight", "Low beam H11, 55 W. High beam 9005, 65 W. A separate row lists headlamps as LED. Daytime running lamps are LED."),
        ("brake", "Brake light", "Rear lamps, brake lamps, rear direction indicator and rear side marker lamps: 3157, 27/8 W. The chart says these may have optional LED lamps. Central high mount brake lamp and cargo box lamp: 912, 12.8 W, and the same note says they may be optional LED."),
        ("turn", "Turn signal", "Front direction indicator and parking lamps: 4257NA, 21/5 W. Side direction indicator: LED. Rear direction indicator is included in the 3157 rear lamp."),
    ],
    [("2020 Ford F-150 Owner's Manual, version 3, April 2020",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2020-Ford-F-150-Owners-Manual-version3_om_EN-US_04_2020.pdf",
      "Ford Motor Company", "2020-04",
      "Keys and Remote Controls for CR2032 and CR2450. Bulb Specification Chart. Motorcraft windshield wiper blade WW-2248.")],
)
F150_2022 = V(
    "Ford", "F-150", 2022, [("ford", "F-150")],
    [
        ("key", "Key fob battery", "One coin type 3 volt lithium battery. The manual prints CR2032 for one remote and CR2450 for the other."),
        ("wiper", "Front wiper", "Motorcraft part WW-2208 for the windshield wiper blade. No inch length is printed."),
        ("rear", "Rear wiper", "No rear wiper part is printed in the parts tables we read."),
        ("head", "Headlight", "Headlamp low beam on XL and some XLT trucks: H11, 55 W. High beam on those trucks: 9005, 65 W. Headlamps on Lariat, Platinum, King Ranch, Limited, and some XLT trucks: LED. Daytime running lamp is H11, 55 W, on XL and some XLT trucks, and LED on the higher trims."),
        ("brake", "Brake light", "Central high mounted stop lamp: 912, 16 W. Taillamp, all functions, on Lariat and higher trims: LED. Rear lamp, stop lamp, rear turn signal and rear side marker on XL optional and XLT: WT21W/7W, 21/7 W."),
        ("turn", "Turn signal", "Front turn signal and parking lamp: 4257NA, 21/5 W, on XL and some XLT trucks, and LED on higher trims. Rear turn on XL optional: WTY21W, 21 W. Side turn signal lamp: LED."),
    ],
    [("2022 Ford F-150 Owner's Manual, first printing, October 2021",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2022-Ford-F-150-Owners-Manual-version-1_om_EN-US_10_2021.pdf",
      "Ford Motor Company", "2021-10",
      "Remote battery sentences, exterior bulb chart, and Motorcraft wiper part WW-2208.")],
)
ESCAPE_2020 = V(
    "Ford", "Escape", 2020, [("ford", "ESCAPE")],
    [
        ("key", "Key fob battery", "Integrated keyhead transmitter: one CR2032, or equivalent. The intelligent access remote uses one CR2450, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft WW-2502 on the driver side and WW-2051 on the passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "Motorcraft WW-1112 for the rear window."),
        ("head", "Headlight", "Base headlamp low beam H9. Base headlamp high beam HB3. Optional headlamp is LED, and the chart says to see a dealer for that lamp."),
        ("brake", "Brake light", "Tail and brake lamp: LED, dealer service. High mount brake lamp: LED, dealer service."),
        ("turn", "Turn signal", "Base headlamp turn: T20 amber. Rear turn lamp: T20 amber. Base headlamp side marker: LED."),
    ],
    [("2020 Ford Escape gas, hybrid and plug in hybrid Owner's Manual, third printing, August 2020",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2020-Ford-Escape-Gas-HEV-PHEV-Owners-Manual-version-3_om_EN_08_2020.pdf",
      "Ford Motor Company", "2020-08",
      "Edition date 201906, third printing. Bulb Specification Chart and Motorcraft wiper parts. Vehicles built from 17 June 2019.")],
)
ESCAPE_2022 = V(
    "Ford", "Escape", 2022, [("ford", "ESCAPE")],
    [
        ("key", "Key fob battery", "The manual prints both a CR2032 remote and a CR2450 remote, each described as one coin type 3 volt lithium battery."),
        ("wiper", "Front wiper", "Motorcraft WW-2502 driver side and WW-2051 passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "Motorcraft WW-1112 for the rear window."),
        ("head", "Headlight", "Base headlamp low beam H9. Base headlamp high beam HB3. Optional headlamp is LED. Base fog lamp H8. Optional fog lamp is LED."),
        ("brake", "Brake light", "Tail and brake lamp: LED. High mount brake lamp: LED. The chart says to see a dealer for lamps marked that way."),
        ("turn", "Turn signal", "Base headlamp turn: T20 amber. Rear turn lamp: T20 amber. Base headlamp side marker: LED. Rear side marker: W5W."),
    ],
    [("2022 Ford Escape Owner's Manual, first printing, September 2021",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2022-Ford-Escape-Owners-Manual-version-1_om_EN-USA_09.2-2021.pdf",
      "Ford Motor Company", "2021-09",
      "Exterior Bulb Specification Chart and Motorcraft wiper parts.")],
)
RANGER_2023 = V(
    "Ford", "Ranger", 2023, [("ford", "RANGER")],
    [
        ("key", "Key fob battery", "A coin cell type was not printed in the remote section of the text we searched. Do not guess a size. Open the Keys and Remote Controls chapter in this edition."),
        ("wiper", "Front wiper", "Motorcraft WW-2615-A driver side and WW-1615-A passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "No rear wiper part is printed next to those windshield parts."),
        ("head", "Headlight", "Low beam H11LL, 55 W. High beam HB3LL, 60 W. A separate row lists headlamps as LED. Front fog lamp bulb H11, 55 W, and a separate row lists front fog lamps as LED."),
        ("brake", "Brake light", "Rear brake and park bulb: W21/5W, 21/5 W. Another row lists the rear direction, park and stop lamp as LED, and a 3157K bulb at 26.9 W for a rear direction, park and stop lamp."),
        ("turn", "Turn signal", "Front park and direction indicator, clear: W21/5W, 21/5 W. Amber front park and direction indicator: 7444NA. Rear direction indicator bulb: WY21W, 21 W. Front side marker bulb: 194, 3.78 W. License plate lamp: W5W, 5 W."),
    ],
    [("2023 Ford Ranger Owner's Manual, first printing, edition date 202208",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2023_Ford_Ranger_Owners_Manual_version_1_om_EN-US.pdf",
      "Ford Motor Company", "2022-08",
      "Canada and United States, vehicles built from 10 October 2022. Bulb Specification Chart and wiper parts WW-2615-A and WW-1615-A.")],
    note="The remote battery type was not in the passages we searched. The bulb chart and wiper parts were.",
)
FUSION_2020 = V(
    "Ford", "Fusion", 2020, [("ford", "FUSION")],
    [
        ("key", "Key fob battery", "A coin cell type was not printed in the passages we searched. Open the remote battery steps in this edition before you buy a cell."),
        ("wiper", "Front wiper", "Motorcraft WW-2601 driver side and WW-2700 passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "No rear wiper part is printed next to those windshield parts."),
        ("head", "Headlight", "High beam H9 if equipped, and a separate high beam row is LED. Low beam H11LL if equipped, and a separate low beam row is LED. Front fog lamp H8."),
        ("brake", "Brake light", "Tail and brake lamp, high series and low series: both rows are LED."),
        ("turn", "Turn signal", "Front direction indicator: PWY24W. Front side marker lamp: LED. Reverse lamp: 921."),
    ],
    [("2020 Ford Fusion Owner's Manual, second printing, November 2019",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2020-Ford-Fusion-Owners-Manual-version-2_om_EN-US_11_2019.pdf",
      "Ford Motor Company", "2019-11",
      "Bulb Specification Chart and Motorcraft wiper parts WW-2601 and WW-2700.")],
)
MUSTANG_2020 = V(
    "Ford", "Mustang", 2020, [("ford", "MUSTANG")],
    [
        ("key", "Key fob battery", "One CR2450, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft WW-2160 driver side and WW-1964 passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "No rear wiper part is printed. This is a coupe and convertible manual."),
        ("head", "Headlight", "The changing a bulb chapter says headlamps are LED and are not serviceable. It lists the same for the rear lamp, brake lamp, front fog lamp, front side marker, daytime running lamp, and central high mounted brake lamp."),
        ("brake", "Brake light", "Listed with the LED lamps that are not serviceable. See a dealer if one fails."),
        ("turn", "Turn signal", "Not given a separate trade number in the LED list we read. The reverse lamp is described as a bulb you can rotate out, but that procedure does not print a trade number."),
    ],
    [("2020 Ford Mustang Owner's Manual, second printing, December 2019",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2020-Ford-Mustang-Owners-Manual-version-2_om_EN-US_12_2019.pdf",
      "Ford Motor Company", "2019-12",
      "Edition date 201906. Remote battery CR2450. Wiper parts WW-2160 and WW-1964. LED lamp list in Changing a Bulb.")],
)
EXPEDITION_2020 = V(
    "Ford", "Expedition", 2020, [("ford", "EXPEDITION")],
    [
        ("key", "Key fob battery", "Integrated keyhead transmitter: one CR2032, or equivalent. Intelligent Access key: one CR2450, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft WW-2248 for the windshield wiper blade. No inch length is printed."),
        ("rear", "Rear wiper", "Motorcraft WW-1107 for the rear window wiper blade. No inch length is printed."),
        ("head", "Headlight", "Halogen low beam H11, 55 W. Halogen high beam HB3, 55 W. A separate row lists the LED headlamp. Halogen front fog lamp 9140, 55 W, and a separate LED fog lamp row."),
        ("brake", "Brake light", "Rear lamp, brake lamp and rear direction indicator: 3057K, 27 W, and a separate LED row for the same functions. Central high mounted brake lamp: LED."),
        ("turn", "Turn signal", "Front direction indicator: 7444NA. The watt cell in that row prints 5, which is the figure in the chart, not a guess. Side direction indicator: LED. Rear direction indicator is included in the 3057K or LED rear lamp."),
    ],
    [("2020 Ford Expedition Owner's Manual, first printing, September 2019",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2020-Ford-Expedition-Owners-Manual-version-1_om_EN-US_09_2019.pdf",
      "Ford Motor Company", "2019-09",
      "Bulb Specification Chart. Windshield wiper blade WW-2248 and rear window wiper blade WW-1107.")],
)
EDGE_2019 = V(
    "Ford", "Edge", 2019, [("ford", "EDGE")],
    [
        ("key", "Key fob battery", "A coin cell type was not printed in the passages we searched."),
        ("wiper", "Front wiper", "Motorcraft WW-2755 driver side and WW-2760 passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "Motorcraft WW-1414 for the rear window."),
        ("head", "Headlight", "Low beam H11LL, 55 W. High beam 9005LL, 55 W. High intensity discharge headlamps: D3S. Front signature lamp: LED."),
        ("brake", "Brake light", "The rows we read do not give a separate brake trade number. Reversing lamps are LED."),
        ("turn", "Turn signal", "Rear direction indicator: LED. Side direction indicator: LED. License plate lamp: W5W, 5 W."),
    ],
    [("2019 Ford Edge Owner's Manual, second printing, December 2018",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2019-Ford-Edge-Owner-Manual-version-2_om_EN-US_12_2018.pdf",
      "Ford Motor Company", "2018-12",
      "Bulb Specification Chart and wiper parts WW-2755, WW-2760, and WW-1414.")],
)
EDGE_2020 = V(
    "Ford", "Edge", 2020, [("ford", "EDGE")],
    [
        ("key", "Key fob battery", "Intelligent Access key: one CR2450, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft WW-2755 driver side and WW-2760 passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "Motorcraft WW-1414 for the rear window."),
        ("head", "Headlight", "Low beam H11LL, 55 W. High beam 9005LL, 55 W. High intensity discharge headlamps: D3S. Front signature lamp: LED."),
        ("brake", "Brake light", "Reversing lamps are LED. A separate brake trade number was not in the rows we read."),
        ("turn", "Turn signal", "Rear direction indicator: LED. Rear side marker: LED. Side direction indicator: LED. License plate lamp: W5W, 5 W."),
    ],
    [("2020 Ford Edge Owner's Manual, first printing, August 2019",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2020-Ford-Edge-Owner-Manual-version-1_om_EN-US_08_2019.pdf",
      "Ford Motor Company", "2019-08",
      "Bulb Specification Chart, CR2450 intelligent access key, and the same wiper part numbers as the 2019 book.")],
)
NAUTILUS_2020 = V(
    "Lincoln", "Nautilus", 2020, [("lincoln", "NAUTILUS")],
    [
        ("key", "Key fob battery", "One CR2450, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft WW-2350 driver side and WW-1750 passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "Motorcraft WW-1206 for the rear window."),
        ("head", "Headlight", "The bulb chart says all exterior lamps are LED and are not serviceable. See a dealer if one fails."),
        ("brake", "Brake light", "Included in the all LED exterior lamp note. No separate trade number is printed."),
        ("turn", "Turn signal", "Included in the all LED exterior lamp note. No separate trade number is printed."),
    ],
    [("2020 Lincoln Nautilus Owner's Manual, first printing, August 2019",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2020-Lincoln-Nautilus-Owners-Manual_version-1_om_EN-US_08_2019.pdf",
      "Ford Motor Company", "2019-09",
      "Lincoln is a Ford Motor Company brand. The manual is hosted on Ford's owner manual site. Bulb chart, CR2450, and wiper parts WW-2350, WW-1750, and WW-1206.")],
)
ESERIES_2021 = V(
    "Ford", "E-Series", 2021, [("ford", "E-350"), ("ford", "E-450")],
    [
        ("key", "Key fob battery", "One CR2032, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft WW-2005 for the windshield wiper blade. No inch length is printed."),
        ("rear", "Rear wiper", "No rear wiper part is printed next to WW-2005."),
        ("head", "Headlight", "Low beam and high beam are both listed as H13."),
        ("brake", "Brake light", "Brake, rear and direction indicator lamp: 3157K."),
        ("turn", "Turn signal", "Front direction indicator: 3157AK. Park lamp: 3157AK. Front side marker: W5W. Reversing lamps: 3156. Front clearance lamp on the exterior mirror: 2825."),
    ],
    [("2021 Ford E-Series Owner's Manual, first printing, December 2019",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2021-Ford-E-Series-Owners-Manual-version-1_om_EN-US_12_2019.pdf",
      "Ford Motor Company", "2019-12",
      "Bulb Specification Chart, CR2032, and windshield wiper blade WW-2005.")],
    note="NHTSA files this van under E-350 and E-450, not under one E-Series name. Recalls below are shown under those two model names.",
)
WRANGLER_2020 = V(
    "Jeep", "Wrangler", 2020, [("jeep", "WRANGLER")],
    [
        ("key", "Key fob battery", "CR2450."),
        ("wiper", "Front wiper", "An inch length or blade part number is not printed in the wiper chapter we read."),
        ("rear", "Rear wiper", "The manual describes rear wiper operation. It does not print a blade length in the section we read."),
        ("head", "Headlight", "Headlamps: H13. Premium head lamps: LED, serviced at a dealer."),
        ("brake", "Brake light", "Rear base tail lamp stop, tail and turn bulb: 3157. Center high mounted stop lamp: LED. Premium LED tail lamps: LED."),
        ("turn", "Turn signal", "Sport front park and turn: 7442NALL. Premium front park and turn: LED. Base Sahara and Rubicon turn lamp: 7440NA. Base park and daytime running lamp: 7443. Front side marker: LED."),
    ],
    [("2020 Jeep Wrangler Owner's Manual",
      "https://vehicleinfo.mopar.com/assets/publications/en-us/Jeep/2020/Wrangler/P123935_20_JL_OM_EN_USC_DIGITAL.pdf",
      "FCA US LLC", "2020",
      "Publication P123935. Bulb replacement table and CR2450.")],
)
WRANGLER_2024 = V(
    "Jeep", "Wrangler", 2024, [("jeep", "WRANGLER")],
    [
        ("key", "Key fob battery", "The recommended replacement battery is CR2450."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Headlamps: H13. Premium head lamps: LED."),
        ("brake", "Brake light", "Rear base tail lamp stop, tail and turn bulb: 3157. Center high mounted stop lamp: LED. Premium LED tail lamps: LED."),
        ("turn", "Turn signal", "Sport front park and turn: 7444NALL. Premium front park and turn: LED. Base Sahara and Rubicon turn lamp: 7440NALL or WY21WLL. Base park and daytime running lamp: 7443LL. Front side marker: LED. Base fog lamps: PSX24W. Premium fog lamps: LED."),
    ],
    [("2024 Jeep Wrangler Owner's Manual",
      "https://vehicleinfo.mopar.com/assets/publications/en-us/Jeep/2024/Wrangler/100576_24_JL_OM_EN_USC_DIGITAL.pdf",
      "FCA US LLC", "2024",
      "Publication 100576. Bulb replacement table and CR2450.")],
)
WRANGLER_2026 = V(
    "Jeep", "Wrangler", 2026, [("jeep", "WRANGLER")],
    [
        ("key", "Key fob battery", "The recommended replacement battery is CR2450."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Headlamps: H13. Premium head lamps: LED. The manual says to see a dealer for LED replacement."),
        ("brake", "Brake light", "Rear base tail lamp stop, tail and turn: 3157. Center high mounted stop lamp: LED. License lamp: LED. Premium LED tail lamps: LED."),
        ("turn", "Turn signal", "Sport front park and turn: 7444NALL. Premium front park and turn: LED. Base Sahara and Rubicon turn lamp: 7440NALL or WY21WLL. Base park and daytime running lamp: 7443LL. Rear base backup bulb: 7440. Base fog lamps: PSX24W."),
    ],
    [("2026 Jeep Wrangler Owner's Manual, edition E1",
      "https://vehicleinfo.mopar.com/assets/publications/en-us-ca/2026/Jeep/Wrangler/102316_26_JL_OM_EN_USC_DIGITAL_E1.pdf",
      "FCA US LLC", "2026",
      "Publication 102316. Bulb table and CR2450.")],
)
CHEROKEE_2023 = V(
    "Jeep", "Cherokee", 2023, [("jeep", "CHEROKEE")],
    [
        ("key", "Key fob battery", "One CR2032."),
        ("wiper", "Front wiper", "An inch length is not printed in the section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the section we read."),
        ("head", "Headlight", "Low beam and high beam headlamps: LED."),
        ("brake", "Brake light", "Rear tail and stop lamps: LED. Center high mounted stop lamp: LED."),
        ("turn", "Turn signal", "Front park and daytime running lamps, front turn signal lamps, and rear turn signal lamps: LED. Back up lamps: W21W. License plate lamp: LED. Front fog lamps: LED."),
    ],
    [("2023 Jeep Cherokee Owner's Manual",
      "https://vehicleinfo.mopar.com/assets/publications/en-us/Jeep/2023/Cherokee/P133074_23_KL_OM_EN_USC_DIGITAL.pdf",
      "FCA US LLC", "2023",
      "Publication P133074. Exterior bulb table and CR2032.")],
)
GRAND_2025 = V(
    "Jeep", "Grand Cherokee", 2025, [("jeep", "GRAND CHEROKEE")],
    [
        ("key", "Key fob battery", "One CR2450."),
        ("wiper", "Front wiper", "An inch length is not printed in the section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the section we read."),
        ("head", "Headlight", "The manual says the exterior lights are LED. See a dealer for replacement."),
        ("brake", "Brake light", "Included in the exterior LED statement. No trade number is printed."),
        ("turn", "Turn signal", "Included in the exterior LED statement. No trade number is printed."),
    ],
    [("2025 Jeep Grand Cherokee and Grand Cherokee L Owner's Manual, edition E4",
      "https://vehicleinfo.mopar.com/assets/publications/en-us/Jeep/2025/Grand_Cherokee/106039_45_WL_OM_EN_USC_DIGITAL_E4.pdf",
      "FCA US LLC", "2025",
      "Publication 106039. Exterior bulbs paragraph and CR2450.")],
    note="The same book covers Grand Cherokee and Grand Cherokee L. NHTSA model name used here is GRAND CHEROKEE.",
)
RAM_2020 = V(
    "Ram", "1500", 2020, [("ram", "1500")],
    [
        ("key", "Key fob battery", "One CR2450."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "No rear wiper length is printed. This is a pickup."),
        ("head", "Headlight", "Halogen reflector low beam: H11LL. Halogen reflector high beam: 9005LL. LED reflector and LED projector headlamps: LED, serviced at a dealer."),
        ("brake", "Brake light", "Base rear tail, turn and stop lamp: 7440LL or W21WLL. Premium rear lamp: LED. Center high mounted stop lamp: 921."),
        ("turn", "Turn signal", "Turn signal and front position on the halogen reflector headlamp: 7444NA. The LED headlamp version of that lamp is dealer serviced. Base turn lamp: 7440NA or WY21W. Front fog lamps on the halogen reflector headlamp: H11LL."),
    ],
    [("2020 Ram 1500 Owner's Manual",
      "https://vehicleinfo.mopar.com/assets/publications/en-us/Ram/2020/1500_DT/P136218_20_DT_OM_EN_USC_DIGITAL.pdf",
      "FCA US LLC", "2020",
      "Publication P136218. Exterior bulb table and CR2450.")],
)
RAM_2023 = V(
    "Ram", "1500", 2023, [("ram", "1500")],
    [
        ("key", "Key fob battery", "One CR2450."),
        ("wiper", "Front wiper", "An inch length is not printed in the section we read."),
        ("rear", "Rear wiper", "No rear wiper length is printed."),
        ("head", "Headlight", "Halogen reflector low beam: H11LL. Halogen reflector high beam: 9005LL. LED reflector and LED projector headlamps: LED."),
        ("brake", "Brake light", "Base rear tail, turn and stop lamp: 7440LL or W21WLL. Premium rear lamp: LED. Center high mounted stop lamp: 921."),
        ("turn", "Turn signal", "Turn signal and front position, halogen reflector: 7444NA. LED headlamps: LED. Front side marker on the halogen reflector: W5W. Front fog lamps, halogen reflector: H11LL. Base turn lamp: 7440NA or WY21W."),
    ],
    [("2023 Ram 1500 Owner's Manual, edition E6",
      "https://vehicleinfo.mopar.com/assets/publications/en-us/Ram/2023/1500_DT/5690659_23_DT_OM_EN_USC_DIGITAL_E6.pdf",
      "FCA US LLC", "2023",
      "Publication 5690659. Exterior bulb table and CR2450.")],
)
RAM_2026 = V(
    "Ram", "1500", 2026, [("ram", "1500")],
    [
        ("key", "Key fob battery", "One CR2450."),
        ("wiper", "Front wiper", "An inch length is not printed in the section we read."),
        ("rear", "Rear wiper", "No rear wiper length is printed."),
        ("head", "Headlight", "The exterior bulbs chapter says to see a dealer for service on LED lamps, including the LED reflector headlamp and LED front fog lamps. It does not print an H11 or 9005 number in the section we read."),
        ("brake", "Brake light", "A trade number for the brake lamp was not printed in the section we read. The chapter describes removing the tail lamp as an assembly."),
        ("turn", "Turn signal", "The chapter describes a park and turn socket behind the headlamp but does not print a trade number there."),
    ],
    [("2026 Ram 1500 Owner's Manual, edition E1",
      "https://vehicleinfo.mopar.com/assets/publications/en-us-ca/2026/Ram/1500/103960_26_DT_OM_EN_USC_DIGITAL_E1_V1.pdf",
      "FCA US LLC", "2026",
      "Publication 103960. CR2450 and the exterior bulbs chapter.")],
    note="This edition sends LED lamps to a dealer and does not print the halogen trade numbers that earlier Ram 1500 books print. Do not copy a 2020 or 2023 number onto a 2026 truck.",
)
DURANGO_2023 = V(
    "Dodge", "Durango", 2023, [("dodge", "DURANGO")],
    [
        ("key", "Key fob battery", "One CR2032."),
        ("wiper", "Front wiper", "An inch length is not printed in the section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the section we read."),
        ("head", "Headlight", "Low beam, high beam headlamps: LED."),
        ("brake", "Brake light", "Rear stop and turn signal lamps: LED. Center high mounted stop lamp: LED."),
        ("turn", "Turn signal", "Front turn signal lamps, bulb reflector: 7444NA. Front daytime running, turn and park lamp on the premium lamp: LED. Front daytime running and park lamp on the base lamp: LED. Rear backup lamps: 921 (W16W). Front fog lamps: LED."),
    ],
    [("2023 Dodge Durango Owner's Manual, edition E3",
      "https://vehicleinfo.mopar.com/assets/publications/en-us/Dodge/2023/Durango/5622870_23_WD_OM_EN_USC_DIGITAL_E3.pdf",
      "FCA US LLC", "2023",
      "Publication 5622870. Exterior bulb table and CR2032.")],
)
CIVIC_2018 = V(
    "Honda", "Civic", 2018, [("honda", "CIVIC")],
    [
        ("key", "Key fob battery", "Master keys with a remote transmitter: CR1620. Smart entry remote: CR2032. The manual marks each one as not available on all models. Page 562."),
        ("wiper", "Front wiper", "Checking and Maintaining Wiper Blades, about pages 547 to 549, tells you how to change the blade rubber. It does not print a driver or passenger inch length."),
        ("rear", "Rear wiper", "This sedan manual does not print a rear wiper length."),
        ("head", "Headlight", "Low beam: 55 W (H11) on halogen bulb type models, or LED. High beam: 60 W (HB3) on halogen models, or LED. The specifications page uses footnotes for halogen headlights and LED headlights."),
        ("brake", "Brake light", "Brake lights: 21 W. High mount brake light: 21 W on models without sport mode, or LED on models with sport mode, according to the footnotes on the specifications page. Tail and rear side marker lights: LED."),
        ("turn", "Turn signal", "Front turn signal lights: 21 W amber on halogen headlight models, or LED on LED headlight models. Rear turn signal lights: 21 W amber. Back up lights: 16 W."),
    ],
    [("2018 Honda Civic Sedan Owner's Manual",
      "https://cdn.dealereprocess.org/cdn/servicemanuals/honda/2018-civic.pdf",
      "American Honda Motor Co., Inc.", "2018",
      "Book id 18 CIVIC 4D. Remote transmitter care, page 562. Light bulb specifications near the end of the book. Wiper rubber procedure about pages 547 to 549. This file is the Honda manual as hosted for dealers.")],
    note="Figures are for the 2018 Civic sedan book. A hatchback or coupe can differ. The manual says some items are not on all models.",
)
CRV_2025 = V(
    "Honda", "CR-V", 2025, [("honda", "CR-V")],
    [
        ("key", "Key fob battery", "CR2032, in Remote Transmitter Care."),
        ("wiper", "Front wiper", "An inch length is not printed in the sections we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the sections we read."),
        ("head", "Headlight", "Headlights are LED. The manual says to have a dealer inspect and replace the light assembly."),
        ("brake", "Brake light", "Brake light, taillight, and rear side marker light: LED. Have a dealer replace the assembly."),
        ("turn", "Turn signal", "Front turn signal, parking and daytime running lights: LED. Door mirror side turn lights: LED. Rear turn signal light: 21 W amber."),
    ],
    [("2025 Honda CR-V Owner's Manual",
      "https://serra-honda-grandville.s3.amazonaws.com/brochures/2025/2025_cr-v_owners_manual.pdf",
      "American Honda Motor Co., Inc.", "2025",
      "Dealer hosted copy of the Honda owner manual. Remote battery CR2032. Replacing light bulbs: headlights, front turn signals, and the rear turn signal 21 W amber.")],
)
GH_2024 = V(
    "Toyota", "Grand Highlander", 2024, [("toyota", "GRAND HIGHLANDER")],
    [
        ("key", "Key fob battery", "Lithium battery CR2450."),
        ("wiper", "Front wiper", "The manual has a wiper insert replacement section. It does not print an inch length in the pages we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the pages we read."),
        ("head", "Headlight", "A headlight trade number is not in the specifications light bulb table. That table only lists a replaceable bulb for the front turn and parking lights."),
        ("brake", "Brake light", "A brake light trade number is not in that table."),
        ("turn", "Turn signal", "Front turn signal and parking lights, bulb type: 7444NA, 28/8 W, wedge base amber. Specifications, light bulbs."),
    ],
    [("Toyota Grand Highlander Owner's Manual, publication OM0E126U",
      "https://assets.sia.toyota.com/publications/en/om-s/OM0E126U/pdf/OM0E126U.pdf",
      "Toyota Motor Corporation", "2023-06",
      "The manual's own software identifier is grandhighlander.2024, and a connected services note says the text was current as of June 2023. Light bulb table in the specifications section. CR2450 in the electronic key battery section.")],
    note="We are calling this the 2024 Grand Highlander because the manual identifies itself as grandhighlander.2024. Confirm the book matches the door label before you buy a bulb.",
)
CROSS_H_2024 = V(
    "Toyota", "Corolla Cross Hybrid", 2024, [("toyota", "COROLLA CROSS HYBRID")],
    [
        ("key", "Key fob battery", "Lithium battery CR2450."),
        ("wiper", "Front wiper", "An inch length is not printed in the pages we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the pages we read."),
        ("head", "Headlight", "A headlight trade number is not in the specifications light bulb table."),
        ("brake", "Brake light", "Tail lights and rear side marker lights, bulb type: 5 W. The table prints a dash instead of a bulb number."),
        ("turn", "Turn signal", "Front turn signal, bulb type: 21 W, wedge base amber, no bulb number printed. Front side marker and parking lights, bulb type: 5 W each, no bulb number printed. Back up lights: 16 W. License plate lights: 5 W."),
    ],
    [("Toyota Corolla Cross Hybrid Owner's Manual, publication OM0A073U",
      "https://assets.sia.toyota.com/publications/en/om-s/OM0A073U/pdf/OM0A073U.pdf",
      "Toyota Motor Corporation", "2023-11",
      "The manual's own software identifier is corollacross.2024.2311.hev. Light bulb table in the specifications section. CR2450 in the electronic key battery section.")],
    note="This is the hybrid book. The software identifier says corollacross.2024. Confirm it matches the door label.",
)
COROLLA_H_2025 = V(
    "Toyota", "Corolla Hybrid", 2025, [("toyota", "COROLLA HYBRID")],
    [
        ("key", "Key fob battery", "Lithium battery CR2032."),
        ("wiper", "Front wiper", "An inch length is not printed in the pages we read."),
        ("rear", "Rear wiper", "This sedan manual does not print a rear wiper length in the pages we read."),
        ("head", "Headlight", "A headlight trade number is not in the specifications light bulb table."),
        ("brake", "Brake light", "A brake light trade number is not in that table."),
        ("turn", "Turn signal", "Rear turn signal lights: 21 W, wedge base amber. The table prints a dash instead of a bulb number. Rear side marker lights, bulb type: 5 W, no bulb number printed. Back up lights: 16 W, no bulb number printed."),
    ],
    [("Toyota Corolla Hybrid Owner's Manual, publication OM12S84U",
      "https://assets.sia.toyota.com/publications/en/om-s/OM12S84U/pdf/OM12S84U.pdf",
      "Toyota Motor Corporation", "2024-09",
      "The manual's own software identifier is om12S84u.corolla.2025, and a note says the text was current as of September 2024. Light bulb table and CR2032.")],
    note="This is the hybrid book, not every Corolla. The software identifier says corolla.2025.",
)
PIU_2021 = V(
    "Ford", "Police Interceptor Utility", 2021, [],
    [
        ("key", "Key fob battery", "One CR2032, or equivalent."),
        ("wiper", "Front wiper", "Motorcraft WW-2616 driver side and WW-2113 passenger side. No inch length is printed."),
        ("rear", "Rear wiper", "Motorcraft WW-1110 for the rear window."),
        ("head", "Headlight", "Low beam and high beam are both LED."),
        ("brake", "Brake light", "Brake and rear lamp: LED. Central high mounted brake lamp: LED."),
        ("turn", "Turn signal", "Front direction indicator: LED. Rear direction indicator: 3757NAK or PY27/7W, 27 W. Reversing lamp: W21W, 21 W. License plate lamp: W5W, 5 W."),
    ],
    [("2021 Ford Police Interceptor Utility Owner's Manual, second printing, December 2020",
      "https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2021-Ford-Police-Interceptor-Owners-Manual-version-2_om_EN-US_12_2020.pdf",
      "Ford Motor Company", "2020-12",
      "Bulb Specification Chart, CR2032, and wiper parts WW-2616, WW-2113, and WW-1110.")],
    note="NHTSA's recalls API does not accept Police Interceptor Utility as a model name. This page does not borrow civilian Explorer recalls. Look up the VIN.",
)

VEHICLES = [
    F150_2018, F150_2020, F150_2022,
    ESCAPE_2020, ESCAPE_2022, RANGER_2023, FUSION_2020, MUSTANG_2020,
    EXPEDITION_2020, EDGE_2019, EDGE_2020, NAUTILUS_2020, ESERIES_2021, PIU_2021,
    WRANGLER_2020, WRANGLER_2024, WRANGLER_2026, CHEROKEE_2023, GRAND_2025,
    RAM_2020, RAM_2023, RAM_2026, DURANGO_2023,
    CIVIC_2018, CRV_2025, GH_2024, COROLLA_H_2025, CROSS_H_2024,
]

from vehicles_wave2 import WAVE2
VEHICLES.extend(WAVE2)
