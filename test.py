from runPhyml import RunPhyml
import json

cmd = {'input':'/mnt/c/Users/Nicolas/Documents/GitHub/tp3/input_test.phy','SequenceTypeOption':'nt','sequential':'y','multiple':'2','pars':'y','model':'HKY85','FqOption':'e','tstv':'5','pinv':'e','nclasses':4,'alpha':'e','useMedian':'y','codposOption':'2','params':'tlr','search':'SPR','randstart':'14','rSeedOption':'2','printSiteLnl':'y','printTrace':'y','runID':'12','noMemoryCheck':'y','noColalias':'y','quietMode':'y','ancestralCalculate':'y','leaveDuplicates':'y'}
dict = json.dumps(cmd)

fh = open("./input_test.phy","r")
phylip = fh.readlines()
fh.close()

test = RunPhyml(dict, 7)
test.run()
