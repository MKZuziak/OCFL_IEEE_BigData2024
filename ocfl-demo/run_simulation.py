import os
from functools import partial
import pickle

from torch import optim
from sklearn.cluster import AffinityPropagation, KMeans, MeanShift, HDBSCAN

from net_architectures import FMNIST_Expanded_CNN, ResNet34
from FedCL.model.federated_model import FederatedModel
from FedCL.node.federated_node import FederatedNode
from FedCL.simulation.simulation import Simulation
from FedCL.aggregators.fedopt_aggregator import Fedopt_Optimizer
from FedCL.files.archive import create_archive


def simulation_run(
    dataset_name: str,
    dataset_path: str,
    root_path: str,
    archive_name: str,
    number_of_clients: int,
    algorithm: str,
):
    # Creates a separate archive for storing results
    (metrics_savepath, 
     nodes_models_savepath, 
     orchestrator_model_savepath,
     clustering_root,
     sim_matrices_savepath,
     cluster_structure_savepath,
     ) = create_archive(
         path=root_path,
         archive_name=archive_name
     )
    
    # Loads the datasets
    with open(dataset_path, 'rb') as file:
        data = pickle.load(file)
    orchestrator_data = data[0]
    nodes_data = data[1]
    LOCAL_EPOCHS = 1 # 3
    
    # Switches net architecture
    if dataset_name == 'FMNIST':
        net_architecture = FMNIST_Expanded_CNN()
        ITERATIONS = 1 #50
        LOADER_BATCH_SIZE = 32
        BATCH_JOB = False
    elif dataset_name == 'MNIST':
        net_architecture = FMNIST_Expanded_CNN()
        ITERATIONS = 1 #50
        LOADER_BATCH_SIZE = 32
        BATCH_JOB = False
    elif dataset_name == 'CIFAR10':
        net_architecture = ResNet34()
        ITERATIONS = 1 #80
        LOADER_BATCH_SIZE = 64
        BATCH_JOB = True
    else:
        raise 'Improper task name'
    
    # Imports the package elements
    optimizer_architecture = partial(optim.SGD, lr=0.01)
    model_tempate = FederatedModel(
        net=net_architecture,
        optimizer_template=optimizer_architecture,
        loader_batch_size=LOADER_BATCH_SIZE
    )
    node_template = FederatedNode()
    fedopt_aggregator = Fedopt_Optimizer()
    simulation_instace = Simulation(
        model_template=model_tempate,
        node_template=node_template
        )
    simulation_instace.attach_orchestrator_model(orchestrator_data=orchestrator_data)
    simulation_instace.attach_node_model({
        node: nodes_data[node] for node in range(number_of_clients)
    })
    
    # Switches for a specific simulation type
    if algorithm == 'baseline':
        simulation_instace.training_protocol_baseline(
            iterations=ITERATIONS,
            sample_size=number_of_clients,
            local_epochs=LOCAL_EPOCHS,
            aggrgator=fedopt_aggregator,
            learning_rate=1.0,
            metrics_savepath=metrics_savepath,
            nodes_models_savepath=nodes_models_savepath,
            orchestrator_models_savepath=orchestrator_model_savepath,
            sim_matrices_savepath=sim_matrices_savepath,
            cluster_structure_savepath=cluster_structure_savepath,
            batch_job=BATCH_JOB
        )
    elif algorithm == 'sattler':
        simulation_instace.training_protocol_sattler(
            iterations=ITERATIONS,
            sample_size=number_of_clients,
            local_epochs=LOCAL_EPOCHS,
            aggrgator=fedopt_aggregator,
            learning_rate=1.0,
            EPS1=2.50, # previous value: 0.35
            EPS2=1.00,
            round_cooldown=40,
            metrics_savepath=metrics_savepath,
            nodes_models_savepath=nodes_models_savepath,
            orchestrator_models_savepath=orchestrator_model_savepath,
            sim_matrices_savepath=sim_matrices_savepath,
            cluster_structure_savepath=cluster_structure_savepath,
            batch_job=BATCH_JOB
        )
    elif algorithm == 'briggs':
        simulation_instace.training_protocol_briggs(
            iterations=ITERATIONS,
            sample_size=number_of_clients,
            local_epochs=LOCAL_EPOCHS,
            aggrgator=fedopt_aggregator,
            clustering_round=20,
            distance_threshold=0.05,
            learning_rate=1.0,
            metrics_savepath=metrics_savepath,
            nodes_models_savepath=nodes_models_savepath,
            orchestrator_models_savepath=orchestrator_model_savepath,
            sim_matrices_savepath=sim_matrices_savepath,
            cluster_structure_savepath=cluster_structure_savepath,
            batch_job=BATCH_JOB
        )
    else:
        if algorithm == 'kmeans':
            clustering_algorithm = KMeans(n_clusters=3)
        elif algorithm == 'affinity':
            clustering_algorithm = AffinityPropagation(affinity='precomputed')
        elif algorithm == 'meanshift':
            clustering_algorithm = MeanShift()
        elif algorithm == 'HDBSCAN':
            if number_of_clients == 15:
                clustering_algorithm = HDBSCAN(
                    min_cluster_size = 3,
                    metric='precomputed'
                )
            else:
                clustering_algorithm = HDBSCAN(
                    min_cluster_size = 6,
                    metric='precomputed'
                )
        else:
            raise "Invalid clustering algorithm"
        simulation_instace.training_protocol_energy_oneshot(
            iterations=ITERATIONS,
            sample_size=number_of_clients,
            local_epochs=LOCAL_EPOCHS,
            aggrgator=fedopt_aggregator,
            learning_rate=1.0,
            clustering_algorithm=clustering_algorithm,
            metrics_savepath=metrics_savepath,
            nodes_models_savepath=nodes_models_savepath,
            orchestrator_models_savepath=orchestrator_model_savepath,
            sim_matrices_savepath=sim_matrices_savepath,
            cluster_structure_savepath=cluster_structure_savepath,
            batch_job=BATCH_JOB
            )