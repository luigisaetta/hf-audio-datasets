# HF Audio Datasets
![Huggingface](https://huggingface.co/front/assets/huggingface_logo.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

This repo contains all the work done to prepare utilities for creating **Audio datasets** from files, and checking audio

## Features
* copy files from/to OCI Object Storage, using ocifs
* effective Data Augmentation for ASR

## Code examples
* [How-to download a set of wav files from OCI Object Storage](./download_from_oss.ipynb)
* [How-to upload a set of files to OCI Object Storage](./upload_to_oss.ipynb)
* [How-to create the HF dataset from local files](./prepare_dataset.ipynb)
* [How-to create an augmented dataset](./prepare_dataset_augmented.ipynb)
* [Load HF dataset from local dir](./test_load_from_local.ipynb)
* [Upload HF dataset to Object Storage](./upload_dataset_to_oss.ipynb)
* [Download HF dataset from Object Storage](./download_dataset_from_oss.ipynb)

## Data examples used
* [ATCO2 dataset](https://www.atco2.org/data)

## Data Augmentation for ASR
Not every technique is working if you want to augment data for ASR.

I have found that:
* adding gaussian noise is not giving any benefits
* speed shifting is working




