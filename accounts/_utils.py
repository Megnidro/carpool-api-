

class AlterCustom: # class pour valider les alternance
    is_driver = None
    is_passenger = None

    @classmethod
    def alternant(self):
        """
        Méthode pour alterner entre les rôles de conducteur et de passager.
        Retourne le nouveau rôle attribué à l'utilisateur (chaîne de caractères).
        """
        if self.is_driver:
            self.is_driver = False
            self.is_passenger = True
            new_role = "Passager"
        else:
            self.is_driver = True
            self.is_passenger = False
            new_role = "Conducteur"

        self.save()
        return new_role
