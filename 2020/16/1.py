def main():
    input = open("input.txt", "r")
    ranges = []
    for section, group in enumerate(input.read().split("\n\n")):
        if section == 0:
            for rule in group.splitlines():
                rule_ranges = [column.strip() for column in rule.split(":")][1]
                rule_ranges = [[int(_min), int(_max)] for (_min, _max) in list(_range.split("-") for _range in rule_ranges.split(" or "))]
                for rule_range in rule_ranges:
                    for i in range(rule_range[0], rule_range[1] + 1):
                        if i not in ranges:
                            ranges.append(i)
        elif section == 2:
            tickets = [ticket.split(",") for ticket in group.splitlines()[1:]]
            values = [int(value) for ticket in tickets for value in ticket]

            error = 0
            for value in values:
                if value not in ranges:
                    error = error + value

    print(error)

if __name__ == "__main__":
    main()
