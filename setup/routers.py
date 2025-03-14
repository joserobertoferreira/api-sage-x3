class AuthRouter:
    """
    Router for the authentication database.
    """

    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read the 'auth', 'contenttypes', and 'sessions' models
        from the 'auth_db' database.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write the 'auth', 'contenttypes', and 'sessions' models
        to the 'default' database.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth, contenttypes, sessiona or admin apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'auth', 'contenttypes' and 'sessions' apps only appear
        in the 'default' database.
        """
        if app_label in self.route_app_labels:
            return db == 'auth_db'
        return None


class SageRouter:
    def db_for_read(self, model, **hints):
        """
        Set the 'sage' database to read.
        """
        return 'sage'

    def db_for_write(self, model, **hints):
        """
        Writes always go to sage.
        """
        return 'sage'

    def allow_relation(self, obj1, obj2, **hints):
        """
        The both objects are in the 'sage' database.
        """

        if obj1._state.db == 'sage' and obj2._state.db == 'sage':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
