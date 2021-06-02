europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# update nilai ibukota german ke berlin
europe['germany'] = 'berlin'

# remove australia dari europa
del europe['australia']

print(europe)
