import matplotlib.pylab as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):
    text = text.upper()
    letter_frequency = {}

    for letter in LETTERS:
        letter_frequency[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequency[letter] += 1

    return letter_frequency

def plot_distribution(letter_frequency):
    plt.bar(letter_frequency.keys(), letter_frequency.values())
    plt.show()

def caesar_crack(text):
    freq = frequency_analysis(text)
    freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
    print("the possible key value: %s" % (LETTERS.find(freq[0][0])-LETTERS.find('E')))

if __name__ == '__main__':
    cipher_text = 'UGVIUMQAJITIHAPWTKHMZQIUNZWUJCLIXMABPCVOIZGQIUYCITQNQMLIAIXPGAQKQABIBBPMUWUMVBQIUEWZSQVOIAIAQUCTIBQWVMVOQVMMZIBIUCTBQVIBQWVITKWUXIVGQPIDMJMMVQVBMZMABMLQVITOWZQBPUAIVLLIBIABZCKBCZMAIVLQBAQUXTMUMVBIBQWVAMAXMKQITTGQVRIDIAQVKMCVQDMZAQBGTIBMZWVQOWBIKYCIQVBMLEQBPUIKPQVMTMIZVQVOBMKPVQYCMAIZBQNQKQITQVBMTTQOMVKMVCUMZQKITUMBPWLAIVLZMKQXMAACKPIAAWTDQVOLQNNMZMVBQITMYCIBQWVATQVMIZITOMJZIQVBMZXWTIBQWVIVLMFBZIXWTIBQWVBPMAMBPQVOAUIGXZWDMBWJMDMZGDMZGQUXWZBIVBQVAMDMZITNQMTLAAWNBEIZMMVOQVMMZQVOZMAMIZKPIVLLMDMTWXUMVBWZQVDMABUMVBJIVSQVOQPIDMIAXMKQITILLQKBQWVBWYCIVBQBIBQDMUWLMTAACKPIABPMJTIKSAKPWTMAUWLMTWZBPMUMZBWVUWLMT'
    caesar_crack(cipher_text) 