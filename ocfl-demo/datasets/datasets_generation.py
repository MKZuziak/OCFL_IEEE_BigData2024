import os
from data_configs import data_configs
from fedata.hub.generate_dataset import generate_dataset


def generate_datasets():
    datasets = ['CIFAR10', 'FMNIST', 'MNIST']
    split_types = ['nonoverlaping', 'overlaping']
    split_balances = ['balanced', 'imbalanced']
    clients_numbers = ['15', '30']
    
    print("--------------GENERATING DATASETS. THIS MAY TAKE A FEW MIUTES--------------".center(10))
    for dataset in datasets:
        for split_type in split_types:
            for split_balance in split_balances:
                for client_number in clients_numbers:
                    try:
                        dir_path = os.path.join(os.getcwd(), dataset, split_type, split_balance, client_number)
                        os.makedirs(dir_path)
                        key = f'{dataset}_{split_type}_{split_balance}_{client_number}'
                        config = data_configs[key]
                        config['save_path'] = dir_path
                        print(f"--------------Generating {split_type} {split_balance} {dataset} for {client_number} clients--------------".center(10))
                        generate_dataset(config=config)
                        
                    except IsADirectoryError as e:
                        print(e)
                        
if __name__ == "__main__":
    generate_datasets()