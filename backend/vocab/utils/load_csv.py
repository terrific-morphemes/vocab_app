import csv
import json
from pathlib import Path

CSV_FNAME = Path("/Users/nicholasmiller/Work/vocab_app/backend/resources/vocab_lists/chemisch_01.csv")
FIXTURE_FNAME = Path("/Users/nicholasmiller/Work/vocab_app/backend/fixtures/chemisch_fixture.json")
fixture = list()

with CSV_FNAME.open() as source:
    reader = csv.DictReader(source)
    vocab_item_count = 0
    vocab_list_count = 0
    learner_count = 0
    for row in reader:
        vocab_item = {
            'pk':vocab_item_count,
            'model':'vocab.vocabitem',
            'fields':{
                'text':row['text'],
                'meaning':row['meaning'],
                'language':row['language'],
                'morphology':row['morphology'],
                'category':row['category'],
                'subcategory':row['subcategory'],
                'source':row['source'],
            }
        }
        fixture.append(vocab_item)
        vocab_item_count += 1
    learner = {
      'pk':learner_count,
      'model':'vocab.learner',
      'fields':{
      'username':'happy_blossom',
      }
    }
    fixture.append(learner)
    vocab_list = {
      'pk':vocab_list_count,
      'model':'vocab.vocablist',
      'fields':{
          'learner':0,
          'vocab_items':list(range(vocab_item_count)),
        }
    }
    fixture.append(vocab_list)
    with FIXTURE_FNAME.open('w') as dest:
        json.dump(fixture, dest, indent=1)
