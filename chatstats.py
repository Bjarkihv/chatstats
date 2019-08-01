# ChatStats - Calculates various statistics from a single Facebook chat (message count, word count, reactions, etc.)
# and presents them in a visual fashion through charts and tables.
# Usage: download chat .json files from your Facebook and select the one you would like to analyze ...

import json

with open('message_1.json') as f:
    data = json.load(f)
    datam = data['messages']

participants = data['participants']


# Takes a word as an argument and counts how many times each chat participant said the word
def wordCount(s):
    d = {}
    for y in range(len(participants)):
        d[participants[y]['name']] = 0
    for x in datam:
        if 'content' in x:
            if s in x['content'].encode("ISO 8859-1").decode("utf-8"):
                for y in range(len(participants)):
                    if x['sender_name'] == participants[y]['name']:
                        d[participants[y]['name']] += 1
    return d


# Takes no argument, counts how many reactions each chat participant sent and how many they received
def reactionCount():
    # gera dictionary í dictionary
    reactionsGotten = {}
    reactionsGiven = {}
    for y in range(len(participants)):
        reactionsGotten[participants[y]['name']] = {}
        reactionsGiven[participants[y]['name']] = {}
    for w in range(len(reactionsGotten)):
        reactionsGotten[participants[w]['name']]['like'] = 0
        reactionsGotten[participants[w]['name']]['dislike'] = 0
        reactionsGotten[participants[w]['name']]['lol'] = 0
        reactionsGotten[participants[w]['name']]['love'] = 0
        reactionsGotten[participants[w]['name']]['wow'] = 0
        reactionsGotten[participants[w]['name']]['angry'] = 0
        reactionsGotten[participants[w]['name']]['sad'] = 0
        reactionsGiven[participants[w]['name']]['like'] = 0
        reactionsGiven[participants[w]['name']]['dislike'] = 0
        reactionsGiven[participants[w]['name']]['lol'] = 0
        reactionsGiven[participants[w]['name']]['love'] = 0
        reactionsGiven[participants[w]['name']]['wow'] = 0
        reactionsGiven[participants[w]['name']]['angry'] = 0
        reactionsGiven[participants[w]['name']]['sad'] = 0
    for x in datam:
        if 'content' in x or 'gifs' in x or 'photos' in x:
            if 'reactions' in x:
                bla = x['reactions']
                for w in range(len(bla)):
                    if bla[w]['reaction'] == 'ð\x9f\x91\x8d':  # like
                        for y in range(len(participants)):
                            if x['sender_name'] == participants[y]['name']:
                                reactionsGotten[participants[y]
                                                ['name']]['like'] += 1
                            if bla[w]['actor'] == participants[y]['name']:
                                reactionsGiven[participants[y]
                                               ['name']]['like'] += 1
                    if bla[w]['reaction'] == 'ð\x9f\x91\x8e':  # dislike
                        for y in range(len(participants)):
                            if x['sender_name'] == participants[y]['name']:
                                reactionsGotten[participants[y]
                                                ['name']]['dislike'] += 1
                            if bla[w]['actor'] == participants[y]['name']:
                                reactionsGiven[participants[y]
                                               ['name']]['dislike'] += 1
                    if bla[w]['reaction'] == 'ð\x9f\x98\x86':  # lol
                        for y in range(len(participants)):
                            if x['sender_name'] == participants[y]['name']:
                                reactionsGotten[participants[y]
                                                ['name']]['lol'] += 1
                            if bla[w]['actor'] == participants[y]['name']:
                                reactionsGiven[participants[y]
                                               ['name']]['lol'] += 1
                    if bla[w]['reaction'] == 'ð\x9f\x98\x8d':  # love
                        for y in range(len(participants)):
                            if x['sender_name'] == participants[y]['name']:
                                reactionsGotten[participants[y]
                                                ['name']]['love'] += 1
                            if bla[w]['actor'] == participants[y]['name']:
                                reactionsGiven[participants[y]
                                               ['name']]['love'] += 1
                    if bla[w]['reaction'] == 'ð\x9f\x98®':  # wow
                        for y in range(len(participants)):
                            if x['sender_name'] == participants[y]['name']:
                                reactionsGotten[participants[y]
                                                ['name']]['wow'] += 1
                            if bla[w]['actor'] == participants[y]['name']:
                                reactionsGiven[participants[y]
                                               ['name']]['wow'] += 1
                    if bla[w]['reaction'] == 'ð\x9f\x98\xa0':  # angry
                        for y in range(len(participants)):
                            if x['sender_name'] == participants[y]['name']:
                                reactionsGotten[participants[y]
                                                ['name']]['angry'] += 1
                            if bla[w]['actor'] == participants[y]['name']:
                                reactionsGiven[participants[y]
                                               ['name']]['angry'] += 1
                    if bla[w]['reaction'] == 'ð\x9f\x98¢':  # sad
                        for y in range(len(participants)):
                            if x['sender_name'] == participants[y]['name']:
                                reactionsGotten[participants[y]
                                                ['name']]['sad'] += 1
                            if bla[w]['actor'] == participants[y]['name']:
                                reactionsGiven[participants[y]
                                               ['name']]['sad'] += 1
    return reactionsGotten, reactionsGiven

# Counts the most common form of "haha" in the chat


def hahaCount():
    count = 0
    d = {"haha": 0, "hahaha": 0, "hahahaha": 0, "hahahahaha": 0, "megahaha": 0}
    for x in datam:
        count = count + 1
        if 'content' in x:
            if x['content'] == 'haha' or x['content'] == 'hahah':
                d["haha"] += 1
            if x['content'] == 'hahaha' or x['content'] == 'hahahah':
                d["hahaha"] += 1
            if x['content'] == 'hahahaha' or x['content'] == 'hahahahah':
                d["hahahaha"] += 1
            if x['content'] == 'hahahahaha' or x['content'] == 'hahahahahah':
                d["hahahahaha"] += 1
            if 'hahahahahaha' in x['content']:
                d["megahaha"] += 1
                # print(datam[count])
                # print(x)
    return d

# Counts how many times each participant has left the group


def leaveCount():
    d = {}
    for y in range(len(participants)):
        d[participants[y]['name']] = 0
    for x in datam:
        if 'content' in x:
            for y in range(len(participants)):
                if x['content'] == participants[y]['name'] + ' left the group.':
                    d[participants[y]['name']] += 1
    return d

# Finds the longest message ever sent in the chat


def longestMsg():
    lengstamsg = 0
    maxlength = 0
    count = 0
    for x in datam:
        count = count + 1
        if 'content' in x:
            if len(x['content'].encode("ISO 8859-1").decode("utf-8")) > maxlength:
                maxlength = len(x['content'].encode(
                    "ISO 8859-1").decode("utf-8"))
                lengstamsg = datam[count -
                                   1]['content'].encode("ISO 8859-1").decode("utf-8")
    return lengstamsg

# Counts how many messages each participant has sent


def messageCount():
    d = {}
    for y in range(len(participants)):
        d[participants[y]['name']] = 0
    for x in datam:
        if 'content' in x:
            for y in range(len(participants)):
                if x['sender_name'] == participants[y]['name']:
                    d[participants[y]['name']] += 1
    return d


print(wordCount("haha"))
print(messageCount())
print(leaveCount())
print(longestMsg())
print(hahaCount())
print(reactionCount())
