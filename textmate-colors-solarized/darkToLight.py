# This is a script that takes the inverse of the dark theme
# to create the light theme.
f = open('Solarized (dark).tmTheme', 'r')
g = open('Solarized (light).tmTheme', 'w')

replaceDict = {'#002B36': '#FDF6E3',
'#073642': '#EEE8D5',
'#586E75': '#93A1A1',
'#657B83': '#839496',
'#839496': '#657B83',
'#93A1A1': '#586E75',
'#EEE8D5': '#073642',
'#FDF6E3': '#002B36'}

for line in f:
    for k,v in replaceDict.iteritems():
        if k in line:
            line = line.replace(k,v)
            break
    g.write(line)

f.close()
g.close()

