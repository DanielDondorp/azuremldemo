# AzureML Pipeline Demos

Practical demonstrations of Azure Machine Learning pipelines, from simple "Hello World" to more complex ML workflows.

## Quick Start

1. **Prerequisites**: Azure CLI (`az login`), Python 3.8+, AzureML workspace with `config.json`. `config.json` saved to project rootfolder.
2. **Install**: `pip install -r requirements.txt`
3. **Start**: Run `notebooks/helloworld.ipynb` for basic pipeline concepts

## Available Demos

- **`helloworld.ipynb`**: Basic pipeline introduction (start here)
- **`catsanddogs.ipynb`**: Building and training Convolutional Neural network for image classification. MLFlow experiment tracking.
- **`yolosam.ipynb`**: Computer vision with YOLO and SAM
- **Additional**: Workspace setup, pipeline templates, testing

## Key Concepts

- **Environments**: Custom conda environments for reproducible execution
- **Components**: Reusable pipeline steps with inputs/outputs
- **Pipelines**: Chained workflows using AzureML DSL
- **MLflow**: Experiment tracking and metrics

## Resources

- [AzureML Documentation](https://docs.microsoft.com/en-us/azure/machine-learning/)
- [AzureML SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/) 