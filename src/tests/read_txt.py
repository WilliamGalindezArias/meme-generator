with open('../_data/SimpleLines/SimpleLines.txt', mode='r') as file:
    lines = file.readlines()
    #print(lines)
    for line in lines:
        line = line.strip('\n')
        line = line.split('-')
        if len(line) > 1:
            print(line)
            print(line[0], line[1])

        #print(line)

    #item_split = [line.split('-') for line in lines]
    #quotes = [line.replace('-', ' ').replace('"', '') for line in lines]
    #print(f'the quotes are: {quotes}')
    #item_split = [quote.split('  ') for quote in quotes]
    #print(quotes[0])
    #print('the list split,', item_split)
    #print('quote,', item_split[0][0])
    #print('author', item_split[0][1])
    #last = [item[1] for item in item_split]
    #print(last)