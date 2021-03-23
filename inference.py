import os
import json
from pororo import Pororo
import IPython

label_path = 'data/label'

label_list = os.listdir('data/label')

for i in range(len(label_list)):
    with open(os.path.join(label_path, label_list[i]), 'r') as f:
        label_json = json.load(f)

    print('Making Summary:', label_list[i])
    summary = Pororo(task = 'summarization', model = 'abstractive', lang = 'ko')

    sum_result = summary(label_json['text'])

    text = open('output/{}.txt'.format(label_list[i]), 'w')
    text.write(sum_result)
    text.close()
