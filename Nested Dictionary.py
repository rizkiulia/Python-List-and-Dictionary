country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } 
         }

# berapa populasi dari kota german?
print(country['germany']['population'])

# update data baru, yaitu negara indonesia dengan capital jakarta dan poulasi 250
country['Indonesia'] = {'capital':'jakarta', 'population':250}

print(country)
