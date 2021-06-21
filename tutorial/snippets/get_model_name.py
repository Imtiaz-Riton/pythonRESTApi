from .models import Snippet, ModelToDelete

model_map = {
    "Snippets" : Snippet,
    "ModelToDelete" : ModelToDelete,
}

def get_model_name(name):
    return model_map[name]