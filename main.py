elves = []
calories = []


def start():
    count = 0
    with open('input.txt', mode='r') as f:
        for item in f:
            item = item.replace('\n', '')
            if item != '':
                elves.append(
                    {
                        "calories": [],
                        "sum-calories": 0,
                    })
                elves[count]["calories"] += [int(item)]
                elves[count]["sum-calories"] = sum(elves[count]["calories"])

            else:
                calories.append(elves[count]["sum-calories"])
                count += 1

    max_calories = max(calories)
    print(max_calories)


if __name__ == '__main__':
    start()
