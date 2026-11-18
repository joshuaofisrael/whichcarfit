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
        ("wiper", "Front wiper", "Driver side: 23.6 in. Passenger side: 17.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "Rear: 11.8 in. Length is from the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2020 Chevrolet Equinox Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/chevrolet/equinox/2020-chevrolet-equinox-owners-manual.pdf", "General Motors LLC", "2020", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
    V("Chevrolet", "Malibu", 2020, [('chevrolet', 'MALIBU')], [
        ("key", "Key fob battery", "The owner's manual says to replace the remote battery with a CR2032, or equivalent."),
        ("wiper", "Front wiper", "Driver side: 25.6 in. Passenger side: 17.7 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "No rear wiper length is printed in the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2020 Chevrolet Malibu Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/chevrolet/malibu/2020-chevrolet-malibu-owners-manual.pdf", "General Motors LLC", "2020", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
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
        ("wiper", "Front wiper", "Driver side: 24 in. Passenger side: 18 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "Rear: 12 in. Length is from the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2021 Chevrolet Equinox Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2021/chevrolet/equinox/2021-chevrolet-equinox-owners-manual.pdf", "General Motors LLC", "2021", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
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
        ("wiper", "Front wiper", "Driver side: 24 in. Passenger side: 18 in. Lengths are from the maintenance parts table."),
        ("rear", "Rear wiper", "Rear: 12 in. Length is from the maintenance parts table."),
        ("head", "Headlight", "The bulb replacement chapter says this vehicle has several LED lamps and to contact a dealer for an LED assembly. The procedure we read does not print a halogen trade number."),
        ("brake", "Brake light", "A brake lamp trade number is not printed in the section we read."),
        ("turn", "Turn signal", "A turn signal trade number is not printed in the section we read."),
    ], [
        ("2022 Chevrolet Equinox Owner's Manual", "https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2022/chevrolet/equinox/2022-chevrolet-equinox-owners-manual.pdf", "General Motors LLC", "2022", "Remote battery CR2032. Maintenance parts table for wiper length. Bulb replacement chapter."),
    ],
    note=""),
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
    note=""),
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
note="The light bulb table lists only the bulb-type lamps (turn signals, side markers, back-up lights). Every lamp missing from that table is LED on this model, per the table's own footnote, not a gap in what we read.")
CAMRY_2023["published"] = "2026-11-18"
CAMRY_2023["modified"] = "2026-11-18"
CAMRY_2023["checked_h"] = "18 Nov 2026"

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

WAVE2.extend([CAMRY_2023, ACCORD_2023])
