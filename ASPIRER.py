import argparse
import warnings

import featureGenerator
import prediction

if __name__ == "__main__":
    # ASPIERE

    warnings.filterwarnings("ignore")
    parser = argparse.ArgumentParser(description='generate feature')
    parser.add_argument("--type", required=True,
                        choices=["benchmark", "predict"],
                        help="the encoding type")
    parser.add_argument('--Fasta_file', type=str, help='input fasta file')
    parser.add_argument('--PSSM_file',  type=str, help='input Pse-PSSM file')
    parser.add_argument('--output_name', type=str, help='output file name')
    args = parser.parse_args()

    if args.type=="benchmark":
        prediction.prediction()
    else:
        featureGenerator.generator(PSSM_file=args.PSSM_file, fasta_file=args.Fasta_file, output_name=args.output_name)
        prediction.prediction(output_name=args.output_name)
