# model_utils.py
def get_model_string(model_name):
    """
    Retourne le nom du modèle en tant que chaîne de caractères.
    """
    return f"allauth.account.models.{model_name}"
