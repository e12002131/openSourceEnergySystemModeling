# Aggregated Electrical Load Profiles
With this project you can create aggregated electrical load profiles. The profiles represent the sum of the connected grid users and are used in grid planning and operation.

The basis of this project are default load profiles for different grid usage types (e.g. household H0, business general G0,...) provided by APCS for the year of 2024. Together with the yearly energy consumption for each type a aggregated profile can be created.


Function description (funktionen.py):

- importSynthload():
Returns the contents of synthload2024.xlsx as type DataFrame (contains default load profiles for different grid usage types for the whole year of 2024).

- initializeLoadProfile(DataFrame df_synthload_in):
Creates and initializes a a new DataFrame where the aggregated laod profile will be saved. The df_synthload_in (contents of synthload2024.xlsx) needs to be handed over to carry over the index (timestamps).

- addLoad(DataFrame df_synthload_in, DataFrame df_load_profile_in, String load_profile, float yearly_energy_consumption):
Adds a load to the aggregated load profile df_load_profile_in based on the deafault load profiles in df_synthload_in (contents of synthload2024.xlsx). The grid usage type for the added load needs to be handed as short identifier (e.g. H0, G0,...) as String load_profile. The yearly energy consumption of the given grid usage type is handed over with yearly_energy_consumption. The function returns a new DataFrame which contains the specified additional load added to the load profile df_load_profile_in.

- pickDay(DataFrame df_load_profile_in, int day_of_year):
Returns the load profile for the a day of year specified in day_of_year for a handed over porfile df_load_profile_in.


How to use:

An example of how to use the functions in funktionen.py is given in example.py.
The different short identifiers (e.g. H0, G0,...) can be found in synthload.xlsx.