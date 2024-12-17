'''
Author: Alex Cecil
email: ajcecil@iastate.edu
Date Created: 2024-01-12
Last Modified: 2024-15-12
Purpose: This script is a python tool which can be used to establish maps from UAS imagery, using Open Drone Maps (ODM) and docker, to run a virtual machine when processing the imagery. The processed data is then downloaded into a designated location
Requirements: To use this script ODM and Docker need to be on the machine, the instructions for both installations can be found at: https://docs.opendronemap.org/installation/
'''


import subprocess
from pyodm import Node
import time
import os


class UAS_map_builder:
    def __init__(self, image_path, output_path):
        self.image_path = image_path
        self.output_path = output_path

    def run_docker_container(self):
        try:
            result = subprocess.run(
                ['docker', 'ps', '--filter', 'ancestor=opendronemap/nodeodm', '--format', '{{.ID}}'],
                capture_output=True, text=True
            )
            container_id = result.stdout.strip()

            if container_id:
                print(f'NodeODM is already running (Container ID: {container_id}).')
            else:
                print('Starting NodeODM Docker container...')
                subprocess.run(
                    ['docker', 'run', '-d', '-p', '3000:3000', 'opendronemap/nodeodm'],
                    check=True
                )
                print('NodeODM Docker container started successfully.')
                time.sleep(10)

        except FileNotFoundError:
            raise EnvironmentError('Docker is not installed or not available in the system PATH.')
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f'Error starting Docker container: {e.stderr}')

    def stop_docker_container(self):
        try:
            result = subprocess.run(
                ['docker', 'ps', '--filter', 'ancestor=opendronemap/nodeodm', '--format', '{{.ID}}'],
                capture_output=True, text=True
            )
            container_id = result.stdout.strip()

            if container_id:
                print(f'Stopping NodeODM Docker container (Container ID: {container_id})...')
                subprocess.run(['docker', 'stop', container_id], check=True)
                print('NodeODM Docker container stopped successfully.')
            else:
                print('No running NodeODM container to stop.')

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f'Error stopping Docker container: {e.stderr}')

    def run_odm(self, image_path, output):
        try:
            node = Node(host='localhost', port=3000)
            print('Connected to NodeODM.')

            if not image_path:
                raise ValueError('No images to process.')

            print('Starting processing task...')
            task = node.create_task(
                options={'dsm': True, 'orthophoto-resolution': 5},
                files=image_path
            )
            print('Task started. Waiting for completion...')
            task.wait_for_completion()

            os.makedirs(output, exist_ok=True)
            task.download_assets(output)
            print(f'Processing complete. Outputs saved to: {output}')

        except Exception as e:
            print(f'An error occurred: {e}')

    @staticmethod
    def get_images_by_folder(folders):
        image_dict = {}
        valid_extensions = {'.jpg', '.jpeg', '.png', '.tif', '.tiff'}

        for folder in folders:
            if not os.path.exists(folder):
                print(f'Warning: Folder does not exist: {folder}')
                image_dict[folder] = []
                continue

            images = [
                os.path.normpath(os.path.join(folder, file))
                for file in os.listdir(folder)
                if os.path.splitext(file)[1].lower() in valid_extensions
            ]
            image_dict[folder] = images

        return image_dict

    def main(self):
        self.stop_docker_container()
        images_by_folder = self.get_images_by_folder(self.image_path)

        for folder, image_path in images_by_folder.items():
            if not image_path:
                print(f'No valid images found in folder: {folder}')
                continue

            output = os.path.join(self.output_path,os.path.basename(folder), 'All_ODM_Files')
            print(output)
            if not os.path.exists(output):
                print('Making:')
                print(output)
                os.makedirs(output)
                
            self.run_docker_container()
            self.run_odm(image_path, output)
            self.stop_docker_container()


if __name__ == '__main__':
    image_folders = [
        'F:/Drone_Maps_Kansas/methods/images/Test_Images',
        # 'F:/Drone_Maps_Kansas/Pits_1_and_2_Images',
        # 'F:/Drone_Maps_Kansas/Pits_3_and_4_Images',
        # 'F:/Drone_Maps_Kansas/Pits_5_and_6_Images',
        # 'F:/Drone_Maps_Kansas/Pits_7_and_8_Images',
        # 'F:/Drone_Maps_Kansas/Pits_9_and_10_Images',
        # 'F:/Drone_Maps_Kansas/Pits_11_and_12_Images'
    ]
    builder = UAS_map_builder(image_path=image_folders, output_path='F:/Drone_Maps_Kansas/Processed')
    builder.main()
    