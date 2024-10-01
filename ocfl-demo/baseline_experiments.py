import os
from functools import partial
import pickle

from net_architectures import FMNIST_Expanded_CNN, ResNet34
from run_simulation import simulation_run

from fedata.hub.generate_dataset import generate_dataset
from FedCL.model.federated_model import FederatedModel
from FedCL.node.federated_node import FederatedNode
from FedCL.simulation.simulation import Simulation
from FedCL.aggregators.fedopt_aggregator import Fedopt_Optimizer
from FedCL.files.archive import create_archive

def baseline_experiments():
    #datasets = ['CIFAR10', 'FMNIST', 'MNIST']
    datasets = ['FMNIST', 'MNIST']
    split_types = ['nonoverlaping', 'overlaping']
    split_balances = ['balanced', 'imbalanced']
    algorithms = ['baseline', 'sattler', 'briggs', 'kmeans', 'affinity', 'meanshift', 'HDBSCAN']
    clients_numbers = ['15', '30']
    
    print("--------------PERFORMING BASELINE EXPERIMENTS. THIS MAY TAKE FROM A FEW TO FEW HUNDRED HOURS DEPENDING ON THE SETUP--------------".center(10))
    for dataset in datasets:
        for split_type in split_types:
            for split_balance in split_balances:
                for client_number in clients_numbers:
                        # Retrieve the dataset path
                        dataset_name = f'{dataset}_{client_number}_dataset_pointers'
                        dataset_path = os.path.join(os.getcwd(), 'datasets', dataset, split_type, split_balance, client_number, dataset_name)

                        # Make a directory for storing the results
                        dir_path = os.path.join(os.getcwd(), 'baseline_experiments_results', dataset, split_type, split_balance, client_number)
                        os.makedirs(dir_path)
                                                
                        for algorithm in algorithms:
                            # Form a directory name
                            archive_name = f'{algorithm}_{dataset}_{split_type}_{split_balance}_{client_number}'
                            simulation_run(
                                dataset_name=dataset,
                                dataset_path=dataset_path,
                                root_path=dir_path,
                                archive_name=archive_name,
                                number_of_clients=int(client_number),
                                algorithm=algorithm
                            )


if __name__ == "__main__":
    baseline_experiments()