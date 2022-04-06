import cdsapi

c = cdsapi.Client()

year = [    '1950', '1951', '1952',
            '1953', '1954', '1955',
            '1956', '1957', '1958',
            '1959', '1960', '1961',
            '1962', '1963', '1964',
            '1965', '1966', '1967',
            '1968', '1969', '1970',
            '1971', '1972', '1973',
            '1974', '1975', '1976',
            '1977', '1978']
month = [   '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12']
 

for y in year:
    for m in month:
        
        c.retrieve(
            'reanalysis-era5-pressure-levels-monthly-means-preliminary-back-extension',
            {
                'format': 'netcdf',
                'product_type': 'reanalysis-monthly-means-of-daily-means',
                'variable': [
                    'geopotential', 'ozone_mass_mixing_ratio', 'temperature',
                    'u_component_of_wind', 'v_component_of_wind',
                ],
                'pressure_level': [
                    '1', '2', '3',
                    '5', '7', '10',
                    '20', '30', '50',
                    '70', '100', '125',
                    '150', '175', '200',
                    '225', '250', '300',
                    '350', '400', '450',
                    '500', '550', '600',
                    '650', '700', '750',
                    '775', '800', '825',
                    '850', '875', '900',
                    '925', '950', '975',
                    '1000',
                ],
                'year': y,
                'month': m,
                'time': '00:00',
            },
            'era5_mm_go3tuv'+y+m+'.nc')
