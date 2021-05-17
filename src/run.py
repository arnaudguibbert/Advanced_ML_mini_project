import pandas as pd
import numpy as np
import seaborn as sns
import os
from utils import split_two, Assessment, plot_time_comparison

# Choose what you want to run
hyperparams_search = False
best_neighbors_LLE_full = 700
best_neighbors_MLLE_full = 275
best_components_MLLE_full = 4
best_neighbors_LLE_semi = 700
best_neighbors_MLLE_semi = 150
best_components_MLLE_semi = 6
semi_data_set = True
full_data_set = True

# Define the parameters for the comparison
san_check = False
k = 5
run = 1
KNN_neigh = 10
min_components, max_components, step_components = 1,8,1
min_neigh_LLE, max_neigh_LLE, nb_neigh_LLE = 70,801,40
min_neigh_MLLE, max_neigh_MLLE, nb_neigh_MLLE = 70,451,40

# Let's the code do the rest

directories = ["figures","data_time"]
for directory in directories:
    if not os.path.exists(directory):
        os.mkdir(directory)

sns.set_style("darkgrid")
range_components = np.arange(min_components,max_components,step_components)
range_neighbors_LLE = np.linspace(min_neigh_LLE,max_neigh_LLE,nb_neigh_LLE,dtype=int)
range_neighbors_MLLE = np.linspace(min_neigh_MLLE,max_neigh_MLLE,nb_neigh_MLLE,dtype=int)

print("Import the data set \n")
# Import the data set 
columns = ["Class"]
columns += ["Frequence word " + str(i) for i in range(1,49)]
columns += ["Special character " + str(i) for i in range(1,7)]
columns += ["Capital length mean"]
columns += ["Capital length longest"]
columns += ["Sum of captital length"]

data = pd.read_csv("../Data/spambasedata.csv",names=columns)
data_np = data.to_numpy().astype(float)

if full_data_set:

    dataset = data_np

    print("Evaluation on the full data set, Initialization of the objects \n")

    # Initialize the objects
    LLE_algo = Assessment(dataset,range_components,range_neighbors_LLE,k=k,run=run,KNN_neigh=KNN_neigh,check=san_check)
    MLLE_algo = Assessment(dataset,range_components,range_neighbors_MLLE,k=k,run=run,KNN_neigh=KNN_neigh,method="modified",check=san_check)

    if hyperparams_search:
        ############ LLE ############
        print("\nLaunch the evaluation of LLE full data set \n")

        LLE_algo.find_hyper()
        LLE_algo.plot_cumulative_error(title="LLE Reconstruction Error",save_file="LLE_error_metric_full_set")
        LLE_algo.generate_all(save_file="LLE_KNN_metric_full_set")
        LLE_algo.plot_time_perf(title="LLE time performances",
                                save_data="LLE_time_perf_full_set")

        print("\nGraphs saved in the figures folder \n")

        print("Launch the evaluation of MLLE full data set \n")

        MLLE_algo.find_hyper()
        MLLE_algo.plot_cumulative_error(title = "MLLE Reconstruction Error",save_file="MLLE_error_metric_full_set")
        MLLE_algo.generate_all(save_file="MLLE_KNN_metric_full_set")
        MLLE_algo.plot_time_perf(title="MLLE time performances",
                                 save_data="MLLE_time_perf_full_set")


        print("\nGraphs saved in the figures folder \n")

    if best_neighbors_LLE_full is not None:
        LLE_algo.generate_pairplot(best_neighbors_LLE_full,
                                   4,
                                   title="LLE neighbors = " + str(best_neighbors_LLE_full),
                                   save_file="LLE_pairplot_full_set")
        print("\nPairplot LLE saved in the figures folder \n")


    if best_neighbors_MLLE_full is not None and best_components_MLLE_full is not None:
        MLLE_algo.generate_pairplot(best_neighbors_MLLE_full,
                                    best_components_MLLE_full,
                                    title="MLLE neighbors = " + str(best_neighbors_MLLE_full) + " components = " + str(best_components_MLLE_full),
                                    save_file="MLLE_pairplot_full_set")
        print("\nPairplot MLLE saved in the figures folder \n")

################################### Assess sensitivity to a smaller data set ###################################

if semi_data_set:

    dataset = split_two(data_np)

    # Initialize the objects
    LLE_algo = Assessment(dataset,range_components,range_neighbors_LLE,k=k,run=run,KNN_neigh=KNN_neigh,check=san_check)
    MLLE_algo = Assessment(dataset,range_components,range_neighbors_MLLE,k=k,run=run,KNN_neigh=KNN_neigh,method="modified",check=san_check)

    if hyperparams_search:
        ############ LLE ############
        print("Launch the evaluation of LLE semi data set")

        LLE_algo.find_hyper()
        LLE_algo.plot_cumulative_error(title = "LLE Reconstruction Error",save_file="LLE_error_metric_semi_set")
        LLE_algo.generate_all(save_file="LLE_KNN_metric_semi_set")
        LLE_algo.plot_time_perf(title="LLE time performances",
                                save_data="LLE_time_perf_semi_set")

        print("Graphs saved in the figures folder")

        print("Launch the evaluation of MLLE semi data set")

        MLLE_algo.find_hyper()
        MLLE_algo.plot_cumulative_error(title = "MLLE Reconstruction Error",save_file="MLLE_error_metric_semi_set")
        MLLE_algo.generate_all(save_file="MLLE_KNN_metric_semi_set")
        MLLE_algo.plot_time_perf(title="MLLE time performances",
                                 save_data="MLLE_time_perf_semi_set")

        print("Graphs saved in the figures folder")

    if best_neighbors_LLE_semi is not None:
        LLE_algo.generate_pairplot(best_neighbors_LLE_full,
                                   4,
                                   title="LLE neighbors = " + str(best_neighbors_LLE_semi),
                                   save_file="LLE_pairplot_semi_set")
        print("Pairplot LLE saved in the figures folder")


    if best_neighbors_MLLE_semi is not None and best_components_MLLE_semi is not None:
        MLLE_algo.generate_pairplot(best_neighbors_MLLE_full,
                                    best_components_MLLE_full,
                                    title="MLLE neighbors = " + str(best_neighbors_MLLE_semi) + " components = " + str(best_components_MLLE_semi),
                                    save_file="MLLE_pairplot_semi_set")
        print("Pairplot MLLE saved in the figures folder")

files = ["data_time/LLE_time_perf_full_set.csv",
         "data_time/MLLE_time_perf_full_set.csv",
         "data_time/LLE_time_perf_semi_set.csv",
         "data_time/MLLE_time_perf_semi_set.csv"]
plot_time = True

for file in files:
    if not os.path.exists(file):
        plot_time = False
        break

if plot_time:
    plot_time_comparison(*files,save_file="time_performances_comparison")
