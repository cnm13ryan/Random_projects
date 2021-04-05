//
//  pi_calculationmpi.c
//
//
//  Created by Chan Nok Man on 5/4/2021.
//

#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]){
    
    int N = 840;
    int i;
    double x,sum = 0.0;
    double pi;
    double step = 1.0/(double) N;
    int count;
    
    MPI_Init(&argc, &argv);
    
    int size;
    MPI_Comm comm;
    comm = MPI_COMM_WORLD;
    MPI_Comm_size(comm, &size);
    
    int rank;
    MPI_Comm_rank(comm, &rank);
    printf("\nThe number of process: %d\n", size);
    printf("Hello World from rank %d \n", rank);
    
    
    int namelen;
    char procname[MPI_MAX_PROCESSOR_NAME];
    MPI_Get_processor_name(procname, &namelen);
    
    //MPI_Barrier(comm);
    //double tstart = MPI_Wtime();
    
    if (rank == 0){
        printf("Rank %d is the controller process on machine %s\n", rank, procname);
        
        double par0_pi = 0.0;
        int st = N/size;
       
        for (i=1; i<=st; i++){
            x = (i-0.5)*step;
            sum = sum + 4.0/(1.0+x*x);
        }
        par0_pi = step * sum;
        printf("Partial sum of Pi, calculated by rank %d, from %d to %d step, is %lf\n", rank, 0, st, par0_pi);
        
        MPI_Status status;
        // MPI_Probe(&pi, )
        MPI_Recv(&pi, 8,MPI_DOUBLE, MPI_ANY_SOURCE, MPI_ANY_TAG, comm, &status);
        MPI_Get_count(&status, MPI_DOUBLE, &count);
        
        par0_pi += pi;
        printf("\nPi with %d steps is %lf\n", N, par0_pi);
        
    }
    else{
        printf("Rank %d is the worker process on machine %s\n", rank, procname);
        
        double par1_pi = 0.0;
        int st1 = N/size + 1;
        int ed1 = N/size + N/size;
        
        for (i= st1; i<=ed1; i++){
            x = (i-0.5)*step;
            sum = sum + 4.0/(1.0+x*x);
        }
        par1_pi = step * sum;
        printf("Partial sum of Pi, calculated by rank %d, from %d to %d step, is %lf\n", rank, st1, ed1, par1_pi);
        
        MPI_Ssend(&par1_pi, 8, MPI_DOUBLE, 0, 0, comm);
        
    }
    MPI_Finalize();
    return 0;
}


