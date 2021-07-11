import featureGenerator
import prediction



if __name__ == "__main__":

    #ASPIERE
    PSSM_file = ""
    fasta_file = ""
    output_name = ""

    # PSSM_file = "./features/pse_pssm_secretP.csv"
    # fasta_file = "./dataset/human.fasta"
    # output_name = "human"

    featureGenerator.generator(PSSM_file=PSSM_file, fasta_file = fasta_file, output_name=output_name)
    prediction.prediction(output_name=output_name)
