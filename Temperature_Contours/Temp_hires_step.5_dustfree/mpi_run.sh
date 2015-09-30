#!/bin/bash -login
#SBATCH --job-name="highres_baseline_tempcontours_step.5"
#SBATCH --output="baseline_highres.o"
#SBATCH -p compute
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=24
#SBATCH -t 05:00:00
#SBATCH --export=ALL
#SBATCH --mail-type=ALL 
#SBATCH --mail-user=emeskhidze@elon.edu


module purge
module load gnu/4.9.2
module load openmpi_ib/1.8.4

ulimit -s unlimited

ibrun --np 96 /home/emeskhi/cloudy/cloudy_comet/c13.03/source/sys_mpi_gcc/mpi_cloudy.exe -r gridrun

