from alvadescpy import smiles_to_descriptors


if __name__ == '__main__':

    print(smiles_to_descriptors('CCC', descriptors=['MW', 'AMW'], labels=True))
