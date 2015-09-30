#!/bin/bash
#PBS -q shared
#PBS -l nodes=10:ppn=4
#PBS -l walltime=05:00:00
#PBS -l mem=50gb
#PBS -M emeskhidze@elon.edu
#PBS -m abe
#PBS -N mpi_run
#PBS -j oe
cd ${PBS_O_WORKDIR}
module purge
module load gnu/4.8.2
module load openmpi_ib/1.6.5
ulimit -s unlimited
mpirun -np 40 /home/emeskhi/cloudy/c13.03/source/sys_mpi_gcc/cloudy.exe -r gridrun
