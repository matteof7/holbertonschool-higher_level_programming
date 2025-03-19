def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    
    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, got {type(attendees).__name__}")
        return
    
    # Vérification des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Vérification que tous les éléments de la liste sont des dictionnaires
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: All attendees must be dictionaries")
        return
    
    # Traitement de chaque invité
    for i, attendee in enumerate(attendees, 1):
        # Création d'une copie du modèle
        invitation = template
        
        # Remplacement des espaces réservés
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, None)
            # Si la valeur est None ou n'existe pas, la remplacer par "N/A"
            if value is None:
                value = "N/A"
            # Remplacement de l'espace réservé
            invitation = invitation.replace(f"{{{key}}}", str(value))
        
        # Écriture du fichier de sortie
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as file:
            file.write(invitation)
        
        print(f"Generated {output_filename}")
