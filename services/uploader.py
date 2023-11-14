class Uploader:

    @staticmethod
    def upload_photo_to_team(instance, filename):
        return f"teams/{instance.slug}/{filename}"
    
    
    @staticmethod
    def upload_photo_to_blog(instance, filename):
        return f"blogs/{instance.slug}/{filename}"
    
    @staticmethod
    def upload_photo_to_service(instance, filename):
        return f"services/{instance.slug}/{filename}"