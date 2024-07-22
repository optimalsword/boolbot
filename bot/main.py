from gather_input import *



if __name__ == '__main__':
    raw = read_inputs('inputs.csv')
    
    features = raw[0]
    data = raw[1]

    print('=== DECISION TREE LEARNING ALGORITHM ===')
    output_feature = input('Please choose your output feature: ')
    if output_feature not in features:
        print('NOT A VALID FEATURE. PICK A VALID ONE')
        exit(1)
    

