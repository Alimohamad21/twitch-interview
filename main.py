def extract_num(word):
    number = ""
    token = ""
    for letter in word:
        if letter.isdigit():
            number = number + letter
        else:
            token = token + letter
    if not len(number):
        number = 0
    return [int(number), token]  # extracts number of bits,cheer without number of bits


def solution(min_cheermote_amount, valid_cheermotes, messages):
    cheer_count = dict()
    output = []
    for cheer in valid_cheermotes:
        cheer_count[cheer] = 0
    message_list = messages.split(',')
    for message in message_list:
        total_bits = 0
        tokens = message.split()
        temp_cheer_count = cheer_count.copy()
        for token in tokens:
            filtered_token = extract_num(token)[1]
            if filtered_token in valid_cheermotes:
                bits = extract_num(token)[0]
                total_bits = total_bits + bits
                if total_bits > 1000000 or bits < min_cheermote_amount or bits > 10000:
                    cheer_count = temp_cheer_count
                    break
                else:
                    cheer_count[filtered_token] = cheer_count[filtered_token] + bits
    new_dict = dict()
    for k, v in cheer_count.items():
        new_dict[v] = k
    sorted_cheers = dict(reversed(sorted(new_dict.items())))  # sort dict in descending order
    for k, v in sorted_cheers.items():
        if k > 0:
            output.append(v + str(k))
    if not len(output):
        output = "NO_CHEERS"
    return output


print(solution(5, ["cheer", "party", "pogchamp"],
               "cheer1 cheer10 pogchamp1 wow!, cheer5 cheer10 this is amazing, party50 party50 lets have a party!"))
