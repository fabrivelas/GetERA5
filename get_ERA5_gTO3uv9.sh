#!/bin/bash
#SBATCH --time=10:00:00
#SBATCH --partition=single
#SBATCH --mem=60000
#SBATCH --ntasks-per-node=12
#SBATCH --mail-user=tobias.kerzenmacher@kit.edu
#SBATCH --constraint=LSDF

##source /home/kit/imk-asf/px5501/pythonenv/bin/activate
source /home/kit/imk-asf/px5501/.Venv/Edge/bin/activate

parallel -j 10 python3 /home/kit/imk-asf/px5501/Git/GetERA5/get_ERA5_gTO3uv.py $year ::: {1990..1999}
install -p -m 644 -g imk-asf-o3as-lsdf /pfs/work7/workspace/scratch/px5501-Era5/era5_mm_go3tuv199*.nc  /lsdf/kit/imk-asf/projects/O3as/Ecmwf/Era5/
#cp /pfs/work7/workspace/scratch/px5501-Era5/era5_mm_go3tuv1978.nc  /lsdf/kit/imk-asf/projects/O3as/Ecmwf/Era5/
#rm /pfs/work7/workspace/scratch/px5501-Era5/era5_mm_go3tuv1978.nc 
