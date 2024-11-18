## // Wscripted- Personal Curation Agent
# 
# Takes in Genre, Theme, and Comparative Title (10 binary neurons each) for a piece of content to offer the user a recommendation, 
# learning from the users subsequent interaction.

description = "Wscripted- Personal Curation Agent - demo #1"
arch_i = [7, 21, 21]               # 10 binary neurons each for Genre, Theme, and Comparative Title
arch_z = [10]                       # 10 binary neurons for output-- if the sum of the response >7, positive recommendation
arch_c = []
connector_function = "full_conn"

# To maintain compatibility with our API, do not change the variable name "Arch" or the constructor class "ar.Arch" in the line below
Arch = ar.Arch(arch_i, arch_z, arch_c, connector_function, description)
