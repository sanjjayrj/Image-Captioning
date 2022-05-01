import string

class data_preprocessing:
    # def __init__(self):
    def load_descriptions(doc):
        descriptions = dict()
        for line in doc.split('\n'):
            # split line by first comma, ie image and caption
            tokens = line.split(",")

            # take the first token as image id, the rest as description
            image_id, image_desc = tokens[0], tokens[1:]

            # extract filename from image id
            image_id = image_id[:-4]

            # convert description tokens back to string
            image_desc = ' '.join(image_desc)
            if image_id not in descriptions:
                descriptions[image_id] = list()
            descriptions[image_id].append(image_desc)
        return descriptions
    # prepare translation table for removing punctuation
    def clean_description(descriptions):
        table = str.maketrans('', '', string.punctuation)
        for key, desc_list in descriptions.items():
            for i in range(len(desc_list)):
                desc = desc_list[i]
                # tokenize
                desc = desc.split()
                # convert to lower case
                desc = [word.lower() for word in desc]
                # remove punctuation from each token
                desc = [w.translate(table) for w in desc]
                # remove hanging 's' and 'a'
                desc = [word for word in desc if len(word)>1]
                # remove tokens with numbers in them
                desc = [word for word in desc if word.isalpha()]
                # store as string
                desc_list[i] =  ' '.join(desc)
    """
        Creating a vocabulary from the 
        processed descriptions.
    """
    def create_vocabulary(descriptions):
        vocab = set()
        for key in descriptions.keys():
            [vocab.update(d.split()) for d in descriptions[key]]
        return vocab
    def save_processed(descriptions, filename):
        doc = open(filename, 'w')
        for key, descs in descriptions.items():
            for desc in descs:
                doc.write(key + ' ' + desc + '\n')
        doc.close()
    