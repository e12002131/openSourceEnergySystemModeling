from funktionen import importSynthload, initializeLoadProfile, addLoad, pickDay
from IPython.display import display

# import synthload2024.xlsx
synthload = importSynthload()

# initialize load
load = initializeLoadProfile(synthload)

# add H0, G0, G1, G2 and G3 load
load = addLoad(synthload, load, 'H0', 8000)
load = addLoad(synthload, load, 'G0', 8000)
load = addLoad(synthload, load, 'G1', 8000)
load = addLoad(synthload, load, 'G2', 8000)
load = addLoad(synthload, load, 'G3', 8000)

# pick day 10
day_of_load = pickDay(load, 10)

# display 'day_of_load'
display(day_of_load)





