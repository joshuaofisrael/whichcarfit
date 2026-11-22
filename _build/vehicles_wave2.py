"""Model years added after opening each official owner manual on 16 Nov 2026."""
from config import PUBLISHED

def V(make, model, year, nhtsa, fitment, sources, note=""):
    return {"make": make, "model": model, "year": str(year), "nhtsa": nhtsa,
            "fitment": fitment, "sources": sources, "note": note,
            "published": PUBLISHED, "modified": PUBLISHED}

WAVE2 = [
    V("Chevrolet", "Silverado 1500", 2020, [('chevrolet', 'SILVERADO 1500')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 21.7 in. Passenger side: 21.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2020 Chevrolet Silverado 1500 Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/chevrolet/silverado-1500/2020-chevrolet-silverado-owners-manual.pdf", "General Motors LLC", "2020", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
    V("Chevrolet", "Equinox", 2020, [('chevrolet', 'EQUINOX')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 60 cm (23.6 in), GM part 84574893. Passenger side: 45.0 cm (17.7 in), GM part 84574892. Lengths and part numbers are from the maintenance replacement parts table."),
        ("rear", "Rear wiper", "Rear: 30.0 cm (11.8 in), GM part 84215609. Length and part number are from the maintenance replacement parts table."),
        ("head", "Headlight", "The LED Lighting section says this vehicle has several LED lamps and to contact your dealer for replacement of any LED lighting assembly. The section we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2020 Chevrolet Equinox Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/chevrolet/equinox/2020-chevrolet-equinox-owners-manual.pdf", "General Motors LLC", "2020", "Document 13555863, CRC 8/2/19. Remote battery CR2032. Maintenance replacement parts table for wiper length and GM part number. LED Lighting section."),
    ],
    note="The 2021 book prints the same GM part numbers and the same centimeter lengths. It prints the inch side as 24, 18, and 12 rather than 23.6, 17.7, and 11.8. Re-read 20 Nov 2026."),
    V("Chevrolet", "Malibu", 2020, [('chevrolet', 'MALIBU')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 650 mm (25.6 in), GM part 23353586. Passenger side: 450 mm (17.7 in), GM part 23353587. Lengths and part numbers are from the maintenance replacement parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance replacement parts table."),
        ("head", "Headlight", "The LED Lighting section says this vehicle has several LED lamps and to contact your dealer for replacement of any LED lighting assembly. The section we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2020 Chevrolet Malibu Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/chevrolet/malibu/2020-chevrolet-malibu-owners-manual.pdf", "General Motors LLC", "2019-08", "Document 13555849, CRC 8/16/19. Re-read 21 Nov 2026. Remote battery CR2032. Maintenance replacement parts table, page 314, for wiper length and GM part number. LED Lighting section."),
    ],
    note="Re-read 21 Nov 2026. The inch lengths were already on this page. The GM part numbers were not. The table does not print a rear wiper."),
    V("Chevrolet", "Tahoe", 2020, [('chevrolet', 'TAHOE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 21.7 in. Passenger side: 21.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "Rear: 13.0 in. Length is from the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2020 Chevrolet Tahoe Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/chevrolet/tahoe-suburban/2020-chevrolet-tahoe-suburban-owners-manual.pdf", "General Motors LLC", "2020", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note="This General Motors book covers Tahoe and Suburban together. The parts table does not split the two nameplates. Recalls below are the campaigns NHTSA files under Tahoe."),
    V("Chevrolet", "Silverado 1500", 2021, [('chevrolet', 'SILVERADO 1500')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 21.7 in. Passenger side: 21.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2021 Chevrolet Silverado 1500 Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2021/chevrolet/silverado-1500/2021-chevrolet-silverado-1500-owners-manual.pdf", "General Motors LLC", "2021", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
    V("Chevrolet", "Equinox", 2021, [('chevrolet', 'EQUINOX')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 60 cm (24 in), GM part 84574893. Passenger side: 45.0 cm (18 in), GM part 84574892. The maintenance replacement parts table prints these inch figures beside the centimeter lengths."),
        ("rear", "Rear wiper", "Rear: 30.0 cm (12 in), GM part 84215609. The centimeter length matches the 2020 table. This edition prints the inch side as 12 rather than 11.8."),
        ("head", "Headlight", "The LED Lighting section says this vehicle has several LED lamps and to contact your dealer for replacement of any LED lighting assembly. The section we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2021 Chevrolet Equinox Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2021/chevrolet/equinox/2021-chevrolet-equinox-owners-manual.pdf", "General Motors LLC", "2021", "Document 14420010. Remote battery CR2032. Maintenance replacement parts table prints 60 cm (24 in), 45.0 cm (18 in), and 30.0 cm (12 in) with GM parts 84574893, 84574892, and 84215609."),
    ],
    note="Same GM part numbers as the 2020 table. The centimeter lengths match. This edition rounds the inch side to 24, 18, and 12. Re-read 20 Nov 2026."),
    V("Chevrolet", "Malibu", 2021, [('chevrolet', 'MALIBU')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 25.6 in. Passenger side: 17.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2021 Chevrolet Malibu Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2021/chevrolet/malibu/2021-chevrolet-malibu-owners-manual.pdf", "General Motors LLC", "2021", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
    V("Chevrolet", "Tahoe", 2021, [('chevrolet', 'TAHOE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 22 in. Passenger side: 22 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "Rear: 12 in. Length is from the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2021 Chevrolet Tahoe Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2021/chevrolet/tahoe-suburban/2021-chevrolet-tahoe-suburban-owners-manual.pdf", "General Motors LLC", "2021", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note="This General Motors book covers Tahoe and Suburban together. The parts table does not split the two nameplates. Recalls below are the campaigns NHTSA files under Tahoe."),
    V("Chevrolet", "Equinox", 2022, [('chevrolet', 'EQUINOX')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 60 cm (24 in), GM part 84566977. Passenger side: 45.0 cm (18 in), GM part 84574892. The maintenance replacement parts table prints these lengths and part numbers."),
        ("rear", "Rear wiper", "Rear: 30.0 cm (12 in), GM part 85118765. The centimeter length matches the 2020 and 2021 tables. The GM part number does not. Those books print 84215609."),
        ("head", "Headlight", "The LED Lighting section says this vehicle has several LED lamps and to contact your dealer for replacement of any LED lighting assembly. The headlamp section that follows shows a bi-halogen bulb procedure and does not print a trade number."),
        ("brake", "Brake light", "The taillamp procedure describes a stop lamp, tail lamp, and rear turn socket. It does not print a trade number."),
        ("turn", "Turn signal", "The front turn signal and fog lamp procedure describes a bulb socket. It does not print a trade number. The rear turn is included in the taillamp procedure, also without a trade number."),
    ], [
        ("2022 Chevrolet Equinox Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2022/chevrolet/equinox/2022-chevrolet-equinox-owners-manual.pdf", "General Motors LLC", "2021-08", "Document 15230998, CRC 8/10/21. Re-read 21 Nov 2026. Remote battery CR2032 on page 13. Maintenance replacement parts table on page 336. LED Lighting and the bi-halogen headlamp procedure on page 278."),
    ],
    note="Re-read 21 Nov 2026. Inch lengths match the 2021 table (24, 18, and 12), not the 2020 table (23.6, 17.7, and 11.8). The driver part changed from 84574893 to 84566977. The rear part changed from 84215609 to 85118765. The passenger part 84574892 is unchanged."),
    V("Chevrolet", "Malibu", 2022, [('chevrolet', 'MALIBU')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 25.6 in. Passenger side: 17.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2022 Chevrolet Malibu Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2022/chevrolet/malibu/2022-chevrolet-malibu-owners-manual.pdf", "General Motors LLC", "2022", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
    V("Chevrolet", "Tahoe", 2022, [('chevrolet', 'TAHOE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 22 in. Passenger side: 22 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "Rear: 12 in. Length is from the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2022 Chevrolet Tahoe Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2022/chevrolet/tahoe-suburban/2022-chevrolet-tahoe-suburban-owners-manual.pdf", "General Motors LLC", "2022", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note="This General Motors book covers Tahoe and Suburban together. The parts table does not split the two nameplates. Recalls below are the campaigns NHTSA files under Tahoe."),
    V("GMC", "Sierra 1500", 2020, [('gmc', 'SIERRA 1500')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 21.7 in. Passenger side: 21.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2020 GMC Sierra 1500 Owner's Manual", "https://www.gmc.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/gmc/sierra-1500/2020-gmc-sierra-owners-manual.pdf", "General Motors LLC", "2020", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
    V("GMC", "Sierra 1500", 2021, [('gmc', 'SIERRA 1500')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 21.7 in. Passenger side: 21.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2021 GMC Sierra 1500 Owner's Manual", "https://www.gmc.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2021/gmc/sierra-1500/2021-gmc-sierra-1500-owners-manual.pdf", "General Motors LLC", "2021", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
    V("Nissan", "Altima", 2018, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low (Halogen): H11. High (Halogen): H9. Fog: H11."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn/Park: 7444NA. Turn: WY21W."),
    ], [
        ("2018 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2018/2018-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2018", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Rogue", 2019, [('nissan', 'ROGUE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "High: H9. Low: H11. Fog lights (if so equipped): H8."),
        ("brake", "Brake light", "Stop: W21W."),
        ("turn", "Turn signal", "Turn: 7444NA. Turn: WY21W."),
    ], [
        ("2019 Nissan Rogue Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/rogue/2019/2019-nissan-rogue-owner-manual.pdf", "Nissan North America, Inc.", "2019", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Altima", 2019, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "FOG LIGHTS (if so equipped) Side marker: W5W."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn signal/park (if so equipped) light: 7444NA. Turn: W21W."),
    ], [
        ("2019 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2019/2019-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2019", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Rogue", 2020, [('nissan', 'ROGUE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "High: H9. Low: H11. Fog lights (if so equipped): H8."),
        ("brake", "Brake light", "Stop: W21W."),
        ("turn", "Turn signal", "Turn: 7444NA. Turn: WY21W."),
    ], [
        ("2020 Nissan Rogue Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/rogue/2020/2020-nissan-rogue-owner-manual.pdf", "Nissan North America, Inc.", "2020", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Altima", 2020, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low (Halogen): H11."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn signal/park (if so equipped) light: 7444NA. Turn: W21W."),
    ], [
        ("2020 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2020/2020-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2020", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Sentra", 2020, [('nissan', 'SENTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low: H11. High/Daytime running (Canada only): H9. Front fog light (Type A) (If so equipped): H8."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn/Park: 3457NAK. Turn: WY21W."),
    ], [
        ("2020 Nissan Sentra Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/sentra/2020/2020-nissan-sentra-owner-manual.pdf", "Nissan North America, Inc.", "2020", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Rogue", 2021, [('nissan', 'ROGUE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The manual says to visit a Nissan dealer if an LED headlight needs replacement. The light chart marks the high and low beams as LED."),
        ("brake", "Brake light", "Stop and tail lamps on the chart we read are marked LED where a separate bulb is not listed."),
        ("turn", "Turn signal", "The exterior light chart lists the front turn signal on its own row. Some positions on that chart are LED and some print a trade number, so match the row before you buy a bulb."),
    ], [
        ("2021 Nissan Rogue Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/rogue/2021/2021-nissan-rogue-owner-manual.pdf", "Nissan North America, Inc.", "2021", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note=""),
    V("Nissan", "Altima", 2021, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "A headlight trade number was not in the rows we read."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn signal/park (if so equipped) light: 7444NA. Turn: W21W."),
    ], [
        ("2021 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2021/2021-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2021", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Sentra", 2021, [('nissan', 'SENTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low: H11. High/Daytime running (Canada only): H9."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn/Park: 3457NAK. Turn: 3457NAK. Turn: WY21W."),
    ], [
        ("2021 Nissan Sentra Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/sentra/2021/2021-nissan-sentra-owner-manual.pdf", "Nissan North America, Inc.", "2021", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note="The 2022, 2023, 2024, and 2025 Sentra transcriptions on this site repeat this chart: CR2032, low beam H11, high beam H9 on the Canada daytime running row, tail W5W, turn and park 3457NAK, and turn WY21W. Those four URLs were removed from the sitemap on 20 Nov 2026 so the chart is not published five times. The 2020 Sentra page is a different chart and stays separate."),
    V("Nissan", "Rogue", 2022, [('nissan', 'ROGUE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The manual says to visit a Nissan dealer if an LED headlight needs replacement. The light chart marks the high and low beams as LED."),
        ("brake", "Brake light", "Stop and tail lamps on the chart we read are marked LED where a separate bulb is not listed."),
        ("turn", "Turn signal", "The exterior light chart lists the front turn signal on its own row. Some positions on that chart are LED and some print a trade number, so match the row before you buy a bulb."),
    ], [
        ("2022 Nissan Rogue Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/rogue/2022/2022-nissan-rogue-owner-manual.pdf", "Nissan North America, Inc.", "2022", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note=""),
    V("Nissan", "Altima", 2022, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "A headlight trade number was not in the rows we read."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn signal/park (if so equipped) light: 7444NA. Turn: W21W."),
    ], [
        ("2022 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2022/2022-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2022", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Sentra", 2022, [('nissan', 'SENTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low: H11. High/Daytime running (Canada only): H9."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn/Park: 3457NAK. Turn: 3457NAK. Turn: WY21W."),
    ], [
        ("2022 Nissan Sentra Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/sentra/2022/2022-nissan-sentra-owner-manual.pdf", "Nissan North America, Inc.", "2022", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Rogue", 2023, [('nissan', 'ROGUE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The manual says to visit a Nissan dealer if an LED headlight needs replacement. The light chart marks the high and low beams as LED."),
        ("brake", "Brake light", "Stop and tail lamps on the chart we read are marked LED where a separate bulb is not listed."),
        ("turn", "Turn signal", "The exterior light chart lists the front turn signal on its own row. Some positions on that chart are LED and some print a trade number, so match the row before you buy a bulb."),
    ], [
        ("2023 Nissan Rogue Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/rogue/2023/2023-nissan-rogue-owner-manual.pdf", "Nissan North America, Inc.", "2023", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note=""),
    V("Nissan", "Altima", 2023, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "A headlight trade number was not in the rows we read."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn: W21W."),
    ], [
        ("2023 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2023/2023-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2023", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Sentra", 2023, [('nissan', 'SENTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low: H11. High/Daytime running (Canada only): H9."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn/Park: 3457NAK. Turn: 3457NAK. Turn: WY21W."),
    ], [
        ("2023 Nissan Sentra Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/sentra/2023/2023-nissan-sentra-owner-manual.pdf", "Nissan North America, Inc.", "2023", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Rogue", 2024, [('nissan', 'ROGUE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The manual says to visit a Nissan dealer if an LED headlight needs replacement. The light chart marks the high and low beams as LED."),
        ("brake", "Brake light", "Stop and tail lamps on the chart we read are marked LED where a separate bulb is not listed."),
        ("turn", "Turn signal", "The exterior light chart lists the front turn signal on its own row. Some positions on that chart are LED and some print a trade number, so match the row before you buy a bulb."),
    ], [
        ("2024 Nissan Rogue Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/rogue/2024/2024-nissan-rogue-owner-manual.pdf", "Nissan North America, Inc.", "2024", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note=""),
    V("Nissan", "Altima", 2024, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "A headlight trade number was not in the rows we read."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn: W21W."),
    ], [
        ("2024 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2024/2024-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2024", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Sentra", 2024, [('nissan', 'SENTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low: H11. High/Daytime running (Canada only): H9."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn/Park: 3457NAK. Turn: 3457NAK. Turn: WY21W."),
    ], [
        ("2024 Nissan Sentra Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/sentra/2024/2024-nissan-sentra-owner-manual.pdf", "Nissan North America, Inc.", "2024", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Rogue", 2025, [('nissan', 'ROGUE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The manual says to visit a Nissan dealer if an LED headlight needs replacement. The light chart marks the high and low beams as LED."),
        ("brake", "Brake light", "Stop and tail lamps on the chart we read are marked LED where a separate bulb is not listed."),
        ("turn", "Turn signal", "The exterior light chart lists the front turn signal on its own row. Some positions on that chart are LED and some print a trade number, so match the row before you buy a bulb."),
    ], [
        ("2025 Nissan Rogue Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/rogue/2025/2025-nissan-rogue-owner-manual.pdf", "Nissan North America, Inc.", "2025", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note=""),
    V("Nissan", "Altima", 2025, [('nissan', 'ALTIMA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "A headlight trade number was not in the rows we read."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn: W21W."),
    ], [
        ("2025 Nissan Altima Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/altima/2025/2025-nissan-altima-owner-manual.pdf", "Nissan North America, Inc.", "2025", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Nissan", "Sentra", 2025, [('nissan', 'SENTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low: H11. High/Daytime running (Canada only): H9."),
        ("brake", "Brake light", "Tail: W5W."),
        ("turn", "Turn signal", "Turn/Park: 3457NAK. Turn: 3457NAK. Turn: WY21W."),
    ], [
        ("2025 Nissan Sentra Owner's Manual", "https://www.nissanusa.com/content/dam/Nissan/us/manuals-and-guides/sentra/2025/2025-nissan-sentra-owner-manual.pdf", "Nissan North America, Inc.", "2025", "Remote battery CR2032. Exterior light chart in the do it yourself chapter."),
    ],
    note=""),
    V("Hyundai", "Tucson", 2020, [('hyundai', 'TUCSON')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low H7 55 High HB3 60 Fog lamp H8 35"),
        ("brake", "Brake light", "Tail/Stop P28/8W 28/8"),
        ("turn", "Turn signal", "Turn Signal lamp/Parking lamp PY28/8W 28/8 Type B Turn Signal lamp PY28/8W 28/8 Type C Turn signal lamp LED LED"),
    ], [
        ("2020 Hyundai Tucson Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2020/tucson/2020-Tucson-Owners-Manual.pdf", "Hyundai Motor America", "2020", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Hyundai", "Elantra", 2020, [('hyundai', 'ELANTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low HB3 60 High HB3 60"),
        ("brake", "Brake light", "Tail lamp W5W 5 Tail/Stop lamp PY28/8W 28/8"),
        ("turn", "Turn signal", "Turn signal lamp PY28/8W 28/8"),
    ], [
        ("2020 Hyundai Elantra Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2020/elentra/2020%20Elantra%20Owner%27s%20Manual.pdf", "Hyundai Motor America", "2020", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Hyundai", "Santa Fe", 2020, [('hyundai', 'SANTA FE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low HB3 60 Type A High HB3 60"),
        ("brake", "Brake light", "Tail lamp W5W 5 Type A Tail/Stop lamp P21/5W 5/21 Tail lamp LED LED Type B Tail/Stop lamp LED LED"),
        ("turn", "Turn signal", "No matching row was extracted from the bulb wattage table."),
    ], [
        ("2020 Hyundai Santa Fe Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2020/santa-fe/2020%20Santa%20Fe%20Owner%27s%20Manual.pdf", "Hyundai Motor America", "2020", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Hyundai", "Tucson", 2021, [('hyundai', 'TUCSON')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "Low H7 55 High HB3 60 Fog lamp H8 35"),
        ("brake", "Brake light", "Tail/Stop P28/8W 28/8"),
        ("turn", "Turn signal", "Turn Signal lamp/Parking lamp PY28/8W 28/8 Type B Turn Signal lamp PY28/8W 28/8 Type C Turn signal lamp LED LED"),
    ], [
        ("2021 Hyundai Tucson Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2021/tucson/2021-Tucson-Owners-Manual.pdf/tmp/m2/extra-2021-Elantra-Owners-Manual.pdf https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2021/elantra/2021-Elantra-Owners-Manual.pdf", "Hyundai Motor America", "2021", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Hyundai", "Elantra", 2022, [('hyundai', 'ELANTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "High HB3 60 Low HB3 60 Headlamp LED LED"),
        ("brake", "Brake light", "Stop lamp P21W/5W 21 Tail lamp LED LED Stop lamp LED LED Rear Tail lamp LED LED"),
        ("turn", "Turn signal", "Turn signal lamp PY21W 21"),
    ], [
        ("2022 Hyundai Elantra Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2022/elantra/2022-Elantra-Owners-Manual.pdf", "Hyundai Motor America", "2022", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Hyundai", "Santa Fe", 2022, [('hyundai', 'SANTA FE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "No matching row was extracted from the bulb wattage table."),
        ("brake", "Brake light", "Tail lamp W5W 5 Tail/Stop lamp P21/5W 5/21 Tail lamp LED LED Tail/Stop lamp LED LED"),
        ("turn", "Turn signal", "Turn signal lamp PY21W 21 Turn signal lamp (Outside mirror) LED LED"),
    ], [
        ("2022 Hyundai Santa Fe Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2022/santa-fe/2022-Santa-Fe-Owners-Manual.pdf", "Hyundai Motor America", "2022", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Hyundai", "Elantra", 2023, [('hyundai', 'ELANTRA')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "High HB3 60 Low HB3 60 Headlight LED LED"),
        ("brake", "Brake light", "Stop lamp P21W/5W 21 Tail lamp LED LED Stop lamp LED LED Rear Tail lamp LED LED"),
        ("turn", "Turn signal", "Turn signal lamp PY21W 21"),
    ], [
        ("2023 Hyundai Elantra Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2023/elantra/2023-Elantra-Owners-Manual.pdf", "Hyundai Motor America", "2023", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Hyundai", "Santa Fe", 2023, [('hyundai', 'SANTA FE')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "No matching row was extracted from the bulb wattage table."),
        ("brake", "Brake light", "Tail lamp W5W 5 Tail/Stop lamp P21/5W 5/21 Tail lamp LED LED Tail/Stop lamp LED LED"),
        ("turn", "Turn signal", "Turn signal lamp PY21W 21 Turn signal lamp (Outside mirror) LED LED"),
    ], [
        ("2023 Hyundai Santa Fe Owner's Manual", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2023/santa-fe/2023-Santa-Fe-Owners-Manual.pdf", "Hyundai Motor America", "2023", "Remote battery CR2032. Bulb wattage table in the specifications chapter."),
    ],
    note=""),
    V("Mazda", "CX-5", 2019, [('mazda', 'CX-5')], [
        ("key", "Key fob battery", "The key transmitter battery is a CR2025, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The maintenance chapter says the exterior lights have either LEDs or normal bulbs. Headlights are listed with the LED lamps, which the manual says are replaced as a unit. The front turn signal procedure does not print a trade number."),
        ("brake", "Brake light", "Brake lights are listed with the LED lamps on at least one type. The section we read does not print a separate trade number for every brake lamp."),
        ("turn", "Turn signal", "The front turn signal and parking light procedure does not print a trade number."),
    ], [
        ("2019 Mazda CX-5 Owner's Manual", "https://www.mazdausa.com/siteassets/pdf/owners-optimized/2019/cx-5/2019-cx-5-owners-manual.pdf", "Mazda Motor Corporation", "2019", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note=""),
    V("Mazda", "CX-5", 2020, [('mazda', 'CX-5')], [
        ("key", "Key fob battery", "The key transmitter battery is a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The maintenance chapter says the exterior lights have either LEDs or normal bulbs. Headlights are listed with the LED lamps, which the manual says are replaced as a unit. The front turn signal procedure does not print a trade number."),
        ("brake", "Brake light", "Brake lights are listed with the LED lamps on at least one type. The section we read does not print a separate trade number for every brake lamp."),
        ("turn", "Turn signal", "The front turn signal and parking light procedure does not print a trade number."),
    ], [
        ("2020 Mazda CX-5 Owner's Manual", "https://www.mazdausa.com/siteassets/pdf/owners-optimized/2021/cx-5/2021-cx-5-owners-manual.pdf", "Mazda Motor Corporation", "2020", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note="Mazda hosts this PDF in the 2021 CX-5 folder. The manual's own edition code uses 20, so this page is filed as model year 2020."),
    V("Mazda", "CX-5", 2021, [('mazda', 'CX-5')], [
        ("key", "Key fob battery", "The key transmitter battery is a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The maintenance chapter says the exterior lights have either LEDs or normal bulbs. Headlights are listed with the LED lamps, which the manual says are replaced as a unit. The front turn signal procedure does not print a trade number."),
        ("brake", "Brake light", "Brake lights are listed with the LED lamps on at least one type. The section we read does not print a separate trade number for every brake lamp."),
        ("turn", "Turn signal", "The front turn signal and parking light procedure does not print a trade number."),
    ], [
        ("2021 Mazda CX-5 Owner's Manual", "https://www.mazdausa.com/siteassets/pdf/owners-optimized/2022/cx-5/2022-cx-5-owners-manual.pdf", "Mazda Motor Corporation", "2021", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note="Mazda hosts this PDF in the 2022 CX-5 folder. The manual's own edition code uses 21, so this page is filed as model year 2021."),
    V("Mazda", "CX-5", 2022, [('mazda', 'CX-5')], [
        ("key", "Key fob battery", "The key transmitter battery is a CR2032, or equivalent."),
        ("wiper", "Front wiper", "An inch length is not printed in the wiper section we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the wiper section we read."),
        ("head", "Headlight", "The maintenance chapter says the exterior lights have either LEDs or normal bulbs. Headlights are listed with the LED lamps, which the manual says are replaced as a unit. The front turn signal procedure does not print a trade number."),
        ("brake", "Brake light", "Brake lights are listed with the LED lamps on at least one type. The section we read does not print a separate trade number for every brake lamp."),
        ("turn", "Turn signal", "The front turn signal and parking light procedure does not print a trade number."),
    ], [
        ("2022 Mazda CX-5 Owner's Manual", "https://www.mazdausa.com/siteassets/pdf/owners-optimized/2023/cx-5/2023-cx-5-owners-manual.pdf", "Mazda Motor Corporation", "2022", "Key battery in the transmitter replacement section. Light bulb section in maintenance."),
    ],
    note="Mazda hosts this PDF in the 2023 CX-5 folder. The manual's own edition code uses 22, so this page is filed as model year 2022."),
]

# Added 18 Nov 2026 (priority SEO move). Published and modified are set to
# that day, not the 16 Nov launch batch date, because these two pages were
# not live until today.
CAMRY_2023 = V("Toyota", "Camry", 2023, [('toyota', 'CAMRY')], [
    ("key", "Key fob battery", "The electronic key chapter says to use a CR2032 lithium battery."),
    ("wiper", "Front wiper", "An inch length is not printed in the pages we read."),
    ("rear", "Rear wiper", "This sedan manual does not print a rear wiper length in the pages we read."),
    ("head", "Headlight", "A headlight trade number is not in the exterior light bulb table. The table's own footnote says a light not listed there is an LED bulb."),
    ("brake", "Brake light", "Brake and tail lamps are not in the exterior light bulb table either, so the same LED footnote applies. No trade number is printed for them."),
    ("turn", "Turn signal", "Front turn signal and parking lights, bulb type: 7444NA, 28/8 W, wedge base amber. Rear turn signal lights, bulb type: WY21W, 21 W, wedge base amber. Front side marker lights, bulb type: W5W, 5 W, wedge base clear. Rear side marker lights, bulb type: W5W, 5 W. Back-up lights, bulb type: 921, 16 W."),
], [
    ("2023 Toyota Camry Owner's Manual, publication OM06259U", "https://assets.sia.toyota.com/publications/en/om-s/OM06259U/pdf/OM06259U.pdf", "Toyota Motor Corporation", "2023", "Light bulbs table in the Vehicle specifications chapter (page 589), footnote 1: bulbs not listed in the table are LED. Electronic key battery: use a CR2032 lithium battery."),
],
note="Re-read 20 Nov 2026 against the 2019 (OM06142U), 2020 (OM06158U), 2021 (OM06242U), 2022 (OM06244U), and 2024 (OM06291U) Camry books. Those five print this same exterior bulb table and the same CR2032 key, so they are not separate pages. The 2025 Camry Hybrid book does not match. Bulbs missing from this table are LED, per the table footnote.")
CAMRY_2023["published"] = "2026-11-18"
CAMRY_2023["modified"] = "2026-11-20"
CAMRY_2023["checked_h"] = "20 Nov 2026"
CAMRY_2023["seo_title"] = "2023 Camry key is CR2032, backup is 921"

ACCORD_2023 = V("Honda", "Accord", 2023, [('honda', 'ACCORD')], [
    ("key", "Key fob battery", "Remote Transmitter Care, Replacing the Remote Battery: battery type CR2032."),
    ("wiper", "Front wiper", "Checking and Maintaining Wiper Blades gives the rubber-replacement steps. It does not print a driver or passenger inch length."),
    ("rear", "Rear wiper", "This sedan manual does not print a rear wiper length."),
    ("head", "Headlight", "Headlights are LED type. The manual says to have an authorized Honda dealer inspect and replace the light assembly."),
    ("brake", "Brake light", "Brake lights, rear side marker and taillights, and rear turn signal lights are LED type, replaced as an assembly by a dealer."),
    ("turn", "Turn signal", "Front turn signal lights and front side marker lights are LED type. Rear turn signal lights are LED type, grouped with the brake and taillight assembly. The specifications table lists every exterior light bulb position as LED, with no bulb trade number on this model."),
], [
    ("2023 Honda Accord Owner's Manual", "https://cdn.dealereprocess.org/cdn/servicemanuals/honda/2023-accord.pdf", "American Honda Motor Co., Inc.", "2023", "Replacing Light Bulbs (page 446) and Remote Transmitter Care, Replacing the Remote Battery (page 462): CR2032. Specifications table lists every light bulb position as LED."),
],
note="Every exterior lamp on this model is LED and replaced at a dealer as an assembly. That is what the manual's own specifications table says, not a fact we could not find.")
ACCORD_2023["published"] = "2026-11-18"
ACCORD_2023["modified"] = "2026-11-18"
ACCORD_2023["checked_h"] = "18 Nov 2026"

# Added 19 Nov 2026 (batched SEO). Fifth-generation RAV4 gas books only.
# Early years (2019 to 2021) still print a 19 W H16 fog bulb in the chart.
# Later years (2022 to 2025) move fog lamps to the dealer LED list.
def _rav4(year, pub, pdf_note, fog_in_chart):
    if fog_in_chart:
        head = ("Headlights, daytime running lights, tail lights, stop lights, "
                "rear side marker lights, the high mounted stoplight, and license "
                "plate lights are listed among the lamps your Toyota dealer replaces. "
                "No headlight trade number is printed in the light bulb table.")
        brake = ("Stop lights, tail lights, rear side marker lights, and the high "
                 "mounted stoplight are listed among the lamps your Toyota dealer replaces. "
                 "No stop lamp trade number is printed in the light bulb table.")
        turn = ("Front side marker lights: W5W, 5 W, wedge base clear. "
                "Fog lights (if equipped): 19 W, H16 halogen. "
                "Front turn signal and parking lights (bulb type): 7444NA, 28/8 W, wedge base amber. "
                "Rear turn signal lights: WY21W, 21 W, wedge base amber. "
                "Back-up lights: W16W, 16 W, wedge base clear.")
        note = ("Gas RAV4 book only, not Hybrid or Prime. Fog lamps still have a "
                "19 W H16 row in this year's light bulb table. Match bulb type rows "
                "to the lamps on your vehicle when a trim uses LED instead.")
    else:
        head = ("Headlights, daytime running lights, LED type front turn signals, "
                "LED type parking lights, LED type front side marker lights, fog lights "
                "(if equipped), tail lights, stop lights, rear side marker lights, "
                "the high mounted stoplight, and license plate lights are listed among "
                "the lamps your Toyota dealer replaces. No headlight trade number is "
                "printed in the light bulb table.")
        brake = ("Stop lights, tail lights, rear side marker lights, and the high "
                 "mounted stoplight are listed among the lamps your Toyota dealer replaces. "
                 "No stop lamp trade number is printed in the light bulb table.")
        turn = ("Front side marker lights (bulb type): W5W, 5 W, wedge base clear. "
                "Front turn signal and parking lights (type A): 7444NA, 28/8 W, wedge base amber. "
                "Front turn signal (type B and C, bulb type): 7444NA, 28/8 W (only the 28 W filament illuminates). "
                "Rear turn signal lights: WY21W, 21 W, wedge base amber. "
                "Back-up lights: W16W, 16 W, wedge base clear. "
                "Fog lights (if equipped) are on the dealer replacement list, not in the DIY bulb table.")
        note = ("Gas RAV4 book only, not Hybrid or Prime. From this year the fog lamp "
                "row leaves the DIY light bulb table and joins the dealer LED list. "
                "Match type A, B, or C front lamp packages to the vehicle.")
    v = V("Toyota", "RAV4", year, [("toyota", "RAV4")], [
        ("key", "Key fob battery", "Lithium battery CR2032 for the wireless remote control or electronic key."),
        ("wiper", "Front wiper", "The manual has a wiper insert replacement section. It does not print an inch length in the pages we read."),
        ("rear", "Rear wiper", "An inch length is not printed in the pages we read."),
        ("head", "Headlight", head),
        ("brake", "Brake light", brake),
        ("turn", "Turn signal", turn),
    ], [
        (f"{year} Toyota RAV4 Owner's Manual, publication {pub}",
         f"https://assets.sia.toyota.com/publications/en/om-s/{pub}/pdf/{pub}.pdf",
         "Toyota Motor Corporation", str(year), pdf_note),
    ], note=note)
    v["published"] = "2026-11-19"
    v["modified"] = "2026-11-19"
    v["checked_h"] = "19 Nov 2026"
    return v

RAV4_2019 = _rav4(2019, "OM0R009U",
    "Light bulbs table: W5W front side marker, 19 W H16 fog, 7444NA front turn, WY21W rear turn, W16W back-up. CR2032 in the wireless remote control or electronic key battery section. Headlights and stop lights are on the dealer replacement list.",
    fog_in_chart=True)
RAV4_2020 = _rav4(2020, "OM0R024U",
    "Light bulbs table: W5W front side marker, 19 W H16 fog, 7444NA front turn, WY21W rear turn, W16W back-up. CR2032 in the wireless remote control or electronic key battery section. Headlights and stop lights are on the dealer replacement list.",
    fog_in_chart=True)
RAV4_2021 = _rav4(2021, "OM0R028U",
    "Light bulbs table: W5W front side marker, 19 W H16 fog, 7444NA front turn, WY21W rear turn, W16W back-up. CR2032 in the wireless remote control or electronic key battery section. Headlights and stop lights are on the dealer replacement list.",
    fog_in_chart=True)
RAV4_2022 = _rav4(2022, "OM0R059U",
    "Light bulbs table: W5W front side marker (bulb type), 7444NA front turn (types A/B/C), WY21W rear turn, W16W back-up. Fog lights move to the dealer list. CR2032 in the wireless remote control or electronic key battery section.",
    fog_in_chart=False)
RAV4_2023 = _rav4(2023, "OM0R100U",
    "Light bulbs table: W5W front side marker (bulb type), 7444NA front turn (types A/B/C), WY21W rear turn, W16W back-up. Fog lights on the dealer list. CR2032 in the wireless remote control or electronic key battery section.",
    fog_in_chart=False)
RAV4_2024 = _rav4(2024, "OM0R147U",
    "Light bulbs table: W5W front side marker (bulb type), 7444NA front turn (types A/B/C), WY21W rear turn, W16W back-up. Fog lights on the dealer list. CR2032 in the wireless remote control or electronic key battery section. Canada production book for USA and Canada.",
    fog_in_chart=False)
RAV4_2025 = _rav4(2025, "OM0R063U",
    "Light bulbs table: W5W front side marker (bulb type), 7444NA front turn (types A/B/C), WY21W rear turn, W16W back-up. Fog lights on the dealer list. CR2032 in the wireless remote control or electronic key battery section.",
    fog_in_chart=False)

# Added 20 Nov 2026. Tesla publishes one Model Y manual for 2020 to 2024
# and a separate 2025+ manual. Wiper lengths and the key fob cell match.
# The light description does not, so only those two books get pages.
MODEL_Y_2020 = V(
    "Tesla", "Model Y", 2020, [("tesla", "Model Y")], [
        ("key", "Key fob battery", "Accessory key fob: one CR2032, positive side facing up. The key card section does not print a coin cell. A phone key uses the phone."),
        ("wiper", "Front wiper", "Driver side 26 inches (650 mm). Passenger side 20 inches (500 mm). The replacement blade connector has to match the original blade."),
        ("rear", "Rear wiper", "The windshield wiper chapter does not print a rear blade length."),
        ("head", "Headlight", "The lights chapter describes LED signature lights along the headlight rim. It does not print a bulb trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the lights chapter we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the lights chapter we read."),
    ], [
        ("2020 to 2024 Tesla Model Y Owner's Manual, Windshield Wiper Blades",
         "https://www.tesla.com/ownersmanual/2020_2024_modely/en_us/GUID-197C481B-B4D4-4973-9772-2AF488442CE1.html",
         "Tesla, Inc.", "2020-2024",
         "Driver blade 26 inches (650 mm). Passenger blade 20 inches (500 mm). No rear length in this chapter."),
        ("2020 to 2024 Tesla Model Y Owner's Manual, Keys",
         "https://www.tesla.com/ownersmanual/2020_2024_modely/en_us/GUID-E004FAB7-1C71-448F-9492-CACF301304D2.html",
         "Tesla, Inc.", "2020-2024",
         "Accessory key fob battery type CR2032. The key card section does not print a coin cell."),
        ("2020 to 2024 Tesla Model Y Owner's Manual, Lights",
         "https://www.tesla.com/ownersmanual/2020_2024_modely/en_us/GUID-371B94E9-E74F-4BBB-9A55-5F4182894B99.html",
         "Tesla, Inc.", "2020-2024",
         "LED signature lights along the headlight rim. No bulb trade number in this chapter."),
    ],
    note="Tesla's own manual URL covers model years 2020 through 2024 in one book. This page is that book. 2021, 2022, 2023, and 2024 are not separate pages because the book does not give them a different wiper or key chart. Recalls below are model year 2020 only. The same API returned 23 campaigns for 2021, 20 for 2022, 17 for 2023, and 5 for 2024, retrieved 20 Nov 2026. Look up the VIN.")
MODEL_Y_2020["published"] = "2026-11-20"
MODEL_Y_2020["modified"] = "2026-11-20"
MODEL_Y_2020["checked_h"] = "20 Nov 2026"
MODEL_Y_2020["seo_title"] = "2020 to 2024 Model Y wiper and key fob"

MODEL_Y_2025 = V(
    "Tesla", "Model Y", 2025, [("tesla", "Model Y")], [
        ("key", "Key fob battery", "Accessory key fob: one CR2032, positive side facing up. The key card section does not print a coin cell. A phone key uses the phone."),
        ("wiper", "Front wiper", "Driver side 26 inches (650 mm). Passenger side 20 inches (500 mm). Same lengths as the 2020 to 2024 book. The connector has to match the original blade."),
        ("rear", "Rear wiper", "The windshield wiper chapter does not print a rear blade length."),
        ("head", "Headlight", "The lights chapter describes a front lightbar and a tail lightbar (front lightbar if equipped) used as daytime running lights, parking lights, and tail lights. It does not print a bulb trade number, and it does not repeat the earlier book's signature-light wording."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the lights chapter we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the lights chapter we read. Hazard flashers are the overhead button, not a bulb number."),
    ], [
        ("2025+ Tesla Model Y Owner's Manual, North America, software 2026.2.8",
         "https://www.tesla.com/ownersmanual/modely/en_us/Owners_Manual.pdf",
         "Tesla, Inc.", "2026-02",
         "Wiper lengths on the windshield wiper blades page (driver 26 inches / 650 mm, passenger 20 inches / 500 mm). Key fob battery CR2032 in Replacing the Key Fob Battery. Lightbar description in Controlling Lights. Cover reads 2025+."),
    ],
    note="This is the 2025+ book, not the 2020 to 2024 book. Wiper lengths and the CR2032 key fob match the earlier book. The light description does not. Do not treat a 2020 recall campaign as a 2025 campaign.")
MODEL_Y_2025["published"] = "2026-11-20"
MODEL_Y_2025["modified"] = "2026-11-20"
MODEL_Y_2025["checked_h"] = "20 Nov 2026"
MODEL_Y_2025["seo_title"] = "2025 Model Y wiper size and key fob"

CAMRY_2025 = V(
    "Toyota", "Camry", 2025, [("toyota", "CAMRY HYBRID")], [
        ("key", "Key fob battery", "Lithium battery CR2450. The 2019 to 2024 Camry books print CR2032 instead."),
        ("wiper", "Front wiper", "The manual discusses wiper service position and wiper inserts. It does not print an inch length."),
        ("rear", "Rear wiper", "This sedan manual does not print a rear wiper length."),
        ("head", "Headlight", "Headlights are not in the light bulb table. The maintenance chapter says lamps other than the three bulb-type positions below are LEDs, replaced by a Toyota dealer."),
        ("brake", "Brake light", "Stop lights are in the LED list, not in the bulb table. No stop lamp trade number is printed."),
        ("turn", "Turn signal", "Front turn signal and parking lights, bulb type: 7444NA, 28/8 W, wedge base amber. Rear turn signal lights, bulb type: WY21W, 21 W, wedge base amber. Back-up lights, bulb type: W16W, 16 W, wedge base clear. There is no W5W side marker row and no 921 row, unlike the 2019 to 2024 table."),
    ], [
        ("2025 Toyota Camry Hybrid Owner's Manual, publication OM06266U",
         "https://assets.sia.toyota.com/publications/en/om-s/OM06266U/pdf/OM06266U.pdf",
         "Toyota Motor Corporation", "2025",
         "Software identifier camry.2025.2403.hev.vh. Light bulb table page 492: 7444NA, WY21W, W16W. CR2450 in the electronic key battery section. LED sentence in Do-it-yourself maintenance."),
    ],
    note="NHTSA files this year under CAMRY HYBRID, and that is the model name used for the recall list. We did not find a separate 2025 gas Camry owner's manual on Toyota's manual host. The 2019 to 2024 gas books are the CR2032 and 921 chart on the 2023 page.")
CAMRY_2025["published"] = "2026-11-20"
CAMRY_2025["modified"] = "2026-11-20"
CAMRY_2025["checked_h"] = "20 Nov 2026"
CAMRY_2025["seo_title"] = "2025 Camry key fob battery is CR2450"

# Added 21 Nov 2026. Fifth-generation CR-V books (2020 and 2022) share
# the halogen-or-LED headlight chart, the 16 W back-up bulb, and both
# remote cells. 2021 was not opened, so it is not copied onto this page.
CRV_2020 = V(
    "Honda", "CR-V", 2020, [("honda", "CR-V")], [
        ("key", "Key fob battery", "Master keys with a remote transmitter: CR1620. Keyless remote: CR2032. The 2022 book prints the same two cells. The 2023 to 2025 books print only the CR2032."),
        ("wiper", "Front wiper", "Checking and Maintaining Wiper Blades describes replacing the rubber. The 2020 book and the 2022 book do not print a driver or passenger inch length."),
        ("rear", "Rear wiper", "The rear-wiper section describes changing the rubber. Neither the 2020 book nor the 2022 book prints an inch length."),
        ("head", "Headlight", "Low beam: 55 W (H11) on halogen bulb type models, or LED. High beam: 60 W (HB3) on halogen bulb type models, or LED. The book says LED headlights are replaced as an assembly by a dealer."),
        ("brake", "Brake light", "Brake, taillight, rear turn signal, and rear side marker lights are LED. High-mount brake light is LED. Have a dealer replace those assemblies. Back-up light: 16 W."),
        ("turn", "Turn signal", "Front turn signal and front side marker lights: LED. Parking and daytime running lights: LED. Rear turn signal is LED, in the brake and taillight assembly, not a separate 21 W bulb. Side turn signals on the door mirrors: LED."),
    ], [
        ("2020 Honda CR-V Owner's Manual",
         "https://techinfo.honda.com/rjanisis/pubs/OM/AH/ATLA2020OM/enu/ATLA2020OM.PDF",
         "American Honda Motor Co., Inc.", "2019-10",
         "Official Honda PDF, file ATLA2020OM, created 3 Oct 2019. Opened 21 Nov 2026. Specifications light-bulb table and Remote Transmitter Care: CR1620 and CR2032. Back-up light 16 W. No wiper inch length."),
        ("2022 Honda CR-V Owner's Manual",
         "https://cdn.dealereprocess.org/cdn/servicemanuals/honda/2022-crv.pdf",
         "American Honda Motor Co., Inc.", "2022",
         "Dealer-hosted copy of the Honda book. Opened 21 Nov 2026. Same two remote cells, same H11 and HB3 halogen rows, same LED rows, and the same 16 W back-up light. No wiper inch length."),
    ],
    note="This page is the 2020 book and the 2022 book. They print the same chart, so 2022 is not a second page. A 2021 CR-V owner's manual was not opened on 21 Nov 2026, and this chart is not copied onto 2021. The 2023 to 2025 chart is different and lives on the 2025 page. Recalls below are model year 2020 only. NHTSA's recalls API, retrieved 21 Nov 2026, returned 4 campaigns for 2021 and 3 for 2022. Look up the VIN.")
CRV_2020["published"] = "2026-11-21"
CRV_2020["modified"] = "2026-11-21"
CRV_2020["checked_h"] = "21 Nov 2026"
CRV_2020["seo_title"] = "2020 and 2022 CR-V: H11 or LED"

# Added 21 Nov 2026. Gas Corolla sedan only. 2020, 2021, and 2022 print
# one CR2032 key and the same exterior bulb table, so they are one page.
# 2023 and 2024 split the key and add an LED front side marker row.
COROLLA_2020 = V(
    "Toyota", "Corolla", 2020, [("toyota", "COROLLA")], [
        ("key", "Key fob battery", "Lithium battery CR2032. The 2020, 2021, and 2022 gas books print that cell for the wireless remote and the electronic key. They do not print a CR2450."),
        ("wiper", "Front wiper", "The maintenance chapter has a wiper insert procedure. None of the 2020, 2021, or 2022 books prints an inch length."),
        ("rear", "Rear wiper", "This sedan manual does not print a rear wiper length."),
        ("head", "Headlight", "A headlight trade number is not in the light bulb table. Headlights and daytime running lights are on the list of bulbs your Toyota dealer replaces."),
        ("brake", "Brake light", "Stop lights, tail lights, and the high mounted stoplight are on the dealer list. No stop lamp trade number is printed."),
        ("turn", "Turn signal", "Front side marker lights: 5 W, wedge base clear, no trade number. Front turn signal and parking lights, vehicles without side turn signal lights: 7444NA, 28/8 W, wedge base amber. Rear side marker lights, bulb type: 5 W, wedge base clear, no trade number. Rear turn signal lights: 21 W, wedge base amber, no trade number. Back-up lights: 16 W, wedge base clear, no trade number. Vehicles with side turn signal lights move the front turn and parking lights onto the dealer list."),
    ], [
        ("2020 Toyota Corolla Owner's Manual, publication OM02580U",
         "https://assets.sia.toyota.com/publications/en/om-s/OM02580U/pdf/OM02580U.pdf",
         "Toyota Motor Corporation", "2020-01",
         "Helm lists OM02580U as the 2020 Corolla owner's manual. Opened 21 Nov 2026. Light bulb table: front side marker 5 W, 7444NA front turn, rear side marker 5 W, rear turn 21 W, back-up 16 W. CR2032 in the electronic key battery section. Headlights and stop lights are on the dealer list."),
        ("2021 Toyota Corolla Owner's Manual, publication OM02582U",
         "https://assets.sia.toyota.com/publications/en/om-s/OM02582U/pdf/OM02582U.pdf",
         "Toyota Motor Corporation", "2020-07",
         "Helm lists OM02582U as the 2021 Corolla owner's manual. Opened 21 Nov 2026. Same CR2032 line and the same exterior bulb table and dealer list as OM02580U."),
        ("2022 Toyota Corolla Owner's Manual, publication OM02617U",
         "https://assets.sia.toyota.com/publications/en/om-s/OM02617U/pdf/OM02617U.pdf",
         "Toyota Motor Corporation", "2021-07",
         "Helm lists OM02617U as the 2022 Corolla owner's manual, English paper. PDF created 15 July 2021. Opened 21 Nov 2026. Light bulb table on printed page 560 matches the 2020 and 2021 tables. CR2032 only."),
    ],
    note="Gas sedan books only. Not the Corolla Hybrid, not the hatchback, and not the Corolla Cross. This page is the 2020, 2021, and 2022 chart. The 2023 and 2024 books split the key and are on the 2023 page. Recalls below are model year 2020 only. NHTSA's recalls API, retrieved 21 Nov 2026, returned 1 campaign for 2021 and no campaign list for 2022 (HTTP 400 with Count 0). Look up the VIN.")
COROLLA_2020["published"] = "2026-11-21"
COROLLA_2020["modified"] = "2026-11-21"
COROLLA_2020["checked_h"] = "21 Nov 2026"
COROLLA_2020["seo_title"] = "2020 to 2022 Corolla key is CR2032"

COROLLA_2023 = V(
    "Toyota", "Corolla", 2023, [("toyota", "COROLLA")], [
        ("key", "Key fob battery", "CR2032 on vehicles without a smart key system, or CR2450 on vehicles with a smart key system. The 2020 to 2022 gas books print CR2032 only."),
        ("wiper", "Front wiper", "The maintenance chapter has a wiper insert procedure. The 2023 and 2024 books do not print an inch length."),
        ("rear", "Rear wiper", "This sedan manual does not print a rear wiper length."),
        ("head", "Headlight", "A headlight trade number is not in the light bulb table. Headlights and daytime running lights are on the list of bulbs your Toyota dealer replaces."),
        ("brake", "Brake light", "Stop lights, tail lights, and the high mounted stoplight are on the dealer list. No stop lamp trade number is printed."),
        ("turn", "Turn signal", "Front side marker lights, bulb type: 5 W, wedge base clear, no trade number. Front turn signal and parking lights, vehicles without side turn signal lights: 7444NA, 28/8 W, wedge base amber. Rear side marker lights, bulb type: 5 W, wedge base clear, no trade number. Rear turn signal lights: 21 W, wedge base amber, no trade number. Back-up lights: 16 W, wedge base clear, no trade number. The dealer list adds front side marker lights (LED type), which the 2020 to 2022 dealer list does not."),
    ], [
        ("2023 Toyota Corolla Owner's Manual, publication OM02568U",
         "https://assets.sia.toyota.com/publications/en/om-s/OM02568U/pdf/OM02568U.pdf",
         "Toyota Motor Corporation", "2023-04",
         "Software identifier om02568u.corolla.2023.2304.cv.vh. Opened 21 Nov 2026. Light bulb table on printed page 398. CR2032 or CR2450 in the electronic key battery section. Dealer list includes front side marker lights (LED type)."),
        ("2023 Toyota Corolla Owner's Manual, earlier printing OM02525U",
         "https://assets.sia.toyota.com/publications/en/om-s/OM02525U/pdf/OM02525U.pdf",
         "Toyota Motor Corporation", "2022-11",
         "Software identifier om02525u.corolla.2023.2211.cv.vh. Opened 21 Nov 2026. Same key line, same exterior wattage table, and the same LED front side marker line as OM02568U."),
        ("2024 Toyota Corolla Owner's Manual, publication OM02684U",
         "https://assets.sia.toyota.com/publications/en/om-s/OM02684U/pdf/OM02684U.pdf",
         "Toyota Motor Corporation", "2023-09",
         "Software identifier om02684u.corolla.2024.2309.cv.vh. Opened 21 Nov 2026. Same CR2032 or CR2450 line and the same exterior table. Dealer list includes front side marker lights (LED type)."),
    ],
    note="Gas sedan books only. The software identifiers say corolla.2023 and corolla.2024, not the hybrid file. This page is the 2023 chart and the 2024 chart. Recalls below are model year 2023 only. NHTSA's recalls API, retrieved 21 Nov 2026, returned 2 campaigns for 2024. A 2025 gas Corolla owner's manual was not on the publication list we opened. The Corolla Hybrid 2025 book is a different car.")
COROLLA_2023["published"] = "2026-11-21"
COROLLA_2023["modified"] = "2026-11-21"
COROLLA_2023["checked_h"] = "21 Nov 2026"
COROLLA_2023["seo_title"] = "2023 Corolla key is CR2032 or CR2450"

WAVE2.extend([CAMRY_2023, ACCORD_2023, CRV_2020, COROLLA_2020, COROLLA_2023,
              RAV4_2019, RAV4_2020, RAV4_2021, RAV4_2022, RAV4_2023, RAV4_2024, RAV4_2025,
              MODEL_Y_2020, MODEL_Y_2025, CAMRY_2025])

for _v in WAVE2:
    if _v["make"] == "Chevrolet" and _v["model"] == "Equinox" and _v["year"] in ("2020", "2021", "2022"):
        if _v["year"] == "2022":
            _v["modified"] = "2026-11-21"
            _v["checked_h"] = "21 Nov 2026"
            _v["seo_title"] = "2022 Equinox driver wiper is 84566977"
        else:
            _v["modified"] = "2026-11-20"
            _v["checked_h"] = "20 Nov 2026"
            if _v["year"] == "2020":
                _v["seo_title"] = "2020 Equinox wipers: 23.6, 17.7, 11.8 in"
            else:
                _v["seo_title"] = "2021 Equinox wipers print 24, 18, and 12"
    if _v["make"] == "Chevrolet" and _v["model"] == "Malibu" and _v["year"] == "2020":
        _v["modified"] = "2026-11-21"
        _v["checked_h"] = "21 Nov 2026"
        _v["seo_title"] = "2020 Malibu wipers are 25.6 and 17.7"
    if _v["make"] == "Nissan" and _v["model"] == "Sentra" and _v["year"] == "2021":
        _v["modified"] = "2026-11-20"
