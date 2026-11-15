DELIMITER = ";"

class TIMESTAMP:
    weekday = ""
    hour = 0
    consumption = 0.0
    price = 0.0

def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    with open(PFilename, "r", encoding="utf-8") as source:
        source.readline()
        for Line in source:
            Row = Line.rstrip()
            if len(Row) == 0:
                continue
            Column = Row.split(DELIMITER)
            Stamp = TIMESTAMP()
            Stamp.weekday = Column[0]
            Stamp.hour = int(Column[1])
            Stamp.consumption = float(Column[2])
            Stamp.price = float(Column[3])
            PTimestamps.append(Stamp)
            Column.clear()
    return None

def displayTimestamps(PTimestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for TIMESTAMP in PTimestamps:
        Total = TIMESTAMP.consumption * TIMESTAMP.price
        print(" - {} {:02d}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(
            TIMESTAMP.weekday, TIMESTAMP.hour, TIMESTAMP.price, TIMESTAMP.consumption, Total))
    return None

def main():
    Timestamps: list[TIMESTAMP] = []
    print("Program starting")
    Filename = input("Insert filename: ")
    readTimestamps(Filename, Timestamps)
    displayTimestamps(Timestamps)
    Timestamps.clear()
    print("Program ending")
    return None

if __name__ == "__main__":
    main()