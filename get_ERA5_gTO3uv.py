import cdsapi
import sys

c = cdsapi.Client()

year = str(sys.argv[1])

if int(year) < 1979:
    source = 'reanalysis-era5-pressure-levels-monthly-means-preliminary-back-extension'
    producttype = 'reanalysis-monthly-means-of-daily-means'
else:
    source = 'reanalysis-era5-pressure-levels-monthly-means'
    producttype = 'monthly_averaged_reanalysis'
    
c.retrieve(
    source,
    {
        'format': 'netcdf',
        'product_type': producttype,
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
        'year': year,
        'month': [   
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'time': '00:00',
    },
    '/pfs/work7/workspace/scratch/px5501-Era5/era5_mm_go3tuv'+year+'.nc')
