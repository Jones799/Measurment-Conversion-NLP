import re
from nltk.stem import WordNetLemmatizer
import decimal





Input = "how many ounces in three cups"






wnl = WordNetLemmatizer()


def is_number(x):
    if type(x) == str:
        x = x.replace(',', '')
    try:
        float(x)
    except:
        return False
    return True

def text2int (textnum, numwords={}):
    units = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen',
    ]
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']
    ordinal_words = {'first':1, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    if not numwords:
        numwords['and'] = (1, 0)
        for idx, word in enumerate(units): numwords[word] = (1, idx)
        for idx, word in enumerate(tens): numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ''
    onnumber = False
    lastunit = False
    lastscale = False

    def is_numword(x):
        if is_number(x):
            return True
        if word in numwords:
            return True
        return False

    def from_numword(x):
        if is_number(x):
            scale = 0
            increment = int(x.replace(',', ''))
            return scale, increment
        return numwords[x]

    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
            lastunit = False
            lastscale = False
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if (not is_numword(word)) or (word == 'and' and not lastscale):
                if onnumber:
                    # Flush the current number we are building
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
                lastunit = False
                lastscale = False
            else:
                scale, increment = from_numword(word)
                onnumber = True

                if lastunit and (word not in scales):
                    # Assume this is part of a string of individual numbers to
                    # be flushed, such as a zipcode "one two three four five"
                    curstring += repr(result + current)
                    result = current = 0

                if scale > 1:
                    current = max(1, current)

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0

                lastscale = False
                lastunit = False
                if word in scales:
                    lastscale = True
                elif word in units:
                    lastunit = True

    if onnumber:
        curstring += repr(result + current)

    return curstring
def Convert(string):
    li = list(string.split(" "))
    return li




input1 = text2int(Input)





units = ["cup", "gallon", "teaspoon", "tablespoon", "liter", "ounce", "quart", "milliliter",
         "cups", "gallons", "teaspoons", "tablespoons", "liters", "ounces", "quarts", "milliliters"]

units2 = (Convert(Input))
Input2 = [wnl.lemmatize(i) for i in units2]


Calculations = {"cup gallon": ".0625", "cup teaspoon":"48", "cup tablespoon":"16", "cup liter":".23657", "cup ounce":"8", "cup quart":".25", "cup milliliter":"236.6",
                "gallon cup":"19.215", "gallon teaspoon":"922.3", "gallon tablespoon":"307.4", "gallon liter":"4.546", "gallon ounce":"153.7", "gallon quart":"4.804", "gallon milliliter":"4546",
                "teaspoon cup":".02083", "teaspoon gallon":".001302", "teaspoon tablespoon":".3333", "teaspoon liter":".004928", "teaspoon ounce":".16666", "teaspoon quart":".0052083", "teaspoon milliliter":"4.929",
                "tablespoon cup":".0625", "tablespoon gallon":".00390625", "tablespoon teaspoon":"3", "tablespoon liter":".0147868", "tablespoon ounce":".500001", "":"", "tablespoon quart":".0156", "tablespoon milliliter":"14.787", "liter cup":"4.227",
                "liter gallon":".26417", "liter teaspoon":"202.9", "liter tablespoon":"67.628", "liter ounce":"33.814", "liter quart":"1.057", "liter milliliter":"1000",
                "ounce cup": "0.125", "ounce gallon": ".00781", "ounce teaspoon": "6", "ounce tablespoon": "2", "ounce liter": ".029573", "ounce quart": ".03125", "ounce milliliter": "29.574",
                "quart cup": "4", "quart gallon": ".25", "quart teaspoon": "192", "quart tablespoon": "64", "quart liter": ".94607", "quart ounce": "32", "quart milliliter": "946.4",
                "milliliter cup": ".004226", "milliliter gallon": ".000264172", "milliliter teaspoon": ".20288", "milliliter tablespoon": ".067628", "milliliter liter": ".001", "milliliter ounce": ".0338", "milliliter quart": ".00105669"}

if any(x in Input for x in units):
    AllMatch = [x for x in Input2 if x in units]
    firstWord = next((x for x in Input2 if x in units), "False")
    try:
        LastWord = (AllMatch[1])
        number_first = (firstWord + " " + LastWord)
        number_second = (LastWord + " " + firstWord)
        FirstWordNumber = input1.split(firstWord, 1)[0]
        SecondWordNumber = input1.split(firstWord, 1)[1]
        first = (re.findall('[0-9]+', FirstWordNumber))
        second = (re.findall('[0-9]+', SecondWordNumber))
        first1 = ' '.join(map(str,first))
        second1 = ' '.join(map(str, second))
        if len(first1.split()) > 0:
            result1 = (Calculations[number_first])
            numberone = decimal.Decimal(first1)
            numbertwo = decimal.Decimal(result1)
            answer = numberone * numbertwo
            answerround = "%.1f" % (answer)
            answer1 = str(answerround)
            beginning = ('there are approximatly ' + answer1 + ' ' + LastWord + "s" + " in " + first1 + " " + firstWord + "s")
            print(beginning)
        else:
            print('')
        if len(second1.split()) > 0:
            result1 = (Calculations[number_second])
            numberone = decimal.Decimal(second1)
            numbertwo = decimal.Decimal(result1)
            answer = numberone * numbertwo
            answerround = "%.1f" % (answer)
            answer1 = str(answerround)
            beginning = ('there are approximately ' + answer1 + ' ' + firstWord + "s" + " in " + second1 + " " + LastWord + "s")
            print(beginning)
        else:
            print('')
    except IndexError:
        pass

    #result = (Calculations[firstWord])
else:
    print("nope")

#From Cup to Gallon Devide cup by 16 for gallon

