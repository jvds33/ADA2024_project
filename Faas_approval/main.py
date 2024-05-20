import random
import json
from google.cloud import firestore

def user_approval(request):
    # Get query parameters
    idea_id = request.args.get('idea_id', 'default_idea')
    
    # Generate a random approval (like or dislike)
    approval = random.choice(['like', 'dislike'])
    
    # Create a Firestore client
    db = firestore.Client()
    
    # Store the approval result in Firestore
    # name of the collection is idea_approvals
    doc_ref = db.collection('idea_approvals').document(idea_id)
    doc_ref.set({
        'idea_id': idea_id,
        'approval': approval
    })
    
    # Return the result
    return json.dumps({'idea_id': idea_id, 'approval': approval})

# Deploy with:
# gcloud functions deploy user_approval --runtime python39 --trigger-http --allow-unauthenticated
