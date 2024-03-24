def GUI_FREQ_ANALYSIS():
    import matplotlib.pylab as plb
    LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def frequency_analyis(text):
        text = text.upper()
        letter_freqency = {}
        for letter in LETTERS:
            letter_freqency[letter] = 0
        for letter in text:
            if letter in LETTERS:
                letter_freqency[letter] += 1
        return letter_freqency
    def plot_distribution(frequencies):
        plb.bar(frequencies.keys(),frequencies.values())
        plb.show()
    if __name__== '__main__':
        #plain_text = "Shannon defined the quantity of information produced by a source"
        #freq = frequency_analyis(plain_text)
        #plot_distribution(freq)
        import ipywidgets as widgets
        from ipywidgets import HBox, VBox
        import numpy as np
        import matplotlib.pyplot as plt
        from IPython.display import display
        %matplotlib inline
        @widgets.interact
        def f(BOX=widgets.Text(value='Shannon defined the quantity of information produced by a source', disabled=False)):
            print(BOX,sep='\n')
            plain_text = BOX
            freq = frequency_analyis(plain_text)
            plot_distribution(freq)
#
GUI_FREQ_ANALYSIS()

#done!
#what you enter in the message box "BOX" (feel free to change "BOX" #to something else xD)  you will see  -  the graph  -  live update #when you change the text, so yea :) that's it 

