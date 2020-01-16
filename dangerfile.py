import json
import sys

# Read in DSL
data = sys.stdin.read()
dsl = json.loads(data)

# Grabbing the DSL
title = dsl['danger']['github']['pr']['title'] 

# Create a results dict
results = {
  'warnings': [],
  'messages': [],
  'fails': [],
  'markdowns': [ { 'message': title } ]
}

# Print that to send a message back to danger
print(json.dumps(results))
