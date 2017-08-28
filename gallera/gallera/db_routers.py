class SingleDbSingleAppDbRouter:
    APP_LABEL = None
    DB_LABEL = None

    def db_for_read(self, model, **hints):
        # pylint: disable=unused-argument
        if model._meta.app_label == self.APP_LABEL:
            return self.DB_LABEL
        return None

    def db_for_write(self, model, **hints):
        # pylint: disable=unused-argument
        if model._meta.app_label == self.APP_LABEL:
            return self.DB_LABEL
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # pylint: disable=unused-argument
        if (
                obj1._meta.app_label == self.APP_LABEL and
                obj2._meta.app_label != self.APP_LABEL
        ):
            return False
        if (
                obj2._meta.app_label == self.APP_LABEL and
                obj1._meta.app_label != self.APP_LABEL
        ):
            return False

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # pylint: disable=unused-argument

        # this causes the app models to only show up in the
        # app-specific db
        if app_label == self.APP_LABEL:
            return db == app_label

        # this prevents every other app from putting its models in the
        # app-specific db
        if db == self.DB_LABEL:
            return False

        return None


class GalleraDbRouter(SingleDbSingleAppDbRouter):
    APP_LABEL = 'gallera'
    DB_LABEL = 'gallera'


