from operator import mul

def main():
    input = open("input.txt", "r")
    rules = []
    ranges = []
    your_ticket = []
    valid = []
    for section, group in enumerate(input.read().split("\n\n")):
        if section == 0:
            for rule in group.splitlines():
                (field, rule_ranges) = [column.strip() for column in rule.split(":")]
                rule_ranges = [[int(_min), int(_max)] for (_min, _max) in list(_range.split("-") for _range in rule_ranges.split(" or "))]

                full_range = []
                for rule_range in rule_ranges:
                    for i in range(rule_range[0], rule_range[1] + 1):
                        full_range.append(i)
                        if i not in ranges:
                            ranges.append(i)
                rules.append([field, full_range])
        elif section == 1:
            your_ticket = [int(value) for value in group.splitlines()[1].split(",")]
        elif section == 2:
            tickets = [ticket.split(",") for ticket in group.splitlines()[1:]]
            tickets = [[int(value) for value in ticket] for ticket in tickets]
            for ticket in tickets:
                for value in ticket:
                    if value not in ranges:
                        break
                else:
                    valid.append(ticket)
                    continue

    checked = []
    fields = []
    positions = [[x[i] for x in valid] for i in range(len(ticket))]
    departure_vals = []
    while len(fields) < len(your_ticket):
        for (pos, position) in enumerate(positions):
            if pos in checked:
                continue
            options = []
            for rule in rules:
                if all(elem in rule[1] for elem in position) and rule[0] not in fields:
                    options.append(rule[0])
            if len(options) == 1:
                checked.append(pos)
                fields.append(options[0])
                if options[0].startswith("departure"):
                    departure_vals.append(your_ticket[pos])
                break

    print(reduce(mul, departure_vals, 1))
if __name__ == "__main__":
    main()
