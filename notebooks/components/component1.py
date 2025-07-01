import os
import argparse
import logging
import mlflow


def main():
    """Main function of the script."""

    # input and output arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, help="path to input data")
    parser.add_argument("--output", type=str, help="path to output data")
    args = parser.parse_args()

    # Start Logging
    mlflow.start_run()

    print("We are running compoment 1")
    logging.info("We are running compoment 1, but this message is using logging")

    # Load data
    files = os.listdir(args.data)
    print(f"we have found {len(files)} files in the input directory")


    # Stop Logging
    mlflow.end_run()


if __name__ == "__main__":
    main()
